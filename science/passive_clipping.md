# Passive likelihood clipping and the uniform converse

The main estimate controls extractable mean energy without multiplying a distance by the total energy bandwidth. It has two ingredients: a passive reference whose logarithm dominates the physical Hamiltonian in spectral order, and concentration of the likelihood ratio.

The operational definitions and fixed-system assumptions are in the [model](model.md). All logarithms are natural.

## 1. A finite passive-reference lemma

Let $`H=\mathrm{diag}(E_i)`$ be finite, and suppose every nonzero energy separation has magnitude at least $`g\gt 0`$. Let $`q_i=e^{-\beta E_i}/Z`$, $`\beta\gt 0`$, and let $`p_i\gt 0`$ be any probability distribution in the same basis. For

```math
0\lt a\lt \frac{\beta g}{2},\qquad
L_i=\log(p_i/q_i),\qquad
F_i=\max\{-a,\min\{L_i,a\}\},
```

define the **normalized** clipped reference

```math
\sigma_i=\frac{q_i e^{F_i}}{Z_c},
\qquad
Z_c=\sum_iq_i e^{F_i},
\qquad
K=-\log\sigma,\qquad
\kappa=\beta-\frac{2a}{g}\gt 0.
```

Then

```math
\boxed{\quad
W_H(p)\le\frac{D(p\Vert\sigma)}{\kappa}.
\quad}
\tag{1}
```

The dimension and maximum energy do not appear in this bound.

### Common spectral order

For $`E_j\gt E_i`$,

```math
K_j-K_i=\beta(E_j-E_i)-(F_j-F_i)
\ge\beta(E_j-E_i)-2a\gt 0.
```

Thus $`K`$ orders different energy shells in the same way as $`H`$. The diagonal observable $`B=K-\kappa H`$ also has that order, because

```math
B_j-B_i=
\frac{2a}{g}(E_j-E_i)-(F_j-F_i)\ge0.
```

Within a degenerate energy shell, $`B_j-B_i=K_j-K_i`$. Therefore one basis ordering makes $`K,H,B`$ all nondecreasing.

Let $`p^\downarrow`$ be the eigenvalues of $`p`$ placed in decreasing order along that basis. The rearrangement inequality shows that this single permutation minimizes the expectations of all three observables. Consequently

```math
W_K(p)=\kappa W_H(p)+W_B(p)\ge\kappa W_H(p),
```

where $`W_B(p)\ge0`$ because doing nothing is an allowed unitary. Entropy is unchanged by the permutation, so

```math
W_K(p)=D(p\Vert\sigma)-D(p^\downarrow\Vert\sigma)
\le D(p\Vert\sigma).
```

