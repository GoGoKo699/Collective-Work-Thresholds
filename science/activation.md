# First activation and exponentially weak work

The [useful-work threshold](model.md#4-exact-threshold-theorem) asks for a fixed fraction of the thermodynamic resource. Strictly positive work requires a smaller block. This page proves its order and states precisely when the work at that scale has exponential size.

## 1. A passive lower window

For two product basis strings $`x,y`$ with $`E(x)\gt E(y)`$, the fixed lattice gives $`E(x)-E(y)\ge g`$. The one-copy likelihood range in [equation (3)](passive_clipping.md#3-product-likelihoods-near-equilibrium) therefore implies

```math
\log\frac{P_\delta(x)}{P_\delta(y)}
=-\beta(E(x)-E(y))+L(x)-L(y)
\le-\beta g+nR\delta.
```

If $`nR\delta\le\beta g`$, there is no strict population inversion across distinct energies. The state is passive and $`W_n=0`$. Population equality does not yield positive work. This proves $`N_{\mathrm{act}}=\Omega(\delta^{-1})`$.

## 2. An integer witness for activation

Let $`z`$ be the normalized integer energy labels and $`f`$ the score from the [model](model.md). Since $`v\gt 0`$, the vector $`f`$ is not in the real span of $`\mathbf1,z`$. The nullspace of an integer matrix is spanned by rational vectors. After clearing denominators and choosing a sign, there is a fixed $`r\in\mathbb Z^d`$ such that

```math
\mathbf1\cdot r=z\cdot r=0,\qquad
h=f\cdot r\gt 0.
```

The gcd condition and a zero energy label also give a fixed Bezout vector $`t\in\mathbb Z^d`$ with

```math
\mathbf1\cdot t=0,\qquad z\cdot t=1.
```

Define

```math
L_\delta=\left\lceil\frac{2\beta g}{h\delta}\right\rceil,
\qquad
m_\delta=L_\delta r+t.
```

Then $`\mathbf1\cdot m_\delta=0`$ and $`E\cdot m_\delta=g`$. The finite-dimensional expansion
$`\log p_\delta=\log q+\delta f+O(\delta^2)`$ gives

```math
\Gamma_\delta=m_\delta\cdot\log p_\delta
=-\beta g+\delta L_\delta h+O(\delta)
=\beta g+O(\delta)\gt 0.
```

The remainder is controlled because $`\|m_\delta\|_1=O(\delta^{-1})`$. The positive and negative parts of $`m_\delta`$ are valid types of equal length

```math
n_\delta=\frac12\|m_\delta\|_1=\Theta(\delta^{-1}).
```

A string of the positive type has energy $`g`$ greater and probability $`e^{\Gamma_\delta}`$ times that of a string of the negative type. Swapping them extracts positive mean work. Combining this with the passive window proves

```math
\boxed{N_{\mathrm{act}}(\delta)=\Theta(\delta^{-1}).}
```

This construction includes degeneracies: a score varying within a degenerate shell supplies a zero-energy integer direction $`r`$, while the Bezout correction supplies the positive gap.

## 3. Work at a fixed factor beyond the witness scale

The constructed block satisfies

```math
\delta n_\delta\longrightarrow
C_{\mathrm{act}}:=\frac{\beta g\|r\|_1}{h}.
```

For any integer sequence with $`n(\delta)\delta\to C\gt C_{\mathrm{act}}`$, pad both witness strings with the same labels to length $`n(\delta)`$. Their energy gap and probability-ratio margin remain unchanged. Positivity gives a fixed bound $`p_{\delta,j}\ge q_{\min}/2`$, so the witness probability is at least $`(q_{\min}/2)^n`$. This proves an exponential lower bound. The uniform converse, with $`n\delta^2\sim C\delta`$, supplies the matching exponential upper order:

```math
e^{-C_1/\delta}\le W_{n(\delta)}(\delta)
\le e^{-c_1/\delta}
\quad\text{for sufficiently small }\delta,
```

for fixed positive constants $`C_1,c_1`$. Meanwhile $`n w_\infty=\Theta(\delta)`$.

This does **not** give an exponential lower bound at the exact least activating integer, where a population inversion can approach a tie arbitrarily rapidly. The [qutrit example](qutrit.md#3-why-exact-onset-needs-a-qualification) gives a concrete sequence for which the first positive work is smaller than $`e^{-C/\delta}`$ for every fixed $`C`$.
