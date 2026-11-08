# Qutrit work, attribution and matched detuning

The fixed-lattice converse in this repository and the one-third construction in [Quantum-Work-Activation](https://github.com/GoGoKo699/Quantum-Work-Activation) resolve the same fixed-rational qutrit problem. Their combination also provides the inherited ingredients for a controlled moving-spectrum result. The finite entropy comparison below supplies the additional step; a fixed-lattice theorem is not applied directly to a shrinking product gap.

## 1. The shared qutrit model

Fix $`\beta\gt0`$, set the first excitation energy to one, and use natural logarithms. Define

```math
H_\alpha=\mathrm{diag}(0,1,\alpha),\qquad
K=\mathrm{diag}(0,0,1),\qquad
\rho_{\delta,\alpha}
=\frac{e^{-\beta H_\alpha+\delta K}}{Z_{\delta,\alpha}},
\qquad \alpha\gt1,\quad\delta\gt0.
```

For sufficiently small $`\delta`$ this state is single-copy passive. It differs from this repository's [middle-level-tilted example](qutrit.md), which remains a separate useful activation example.

Let $`W_n(\delta;\alpha)`$ be the maximum mean decrease of the additive Hamiltonian $`H_\alpha^{(n)}`$ under a unitary on $`n`$ independent copies. The operations and resources are those in the [model](model.md#1-fixed-system-and-admissible-operations): no bath, catalyst, ancillary machine, feedback or discarded subsystem. Let $`w_\infty(\delta;\alpha)`$ be the energy difference to the positive-temperature Gibbs state of the **actual** $`H_\alpha`$ with the same entropy. Set

```math
N_f(\delta;\alpha)=\min\{n\ge1:
W_n(\delta;\alpha)\ge f n w_\infty(\delta;\alpha)\}.
```

## 2. The fixed-rational reconciliation

For every fixed rational $`\alpha=a/b\gt1`$ in lowest terms and fixed $`0\lt f\le1/3`$,

```math
\boxed{N_f(\delta;\alpha)=\Theta(\delta^{-2}).}
```

The two proof ingredients have different owners:

| Ingredient | Authoritative source |
|---|---|
| All-unitary lower bound $`N_f=\Omega(\delta^{-2})`$, for every fixed $`f\gt0`$ | This repository's [passive-clipping converse](passive_clipping.md#4-the-uniform-work-bound) |
| Constructive upper bound $`N_f=O(\delta^{-2})`$, for $`0\lt f\le1/3`$ | Quantum-Work-Activation's [one-third type-matching construction](https://github.com/GoGoKo699/Quantum-Work-Activation/blob/3fb4500d87acdb60746e10a9a5ae5917a2b698ec/science/achievability.md) |

For the converse, $`H_\alpha`$ has fixed lattice spacing $`1/b`$. The analytic state path has score $`K-\langle K\rangle_\gamma`$, where $`\gamma=\gamma_{\beta,\alpha}`$. Its transverse variance is

```math
R_{\alpha,\beta}=\mathrm{Var}_{\gamma}(K)
-\frac{\mathrm{Cov}_{\gamma}(H_\alpha,K)^2}
{\mathrm{Var}_{\gamma}(H_\alpha)}\gt0.
```

It is positive because $`K`$ is not affine in $`H_\alpha`$ on the three positive-probability levels. Thus every hypothesis of the [general model](model.md) is satisfied. The lower bound removes the logarithmic loss in QWA's earlier rational estimate; its combination with QWA's construction is a reconciliation of inherited results, not another discovery of either ingredient. The general CWT quarter-yield theorem retains its broader finite-spectrum and $`C^2`$-path scope.

## 3. An entropy comparison for the actual matched state

Let $`\epsilon\ge0`$ and $`t=\delta-\beta\epsilon\gt0`$. The state prepared for the actual detuned Hamiltonian obeys the exact identity

```math
\rho_{\delta,2+\epsilon}=\rho_{t,2}.
```

For every integer $`n\ge1`$,

```math
\boxed{
W_n(t;2)\le W_n(\delta;2+\epsilon)
\le W_n(t;2)+\frac12 n\epsilon\delta.
}
```

Here the same input is evaluated under two different energy objectives. To see why entropy controls their difference, put $`P=\rho_{\delta,2+\epsilon}^{\otimes n}`$, $`\sigma=UPU^\dagger`$, $`K_n=\sum_jK_j`$, and $`L=\mathrm{Tr}[K_n(P-\sigma)]`$. If $`W_\epsilon(U)`$ and $`W_0(U)`$ are this unitary's actual and harmonic work, then

```math
W_\epsilon(U)=W_0(U)+\epsilon L,
\qquad
D(\sigma\Vert P)=\delta L-\beta W_\epsilon(U)
=tL-\beta W_0(U).
```

The second identity uses unitary entropy invariance and the logarithm of the actual product input. If $`\sigma_j`$ is its $`j`$th marginal, entropy subadditivity, local binary measurement data processing and Pinsker's inequality in nats give

```math
\begin{aligned}
D(\sigma\Vert P)&\ge\sum_jD(\sigma_j\Vert\rho_{\delta,2+\epsilon}),\\
\sum_jD(\sigma_j\Vert\rho_{\delta,2+\epsilon})
&\ge2\sum_j\left(\mathrm{Tr}[K(\rho_{\delta,2+\epsilon}-\sigma_j)]\right)^2
\ge\frac{2L^2}{n}.
\end{aligned}
```

This applies even when the output is coherent and correlated. The measurement is a mathematical proof device; the extraction protocol performs only its prescribed unitary. For an actual-work optimizer, $`W_\epsilon\ge0`$, so $`0\le L\le n\delta/2`$, giving the upper comparison. For a harmonic optimizer, $`W_0\ge0`$ and $`tL=D+\beta W_0\ge0`$, giving the lower comparison. No block-size restriction or monotonicity of yield is used.

## 4. Normalize by the actual Hamiltonian

The equal-entropy Gibbs equation has a smooth solution uniformly for $`\alpha`$ in a fixed compact neighborhood of 2: its inverse-temperature derivative is $`-\beta_*\mathrm{Var}(H_\alpha)\ne0`$. The [quadratic normalization argument](model.md#3-available-work-and-its-quadratic-coefficient), applied to the analytic qutrit family, therefore gives

```math
w_\infty(\delta;\alpha)
=\frac{R_{\alpha,\beta}}{2\beta}\delta^2+O(\delta^3)
```

with a uniform remainder in that neighborhood. Write

```math
x=e^{-\beta},\qquad Z_0=1+x+x^2,\qquad
R_2=\frac{x^2}{Z_0(1+4x+x^2)},\qquad \gamma_1=\frac{x}{Z_0}.
```

For $`\epsilon=\nu\delta^{3/2}`$ with fixed $`\beta,\nu\gt0`$, smoothness of $`R_{\alpha,\beta}`$ yields

```math
w_\infty(\delta;2+\epsilon)
=\frac{R_2}{2\beta}\delta^2+O(\delta^3),
\qquad
w_\infty(t;2)=\frac{R_2}{2\beta}t^2+O(t^3).
```

Consequently

```math
\frac{w_\infty(t;2)}{w_\infty(\delta;2+\epsilon)}
=1-2\beta\nu\sqrt\delta+O(\delta).
```

```math
\frac{\epsilon\delta}{2w_\infty(\delta;2+\epsilon)}
=\frac{\beta\nu}{R_2}\sqrt\delta+O(\delta^{3/2}).
```

The second expression is the comparison error divided by the actual available work per copy. It vanishes independently of $`n`$. Replacing the actual benchmark by the effective harmonic benchmark without this check would omit a physical change in the energy objective.

## 5. The specified matched-detuning threshold

For every fixed $`\beta,\nu\gt0`$,

```math
\boxed{
N_{1/10}(\delta;2+\nu\delta^{3/2})=\Theta(\delta^{-2}).
}
```

For necessity, choose a fixed sufficiently small CWT forbidden window in $`nt^2`$ so that its harmonic work fraction is below $`1/40`$. Since $`t/\delta\to1`$, the benchmark ratio tends to one and the normalized additive error tends to zero, all integers with $`n\delta^2\le c`$ fail fraction $`1/10`$ for one fixed sufficiently small $`c\gt0`$ and all sufficiently small $`\delta`$. This proves a lower bound on the minimum, rather than just on one chosen sequence.

For sufficiency, QWA's harmonic construction supplies one block $`n\le C/t^2`$ with $`W_n(t;2)\ge n w_\infty(t;2)/3`$. The lower comparison and the benchmark ratio then give an actual fraction above $`1/10`$ for all sufficiently small $`\delta`$. Transferring a bare one-third guarantee proves every fixed fraction strictly below one third; no endpoint claim at one third is needed here.

This result concerns this matched positive-detuning path. It does not classify every vanishing detuning or supply a full crossover function. QWA's fixed-irrational results retain their own hypotheses and are not used in this proof.

## 6. Keep the order-delta two-copy boundary

QWA's inherited [two-copy counterexample](https://github.com/GoGoKo699/Quantum-Work-Activation/blob/3fb4500d87acdb60746e10a9a5ae5917a2b698ec/science/calibration.md#5-harmonic-resonance-an-exact-two-copy-boundary) prevents a uniform extension of the fixed-harmonic theorem to every order-$`\delta`$ neighborhood. For sufficiently small positive $`\epsilon`$ and $`0\lt t\lt\beta`$, swapping $`|11\rangle`$ with one of $`|02\rangle,|20\rangle`$ is optimal and gives

```math
W_2(\delta;2+\epsilon)
=\epsilon\frac{x^2}{(1+x+x^2e^t)^2}(e^t-1).
```

At $`\epsilon=\delta/(8\beta)`$, its actual normalized yield tends to $`7(1+3\gamma_1)/64\gt1/10`$, so $`N_{1/10}=2`$ eventually. The entropy-comparison error is then order one after normalization and gives no contradiction.

For the specified $`\epsilon=\nu\delta^{3/2}`$ path, the same exact formula instead gives

```math
\frac{W_2(\delta;2+\nu\delta^{3/2})}
{2w_\infty(\delta;2+\nu\delta^{3/2})}
=\beta\nu(1+3\gamma_1)\sqrt\delta+O(\delta)\longrightarrow0.
```

Thus first activation occurs at two copies on this moving path, while useful mean work still requires order $`\delta^{-2}`$ copies. The original fixed-lattice activation theorem remains unchanged.
