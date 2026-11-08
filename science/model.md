# Model, theorem and thermodynamic normalization

The question is how large a jointly controlled block must be to recover a fixed fraction of the work available in a weakly nonthermal state. The resource is the number of copies acted on together. Work is the mean decrease of the systems' energy.

## 1. Fixed system and admissible operations

Let a fixed finite Hamiltonian have a nonconstant commensurate spectrum. After an irrelevant constant energy shift, write

```math
H=\sum_{j=1}^d E_j|j\rangle\langle j|,
\qquad E_j=gz_j,\qquad
z_j\in\mathbb Z_{\ge0},\qquad
\min_jz_j=0,\qquad \gcd(z_1,\ldots,z_d)=1,
\qquad g\gt 0.
```

The index labels individual basis states, so distinct indices can have the same energy. The Hamiltonian, dimension and lattice spacing are fixed while the perturbation tends to zero.

Fix $`\beta\gt 0`$ and the Gibbs probabilities $`q_j=e^{-\beta E_j}/Z_\beta`$. Let $`p_\delta`$ be a $`C^2`$ probability path in this fixed basis for $`0\le\delta\lt \bar\delta`$, with $`p_0=q`$. Positivity holds throughout a sufficiently small interval. The initial state is $`\rho_\delta=\mathrm{diag}(p_\delta)`$.

For an integer $`n\ge1`$, define

```math
H_n=\sum_{i=1}^n H^{(i)},\qquad
W_n(\delta)=
\mathrm{Tr}(\rho_\delta^{\otimes n}H_n)
-\min_U\mathrm{Tr}
\bigl(U\rho_\delta^{\otimes n}U^\dagger H_n\bigr).
```

The minimization permits every unitary on the supplied copies. It represents unrestricted cyclic driving with the same initial and final Hamiltonian. There is no heat bath, catalyst, refreshed ancilla, measurement, postselection or auxiliary entropy sink. The state and its parameters are known. No restriction on gate synthesis or driving time is imposed.

Unitary rearrangement pairs the largest state eigenvalues with the lowest energies. Thus a diagonal state is passive exactly when no higher-energy basis vector has strictly greater population than a lower-energy one. Probabilities within an energy degeneracy can be ordered arbitrarily. A basis permutation attains the minimum; allowing general unitaries cannot lower it further.

## 2. The nonthermal direction

Define the score and its projection away from changing temperature:

```math
f_j=\frac{p'_{0,j}}{q_j},\qquad
V=\mathrm{Var}_q(E)\gt 0,\qquad
c=\mathrm{Cov}_q(E,f),
```

```math
u_j=q_j\left[f_j-\frac{c}{V}(E_j-\mathbb E_qE)\right],
\qquad
v=\sum_j\frac{u_j^2}{q_j}
=\mathrm{Var}_q(f)-\frac{c^2}{V}.
```

Normalization gives $`\mathbb E_qf=0`$. Assume **$`v\gt 0`$**. This says that the path has a first-order component transverse to the Gibbs-temperature curve. It permits splitting populations within an energy degeneracy. For a nondegenerate two-level system the transverse subspace is absent; at least three distinct population coordinates are needed in that case.

## 3. Available work and its quadratic coefficient

Let $`q_{\beta_\delta}`$ be the locally unique positive-temperature Gibbs state with the same entropy as $`p_\delta`$. Since

```math
\frac{d}{d\beta}S(q_\beta)=-\beta\mathrm{Var}_{q_\beta}(E)\ne0,
```

the implicit-function theorem supplies a $`C^2`$ function $`\beta_\delta`$ near zero. Differentiating the entropy constraint gives

```math
\beta'_0=-\frac cV,\qquad
p_\delta-q_{\beta_\delta}=\delta u+O(\delta^2),
\qquad
\sum_j u_j=\sum_jE_ju_j=0.
```

Set

```math
w_\infty(\delta)=
\sum_j E_j\bigl(p_{\delta,j}-q_{\beta_\delta,j}\bigr).
```

The equal-entropy identity and the local expansion of relative entropy imply

```math
D(p_\delta\Vert q_{\beta_\delta})
=\beta_\delta w_\infty(\delta)
=\frac v2\delta^2+o(\delta^2),
```

