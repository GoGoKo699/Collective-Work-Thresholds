# From Watrous to collective work thresholds

Imagine many identical three-level systems, each prepared with known populations close to thermal equilibrium. One system may offer no work under cyclic driving, yet a joint operation on several systems can lower their mean energy. The question is how many copies must be controlled together before that energy decrease becomes a useful fraction of the available work.

There are two different thresholds. One concerns the first pair of populations that can profitably be exchanged. The other concerns rearranging enough probability mass to recover a fixed fraction of the thermodynamic resource. This bridge develops that distinction from the selected textbook. The [model and theorem](../science/model.md) remain authoritative for the assumptions and claims; the [30-milestone map](MILESTONES.md) organizes the connected understanding targets.

## The selected anchor

The educational anchor is **John Watrous, _The Theory of Quantum Information_, Cambridge University Press, 2018**. The [author's page](https://cs.uwaterloo.ca/~watrous/TQI/) provides a pre-publication manuscript and individual chapters. Section and theorem numbers below refer to that author manuscript. The relevant passages support the following connections; the thermodynamic derivations are supplied here and in the linked science pages.

| Watrous passage | Connection developed in this project |
|---|---|
| [§2.1.1–2 and §2.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Density matrices, independent copies and unitary operations become a model of mean work. |
| [§4.3.1–2, especially Theorem 4.28](https://cs.uwaterloo.ca/~watrous/TQI/TQI.4.pdf) | Doubly stochastic matrices and majorization explain why passive sorting solves the unitary optimization. |
| [§5.1 and §5.2.1–2, especially Propositions 5.19–5.22](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf) | Entropy invariance, additivity and relative-entropy positivity become thermodynamic energy bounds. |
| [§§5.1–5.2, Theorems 5.15, 5.35 and 5.38](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf) | Data processing and Pinsker bound a collective occupation change, allowing actual and harmonic work to be compared. |
| [§1.2.2, Theorem 1.16](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf) | Concentration of bounded independent variables controls product likelihoods while the state itself approaches equilibrium. |

### Translate notation before using entropy as energy

Watrous uses $`H(\rho)`$ for entropy and base-two logarithms. This project reserves $`H`$ for the Hamiltonian, writes entropy as $`S`$, and uses natural logarithms. If $`H_{\mathrm{book}}`$ and $`D_{\mathrm{book}}`$ denote the book's entropy quantities, then

```math
S(\rho)=(\ln 2)H_{\mathrm{book}}(\rho),
\qquad
D(\rho\Vert\sigma)=(\ln 2)D_{\mathrm{book}}(\rho\Vert\sigma).
```

Hereafter $`\log=\ln`$. We write the adjoint as $`U^\dagger`$, where Watrous writes $`U^*`$. The states and transformations are the same mathematical objects. Boltzmann's constant is set to one, so inverse temperature $`\beta`$ has units of inverse energy. An identity such as $`D=\beta w`$ uses entropy in nats; in the book's units it reads $`D_{\mathrm{book}}=\beta w/\ln 2`$.

## States, spectra and work

A density matrix is a positive semidefinite matrix with trace one. For a state diagonal in an energy eigenbasis, the matrix and its physical interpretation are

```math
\rho=\sum_j p_j\lvert j\rangle\langle j\rvert,
\qquad
H=\sum_j E_j\lvert j\rangle\langle j\rvert,
\qquad
\mathrm{Tr}(\rho H)=\sum_j p_jE_j.
```

The probabilities describe occupations; the Hamiltonian assigns energies. Independent copies have state $`\rho^{\otimes n}`$ and additive Hamiltonian $`H_n=\sum_{i=1}^n H^{(i)}`$. A basis string $`x=(x_1,\ldots,x_n)`$ therefore has probability $`P(x)=\prod_i p_{x_i}`$ and energy $`E(x)=\sum_iE_{x_i}`$.

Under cyclic driving the Hamiltonian is the same before and after the operation, while the state changes to $`U\rho^{\otimes n}U^\dagger`$. Its spectrum and entropy are unchanged. The extracted mean work is the initial mean energy minus the final mean energy. Maximizing over all unitaries defines the ergotropy $`W_n`$.

Why does this optimization reduce to sorting? For a diagonal input, the final diagonal entries satisfy

```math
r_i=\sum_j A_{ij}p_j,
\qquad
A_{ij}=\lvert\langle i\lvert U\rvert j\rangle\rvert^2.
```

Unitarity makes every row and column of $`A`$ sum to one. The Birkhoff–von Neumann theorem, Watrous's Theorem 4.28, expresses any such doubly stochastic matrix as a convex combination of permutation matrices. Because mean energy is linear, this combination cannot beat its best permutation. A permutation is itself a valid unitary, so the bound is attained. This argument uses only that unitary-induced matrices are doubly stochastic; it does not assume the converse for every matrix.

To identify the best permutation, consider two levels with $`E_j\gt E_i`$. If their populations obey $`p_j\gt p_i`$, exchanging them extracts

```math
(E_j-E_i)(p_j-p_i)\gt0.
```

Repeating these improvements places larger probabilities at lower energies. A state already arranged this way is **passive**. Population ties give zero work, and ordering within a degenerate energy shell has no energy cost. Majorization supplies the general connection between unitary motion and mixing of diagonal entries; the energy assignment selects the minimizing order. The [model](../science/model.md#1-fixed-system-and-admissible-operations) states this for the entire product space.

## A complete three-copy swap

Measure energies in units of the level spacing and take

```math
H=\mathrm{diag}(0,1,2),
\qquad
p_\delta=
\frac{(1,e^{-\beta+\delta},e^{-2\beta})}
{1+e^{-\beta+\delta}+e^{-2\beta}}.
```

At $`\beta=\ln4`$ and $`\delta=\ln2`$, these probabilities are exactly

```math
p=\left(\frac{16}{25},\frac8{25},\frac1{25}\right).
```

They decrease with energy, so one copy is passive. On three copies, exchange just the basis states $`\lvert111\rangle`$ and $`\lvert002\rangle`$, leaving the other 25 basis states fixed.

| Basis state | Energy | Initial probability | Final probability |
|---|---:|---:|---:|
| $`\lvert111\rangle`$ | 3 | $`512/15625`$ | $`256/15625`$ |
| $`\lvert002\rangle`$ | 2 | $`256/15625`$ | $`512/15625`$ |

This is one unitary on the original systems. Its mean energy decrease is

```math
W_{\mathrm{swap}}
=(3-2)\left(\frac{512}{15625}-\frac{256}{15625}\right)
=\frac{256}{15625}=0.016384.
```

The lower-energy target was already occupied. Its reverse transition costs energy, which is why the two probabilities must be subtracted. In an energy-transition description, the work is $`+1`$ with probability $`512/15625`$, $`-1`$ with probability $`256/15625`$, and zero otherwise. The positive quantity above is their mean. No measured outcome determines the applied operation.

For the whole qutrit family, this particular pair has probability ratio

```math
\frac{P_\delta(111)}{P_\delta(002)}=e^{3\delta-\beta}.
```

It yields positive work exactly when $`3\delta\gt\beta`$. Equality is a tie. The [exact activation formula](../science/qutrit.md#1-exact-first-activation) gives three as the first activating block for the chosen parameters; two copies remain passive. This finite example makes activation concrete. Recovering a fixed fraction near equilibrium requires the later argument about probability mass.

## Entropy and the available work

The textbook's entropy identities now acquire an energy interpretation. For a Gibbs state

```math
q_\gamma=\frac{e^{-\gamma H}}{Z_\gamma},
\qquad
Z_\gamma=\mathrm{Tr}(e^{-\gamma H}),
```

expanding the definition of relative entropy gives, for any normalized state $`\tau`$,

```math
D(\tau\Vert q_\gamma)
=-S(\tau)+\gamma\,\mathrm{Tr}(\tau H)+\log Z_\gamma.
```

If $`S(\tau)=S(q_\gamma)`$, this becomes

```math
D(\tau\Vert q_\gamma)
=\gamma\left[\mathrm{Tr}(\tau H)-\mathrm{Tr}(q_\gamma H)\right].
```

For $`\gamma\gt0`$, relative-entropy positivity therefore says that the Gibbs state minimizes energy among states with that entropy. Watrous's Proposition 5.22 supplies the positivity for normalized density matrices; the displayed thermodynamic identity follows by inserting the Gibbs logarithm.

For our input $`p_\delta`$, choose the nearby positive-temperature Gibbs state $`q_{\beta_\delta}`$ with the same entropy. This choice exists locally because

```math
\frac{d}{d\beta}S(q_\beta)
=-\beta\,\mathrm{Var}_{q_\beta}(E)\ne0
```

for a nonconstant Hamiltonian at positive temperature. Define the available work per copy as

```math
w_\infty(\delta)
=\sum_j E_j\bigl(p_{\delta,j}-q_{\beta_\delta,j}\bigr).
```

Every allowed output on $`n`$ copies has entropy $`nS(p_\delta)`$, by unitary invariance and product additivity. Applying the relative-entropy identity to that output and $`q_{\beta_\delta}^{\otimes n}`$ gives

```math
0\le W_n(\delta)\le n w_\infty(\delta).
```

Equal entropy does not imply equal spectra, so this bound need not be attainable on a finite block. The fixed-input asymptotic attainability of $`w_\infty`$ is the inherited [Alicki–Fannes result](../references/RELATED_WORK.md#alicki-fannes). Here the input changes with $`\delta`$ while the block grows. The project establishes a uniform threshold in that joint limit rather than interchanging it with the fixed-input limit.

## Removing the temperature direction

A nearby Gibbs state can differ from the reference simply because its temperature changed. Such a change supplies no extractable work, even collectively. The theorem needs a quantitative way to remove that direction.

Let $`q=q_\beta`$ and suppose $`p_\delta`$ is a twice continuously differentiable probability path with $`p_0=q`$. Its **score**

```math
f_j=\frac{p'_{0,j}}{q_j}
```

is the first-order change of the log population. Normalization gives $`\mathbb E_q f=0`$. Write $`\bar E=\mathbb E_qE`$, $`V=\mathrm{Var}_q(E)`$ and $`c=\mathrm{Cov}_q(E,f)`$. A temperature change has derivative proportional to $`-q_j(E_j-\bar E)`$. Differentiating the equal-entropy constraint gives $`\beta'_0=-c/V`$. Consequently

```math
p_\delta-q_{\beta_\delta}
=\delta u+O(\delta^2),
\qquad
u_j=q_j\left[f_j-\frac{c}{V}(E_j-\bar E)\right].
```

The vector $`u`$ obeys $`\sum_j u_j=\sum_jE_ju_j=0`$. In the weighted inner product $`\langle a,b\rangle_q=\sum_jq_ja_jb_j`$, its rescaled version $`u_j/q_j`$ is the part of the score orthogonal to a temperature change. Its squared size is

```math
v=\sum_j\frac{u_j^2}{q_j}
=\mathrm{Var}_q(f)-\frac{c^2}{V}.
```

The hypothesis $`v\gt0`$ is thus a physical restriction on the perturbation, not a choice of coordinates. A local Taylor expansion on the positive probability simplex gives

```math
D(p_\delta\Vert q_{\beta_\delta})
=\frac v2\delta^2+o(\delta^2)
=\beta_\delta w_\infty(\delta),
\qquad
w_\infty(\delta)=\frac{v}{2\beta}\delta^2+o(\delta^2).
```

The quadratic term measures the distance left after temperature adjustment. The [normalization proof](../science/model.md#3-available-work-and-its-quadratic-coefficient) derives it without assuming more than the stated smoothness. A general twice differentiable path provides the displayed little-o remainder; an analytic example can support stronger remainder estimates.

## Clipping a likelihood without paying for bandwidth

The central converse must control every unitary, including one designed to harvest rare population inversions. A probability-distance estimate alone tends to multiply the error by the energy range of $`H_n`$, which grows with $`n`$. The useful comparison instead combines spectral order with relative entropy.

For this argument use the **fixed reference** $`Q=q_\beta^{\otimes n}`$, and let $`P=p_\delta^{\otimes n}`$. This reference has a different role from the entropy-matched Gibbs state used to define $`w_\infty`$. Define the log-likelihood and clip it to a bounded interval:

```math
L(x)=\log\frac{P(x)}{Q(x)},
\qquad
F(x)=\max\{-a,\min\{L(x),a\}\},
\qquad
0\lt a\lt\frac{\beta g}{2}.
```

Here $`g\gt0`$ is the fixed lattice spacing: distinct product energies remain separated by at least $`g`$. Form the normalized reference

```math
\sigma(x)=\frac{Q(x)e^{F(x)}}{Z_c},
\qquad
Z_c=\sum_xQ(x)e^{F(x)},
\qquad
K=-\log\sigma,
\qquad
\kappa=\beta-\frac{2a}{g}\gt0.
```

The auxiliary observable $`K`$ is dimensionless. Its level differences satisfy

```math
K(y)-K(x)
=\beta[E(y)-E(x)]-[F(y)-F(x)]
\ge\kappa[E(y)-E(x)]
```

whenever $`E(y)\gt E(x)`$. The clipped correction can change by at most $`2a`$ across any pair. Thus $`K`$ preserves the energy order. So does $`B=K-\kappa H_n`$. Within an energy degeneracy, order the basis by $`K`$; $`B`$ then has the same order there too.

One probability permutation minimizes all three expectations. If $`P^\downarrow`$ denotes that rearrangement, the optimized decreases obey

```math
W_K(P)=\kappa W_{H_n}(P)+W_B(P)
\ge\kappa W_{H_n}(P).
```

The inequality uses $`W_B(P)\ge0`$: doing nothing is allowed. This is an argument about common spectral order, not a claim that $`B`$ is a positive operator.

Entropy is invariant under the rearrangement. Therefore

```math
W_K(P)
=D(P\Vert\sigma)-D(P^\downarrow\Vert\sigma)
\le D(P\Vert\sigma),
```

and hence

```math
W_n(\delta)\le\frac{D(P\Vert\sigma)}{\kappa}.
```

This connects Watrous's sorting and entropy tools. The physical energy decrease is controlled by a dimensionless information quantity divided by an inverse-energy slope. No maximum energy or Hilbert-space dimension multiplies it.

### Why normalization requires two tails

Normalization cannot be dropped from this construction. Direct substitution gives

```math
D(P\Vert\sigma)
=\mathbb E_P[L-F]+\log Z_c.
```

Let $`U=\{L\gt a\}`$ and $`D_-=\{L\lt-a\}`$. The identity

```math
Z_c-1=e^aQ(U)-P(U)+e^{-a}Q(D_-)-P(D_-)
```

and $`\log Z_c\le Z_c-1`$ imply

```math
D(P\Vert\sigma)
\le\mathbb E_P[(L-a)_+]+e^{-a}Q(L\lt-a).
```

The discarded upper-tail normalization term and lower-tail terms are nonpositive. The remaining upper excess is measured under $`P`$, while the lower-tail correction is measured under $`Q`$. Both probability laws enter the bound. The [finite clipping lemma](../science/passive_clipping.md#1-a-finite-passive-reference-lemma) and [tail calculation](../science/passive_clipping.md#2-exact-control-of-normalization-and-tails) give the exact argument, including degeneracies.

## Concentration as the state changes

Write the block likelihood as a sum:

```math
L=\sum_{i=1}^n\ell_\delta(X_i),
\qquad
\ell_\delta(j)=\log\frac{p_{\delta,j}}{q_j},
\qquad
s=n\delta^2.
```

For every fixed $`\delta`$, the increments are independent and identically distributed under either $`P`$ or $`Q`$. Their distribution changes when $`\delta`$ changes. This is a triangular-array setting: concentration must hold with constants valid throughout a small interval of perturbations.

Smoothness and positive reference probabilities give fixed constants $`R,M`$ such that the range of $`\ell_\delta`$ is at most $`R\delta`$ and

```math
\begin{aligned}
\mu_P:=\mathbb E_PL
&=nD(p_\delta\Vert q)\in[0,Ms],\\
\mu_Q:=\mathbb E_QL
&=-nD(q\Vert p_\delta)\in[-Ms,0].
\end{aligned}
```

Watrous's Theorem 1.16 states a two-sided Hoeffding bound for independent identically distributed variables in $`[0,1]`$, with prefactor two. The one-sided form used here follows from the following short moment-generating-function argument.

For a centered variable $`Y`$ supported in an interval of length $`b`$, set $`h(t)=\log\mathbb E e^{tY}`$. Its second derivative is the variance under exponential reweighting. That reweighting leaves the support unchanged, so $`h''(t)\le b^2/4`$. Since $`h(0)=h'(0)=0`$, integration gives $`h(t)\le t^2b^2/8`$. Independence, Markov's inequality and optimization over $`t\ge0`$ therefore give

```math
\Pr(L-\mathbb EL\ge u)
\le \exp\left(-\frac{2u^2}{R^2s}\right),
\qquad u\ge0.
```

Applying the same argument to the negative centered sum gives the lower-tail version. This establishes the one-sided estimate directly, without changing the book's stated prefactor by assertion.

Choose $`a=\beta g/4`$. If $`s\le a/(2M)`$, each relevant tail is at least $`a/2`$ from its mean. Integrating the upper tail controls $`\mathbb E_P[(L-a)_+]`$; the lower tail controls the normalization correction under $`Q`$. Substitution into the clipping bound yields

```math
W_n(\delta)\le
\frac2\beta\left(\frac{R^2s}{2a}+e^{-a}\right)
\exp\left(-\frac{a^2}{2R^2s}\right),
\qquad
0\lt s\le\frac a{2M}.
```

Because $`n w_\infty`$ is asymptotic to $`vs/(2\beta)`$, the work fraction is bounded by a constant times $`(1+s)e^{-c_0/s}/s`$. It tends to zero when $`s\to0`$. The estimate holds for all sufficiently small perturbations and all integers in that range, including block sizes only logarithmically below $`\delta^{-2}`$. No normal approximation or exchange of asymptotic limits is needed. The [uniform converse](../science/passive_clipping.md#4-the-uniform-work-bound) supplies its full constants and quantifiers.

## Why the first inversion comes earlier

An extreme pair of strings can accumulate a likelihood difference proportional to $`n\delta`$. Typical likelihood fluctuations instead have size $`\delta\sqrt n`$, with mean drift of order $`n\delta^2`$. The different sizes suggest two thresholds; lattice arguments and concentration make both precise.

For a higher-energy string $`x`$ and a lower-energy string $`y`$,

```math
\log\frac{P_\delta(x)}{P_\delta(y)}
\le-\beta g+nR\delta.
```

Thus $`nR\delta\le\beta g`$ leaves the entire block passive, including equality. Conversely, write $`E_j=gz_j`$, with integer labels of gcd one and one label zero. Transversality supplies an integer direction $`r`$ satisfying

```math
\mathbf1\cdot r=z\cdot r=0,
\qquad
h=f\cdot r\gt0.
```

This follows because the nullspace of the integer matrix with rows $`\mathbf1,z`$ has a rational basis, and the score is not in the span of those rows. Bezout's identity supplies another integer vector $`t`$ with $`\mathbf1\cdot t=0`$ and $`z\cdot t=1`$. Set

```math
m_\delta=
\left\lceil\frac{2\beta g}{h\delta}\right\rceil r+t.
```

The positive and negative parts of $`m_\delta`$ are occupation counts of two strings of equal length $`\frac12\lVert m_\delta\rVert_1=\Theta(\delta^{-1})`$. Their energies differ by $`g`$, and the higher-energy string's logarithmic probability advantage is

```math
m_\delta\cdot\log p_\delta
=\beta g+O(\delta)\gt0
```

for sufficiently small $`\delta`$. One swap activates the block. This gives $`N_{\mathrm{act}}=\Theta(\delta^{-1})`$; the [activation proof](../science/activation.md) controls the integer construction and its remainder.

Those witness strings can have exponentially small probability. Moreover, the exact first activating integer can be arbitrarily close to a population tie. An exponential lower bound therefore requires a specified margin beyond onset, as explained by the [qutrit counterexample](../science/qutrit.md#3-why-exact-onset-needs-a-qualification). Strict positivity alone does not supply a useful yield.

## Turning types into useful work

A useful fraction requires many compatible swaps. Three conditions must hold together: enough probability lies in the sources, enough basis states exist in the targets, and the selected swaps form one unitary. The [finite construction](../science/useful_work.md) supplies all three.

### A common displacement with an exact energy drop

An occupation type $`k=(k_1,\ldots,k_d)`$ records how many copies occupy each basis level. It contains

```math
M(k)=\frac{n!}{\prod_j k_j!}
```

different strings, each of probability $`\prod_jp_j^{k_j}`$. For this construction write $`p=p_\delta`$, $`q_\delta=q_{\beta_\delta}`$, and $`\Delta_\delta=p-q_\delta`$. Fix $`\alpha=3/4`$ and $`n=\lceil C/\delta^2\rceil`$.

The intended count displacement is $`\alpha n\Delta_\delta`$. A bounded integer rounding, corrected with the same Bezout vector as above, produces $`m\in\mathbb Z^d`$ satisfying

```math
\sum_jm_j=0,
\qquad
z\cdot m=w=
\left\lfloor\frac{\alpha n w_\infty(\delta)}g\right\rfloor,
\qquad
\lVert m-\alpha n\Delta_\delta\rVert_\infty\le B_H.
```

The constant $`B_H`$ depends only on the fixed Hamiltonian. Moving a string of type $`k`$ to type $`k-m`$ lowers its energy by exactly $`gw`$. Downward energy rounding matters because it helps the population ratio when inverse temperature is positive.

Let $`\Gamma=m\cdot\log p`$. Using the equal-entropy identity and

```math
(p-q_\delta)\cdot\log(p/q_\delta)
=D(p\Vert q_\delta)+D(q_\delta\Vert p)
```

gives the uniform lower bound

```math
\Gamma\ge\alpha nD(q_\delta\Vert p)-O(\delta)
=\frac{\alpha Cv}{2}+o(1).
```

Thus the source microstate is more probable than its target by a factor $`e^\Gamma`$. The actual $`\Gamma`$ need not converge because the integer energy drop can jump; only this lower bound is used.

### Capacity is a separate requirement

A favorable probability ratio does not ensure that every source string has a distinct target. We need $`M(k-m)\ge M(k)`$. For central types with $`k_j=np_j+O(\sqrt n)`$, the finite factorial estimate gives

```math
\log\frac{M(k-m)}{M(k)}
\ge
\Gamma-\frac1{2n}\sum_j\frac{m_j^2}{p_j}
-\mathcal E.
```

At fixed $`C`$ and small $`\delta`$, the quadratic penalty tends to $`\alpha^2Cv/2`$. The error can be bounded by a fixed constant times $`\sqrt C`$ plus a term tending to zero. The positive margin is therefore proportional to $`\alpha(1-\alpha)Cv/2`$. Choosing one sufficiently large finite $`C`$ makes it dominate the error throughout the chosen central set.

The canonical proof uses an explicit factorial inequality rather than an uncontrolled Stirling approximation. It also checks that every target count is nonnegative. Neither fact follows from an informal typical-set picture alone.

### Energy residues make all swaps compatible

Select central source types whose total integer energy lies in the upper half of the residues modulo $`2w`$:

```math
z\cdot k\bmod 2w\in\{w,w+1,\ldots,2w-1\}.
```

Subtracting $`m`$ reduces that energy by $`w`$, placing every target in the lower residue half. Sources and targets are therefore disjoint. Different source types have different target types because the same vector is subtracted, and the multiplicity bound permits an injection within each pair of types. Exchanging every paired string and fixing the rest is a system-only permutation unitary. The selection describes its action on the basis; it requires no measurement of a prepared block.

Full support, a zero energy label and gcd one make each nontrivial Fourier mode of the residue distribution strictly contractive. The upper residue half consequently receives approximately half the probability. Although $`w`$ can jump with $`\delta`$, it ranges over only finitely many positive integers at the chosen fixed $`C`$. The mixing bound can therefore be made uniform over those jumps.

The extracted work is bounded below by

```math
gw(1-e^{-\Gamma})
\times\text{selected source probability}.
```

The factor $`1-e^{-\Gamma}`$ subtracts the target's initial population, just as in the three-copy example. The explicit choices in the [constructive proof](../science/useful_work.md#6-one-fixed-explicit-c-suffices) ensure, for every sufficiently small $`\delta`$,

```math
\frac{gw}{n w_\infty}\ge\frac7{10},
\qquad
1-e^{-\Gamma}\ge\frac{99}{100},
\qquad
\text{selected source probability}\ge\frac{39}{80}.
```

Their product is

```math
\frac7{10}\frac{99}{100}\frac{39}{80}
=\frac{27027}{80000}
=0.3378375\gt\frac14.
```

This proves a quarter yield with slack at one fixed inverse-square block scale. It does not optimize the necessary prefactor or the implemented control.

## Comparing actual and harmonic work by entropy

The fixed-lattice converse cannot simply be reused for every moving spectrum. A new comparison is needed, and Watrous's entropy tools provide it. Consider the top-level-tilted qutrit $`H_{2+\epsilon}=\mathrm{diag}(0,1,2+\epsilon)`$, $`K=\mathrm{diag}(0,0,1)`$ and the input $`\rho\propto e^{-\beta H_{2+\epsilon}+\delta K}`$. It is exactly the harmonic input with effective tilt $`t=\delta-\beta\epsilon`$. The input probabilities agree, but the physical energy objectives differ.

Write $`P=\rho^{\otimes n}`$, $`\sigma=UPU^\dagger`$, and $`L=\mathrm{Tr}[K_n(P-\sigma)]`$. The logarithm of this product input and entropy invariance give

```math
D(\sigma\Vert P)=\delta L-\beta W_\epsilon(U),
\qquad W_\epsilon(U)=W_0(U)+\epsilon L.
```

The quantity $`L`$ is the decrease of the expected number of top-level occupations. The product-reference divergence is at least the sum of its marginal divergences. Measuring the binary occupation observable in the proof can only reduce those divergences, by data processing; Pinsker in natural logarithms then gives

```math
D(\sigma\Vert P)\ge2\sum_j d_j^2\ge2L^2/n,
\qquad d_j=\mathrm{Tr}[K(\rho-\sigma_j)].
```

For an actual-work optimizer, $`W_\epsilon\ge0`$, so $`0\le L\le n\delta/2`$. The harmonic optimizer also has $`L\ge0`$ when $`t\gt0`$. Thus, for $`\epsilon\ge0`$ and $`t\gt0`$,

```math
W_n(t;2)\le W_n(\delta;2+\epsilon)
\le W_n(t;2)+n\epsilon\delta/2.
```

This is an information bound on arbitrary coherent outputs, not a protocol requiring measured feedback. The book's base-two Pinsker coefficient becomes the factor two above after multiplying its relative entropy by $`\ln2`$.

For $`\epsilon=\nu\delta^{3/2}`$ with fixed positive $`\beta,\nu`$, the actual benchmark remains $`R_2\delta^2/(2\beta)+O(\delta^3)`$. The harmonic benchmark at $`t`$ divided by that actual benchmark tends to one, while the normalized additive error is $`O(\sqrt\delta)`$, uniformly in the block size. CWT's inherited harmonic converse and QWA's inherited harmonic one-third construction therefore imply $`N_{1/10}=\Theta(\delta^{-2})`$ on this specified path. The [qutrit transfer account](../science/qutrit_transfer.md) proves the entropy estimate, actual normalization and minimum-block quantifiers together.

The [inherited order-delta two-copy example](../science/qutrit_transfer.md#6-keep-the-order-delta-two-copy-boundary) remains compatible: at $`\epsilon=\delta/(8\beta)`$ the normalized error no longer vanishes, and two copies recover more than one tenth eventually. At order $`\delta^{3/2}`$ two copies are still active, but their recovered fraction tends to zero. One-copy continuity, early activation and useful yield are three different statements.

## The theorem, its resources and its boundaries

The two arguments now meet. For a fixed nonconstant finite Hamiltonian with commensurate energy levels, fixed $`\beta\gt0`$, and a positive diagonal $`C^2`$ input path $`p_\delta`$ with $`p_0=q_\beta`$ and $`v\gt0`$,

```math
N_{\mathrm{act}}(\delta)=\Theta(\delta^{-1}),
\qquad
N_{1/4}(\delta)=\Theta(\delta^{-2}).
```

The lower useful-block bound holds for every fixed positive fraction. The construction matches it for all fixed fractions up to one quarter. This conclusion needs no assumption that $`W_n/n`$ increases monotonically with $`n`$. Exact definitions and quantifiers are in the [threshold theorem](../science/model.md#4-exact-threshold-theorem).

| Assumption or resource | Why it matters |
|---|---|
| Fixed finite commensurate Hamiltonian | The same positive energy spacing controls all product spectra. Constants may depend on it and on the dimension. |
| Diagonal input path | Coherent rotations of a Gibbs state can make its entire available work accessible from one copy. |
| Fixed positive temperature and nonzero transverse derivative | The entropy-matched Gibbs construction and the quadratic work coefficient rely on these conditions. A temperature path is completely passive; a higher-order departure changes the copy exponents. |
| Known independent copies and unrestricted cyclic unitary control | These define the optimization. The supplied construction is a permutation on the copies. |
| Mean work | Individual transitions can cost energy. The theorem does not determine deterministic work, failure probabilities or charging power. |
| Joint block size | Gate count, control duration and the number of independent repetitions are not bounded by this copy threshold. |

The [physical interpretation](../science/interpretation.md) gives the concrete scope counterexamples. An incommensurate spectrum or a Hamiltonian varying with the perturbation can have shrinking product gaps, so the fixed-lattice proof cannot be transferred by continuity of a one-copy energy ratio.

The scientific attribution is separate from the single educational anchor. The equal-entropy endpoint, collective type-shift methods and ordering-preserving passivity comparisons have research antecedents detailed in [related work](../references/RELATED_WORK.md). The [Quantum-Work-Activation comparison](../references/RELATED_WORK.md#concurrent-work) shares the rational-qutrit question and passive-clipping entry point. Its one-third construction combines with the converse here to give the fixed-rational qutrit law for every fixed fraction up to one third. Each ingredient retains its ownership. The quantitative strengthening here removes the extensive bandwidth factor from the converse, closes the logarithmic gap for every subcritical block sequence, and matches it with a quarter-yield construction for general fixed finite commensurate spectra and transverse diagonal paths. The companion's irrational-spectrum claims are outside this theorem and are not proof dependencies.

