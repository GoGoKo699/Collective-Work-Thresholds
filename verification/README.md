# Finite-block ergotropy: focused numerical reproduction

This directory checks the harmonic **middle-level tilt** used in the [qutrit example](../science/qutrit.md):

```math
H=\mathrm{diag}(0,1,2),\qquad
p_j=Z^{-1}\exp[-\beta j+\delta\mathbf1_{j=1}],
\qquad \beta\gt 0,\quad 0\le\delta\lt \beta.
```

Work is the maximum mean system-energy decrease under an arbitrary unitary on
the supplied block. The code computes this finite-dimensional spectral
rearrangement. It does not model a bath, catalyst, efficient circuit, control
cost, fluctuations, or postselection. It does not cover general spectra or
other perturbation directions, and it does not certify the asymptotic theorem.

## Files and commands

- `ergotropy_validate.py`: reusable module and command-line entry point.
- `checked_cases.json`: machine-readable results and focused checks.

Python 3.10 or later and only its standard library are required; the tested Python version is
recorded in the JSON. Run without Python's `-O` option so the finite-case
assertions remain enabled.

From the repository root:

```bash
python3 verification/ergotropy_validate.py check --output verification/checked_cases.json
python3 verification/ergotropy_validate.py calc --beta 1 --delta 0.1 --n 100
python3 verification/ergotropy_validate.py calc --beta 1 --delta 0.05 --n 400 --digits 120
python3 verification/ergotropy_validate.py calc --beta 1 --delta 1/11 --n 11
python3 verification/ergotropy_validate.py calc --beta 1 --delta 0.1 --n 100 --mode float
```

Parameters are **decimal or rational strings**, parsed as exact fractions.
Thus `0.1` means exactly one tenth, and `1/11` means exactly one eleventh.
The module API rejects Python float parameters. The results describe the
specified numbers; exact parsing does not remove physical calibration error.

## What is exact

For a type with middle occupation $`k_1`$ and upper occupation $`k_2`$, the
unnormalized log weight is

```math
L=-\beta(k_1+2k_2)+\delta k_1.
```

A common rational denominator converts this to an integer ordering key.
Equal keys are grouped **exactly**; no floating tolerance decides a tie.
Multinomial multiplicities, energy-shell dimensions, and the matching of
probability blocks to increasing energy are all Python integers.

The calculation verifies that exactly $`3^n`$ eigenvalues were matched and
that both complete integer energy sums equal $`n3^n`$. Exact arithmetic also
determines whether the work vanishes. The first-activation count is the
smallest odd integer **strictly greater** than $`\beta/\delta`$; it is `null`
for $`\delta=0`$. For example, $`\beta=1,\delta=1/11`$ first activates at
13 copies, so the equality boundary at 11 copies remains passive.

## Work without subtracting two large energies

Let the distinct per-microstate probabilities be $`p_1\gt \cdots\gt p_G`$.
For all groups through group $`i`$, let $`D_i`$ be their original total
energy minus the energy of the same number of lowest-energy basis states.
Both quantities include the exact multiplicities. Every $`D_i`$ is a
nonnegative integer and $`D_G=0`$. Summation by parts gives

```math
W_n=\sum_{i=1}^{G-1}D_i(p_i-p_{i+1}).
```

This is a sum of nonnegative terms. The probability difference is evaluated as
$`p_i[1-\exp(L_{i+1}-L_i)]`$, using `expm1` in float mode and a stable power
series for small gaps in Decimal mode. The calculation therefore does not
obtain tiny work by subtracting two energies of order $`n`$.

The main computation enumerates $`(n+1)(n+2)/2`$ occupation types, not
$`3^n`$ strings. Arbitrary-precision integer costs and Decimal precision still
increase with block size. The included large checks stop at $`n=400`$.

## Transcendental arithmetic and its limits

The ordering and combinatorics above are exact. Exponentials, logarithms,
probabilities, and numerical work values are rounded arithmetic.

- Default mode uses Python `decimal` at 80 requested significant digits,
  with at least 30 guard digits and extra guards for small parameters.
  `--digits 120` increases the requested precision. Small probability gaps
  use a series to avoid subtracting nearly equal numbers. Decimal underflow
  raises an exception instead of silently changing a positive value to zero.
- Float mode retains the **same exact ordering and matching**, then evaluates
  a positive log-domain sum. It reports exact-zero status separately from
  numerical underflow and reports underflowed scaled tail terms. It is not
  a way to certify arbitrarily small work.