This proves (1), including degeneracies and ties. Ordering-preserving comparisons are part of the established [passivity-deformation framework](../references/RELATED_WORK.md#passivity-deformation); the present use connects them to a clipped likelihood reference.

## 2. Exact control of normalization and tails

The normalized reference obeys

```math
\boxed{\quad
D(p\Vert\sigma)
\le \mathbb E_p[(L-a)_+]
 +e^{-a}\Pr_q(L\lt -a).
\quad}
\tag{2}
```

For completeness, write $`U=\{L\gt a\}`$ and $`D_-=\{L\lt -a\}`$. Since $`\sum_iq_ie^{L_i}=1`$,

```math
Z_c-1=e^a q(U)-p(U)+e^{-a}q(D_-)-p(D_-).
```

Also,

```math
D(p\Vert\sigma)
=\sum_U p_i(L_i-a)
 +\sum_{D_-}p_i(L_i+a)+\log Z_c.
```

Use $`\log Z_c\le Z_c-1`$. The terms $`e^a q(U)-p(U)`$, $`\sum_{D_-}p_i(L_i+a)`$, and $`-p(D_-)`$ are nonpositive. Dropping them gives (2). This calculation requires neither an estimate that $`Z_c`$ is near one nor a lower bound on individual probabilities.

The upper excess is weighted by $`p`$; the lower-tail normalization correction is weighted by $`q`$. Both laws are needed. Replacing $`\sigma`$ by its unnormalized numerator would invalidate the relative-entropy argument.

## 3. Product likelihoods near equilibrium

For the path in the [model](model.md), write

```math
\ell_\delta(j)=\log(p_{\delta,j}/q_j),\qquad
L=\sum_{i=1}^n\ell_\delta(X_i),\qquad
s=n\delta^2.
```

Smoothness, normalization and full support provide fixed $`R,M,\delta_0\gt 0`$ such that, for every $`0\lt \delta\le\delta_0`$,

```math
\begin{aligned}
\mathrm{osc}_j\ell_\delta(j)&\le R\delta,\\
D(p_\delta\Vert q)&\le M\delta^2,\\
D(q\Vert p_\delta)&\le M\delta^2.
\end{aligned}
\tag{3}
```

Under $`P=p_\delta^{\otimes n}`$ and $`Q=q^{\otimes n}`$, respectively,

```math
\mu_P=\mathbb E_PL=nD(p_\delta\Vert q)\in[0,Ms],
\qquad
\mu_Q=\mathbb E_QL=-nD(q\Vert p_\delta)\in[-Ms,0].
```

[Hoeffding's inequality](https://doi.org/10.1080/01621459.1963.10500830) applies under either law because the increments are independent and each has range at most $`R\delta`$. For every $`t\ge0`$:

```math
\begin{aligned}
\Pr(L-\mathbb EL\ge t)&\le\exp\!\left(-\frac{2t^2}{R^2s}\right),\\
\Pr(L-\mathbb EL\le-t)&\le\exp\!\left(-\frac{2t^2}{R^2s}\right).
\end{aligned}
\tag{4}
```

For $`a\gt Ms`$, tail integration gives

```math
\begin{aligned}
\mathbb E_P[(L-a)_+]
&=\int_0^\infty\Pr_P(L\gt a+t)\,dt\\
&\le\int_{a-Ms}^\infty e^{-2u^2/(R^2s)}\,du\\
&\le\frac{R^2s}{4(a-Ms)}
 \exp\!\left[-\frac{2(a-Ms)^2}{R^2s}\right].
\end{aligned}
```

The last step follows by replacing the integrand's factor one by $`u/(a-Ms)`$. The lower tail under $`Q`$ is bounded by the same exponential because $`a+\mu_Q\ge a-Ms`$. Hence (2) yields

```math
\begin{aligned}
D(P\Vert\sigma)
&\le\left[\frac{R^2s}{4(a-Ms)}+e^{-a}\right]
\exp\!\left[-\frac{2(a-Ms)^2}{R^2s}\right].
\end{aligned}
\tag{5}
```

## 4. The uniform work bound

Every distinct energy of $`H_n`$ differs by an integer multiple of the **same** fixed $`g`$. Apply (1) to the entire product space with $`a=\beta g/4`$, so that $`\kappa=\beta/2`$. For $`s\le a/(2M)`$, (5) gives

```math
\boxed{
W_n(\delta)\le
\frac2\beta\left[\frac{R^2s}{2a}+e^{-a}\right]
\exp\!\left[-\frac{a^2}{2R^2s}\right],
\qquad s=n\delta^2.
}
\tag{6}
```

The constants in the headline form can therefore be chosen as

```math
A=\frac{2e^{-a}}\beta,\qquad
B=\frac{e^aR^2}{2a},\qquad
c_0=\frac{a^2}{2R^2},\qquad
s_0=\frac{a}{2M}.
```

They are independent of the exponentially growing Hilbert-space dimension and of $`n`$. The fixed lattice spacing enters through $`a`$; replacing it by a gap that shrinks with $`n`$ would change the conclusion.

For sufficiently small $`\delta`$, the quadratic work density obeys
$`n w_\infty(\delta)\ge(v/(4\beta))s`$. Thus

```math
\frac{W_n(\delta)}{n w_\infty(\delta)}
\le
\frac{8}{v}
\left[\frac{R^2s}{2a}+e^{-a}\right]
\frac{e^{-a^2/(2R^2s)}}s
\longrightarrow0\quad(s\to0).
```

For every fixed $`f\gt 0`$, one can choose a fixed $`s_f\gt 0`$ so that **all** sufficiently small $`\delta`$ and **all** integers with $`n\delta^2\le s_f`$ fail to recover fraction $`f`$. This proves $`N_f(\delta)=\Omega(\delta^{-2})`$ without assuming a monotone yield curve.

## 5. Why the energy-bandwidth factor matters

A trace-distance comparison with a passive reference would instead give a bound proportional to $`\|H_n\|_\infty\|P-\sigma\|_1`$. The energy bandwidth is extensive, so this leaves an extra factor $`n`$. After normalization by the available work, that factor prevents a converse throughout the entire window $`n\delta^2\to0`$.

The order comparison (1) removes that loss. For example, at $`n=\lfloor\delta^{-2}/\sqrt{\log(1/\delta)}\rfloor`$, (6) still proves a vanishing work fraction, whereas an estimate of the form $`Cn e^{-c/(n\delta^2)}`$ does not. This is the quantitative distinction from the directly related rational-qutrit passive-approximation argument discussed in [related work](../references/RELATED_WORK.md#concurrent-work).
