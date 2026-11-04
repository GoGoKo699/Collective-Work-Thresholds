#!/usr/bin/env python3
"""Reproducible ergotropy checks for the harmonic, middle-tilted qutrit.

H=diag(0,1,2), p_j proportional to exp(-beta*j+delta*[j==1]).
Exact rational log ordering and integer multiplicity matching are separated
from transcendental evaluation. Work is a sum of nonnegative terms, not the
difference of two O(n) energies. This numerical module does not certify the
asymptotic theorem. See README.md for arithmetic and resource limitations.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal, localcontext, Underflow
from fractions import Fraction
from itertools import product
import json
import math
from pathlib import Path
import platform
from typing import NamedTuple


@dataclass(frozen=True)
class Model:
    beta_text: str
    delta_text: str
    beta: Fraction
    delta: Fraction
    denominator: int
    beta_units: int
    delta_units: int

    @classmethod
    def parse(cls, beta: str, delta: str) -> "Model":
        if not isinstance(beta, str) or not isinstance(delta, str):
            raise TypeError("Pass beta and delta as decimal/rational strings, never floats")
        b, d = Fraction(beta), Fraction(delta)
        if b <= 0 or not (0 <= d < b):
            raise ValueError("Require beta > 0 and 0 <= delta < beta.")
        denominator = math.lcm(b.denominator, d.denominator)
        return cls(beta, delta, b, d, denominator,
                   int(b * denominator), int(d * denominator))

    def first_activation(self) -> int | None:
        """Smallest odd integer strictly greater than beta/delta, exactly."""
        if self.delta == 0:
            return None
        ratio = self.beta / self.delta
        candidate = ratio.numerator // ratio.denominator + 1
        return candidate if candidate % 2 else candidate + 1


class Term(NamedTuple):
    log_units: int
    next_gap_units: int
    cumulative_energy_surplus: int


@dataclass
class SpectralPlan:
    n: int
    denominator: int
    terms: list[Term]
    type_count: int
    distinct_log_weights: int
    matched_dimension: int
    original_energy_sum: int
    assigned_energy_sum: int

    @property
    def exact_zero(self) -> bool:
        return not self.terms


def build_plan(n: int, model: Model) -> SpectralPlan:
    """Exact combinatorial plan; no floating-point arithmetic is used."""
    if n < 1:
        raise ValueError("n must be a positive integer")
    # Each group stores its count and the sum of original energies, with
    # repetitions. A group includes every type with exactly equal log weight.
    groups: dict[int, list[int]] = defaultdict(lambda: [0, 0])
    shells = [0] * (2*n + 1)
    type_count = 0
    for middle in range(n + 1):
        choose_middle = math.comb(n, middle)
        remaining = n - middle
        choose_top = 1
        for top in range(remaining + 1):
            count = choose_middle * choose_top
            energy = middle + 2*top
            key = -model.beta_units * energy + model.delta_units * middle
            groups[key][0] += count
            groups[key][1] += count * energy
            shells[energy] += count
            type_count += 1
            if top < remaining:
                choose_top = choose_top * (remaining - top) // (top + 1)

    dimension = 3**n
    assert sum(shells) == sum(g[0] for g in groups.values()) == dimension
    keys = sorted(groups, reverse=True)
    target_energy, available = 0, shells[0]
    original_sum = assigned_sum = matched = 0
    terms: list[Term] = []
    for group_index, key in enumerate(keys):
        count, source_energy_sum = groups[key]
        original_sum += source_energy_sum
        left = count
        while left:
            while available == 0:
                target_energy += 1
                available = shells[target_energy]
            take = min(left, available)
            assigned_sum += take * target_energy
            matched += take
            left -= take
            available -= take
        surplus = original_sum - assigned_sum
        assert surplus >= 0, "A lowest-energy prefix cannot exceed a chosen subset"
        if group_index + 1 < len(keys) and surplus:
            gap = key - keys[group_index + 1]
            assert gap > 0
            terms.append(Term(key, gap, surplus))
    assert matched == dimension
    assert original_sum == assigned_sum == n * dimension
    return SpectralPlan(n, model.denominator, terms, type_count, len(keys),
                        matched, original_sum, assigned_sum)


def fraction_decimal(x: Fraction) -> Decimal:
    return Decimal(x.numerator) / Decimal(x.denominator)


def floor_log10_fraction(x: Fraction) -> int:
    """Exact floor(log10(x)) for positive rational x, for precision guards."""
    assert x > 0
    exponent = len(str(x.numerator)) - len(str(x.denominator))
    if exponent >= 0:
        below = x.numerator < x.denominator * 10**exponent
    else:
        below = x.numerator * 10**(-exponent) < x.denominator
    return exponent - int(below)


def working_precision(model: Model, digits: int) -> int:
    if digits < 25:
        raise ValueError("Decimal mode requires at least 25 requested digits")
    small_orders = [max(0, -floor_log10_fraction(model.beta))]
    if model.delta:
        small_orders.append(max(0, -floor_log10_fraction(model.delta)))
    # Extra precision also protects the endpoint's O(delta^2) energy identity.
    return digits + 30 + 2*max(small_orders)


def one_minus_exp_negative(x: Decimal) -> Decimal:
    """1-exp(-x), x>0, without cancellation for arbitrarily small x."""
    assert x > 0
    if x > Decimal("0.125"):
        return 1 - (-x).exp()
    term = total = x
    k = 1
    while True:
        k += 1
        term *= -x / k
        updated = total + term
        if updated == total:
            return total
        total = updated


def divergence_integrand(ratio: Decimal) -> Decimal:
    """r log(r)-r+1, using a stable series near r=1."""
    assert ratio > 0
    t = ratio - 1
    if abs(t) > Decimal("0.125"):
        return ratio * ratio.ln() - ratio + 1
    if not t:
        return Decimal(0)
    term = total = t*t / 2
    k = 2
    while True:
        # term_(k+1)/term_k = -t*(k-1)/(k+1).
        term *= -t * (k-1) / (k+1)
        k += 1
        updated = total + term
        if updated == total:
            return total
        total = updated


def probabilities(beta: Decimal, delta: Decimal) -> tuple[list[Decimal], Decimal]:
    weights = [Decimal(1), (-beta+delta).exp(), (-2*beta).exp()]
    z = sum(weights)
    return [x/z for x in weights], z.ln()


def uniform_divergence(p: list[Decimal]) -> Decimal:
    # D(p || (1/3,1/3,1/3)), evaluated without entropy-deficit cancellation.
    return sum(divergence_integrand(3*x) for x in p) / 3


def positive_relative_entropy(p: list[Decimal], q: list[Decimal]) -> Decimal:
    # The linear terms cancel for normalized p,q; this form is nonnegative.
    return sum(y * divergence_integrand(x/y) for x, y in zip(p, q))


def decimal_work(plan: SpectralPlan, model: Model, digits: int = 80) -> Decimal:
    if plan.exact_zero:
        return Decimal(0)
    with localcontext() as ctx:
        ctx.prec = working_precision(model, digits)
        ctx.traps[Underflow] = True
        beta, delta = fraction_decimal(model.beta), fraction_decimal(model.delta)
        _, log_z = probabilities(beta, delta)
        denominator = Decimal(plan.denominator)
        gaps: dict[int, Decimal] = {}
        total = Decimal(0)
        for key, gap, surplus in plan.terms:
            if gap not in gaps:
                gaps[gap] = one_minus_exp_negative(Decimal(gap)/denominator)
            normalized_log = Decimal(key)/denominator - plan.n*log_z
            total += Decimal(surplus) * normalized_log.exp() * gaps[gap]
        assert total > 0
        # Return the requested number of significant digits, not guard digits.
        ctx.prec = digits
        return +total


def float_work(plan: SpectralPlan, model: Model) -> dict:
    if plan.exact_zero:
        return {"work": 0.0, "log_work": None, "exact_zero": True,
                "numerical_underflow": False, "scaled_tail_underflows": 0}
    beta, delta = float(model.beta), float(model.delta)
    if not math.isfinite(beta) or not math.isfinite(delta):
        raise ValueError("Parameters exceed float range; use Decimal mode")
    log_z = math.log1p(math.exp(-beta+delta) + math.exp(-2*beta))
    log_terms = []
    for key, gap, surplus in plan.terms:
        g = float(Fraction(gap, plan.denominator))
        if g == 0:
            raise ValueError("A positive exact log gap underflows float; use Decimal mode")
        log_gap_factor = math.log(-math.expm1(-g))
        log_terms.append(math.log(surplus) + float(Fraction(key, plan.denominator))
                         - plan.n*log_z + log_gap_factor)
    maximum = max(log_terms)
    scaled = [math.exp(x-maximum) for x in log_terms]
    log_work = maximum + math.log(math.fsum(scaled))
    work = math.exp(log_work)
    return {"work": work, "log_work": log_work, "exact_zero": False,
            "numerical_underflow": work == 0,
            "scaled_tail_underflows": sum(x == 0 for x in scaled)}


def endpoint(model: Model, digits: int = 80) -> dict[str, Decimal | int | list]:
    """Positive-temperature equal-entropy Gibbs state, with a bracketed root.

    Solves equality of divergences from the uniform state, avoiding subtraction
    of entropies close to log(3). Work uses D(p||q_star)/beta_star and is checked
    against the energy difference; neither uses a cancellation-prone float.
    """
    with localcontext() as ctx:
        ctx.prec = working_precision(model, digits)
        ctx.traps[Underflow] = True
        beta, delta = fraction_decimal(model.beta), fraction_decimal(model.delta)
        p, _ = probabilities(beta, delta)
        thermal, _ = probabilities(beta, Decimal(0))
        target = uniform_divergence(p)
        lo, hi = Decimal(0), beta
        if model.delta == 0:
            lo = hi = beta
            iterations = 0
        else:
            while uniform_divergence(probabilities(hi, Decimal(0))[0]) < target:
                hi *= 2
            tolerance = hi * (Decimal(10) ** (-(ctx.prec-15)))
            iterations = 0
            while hi-lo > tolerance:
                mid = (hi+lo)/2
                if mid == lo or mid == hi:
                    break
                value = uniform_divergence(probabilities(mid, Decimal(0))[0])
                if value < target:
                    lo = mid
                else:
                    hi = mid
                iterations += 1
                if iterations > 20000:
                    raise ArithmeticError("Endpoint bisection exceeded its safety bound")
        theta = (lo+hi)/2
        q_star, _ = probabilities(theta, Decimal(0))
        ep, eq = p[1]+2*p[2], q_star[1]+2*q_star[2]
        kl = positive_relative_entropy(p, q_star)
        work_density = kl/theta
        q0, q1, q2 = thermal
        variance_e = q0*q1 + 4*q0*q2 + q1*q2
        transverse_fisher = 4*q0*q1*q2 / variance_e
        coefficient = transverse_fisher/(2*beta)
        result = {"beta_star": theta, "beta_star_bracket_width": hi-lo,
                  "entropy_residual": uniform_divergence(q_star)-target,
                  "work_density": work_density,
                  "direct_energy_difference": ep-eq,
                  "energy_kl_identity_residual": ep-eq-work_density,
                  "quadratic_coefficient": coefficient,
                  "transverse_fisher": transverse_fisher,
                  "root_iterations": iterations, "probabilities": p,
                  "gibbs_equal_entropy_probabilities": q_star,
                  "internal_decimal_precision": ctx.prec}
        return result


def brute_force_work(n: int, model: Model, digits: int = 120) -> Decimal:
    """Independent full-spectrum rearrangement, restricted to small n.

    Enumerates all 3^n basis strings, computes Fraction log scores directly,
    sorts source eigenvalues and target energies, and sums signed assigned
    energy changes at high precision. No types, binomial coefficients, shell
    multiplicities, or positive-prefix formula are used here.
    """
    if n > 9:
        raise ValueError("Independent brute force is deliberately limited to n<=9")
    rows = []
    for state in product(range(3), repeat=n):
        energy = sum(state)
        middle = state.count(1)
        score = -model.beta*energy + model.delta*middle
        rows.append((score, energy))
    target = sorted(energy for _, energy in rows)
    rows.sort(key=lambda pair: (-pair[0], pair[1]))
    with localcontext() as ctx:
        ctx.prec = working_precision(model, digits)
        beta, delta = fraction_decimal(model.beta), fraction_decimal(model.delta)
        _, log_z = probabilities(beta, delta)
        cache: dict[Fraction, Decimal] = {}
        total = Decimal(0)
        for (score, source_energy), target_energy in zip(rows, target):
            energy_change = source_energy-target_energy
            if energy_change:
                if score not in cache:
                    cache[score] = (fraction_decimal(score)-n*log_z).exp()
                total += energy_change*cache[score]
        ctx.prec = digits
        return +total


def decimal_string(x: Decimal, digits: int = 80) -> str:
    # Do not pad an 80-digit computation with zeros to look like 120 digits.
    significant = min(digits, len(x.as_tuple().digits))
    return "0" if not x else format(x, f".{significant-1}E")


def serialize(x, digits: int = 80):
    if isinstance(x, Decimal):
        return decimal_string(x, digits)
    if isinstance(x, dict):
        return {k: serialize(v, digits) for k, v in x.items()}
    if isinstance(x, list):
        return [serialize(v, digits) for v in x]
    return x


def relative_disagreement(a: Decimal, b: Decimal) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = 160
        if not a and not b:
            return Decimal(0)
        return abs(a-b)/max(abs(a), abs(b))


def plan_metadata(plan: SpectralPlan) -> dict:
    return {"type_count": plan.type_count,
            "distinct_exact_log_weights": plan.distinct_log_weights,
            "nonnegative_work_terms": len(plan.terms),
            "matched_dimension": str(plan.matched_dimension),
            "matched_dimension_equals_3_to_n": plan.matched_dimension == 3**plan.n,
            "total_integer_energy_sums_agree":
                plan.original_energy_sum == plan.assigned_energy_sum == plan.n*3**plan.n,
            "exact_zero": plan.exact_zero}


def calculate(beta: str, delta: str, n: int, mode: str, digits: int) -> dict:
    model = Model.parse(beta, delta)
    plan = build_plan(n, model)
    iso = endpoint(model, digits)
    out = {"model": "H=(0,1,2); middle-level exponential tilt",
           "beta_input": beta, "delta_input": delta, "n": n,
           "beta_exact": str(model.beta), "delta_exact": str(model.delta),
           "first_activation_exact": model.first_activation(),
           "arithmetic": mode, "requested_decimal_digits": digits,
           "spectral_plan": plan_metadata(plan), "endpoint": iso}
    if mode == "decimal":
        work = decimal_work(plan, model, digits)
        with localcontext() as ctx:
            ctx.prec = working_precision(model, digits)
            total_resource = n*iso["work_density"]
            fraction = work/total_resource if total_resource else None
        out.update(work=work, total_asymptotic_work=total_resource,
                   recovered_fraction=fraction)
    else:
        out["float_evaluation"] = float_work(plan, model)
        denominator = float(n*iso["work_density"])
        out["recovered_fraction"] = (out["float_evaluation"]["work"]/denominator
                                     if denominator else None)
    out["arithmetic_scope"] = (
        "Ordering, multiplicities, matching, exact-zero status, and onset count are exact. "
        "Transcendental values use rounded arithmetic, not formal interval bounds. "
        "Use decimal precision escalation for tiny work; float underflow is flagged.")
    return serialize(out, digits)


def run_checks() -> dict:
    results = {"generated_at_utc": datetime.now(timezone.utc).isoformat(),
               "python_version": platform.python_version(),
               "dependencies": "Python standard library only",
               "purpose": "Focused numerical checks; not a theorem certificate",
               "precision_policy": (
                   "Large cases: 80 and 120 requested digits. Independent comparison: "
                   "100-digit compressed versus 140-digit brute force. Coefficient: "
                   "100 requested digits. Each uses 30+ adaptive guard digits. "
                   "JSON prints at most 120 significant digits, without padding."),
               "large_cases": [], "onset_cases": [],
               "independent_brute_force_cases": [], "coefficient_cases": []}

    for delta, n in [("0.1", 100), ("0.05", 400)]:
        model = Model.parse("1", delta)
        plan = build_plan(n, model)
        w80, w120 = decimal_work(plan, model, 80), decimal_work(plan, model, 120)
        disagreement = relative_disagreement(w80, w120)
        assert disagreement < Decimal("1e-75")
        iso80, iso120 = endpoint(model, 80), endpoint(model, 120)
        endpoint_disagreement = relative_disagreement(iso80["work_density"], iso120["work_density"])
        assert endpoint_disagreement < Decimal("1e-75")
        floating = float_work(plan, model)
        float_difference = relative_disagreement(Decimal.from_float(floating["work"]), w120)
        assert float_difference < Decimal("5e-11")
        with localcontext() as ctx:
            ctx.prec = 140
            fraction = w120/(n*iso120["work_density"])
        results["large_cases"].append({
            "beta_input": "1", "delta_input": delta, "n": n,
            "n_delta_squared_exact": str(n*model.delta**2),
            "first_activation_exact": model.first_activation(),
            "work_80_digits": w80, "work_120_digits": w120,
            "recovered_fraction": fraction,
            "work_relative_precision_disagreement": disagreement,
            "endpoint_relative_precision_disagreement": endpoint_disagreement,
            "float_relative_disagreement_with_120_digits": float_difference,
            "float_evaluation": floating,
            "spectral_plan": plan_metadata(plan), "endpoint": iso120})

    for beta, delta, expected in [("1", "0.1", 11), ("1", "1/11", 13),
                                  ("0.3", "0.1", 5)]:
        model = Model.parse(beta, delta)
        assert model.first_activation() == expected
        neighbors = []
        for n in [expected-2, expected-1, expected]:
            plan = build_plan(n, model)
            assert plan.exact_zero == (n < expected)
            neighbors.append({"n": n, "exact_zero": plan.exact_zero,
                              "work": decimal_work(plan, model, 80)})
        results["onset_cases"].append({"beta_input": beta, "delta_input": delta,
                                       "expected_first_activation": expected,
                                       "computed_first_activation": model.first_activation(),
                                       "neighbor_checks": neighbors})

    # Includes exact ties, Gibbs, active blocks, and a decimal which binary
    # float rounds across a relevant activation boundary.
    brute_cases = [("1", "0", 6), ("1", "0.4", 3),
                   ("1", "0.3", 5), ("1", "0.2", 7),
                   ("1", "1/3", 3),
                   ("1", "0.3333333333333333333333334", 3)]
    for beta, delta, n in brute_cases:
        model = Model.parse(beta, delta)
        plan = build_plan(n, model)
        compressed = decimal_work(plan, model, 100)
        brute = brute_force_work(n, model, 140)
        disagreement = relative_disagreement(compressed, brute)
        assert disagreement < Decimal("1e-90")
        results["independent_brute_force_cases"].append({
            "beta_input": beta, "delta_input": delta, "n": n,
            "enumerated_dimension": 3**n,
            "first_activation_exact": model.first_activation(),
            "exact_zero": plan.exact_zero, "compressed_work": compressed,
            "brute_force_work": brute, "relative_disagreement": disagreement})

    previous_error = None
    for delta in ["0.01", "0.001", "0.0001", "0.000001"]:
        model = Model.parse("1", delta)
        iso = endpoint(model, 100)
        with localcontext() as ctx:
            ctx.prec = 140
            d = fraction_decimal(model.delta)
            ratio = iso["work_density"]/(iso["quadratic_coefficient"]*d*d)
            error = abs(ratio-1)
            identity_relative = abs(iso["energy_kl_identity_residual"])/iso["work_density"]
        assert identity_relative < Decimal("1e-90")
        if previous_error is not None:
            assert error < previous_error
        previous_error = error
        results["coefficient_cases"].append({
            "beta_input": "1", "delta_input": delta,
            "work_density": iso["work_density"],
            "analytic_quadratic_coefficient": iso["quadratic_coefficient"],
            "ratio_to_coefficient_times_delta_squared": ratio,
            "energy_kl_identity_relative_residual": identity_relative,
            "entropy_residual": iso["entropy_residual"]})
    assert previous_error < Decimal("1e-4")
    results["checks_passed"] = True
    results["qualification"] = (
        "Precision agreement and brute-force comparisons are numerical evidence, "
        "not rigorous interval error bounds, external proof verification, or a proof "
        "of asymptotic exponents. Exact combinatorial assertions cover the stated "
        "finite cases only.")
    return serialize(results, 120)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    calc = commands.add_parser("calc", help="Compute one finite block")
    calc.add_argument("--beta", required=True, help="Exact decimal or rational string")
    calc.add_argument("--delta", required=True, help="Exact decimal or rational string")
    calc.add_argument("--n", required=True, type=int)
    calc.add_argument("--mode", choices=["decimal", "float"], default="decimal")
    calc.add_argument("--digits", type=int, default=80)
    check = commands.add_parser("check", help="Run the focused reproducibility checks")
    check.add_argument("--output", type=Path, default=Path(__file__).with_name("checked_cases.json"))
    args = parser.parse_args()
    if args.command == "calc":
        output = calculate(args.beta, args.delta, args.n, args.mode, args.digits)
        print(json.dumps(output, indent=2, allow_nan=False))
    else:
        output = run_checks()
        args.output.write_text(json.dumps(output, indent=2, allow_nan=False)+"\n")
        print(json.dumps({"checks_passed": True, "output": str(args.output.resolve()),
                          "large_case_count": len(output["large_cases"]),
                          "onset_case_count": len(output["onset_cases"]),
                          "brute_force_case_count": len(output["independent_brute_force_cases"]),
                          "coefficient_case_count": len(output["coefficient_cases"])}))


if __name__ == "__main__":
    main()