- The JSON records differences between repeated calculations at different
  precisions. These are observed consistency checks, **not rigorous interval
  error bounds**. Requested precision alone is not a formal error guarantee.

The equal-entropy Gibbs inverse temperature is found by bracketed bisection
on divergence from the uniform distribution. This avoids cancellation in
entropies close to $`\log3`$. The work density is evaluated through the
positive expression $`D(p\Vert q_*)/\beta_*`$, using a stable nonnegative
divergence integrand near equality. The direct energy difference, entropy
residual, and relative-entropy identity residual are also recorded.

## Included results

For $`\beta=1`$, both requested cases have $`n\delta^2=1`$:

| $`\delta`$ | $`n`$ | Mean work $`W_n`$ | $`W_n/(nw_\infty)`$ |
|---:|---:|---:|---:|
| 0.1 | 100 | 0.03507712441518032594 | 0.4764445505281789 |
| 0.05 | 400 | 0.03313205766737648568 | 0.4645257230941980 |

The 80-versus-120-digit work calculations differed by less than
$`7\times10^{-81}`$ relatively in these runs. Float-mode results differed
from the high-precision results by less than $`8\times10^{-15}`$ relatively
for these two cases. Those observations do not establish universal error
bounds or an asymptotic crossover.

The focused `check` command also verifies:

1. **Exact activation boundaries:** three rational/decimal parameter pairs,
   checked at the two immediately preceding block sizes and at the predicted
   first activating odd block. This includes an exact equality tie and a
   decimal ratio whose binary-float representation is hazardous.
2. **Independent small-block rearrangement:** six cases enumerate every one
   of $`3^n`$ strings and sort exact Fraction log scores and target energies.
   This implementation uses neither type multiplicities nor the nonnegative
   prefix formula. High-precision signed work sums agree with the compressed
   method. Enumeration is deliberately restricted to $`n\le9`$.
3. **A tiny positive onset:** at $`n=3`$,
   `delta=0.3333333333333333333333334` gives
   $`W_3\approx6.0391345806368145\times10^{-27}`$, whereas exact `delta=1/3`
   gives zero. This checks the actual probability-ordering risk.
4. **The same-entropy quadratic coefficient:** at $`\beta=1`$,
   $`v/(2\beta)\approx0.06907222732952539`$. The computed ratio
   $`w_\infty/[v\delta^2/(2\beta)]`$ approaches one from
   1.00646557 at $`\delta=.01`$ to 1.00000064513 at $`\delta=10^{-6}`$.
   Entropy and energy/relative-entropy residuals accompany the values.

These checks address ordering, multiplicity transport, cancellation, the
endpoint calculation, and strict activation boundaries. They are finite
numerical evidence, not a replacement for the analytic converse or
achievability proof.


## Hosted mathematical rendering

The [read-only GitHub workflow](../.github/workflows/hosted-math.yml) checks the actual commit-pinned GitHub pages. Its [capture script](hosted/capture_hosted_math.cjs) and [source checker](hosted/check_rendered_math.py) inventory every tracked Markdown page, compile reference MathML, and compare all rendered inline and display expressions at viewport widths 1440 and 760 pixels. The dependencies are Playwright 1.56.1 and MathJax 3.2.1, with Node.js 18+ and Python 3.10+.

The job retains the source inventory, HTML, screenshots, structural comparisons and `hosted-report.json` as a short-lived Actions artifact, including failed attempts. It needs only repository read permission and uses a fresh anonymous browser. A run on a different commit is a separate observation; a successful source-only check is not a hosted rendering result.

The comparison checks expression coverage, symbols, structural slots, source hashes and display geometry. The [text contracts](hosted/math-contract.json) additionally protect headline formulas and expressions previously affected by renderer defects. A passing automated report still requires visual inspection of important formulas, tables and navigation against the same source. It establishes neither scientific correctness nor a guarantee about future GitHub rendering. Local execution requires an environment that can validate the GitHub HTTPS connection; certificate checks must remain enabled.

For a local capture, install the pinned packages in a temporary dependency directory, install Chromium through Playwright, and run the collector with `--root`, `--repository`, `--revision` (the full commit SHA), `--output` (a new empty evidence directory), and `--contract verification/hosted/math-contract.json`. Optional repeated `--page` arguments restrict diagnostic samples and need a correspondingly restricted contract; final review should cover the complete reader-facing scope. The workflow pins Ubuntu 24.04 for compatibility with these browser dependencies.
