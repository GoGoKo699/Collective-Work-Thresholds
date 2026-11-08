#!/usr/bin/env python3
"""Bounded independent finite checks of the harmonic/detuned comparison.

Uses only the Python standard library. Microstates are explicitly enumerated
for n<=8. Energy and negative-log-population ordering use exact Fraction keys;
probabilities and equal-entropy Gibbs benchmarks use 80-digit Decimal numbers.
These are numerical consistency checks, not interval-certified proof.
"""

from __future__ import annotations

import argparse
import itertools
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path


PRECISION = 80
TOL = Decimal("1e-65")


def dec(q):
    q = Fraction(q)
    return Decimal(q.numerator) / Decimal(q.denominator)


def probabilities(beta, delta, epsilon):
    beta, delta, epsilon = map(dec, (beta, delta, epsilon))
    weights = (Decimal(1), (-beta).exp(), (-beta * (2 + epsilon) + delta).exp())
    z = sum(weights)
    return tuple(w / z for w in weights)


def full_work(n, beta, delta, epsilon, harmonic_objective=False):
    """Enumerate all 3**n microstates with exact rational ordering keys."""
    beta, delta, epsilon = map(Fraction, (beta, delta, epsilon))
    assert n <= 8 and delta - beta * epsilon > 0
    alpha = Fraction(2) if harmonic_objective else Fraction(2) + epsilon
    p = probabilities(beta, delta, epsilon)
    rows = []
    for state in itertools.product(range(3), repeat=n):
        k1, k2 = state.count(1), state.count(2)
        energy = k1 + alpha * k2
        # The state is always the SAME actual matched input, including when
        # its work is evaluated with the harmonic objective.
        score = beta * (k1 + (2 + epsilon) * k2) - delta * k2
        probability = p[0] ** (n - k1 - k2) * p[1] ** k1 * p[2] ** k2
        rows.append((energy, score, probability))
    initial = sum(dec(e) * probability for e, _, probability in rows)
    sorted_energies = sorted(e for e, _, _ in rows)
    sorted_populations = [row[2] for row in sorted(rows, key=lambda row: row[1])]
    passive = sum(dec(e) * probability for e, probability in zip(sorted_energies, sorted_populations))
    work = initial - passive
    assert work >= -TOL
    return max(work, Decimal(0))


def benchmark(beta, delta, epsilon):
    beta, delta, epsilon = map(dec, (beta, delta, epsilon))
    energies = (Decimal(0), Decimal(1), Decimal(2) + epsilon)
    weights = tuple((-beta * e + delta * int(i == 2)).exp() for i, e in enumerate(energies))
    z = sum(weights)
    p = tuple(w / z for w in weights)
    entropy = -sum(v * v.ln() for v in p)

    def gibbs(b):
        w = tuple((-b * e).exp() for e in energies)
        return tuple(v / sum(w) for v in w)

    lo, hi = Decimal(0), max(Decimal(1), 2 * beta)
    while -sum(v * v.ln() for v in gibbs(hi)) > entropy:
        hi *= 2
    for _ in range(280):
        middle = (lo + hi) / 2
        g = gibbs(middle)
        if -sum(v * v.ln() for v in g) > entropy:
            lo = middle
        else:
            hi = middle
    bstar = (lo + hi) / 2
    g = gibbs(bstar)
    d = sum(v * (v / w).ln() for v, w in zip(p, g))
    return d / bstar


def harmonic_constants(beta):
    x = (-dec(beta)).exp()
    z = 1 + x + x * x
    gamma1 = x / z
    r2 = x * x / (z * (1 + 4 * x + x * x))
    return x, gamma1, r2


