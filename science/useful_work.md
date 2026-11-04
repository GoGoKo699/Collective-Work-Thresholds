# A finite construction for useful work

This page proves the upper bound in the [threshold theorem](model.md#4-exact-threshold-theorem). A permutation of the supplied copies extracts at least a quarter of their available mean work at one fixed inverse-square block scale. The proof gives an explicit finite sufficient-condition lemma, including probability mass, target capacity, integer rounding and disjointness. It uses no auxiliary system and does not bound circuit complexity or duration.

Type transport is an established collective-work method; the [related-work account](../references/RELATED_WORK.md) separates those foundations from this quantified general finite-spectrum statement.

## 1. Constructive statement

Fix a finite Hamiltonian with a commensurate, nonconstant spectrum. After subtracting its minimum energy, write

```math
E_j=g z_j,
\qquad z_j\in\mathbb Z_{\ge0},
\qquad \min_j z_j=0,
\qquad \gcd(z_1,\ldots,z_d)=1,
\qquad g>0.
```

The index $`j`$ labels individual energy eigenvectors, so repeated $`z_j`$ are permitted. Fix $`\beta>0`$ and $`q_j=e^{-\beta E_j}/Z`$. Let $`p_\delta`$, $`0\le\delta<\bar\delta`$, be a $`C^2`$ probability path in this fixed basis with $`p_0=q`$. Positivity near zero follows from $`q_j>0`$.

Define

```math
f_j=\frac{p'_{0,j}}{q_j},\qquad
V=\operatorname{Var}_q(E),\qquad
c=\operatorname{Cov}_q(E,f),\qquad
u_j=q_j\left[f_j-\frac{c}{V}(E_j-\mathbb E_q E)\right],
\qquad
v=\sum_j\frac{u_j^2}{q_j}>0.
```

The assumption $`v>0`$ is transversality to the Gibbs-temperature curve, as in the [model](model.md). Let $`q_\delta`$ be the positive-temperature Gibbs state with $`S(q_\delta)=S(p_\delta)`$, defined locally near zero. Put

```math
w_\infty(\delta)=\sum_j E_j(p_{\delta,j}-q_{\delta,j}),
\qquad
a=\frac{v}{2\beta}>0.
```

Here $`w_\infty`$ is the established equal-entropy Gibbs bound, and asymptotically achievable work per copy. The proof below only needs the energy difference and entropy identity, not that prior asymptotic achievability theorem.

**Theorem.** There exist a finite constant $`C>0`$ and $`\delta_0>0`$, depending only on the fixed Hamiltonian, $`\beta`$, and the local path, such that for every $`0<\delta\le\delta_0`$, at the integer block size

```math
n=\left\lceil\frac C{\delta^2}\right\rceil
```

a permutation unitary on the $`n`$ copies extracts at least

```math
\frac14 n w_\infty(\delta).
```

An explicit sufficient choice of $`C`$ is given in Section 6. Section 5 gives a completely finite sufficient-condition lemma: it can be checked for a specified $`p,n,m`$, without taking a limit or using a local central-limit approximation. The abstract $`C^2`$ assumption supplies existence of a small enough $`\delta_0`$; a numerical value of $`\delta_0`$ additionally requires quantitative bounds on the chosen path. No universal numerical $`\delta_0`$ follows from the tangent alone.

## 2. Thermodynamic identities

Use the equal-entropy Gibbs state and transverse vector established in the [model](model.md#3-available-work-and-its-quadratic-coefficient). Write $`q_\delta=q_{\beta_\delta}`$, $`\Delta_\delta=p_\delta-q_\delta`$ and $`\ell_\delta=\log(p_\delta/q_\delta)`$. The needed identities are

```math
\Delta_\delta=\delta u+O(\delta^2),\qquad
D(p_\delta\Vert q_\delta)=\beta_\delta w_\infty(\delta),
```

```math
D(p_\delta\Vert q_\delta)
=D(q_\delta\Vert p_\delta)+o(\delta^2)
=\frac v2\delta^2+o(\delta^2),\qquad
w_\infty(\delta)=a\delta^2+o(\delta^2).
```

Also $`\ell_\delta=O(\delta)`$ componentwise by positivity and the displayed first-order expansion. All limits below are taken at the one fixed constant $`C`$ chosen in Section 6. It does not depend on $`\delta`$. The first-order entropy and energy components have already been removed in $`u`$.

## 3. Bounded integer rounding with the energy rounded downward

Fix $`\alpha=3/4`$. Choose an index $`j_0`$ with $`z_{j_0}=0`$. By Bezout's identity there is one fixed $`t\in\mathbb Z^d`$ satisfying

```math
\sum_j t_j=0,\qquad z\cdot t=1.
```

For example, choose integer coefficients on the nonzero $`z_j`$ whose weighted sum is one, and choose the $`j_0`$-coordinate to restore zero sum. Define

```math
Z_1=\sum_j z_j\ge1,
\qquad
B_H=(d-1)+(Z_1-1)\lVert t\rVert_\infty.
```

For any real vector $`x`$ with $`\sum_jx_j=0`$, let

```math
m_j^{(0)}=\lfloor x_j\rfloor\quad(j\ne j_0),
\qquad
m_{j_0}^{(0)}=-\sum_{j\ne j_0}m_j^{(0)},
\qquad
w=\lfloor z\cdot x\rfloor.
```

The coordinate rounding error has infinity norm at most $`d-1`$. Moreover,

```math
h:=w-z\cdot m^{(0)}
 =\left\lfloor\sum_{j\ne j_0}z_j\{x_j\}\right\rfloor
 \in\{0,\ldots,Z_1-1\},
```

where $`\{x_j\}=x_j-\lfloor x_j\rfloor`$, also for negative $`x_j`$. Therefore

```math
m=m^{(0)}+ht
```

is integer and obeys

```math
\sum_jm_j=0,\qquad z\cdot m=w,\qquad
\lVert m-x\rVert_\infty\le B_H.
```

Apply this construction to $`x=\alpha n\Delta_\delta`$. Since $`g z\cdot\Delta_\delta=w_\infty(\delta)`$, it gives

```math
w=\left\lfloor\frac{\alpha n w_\infty(\delta)}g\right\rfloor,
\qquad
\sum_jE_jm_j=gw,
\qquad
\lVert m-\alpha n\Delta_\delta\rVert_\infty\le B_H.
```

The energy drop $`gw`$ is an exact integer multiple of $`g`$, rounded downward. The bound $`B_H`$ does not depend on $`C,n,\delta`$, or where a floor function jumps.

### The individual probability ratio

Let $`R=m\cdot\log p_\delta`$. Since $`\beta_\delta>0`$ locally and $`gw\le\alpha n w_\infty`$,

```math
\begin{aligned}
R
&=-\beta_\delta gw+m\cdot\ell_\delta\\
&\ge-\alpha nD(p_\delta\Vert q_\delta)
 +\alpha n\Delta_\delta\cdot\ell_\delta
 -dB_H\lVert\ell_\delta\rVert_\infty\\
&=\alpha nD(q_\delta\Vert p_\delta)
 -dB_H\lVert\ell_\delta\rVert_\infty
 =:L_\delta.
\end{aligned}
```

The equality is the identity

```math
(p-q)\cdot\log(p/q)=D(p\Vert q)+D(q\Vert p).
```

Consequently $`L_\delta\to\alpha Cv/2`$. The actual $`R`$ need not converge, because the downward energy rounding can add a bounded positive term. Only this uniform lower bound is used.

## 4. An exact factorial bound for the type multiplicities

A type $`k\in\mathbb Z_{\ge0}^d`$, $`\sum_j k_j=n`$, has multiplicity

```math
M(k)=\frac{n!}{\prod_j k_j!}.
```

For integers $`k\ge1`$ and $`m`$ with $`|m|\le k/2`$, set $`t=|m|`$. Expanding the finite products for $`k!/(k-m)!`$, for both signs of $`m`$, gives

```math
\left|\log\frac{k!}{(k-m)!}
       -m\log k+\frac{m^2}{2k}\right|
 \le\frac{|m|}{2k}
    +\frac{t(t+1)(2t+1)}{6k^2}.
\tag{F}
```

To verify this, for $`m\ge0`$ use $`\sum_{r=0}^{m-1}\log(k-r)`$; for $`m=-t<0`$ use $`-\sum_{r=1}^t\log(k+r)`$. The linear correction is $`-m(m-1)/(2k)`$ in both cases. The inequality $`|\log(1+y)-y|\le y^2`$ for $`|y|\le1/2`$, together with $`\sum_{r=1}^t r^2=t(t+1)(2t+1)/6`$, proves (F). No Stirling error is hidden here.

For a positive distribution $`p`$, an integer $`n\ge1`$, and $`K\ge1`$, define $`p_*=\min_jp_j`$. Let

```math
T_{n,p,K}=\{k:\ |k_j-np_j|\le K\sqrt n\ \text{for every }j\}.
```

Suppose

```math
\frac K{\sqrt n}\le\frac{p_*}2,
\qquad
\lVert m\rVert_\infty\le\frac{np_*}4.
\tag{V}
```

Then every $`k\in T_{n,p,K}`$ satisfies $`k_j\ge np_*/2\ge1`$ and $`|m_j|\le k_j/2`$, so $`k-m`$ is a valid nonnegative type. Applying (F), and replacing $`k_j`$ by $`np_j`$, gives

```math
\log\frac{M(k-m)}{M(k)}
 \ge R-Q-\mathcal E,
\tag{M}
```

uniformly over the whole typical set, where

```math
R=m\cdot\log p,
\qquad
Q=\frac1{2n}\sum_j\frac{m_j^2}{p_j},
```

and the following explicit error is sufficient:

```math
\begin{aligned}
\mathcal E(n,p,m,K)
={}&\frac{2K\lVert m\rVert_1}{p_*\sqrt n}
 +\frac{K\lVert m\rVert_2^2}{p_*^2 n^{3/2}}
 +\frac{\lVert m\rVert_1}{np_*}\\
&+\frac{2}{3n^2p_*^2}
       \sum_j |m_j|(|m_j|+1)(2|m_j|+1).
\end{aligned}
\tag{E}
```

Indeed, $`|\log[k_j/(np_j)]|\le2K/(p_*\sqrt n)`$ gives the first term. The change in the quadratic denominator is at most $`K m_j^2/(p_*^2n^{3/2})`$. The two terms in (F), using $`k_j\ge np_*/2`$, give the remaining terms. Also $`\sum_jm_j=0`$ removes the $`m_j\log n`$ contribution exactly.

## 5. Finite sufficient-condition lemma and actual source mass

Let $`p`$ be positive, $`n\ge1`$ be an integer, $`K\ge1`$, and $`m\in\mathbb Z^d`$ satisfy (V), $`\sum_jm_j=0`$, and

```math
w=z\cdot m\in\mathbb Z_{>0},\qquad
R=m\cdot\log p>0,\qquad
R-Q-\mathcal E\ge0.
\tag{S}
```

Define the finite Fourier contraction

```math
\lambda(p,2w)=
\max_{1\le h\le2w-1}
\left|\sum_jp_j\exp\!\left(\frac{2\pi i h z_j}{2w}\right)\right|<1.
```

**Finite lemma.** A system-only permutation unitary extracts at least

```math
gw(1-e^{-R})
\left[
 \frac12-\frac{d}{4K^2}
 -\frac{2w-1}{2}\lambda(p,2w)^n
\right]_+.
\tag{W}
```

**Proof.** For the multinomial type $`k`$, each coordinate has variance at most $`n/4`$. Chebyshev and a union bound give

```math
\Pr_p[k\notin T_{n,p,K}]\le\frac d{4K^2}.
```

Let $`Z_n=\sum_{i=1}^n z_{X_i}`$, where the $`X_i`$ are independent with law $`p`$. Fourier inversion on $`\mathbb Z/(2w)\mathbb Z`$ gives, for every residue $`r`$,

```math
\left|\Pr_p[Z_n\equiv r\pmod{2w}]-\frac1{2w}\right|
 \le\frac{2w-1}{2w}\lambda(p,2w)^n.
```

Summing over the $`w`$ residues $`\{w,\ldots,2w-1\}`$ shows that their total probability is at least

```math
\frac12-\frac{2w-1}{2}\lambda(p,2w)^n.
```

The strict inequality $`\lambda<1`$ needs justification. If a nontrivial Fourier sum had modulus one, positivity of every $`p_j`$ would force all its phase factors to agree. The label $`z_{j_0}=0`$ forces the common phase to equal one. Then $`2w`$ divides $`h z_j`$ for every $`j`$; the gcd assumption forces $`2w`$ to divide $`h`$, a contradiction. Duplicate energies merely repeat some phase factors and do not affect this argument.

Select all types that are typical and whose total integer energy lies in the upper residue half. Their total probability is at least the bracket in (W). By (M) and (S), $`M(k-m)\ge M(k)`$ for every selected type. Inject every computational-basis string of type $`k`$ into a different string of type $`k-m`$.

All these injections can be used simultaneously:

- Different source types have different target types, since the same $`m`$ is subtracted.
- Every source has energy residue in the upper half, whereas its target has residue in the lower half, because its energy is exactly $`w`$ smaller.
- Thus a string cannot be both a selected source and a target. Within each target type, the injection is one-to-one.

Swap each paired source and target, and fix every other basis string. This is a product of disjoint transpositions and hence a unitary on the original system. No labels, measurement records, or unused target strings require an auxiliary system.

For a paired source $`x`$ and target $`y`$,

```math
E(x)-E(y)=gw,
\qquad
\frac{P_p(x)}{P_p(y)}=e^R.
```

The pair's mean work is $`gw[P_p(x)-P_p(y)]`$. Summing over all paired source strings proves (W). The target probability is explicitly subtracted; it is not treated as an empty destination. This completes the finite proof.

## 6. One fixed explicit $`C`$ suffices

Define fixed positive numbers

```math
q_*=\min_jq_j,
\qquad U=\lVert u\rVert_1,
\qquad \alpha=\frac34,
\qquad K=10\sqrt d,
\qquad \mu=\frac{\alpha(1-\alpha)v}{2}.
```

Take any fixed

```math
C\ge\max\left\{
 1,\ \frac{100g}{a},
 \left(\frac{16K\alpha U}{q_*\mu}\right)^2,
 \frac{3\log100}{\alpha v}
\right\}.
\tag{C}
```

For every $`\delta`$, set $`n=\lceil C/\delta^2\rceil`$ and choose $`m,w`$ by the exact rounding construction in Section 3. Bounded rounding gives the following limits along **all** sufficiently small positive $`\delta`$, not only subsequences avoiding integer jumps:

```math
n\delta^2\longrightarrow C,
\qquad
\frac{m}{n\delta}\longrightarrow\alpha u,
\qquad
L_\delta\longrightarrow\frac{\alpha Cv}{2},
\qquad
Q\longrightarrow\frac{\alpha^2Cv}{2}.
```

For the exact error (E), only its first term survives:

```math
\mathcal E\longrightarrow
 \frac{2K\alpha U\sqrt C}{q_*}
 \le\frac{\mu C}{8},
```

where the final inequality is precisely the third condition in (C). The remaining terms vanish because $`m=O(\sqrt n)`$ at fixed $`C`$. It follows that for all sufficiently small $`\delta`$,

```math
\begin{aligned}
L_\delta&\ge\frac{\alpha Cv}{2}-\frac{\mu C}{8},\\
Q&\le\frac{\alpha^2Cv}{2}+\frac{\mu C}{8},\\
\mathcal E&\le\frac{\mu C}{4}.
\end{aligned}
\tag{A}
```

Hence

```math
R-Q-\mathcal E\ge\frac{\mu C}{2}>0,
\qquad
R\ge\frac{\alpha Cv}{3}\ge\log100.
```

Condition (V) also holds eventually: $`K/\sqrt n\to0`$, $`p_*\to q_*>0`$, and $`\lVert m\rVert_\infty/n=O(\delta)`$. Thus all selected target types are valid, and their multiplicities dominate the source multiplicities, for every sufficiently small $`\delta`$.

### Positive work drop and a finite set of possible moduli

Shrink the permitted $`\delta`$-interval so that $`0<\delta\le1`$ and

```math
\frac a2\le\frac{w_\infty(\delta)}{\delta^2}\le2a.
```

Then

```math
\frac{aC}{2}\le n w_\infty(\delta)\le2a(C+1),
```

so the second condition in (C) gives

```math
w\ge1,
\qquad
\frac{gw}{n w_\infty}
 \ge\alpha-\frac{g}{n w_\infty}
 \ge\alpha-\frac{2g}{aC}
 \ge0.73>0.7.
```

Moreover $`w\le W_0`$, where the fixed integer

```math
W_0=\left\lceil\frac{2\alpha a(C+1)}g\right\rceil
```

depends on $`C`$ but not $`\delta`$. This is why jumps of $`w`$ do not obstruct a uniform modulo estimate.

### Uniform modulo mixing for those moduli

Define

```math
\lambda_*=
\max_{1\le w\le W_0}
\max_{1\le h\le2w-1}
\left|\sum_jq_j e^{2\pi i h z_j/(2w)}\right|<1,
\qquad
\lambda=\frac{1+\lambda_*}{2}<1.
```

There are finitely many modes, and their strict contractions were proved in Section 5. If

```math
\lVert p_\delta-q\rVert_1\le\frac{1-\lambda_*}{2},
```

then $`\lambda(p_\delta,2w)\le\lambda`$ for every permitted $`w`$. Choose the fixed integer

```math
n_{\mathrm{mix}}=
\left\lceil
 \frac{\log[50(2W_0-1)]}{-\log\lambda}
\right\rceil.
```

For $`n\ge n_{\mathrm{mix}}`$, the modulo error in (W) is at most $`1/100`$, uniformly over every possible floor value of $`w`$. This holds whenever $`\delta\le\sqrt{C/n_{\mathrm{mix}}}`$, in addition to the probability-closeness condition. Therefore the selected source mass is at least

```math
\frac12-\frac{d}{4K^2}-\frac1{100}
 =\frac12-\frac1{400}-\frac1{100}
 =\frac{39}{80}=0.4875.
```

Using $`gw/(n w_\infty)\ge0.7`$, $`1-e^{-R}\ge0.99`$, and (W), the extracted fraction is at least

```math
\frac7{10}\frac{99}{100}\frac{39}{80}
 =\frac{27027}{80000}
 =0.3378375>\frac14.
```

This proves the theorem with slack in the numerical fraction.

### A precise choice rule for $`\delta_0`$

Choose any $`\delta_0>0`$ small enough that, for every $`0<\delta\le\delta_0`$: the equal-entropy Gibbs state exists with $`\beta_\delta>0`$; the two-sided $`w_\infty/\delta^2`$ bound holds; (V) and (A) hold; $`\lVert p_\delta-q\rVert_1\le(1-\lambda_*)/2`$; and $`\delta\le\min\{1,\sqrt{C/n_{\mathrm{mix}}}\}`$. Each is a stated finite inequality and was shown above to hold throughout a sufficiently small interval. Their finite intersection therefore supplies such a $`\delta_0`$. No condition assumes the desired work bound, no limit interchanges $`C`$ with $`\delta`$, and no continuity of $`m`$ or $`w`$ is used.

