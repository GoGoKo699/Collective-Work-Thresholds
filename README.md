# Collective Work Thresholds

**How many nearly thermal systems must be controlled together before a useful amount of work can be extracted?** For a fixed finite energy lattice, the first positive work appears at one scale, while a fixed fraction of the available mean work requires a parametrically larger block.

Let $`p_\delta`$ be a smooth diagonal perturbation of a positive-temperature Gibbs state, with a nonzero first-order departure from the Gibbs-temperature curve. Let $`W_n(\delta)`$ be the maximum mean energy decrease under an arbitrary cyclic unitary on $`n`$ independent copies, and let $`w_\infty(\delta)`$ be the established equal-entropy Gibbs work per copy.

| Quantity | Proven behavior as the state perturbation tends to zero |
|---|---|
| Available work per copy | $`w_\infty(\delta)=\frac{v}{2\beta}\delta^2+o(\delta^2)`$, with $`v\gt 0`$ |
| First block with positive work | $`N_{\mathrm{act}}(\delta)=\Theta(\delta^{-1})`$ |
| First block recovering at least 25% of the available mean work | $`N_{1/4}(\delta)=\Theta(\delta^{-2})`$ |

For all sufficiently small positive perturbations, the central converse holds for **every global unitary**. With $`s=n\delta^2`$, there are fixed positive constants such that

```math
W_n(\delta)\le A(1+Bs)\exp(-c_0/s),
\qquad 0\lt s\le s_0.
```

The constants depend on the fixed Hamiltonian, temperature and probability path, but not on the block size. Consequently every sequence with $`n\delta^2\to0`$ recovers a vanishing fraction of the thermodynamic work. The proof converts a clipped passive reference into an energy bound through relative entropy, avoiding an extensive energy-bandwidth factor.

## Connection with Quantum Work Activation

The sister project [Quantum-Work-Activation](https://github.com/GoGoKo699/Quantum-Work-Activation) studies the spectral arithmetic of the same mean-work task for qutrits. For every fixed rational ratio, **CWT's all-unitary converse** and **QWA's one-third construction** together give $`N_f=\Theta(\delta^{-2})`$ for $`0\lt f\le1/3`$. Each inherited ingredient retains its attribution; the general CWT quarter-yield theorem above retains its broader scope.

The [qutrit connection and matched-detuning proof](science/qutrit_transfer.md) establish a finite entropy comparison and its consequence

```math
N_{1/10}(\delta;2+\nu\delta^{3/2})=\Theta(\delta^{-2}),
\qquad \beta,\nu\gt0\ \text{fixed}.
```

The state is prepared as the Gibbs tilt of the actual detuned Hamiltonian, and the yield uses that Hamiltonian's own equal-entropy Gibbs benchmark. QWA's order-$`\delta`$ two-copy counterexample is retained: the specified order-$`\delta^{3/2}`$ result does not assert a full crossover law.

## Read the science

Start with the [model, exact theorem and thermodynamic normalization](science/model.md). The [passive-clipping bound](science/passive_clipping.md) proves necessity, and the [finite type-matching construction](science/useful_work.md) proves sufficiency. The [activation argument](science/activation.md) locates the smaller positive-work scale.

| Question | Authoritative account |
|---|---|
| Which systems, operations and asymptotic limits are included? | [Model and theorem](science/model.md) |
| Why can no collective unitary overcome the small-block barrier? | [Passive likelihood clipping](science/passive_clipping.md) |
| How can a permutation recover a fixed useful fraction? | [Useful-work construction](science/useful_work.md) |
| When does the first population inversion appear? | [Activation](science/activation.md) |
| What does the theorem look like for three levels? | [Qutrit example](science/qutrit.md) |
| How do the qutrit results combine, and what survives matched detuning? | [Qutrit transfer and entropy comparison](science/qutrit_transfer.md) |
| Why are the assumptions physically consequential? | [Interpretation and boundaries](science/interpretation.md) |
| How are finite work values checked without numerical cancellation? | [Verification](verification/README.md) |
| Which ingredients are inherited from earlier work? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

The proof allows repeated energies and arbitrary fixed finite commensurate spectra. It concerns mean work from known independent inputs under unrestricted global control. Gate complexity, operation time and reliable-work fluctuations are separate resources. The diagonal, fixed-spectrum and positive-temperature assumptions are essential.

For $`H=\mathrm{diag}(0,1,2)`$ and $`p_\delta\propto(1,e^{-\beta+\delta},e^{-2\beta})`$, first activation occurs at the **smallest odd integer strictly greater than** $`\beta/\delta`$. Equality is a population tie and produces no work.

The general theorem is a quantitative strengthening of passive-approximation and collective type-matching methods. Its comparison with the concurrent [Quantum-Work-Activation](https://github.com/GoGoKo699/Quantum-Work-Activation) investigation and with published results is stated in the [related-work account](references/RELATED_WORK.md).

## Learn the result

The educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**, available through the [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/).

Begin with the [Watrous-to-project bridge](learning/WATROUS_BRIDGE.md). It translates the relevant material on states, majorization, entropy, relative entropy and concentration into the work-extraction setting, then explains the additional thermodynamic and lattice arguments. A worked three-level example makes a collective population swap explicit; the bridge then uses data processing and Pinsker to compare actual and harmonic work.

The [30-milestone map](learning/MILESTONES.md) organizes the complete conceptual route into background/preliminaries and narrative/innovation. Its dependencies and source pointers connect the local mechanisms to the final two-threshold theorem. The map is shared by all readers; the specialist proofs remain in the scientific pages above. Reading the entire textbook is not a prerequisite.

## Reproduce the examples

From the repository root, run:

```bash
python3 verification/ergotropy_validate.py check --output verification/checked_cases.json
```

The module uses Python 3.10+ and its standard library. It keeps probability ordering and occupation multiplicities exact, evaluates work as a sum of nonnegative terms, and checks selected cases against independent full-spectrum enumeration and increased numerical precision. The [verification guide](verification/README.md) states the arithmetic limits and includes single-case commands. These finite checks do not replace the general proofs.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
