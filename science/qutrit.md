# An equally spaced qutrit

The three-level model makes the distinction between activation and useful work explicit:

```math
H=\mathrm{diag}(0,1,2),\qquad
p_\delta=\frac{(1,e^{-\beta+\delta},e^{-2\beta})}
{1+e^{-\beta+\delta}+e^{-2\beta}},
\qquad 0\lt \delta\lt \beta.
```

The state is passive for one copy. The perturbation increases the middle-level population; it is transverse to the Gibbs curve.

## 1. Exact first activation

For a basis string, let $`A`$ count its middle-level occupations and let $`E`$ be its total integer energy. Its unnormalized logarithmic population is $`-\beta E+\delta A`$.

For two strings with energy difference $`h\gt 0`$, inversion requires

```math
\begin{aligned}
\delta\,\Delta A&\gt \beta h.
\end{aligned}
\tag{1}
```

The parity relation is $`\Delta A\equiv h\pmod2`$, and $`\Delta A\le n`$. Let $`L_n`$ be the largest odd integer at most $`n`$. At $`h=1`$, the largest possible middle-level difference is exactly $`L_n`$:

- For odd $`n`$, the high-energy string has all $`n`$ entries in the middle level. The low-energy string has $`(n+1)/2`$ zero-energy entries and $`(n-1)/2`$ top-level entries.
- For even $`n`$, use $`n-1`$ middle-level entries and one zero for the high-energy string, and a zero/top string of energy $`n-2`$ for the low-energy string.

For $`h\ge2`$, the ratio $`\Delta A/h\le n/2\le L_n`$. Hence an inversion exists if and only if $`\delta L_n\gt \beta`$. Therefore

```math
\boxed{\quad
N_{\mathrm{act}}(\delta)
=\min\{m\in\mathbb Z_{\gt 0}:m\text{ odd and }m\gt \beta/\delta\}.
\quad}
```

At equality the populations tie and the block remains passive. For example, $`\beta=1,\delta=0.1`$ first activates at 11 copies; $`\delta=0.05`$ first activates at 21.

## 2. Explicit normalization and converse

Let $`q`$ be the Gibbs distribution at $`\delta=0`$ and $`A_j=\mathbf1_{\{j=1\}}`$. The transverse coefficient is

```math
v=\mathrm{Var}_q(A)
-\frac{\mathrm{Cov}_q(E,A)^2}{\mathrm{Var}_q(E)}\gt 0,
\qquad
w_\infty(\delta)=\frac{v}{2\beta}\delta^2+O(\delta^3).
```

Here analyticity permits the stronger cubic remainder. Set
$`\psi(t)=\log(1-q_1+q_1e^t)`$. The one-copy likelihood has range exactly $`\delta`$, while

```math
\begin{aligned}
D(p_\delta\Vert q)
&=\int_0^\delta t\,\psi''(t)\,dt,\\
D(q\Vert p_\delta)
&=\int_0^\delta(\delta-t)\,\psi''(t)\,dt.
\end{aligned}
```

Because $`\psi''(t)\le1/4`$, the [general converse](passive_clipping.md) admits $`R=1,M=1/8,g=1`$. Thus, with $`s=n\delta^2`$,

```math
\boxed{
W_n(\delta)\le
\frac2\beta
\left(\frac{2s}{\beta}+e^{-\beta/4}\right)
\exp\!\left(-\frac{\beta^2}{32s}\right),
\qquad 0\lt s\le\beta.
}
```

For any sequence $`n\delta\to C\gt \beta`$, the explicit inversion has a probability-ratio margin tending to $`e^{C-\beta}\gt 1`$. Its probability is exponentially small in $`1/\delta`$. Together with the converse, this gives the exponential work order at a fixed factor beyond onset.

## 3. Why exact onset needs a qualification

Let $`n`$ tend to infinity through odd integers and choose

```math
\varepsilon_n=e^{-n^2},\qquad
\delta_n=\frac{\beta+\varepsilon_n}{n}.
```

For all sufficiently large odd $`n`$, the first activating block is $`n`$. A gap of at least two cannot invert because $`n\delta_n\lt 2\beta`$. For a gap of one, the next permitted middle-level difference below $`n`$ is $`n-2`$, which still fails (1). Thus the only inversion moves the unique all-middle-level population across the energy-one boundary to the zero/top strings of energy $`n-1`$. Its entire ergotropy is

```math
W_n(\delta_n)=p_{\delta_n}(1)^n
\left[1-e^{-\varepsilon_n}\right]\le e^{-n^2}.
```

Since $`\delta_n\sim\beta/n`$, no uniform $`e^{-\Theta(1/\delta)}`$ lower bound holds at the exact first activation. In numerical work the bracket should be evaluated as $`-\mathrm{expm1}(-\varepsilon_n)`$ or symbolically.

## 4. Finite rearrangement

A type $`k=(k_0,k_1,k_2)`$ has exact multiplicity $`n!/(k_0!k_1!k_2!)`$, energy $`k_1+2k_2`$, and log-weight $`-\beta(k_1+2k_2)+\delta k_1`$. Sorting these populations against the integer energy-shell capacities computes the optimal ergotropy without listing all $`3^n`$ strings. The count arithmetic can be exact even though the normalized probability arithmetic is numerical.

Finite calculations illustrate the theorem; the all-unitary converse and asymptotic threshold are established by the proofs. Tiny positive work must be distinguished from floating-point cancellation, especially near a strict population tie.


The [reproduction module](../verification/README.md) groups equal log-weights exactly. If $`D_i`$ is the total original energy of the $`i`$ highest-population groups minus the minimum energy of the same number of basis states, then $`D_i`$ is a nonnegative integer. Summation by parts gives

```math
W_n=\sum_{i=1}^{G-1}D_i(P_i-P_{i+1}),
```

where $`P_1\gt \cdots\gt P_G`$ are their normalized probabilities per microstate. This positive sum avoids subtracting two energies of order $`n`$. Decimal or rational parameter strings preserve exact population ties; transcendental probability arithmetic remains rounded and its precision is checked separately.

For $`\beta=1`$, the committed high-precision calculations give:

| Perturbation | Copies | Scaled block $`n\delta^2`$ | Mean work | Fraction of $`nw_\infty`$ |
|---:|---:|---:|---:|---:|
| 0.1 | 100 | 1 | 0.03507712441518033 | 0.4764445505281789 |
| 0.05 | 400 | 1 | 0.03313205766737649 | 0.4645257230941980 |

The work values are in units of the one-level spacing. Their agreement across numerical precisions is an observed consistency check, not a rigorous interval guarantee. The code and [machine-readable results](../verification/checked_cases.json) also check strict onset and the quadratic same-entropy coefficient. Two equal scaled-block values do not establish a universal crossover function.