def two_copy_formula(beta, delta, epsilon):
    beta_d, delta_d, epsilon_d = map(dec, (beta, delta, epsilon))
    x = (-beta_d).exp()
    t = delta_d - beta_d * epsilon_d
    z = 1 + x + x * x * t.exp()
    return epsilon_d * x * x / (z * z) * (t.exp() - 1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(Path(__file__).with_name("verification_results.json")))
    args = parser.parse_args()
    results = {
        "method": "Full microstate enumeration n<=8; exact Fraction ordering; 80-digit Decimal arithmetic; 280-step equal-entropy root bisection",
        "limitations": "Numerical consistency checks only; no interval-certified arithmetic and no asymptotic proof or crossover inference.",
        "sandwich_cases": [], "normalization_cases": [], "two_copy_cases": []
    }
    with localcontext() as context:
        context.prec = PRECISION
        # Include blocks with positive harmonic work, not only passive cases.
        for beta in map(Fraction, ("0.3", "1", "3")):
            delta = 3 * beta / 5
            for epsilon in map(Fraction, ("0.05", "0.15")):
                t = delta - beta * epsilon
                for n in (2, 5, 8):
                    w0 = full_work(n, beta, delta, epsilon, True)
                    we = full_work(n, beta, delta, epsilon)
                    error = dec(n * epsilon * delta / 2)
                    assert w0 <= we + TOL
                    assert we <= w0 + error + TOL
                    results["sandwich_cases"].append({
                        "beta": str(beta), "delta": str(delta), "epsilon": str(epsilon),
                        "t": str(t), "n": n, "harmonic_work": str(w0),
                        "actual_work": str(we), "upper_additive_error": str(error),
                        "lower_margin": str(we - w0), "upper_margin": str(w0 + error - we)
                    })
            x, gamma1, r2 = harmonic_constants(beta)
            for delta in map(Fraction, ("0.04", "0.01", "0.0025", "0.000625")):
                # These delta values have rational square roots, making all
                # state and energy ordering keys exactly rational.
                root = Fraction(str(dec(delta).sqrt()))
                assert root * root == delta
                epsilon = delta * root  # fixed nu=1
                t = delta - beta * epsilon
                assert t > 0
                wa = benchmark(beta, delta, epsilon)
                wh = benchmark(beta, t, Fraction(0))
                leading = r2 * dec(delta) ** 2 / (2 * dec(beta))
                results["normalization_cases"].append({
                    "beta": str(beta), "nu": "1", "delta": str(delta),
                    "epsilon": str(epsilon), "actual_benchmark": str(wa),
                    "harmonic_effective_benchmark": str(wh),
                    "actual_over_leading_coefficient": str(wa / leading),
                    "harmonic_over_actual": str(wh / wa),
                    "first_order_ratio_prediction": str(1 - 2 * dec(beta) * dec(root)),
                    "normalized_comparison_error": str(dec(epsilon * delta) / (2 * wa))
                })
            for power in ("order_delta", "order_delta_3_over_2"):
                for delta in map(Fraction, ("0.01", "0.0025", "0.000625")):
                    if power == "order_delta":
                        nu = 1 / (8 * beta)
                        epsilon = nu * delta
                        prediction = Decimal(7) / 64 * (1 + 3 * gamma1)
                        scale = Decimal(1)
                    else:
                        nu = Fraction(1)
                        root = Fraction(str(dec(delta).sqrt()))
                        epsilon = delta * root
                        prediction = dec(beta) * (1 + 3 * gamma1)
                        scale = dec(root)
                    exact_enumerated = full_work(2, beta, delta, epsilon)
                    closed = two_copy_formula(beta, delta, epsilon)
                    assert abs(exact_enumerated - closed) < TOL
                    wa = benchmark(beta, delta, epsilon)
                    fraction = exact_enumerated / (2 * wa)
                    if power == "order_delta":
                        assert fraction > Decimal("0.1")
                    results["two_copy_cases"].append({
                        "regime": power, "beta": str(beta), "nu": str(nu),
                        "delta": str(delta), "epsilon": str(epsilon),
                        "enumerated_work": str(exact_enumerated), "closed_work": str(closed),
                        "absolute_formula_difference": str(abs(exact_enumerated - closed)),
                        "actual_recovered_fraction": str(fraction),
                        "fraction_divided_by_scale": str(fraction / scale),
                        "predicted_limit_after_scaling": str(prediction)
                    })
        results["summary"] = {
            "sandwich_cases_passed": len(results["sandwich_cases"]),
            "normalization_cases_computed": len(results["normalization_cases"]),
            "two_copy_formula_cases_passed": len(results["two_copy_cases"]),
            "positive_harmonic_work_cases": sum(Decimal(r["harmonic_work"]) > TOL for r in results["sandwich_cases"]),
            "maximum_two_copy_formula_absolute_error": str(max(Decimal(r["absolute_formula_difference"]) for r in results["two_copy_cases"])),
            "all_assertions_passed": True
        }
    Path(args.output).write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results["summary"], indent=2))


if __name__ == "__main__":
    main()