```math
\boxed{\quad
w_\infty(\delta)=\frac{v}{2\beta}\delta^2+o(\delta^2)\gt 0.
\quad}
```

To see the expansion, both distributions agree at zero and their first derivatives differ by $`u`$. The Hessian of relative entropy on the open simplex gives $`\frac12\sum_j u_j^2/q_j`$. The same quadratic term holds for $`D(q_{\beta_\delta}\Vert p_\delta)`$. Only the displayed little-o remainder is used for a general $`C^2`$ path.

For every finite block,

```math
0\le W_n(\delta)\le n w_\infty(\delta).
```

Indeed the final state under a unitary has entropy $`nS(p_\delta)=nS(q_{\beta_\delta})`$. Its nonnegative relative entropy to $`q_{\beta_\delta}^{\otimes n}`$ forces its energy to be at least $`nE(q_{\beta_\delta})`$. The fixed-state asymptotic attainability
$`\lim_{n\to\infty}W_n/n=w_\infty`$ is the inherited [Alicki–Fannes result](../references/RELATED_WORK.md#alicki-fannes). The converse below does not exchange that fixed-state limit with $`\delta\to0`$.

## 4. Exact threshold theorem

For $`0\lt f\lt 1`$, define the following minima, with $`\min\varnothing=\infty`$:

```math
N_{\mathrm{act}}(\delta)=\min\{n\ge1:W_n(\delta)\gt 0\},
\qquad
N_f(\delta)=\min\{n\ge1:W_n(\delta)\ge f n w_\infty(\delta)\}.
```

For every fixed system and path satisfying the preceding assumptions:

1. $`N_{\mathrm{act}}(\delta)=\Theta(\delta^{-1})`$.
2. $`N_{1/4}(\delta)=\Theta(\delta^{-2})`$.
3. There exist $`A,B,c_0,s_0,\delta_0\gt 0`$, independent of $`n,\delta`$, such that

```math
W_n(\delta)\le A(1+Bn\delta^2)
\exp\!\left(-\frac{c_0}{n\delta^2}\right)
\quad\text{whenever}\quad
0\lt \delta\le\delta_0,\quad n\delta^2\le s_0.
```

In particular,

```math
n(\delta)\delta^2\longrightarrow0
\quad\Longrightarrow\quad
\frac{W_{n(\delta)}(\delta)}
{n(\delta)w_\infty(\delta)}\longrightarrow0.
```

The lower bound applies to every fixed positive yield fraction. The explicit construction proves sufficiency for one quarter, and therefore also gives $`N_f=\Theta(\delta^{-2})`$ for every fixed $`0\lt f\le1/4`$. No monotonicity of $`W_n/n`$ is assumed.

All constants may depend on the fixed Hamiltonian, temperature and local path. The theorem supplies neither an optimal leading constant nor a crossover function. It is not uniform over a shrinking lattice spacing or changing dimension.

For the top-level-tilted qutrit subfamily shared with Quantum-Work-Activation, that project's inherited one-third construction combines with this converse to give $`N_f=\Theta(\delta^{-2})`$ for every fixed rational spectrum and $`0\lt f\le1/3`$. The [qutrit connection](qutrit_transfer.md#2-the-fixed-rational-reconciliation) checks its hypotheses and credits both ingredients. This sharper qutrit yield does not replace the broad quarter-yield theorem for arbitrary finite spectra and transverse paths.

The same [connection](qutrit_transfer.md#5-the-specified-matched-detuning-threshold) proves the separate matched path $`\alpha_\delta=2+\nu\delta^{3/2}`$ at yield $`1/10`$. Its finite entropy comparison transfers a fixed-harmonic result; it does not apply the fixed-lattice theorem uniformly to a moving lattice.

## 5. Proof route

The [clipping lemma and concentration argument](passive_clipping.md) prove the uniform all-unitary bound and the necessary useful-block size. The [integer activation construction](activation.md) proves the first threshold. The [finite multiplicity and residue construction](useful_work.md) gives a permutation extracting a quarter of the available work at $`n=\lceil C/\delta^2\rceil`$ for one fixed sufficiently large $`C`$.

The [qutrit example](qutrit.md) gives an exact activation formula and a simple explicit converse. The [interpretation](interpretation.md) explains why the hypotheses and the distinction between mean work and other resources matter.
