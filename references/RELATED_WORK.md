# Related work and attribution

The result concerns a joint limit: the number of copies grows while a fixed finite-dimensional input approaches a Gibbs state. The operation is an arbitrary system-only cyclic unitary, and the objective is a fixed fraction of **mean ergotropy**. These details distinguish the theorem from fixed-state asymptotic conversion, fixed-error battery extraction and statements about the first population inversion.

The comparison below identifies the closest inspected results. It is a bounded literature comparison, not an exhaustive priority claim. Bibliographic entries are in [references.bib](references.bib).

## Alicki-Fannes

**Robert Alicki and Mark Fannes, “Entanglement boost for extractable work from ensembles of quantum batteries,” Physical Review E 87, 042123 (2013).** [Publisher](https://doi.org/10.1103/PhysRevE.87.042123) · [Author preprint](https://arxiv.org/abs/1211.1209).

The equal-entropy Gibbs endpoint and its attainability per copy in the fixed-state many-copy limit are inherited. This repository does not claim that endpoint as a new result. It asks how the necessary block size behaves when the state itself approaches Gibbs. The finite-block upper bound by the Gibbs endpoint is also derived directly from relative entropy in the [model](../science/model.md#3-available-work-and-its-quadratic-coefficient).

## Collective concentration and type matching

**Martí Perarnau-Llobet and Raam Uzdin, “Collective operations can extremely reduce work fluctuations,” New Journal of Physics 21, 083023 (2019).** [Publisher](https://doi.org/10.1088/1367-2630/ab36a9) · [Version 3](https://arxiv.org/abs/1810.02237v3).

Their collective protocols and type shifts toward the equal-entropy Gibbs state are essential foundations. In particular, equation (20) and the associated concentration estimate already make an inverse-square sufficient scale natural near Gibbs. They treat isolated work extraction as well as a thermal-bath setting; the isolated setting must not be presented as absent from their work.

The constructive proof here is a quantified finite-spectrum implementation with an explicit quarter yield. Its role is to match the converse throughout the joint limit. The existence of a type-shift protocol or the sufficient exponent alone is not the added conclusion.

## Second-order thermodynamics

**Christopher T. Chubb, Marco Tomamichel and Kamil Korzekwa, “Beyond the thermodynamic limit: finite-size corrections to state interconversion rates,” Quantum 2, 108 (2018).** [Publisher](https://doi.org/10.22331/q-2018-11-27-108) · [Version 5](https://arxiv.org/abs/1711.01193v5).

Definition 1 and Theorem 10 concern thermal operations with a Gibbs bath and fixed-infidelity state conversion. Equations (62)–(67) discuss work distillation and formation through a battery. Their second-order terms give an important statistical interpretation of the inverse-square scale.

Our inference from those hypotheses is that the theorem does not directly supply the present isolated **mean-energy** converse: a useful mean decrease need not produce their fixed-fidelity product target, and the fixed-input expansion is not stated as a uniform theorem for an input tending to Gibbs. The comparison credits the statistical scale while retaining the different operational claim.

## Passivity deformation

**Raam Uzdin and Saar Rahav, “Passivity Deformation Approach for the Thermodynamics of Isolated Quantum Setups,” PRX Quantum 2, 010336 (2021).** [Publisher](https://doi.org/10.1103/PRXQuantum.2.010336) · [Author preprint](https://arxiv.org/abs/1912.07922).

Ordering-preserving deformation of observables is an established method for thermodynamic bounds. The common-order rearrangement step in the [clipping lemma](../science/passive_clipping.md#1-a-finite-passive-reference-lemma) belongs to that methodological foundation.

The specific estimate used here combines the clipped likelihood reference $`\sigma`$ with $`K=-\log\sigma`$ and $`K-(\beta-2a/g)H`$. Relative entropy then controls energy without a dimension or energy-bandwidth factor. The clipping-tail normalization and its product-state use are proved explicitly in this account.

## Finite-copy passivity and geometry

**Raffaele Salvia and Vittorio Giovannetti, “Energy upper bound for structurally stable N-passive states,” Quantum 4, 274 (2020).** [Publisher](https://doi.org/10.22331/q-2020-05-28-274) · [Version 4](https://arxiv.org/abs/1912.02099v4).

Their energy bounds use an $`N`$-passivity premise. The states considered here already activate at order $`\delta^{-1}`$, while the useful-work question concerns larger, nonpassive blocks. Thus that premise cannot simply be applied to obtain the useful-work converse. Passivizing one block also does not make its spectrum an independent tensor power for reuse of the theorem.

**Nikolaos Koukoulekidis, Rhea Alexander, Thomas Hebdige and David Jennings, “The geometry of passivity for quantum systems and a novel elementary derivation of the Gibbs state,” Quantum 5, 411 (2021).** [Publisher](https://doi.org/10.22331/q-2021-03-15-411) · [Version 3](https://arxiv.org/abs/1912.07968v3).

This supplies geometric background on passivity and Gibbs states. The uniform fixed-fraction mean-work threshold is not a statement identified in that inspected account.

## Rare-tail work in a different model

**“Exponentially Accurate Work Extraction by Swapping Detuned Bosonic Modes,” Pudim Physics Research Ledger, RO-2026-0008, version 1.0 (2026).** [Report page](https://pudimphysics.org/research/RO-2026-0008) · [Letter and supplement](https://pudimphysics.org/research/RO-2026-0008/releases/v1.0/combined.pdf).

This public AI research report is not identified here as peer-reviewed literature. Its ordered low-energy prefix and geometric-tail argument, including Supplementary Lemma 1 and equations (S7)–(S10), demonstrate exponentially weak work in a fixed two-mode model. Its stated scope excludes growing-copy arrays. Applying its low-energy-prefix estimate to tensor powers does not by itself retain typical probability mass. The qualitative rare-tail phenomenon should therefore be credited, while the growing-copy mean-work converse remains a different mathematical question.

## Related finite-bath work

The [Landauer-Bath-Threshold](https://github.com/GoGoKo699/Landauer-Bath-Threshold) project studies reversible erasure with a detuned finite reservoir. Its [spectral obstruction](https://github.com/GoGoKo699/Landauer-Bath-Threshold/blob/main/science/spectral_obstruction.md) uses complex spectral moments to distinguish available transitions from probability-weighted usefulness.

That distinction is a relevant conceptual antecedent. The present task fixes the Hamiltonian and varies independent input states, bounds extracted mean work rather than reset-channel heat, and uses a passive-reference inequality. Neither theorem directly implies the other.

## Concurrent work

The contemporaneous **Quantum-Work-Activation** research note (November 4, 2026; [project repository](https://github.com/GoGoKo699/Quantum-Work-Activation)) develops the same isolated mean-work block-size problem for near-Gibbs qutrits. Its rational-spectrum argument uses a clipped passive reference, concentration, and an energy-bandwidth estimate. The initial note is an unpublished derivation with remaining proof work, rather than a peer-reviewed result.

For a sufficiently small fixed fraction its rational-qutrit statement has the form

```math
\frac{c}{\delta^2\log(1/\delta)}
\le N_f(\delta)\le \frac{C}{\delta^2},
\qquad
W_n(\delta)\le Cn\,e^{-c/(n\delta^2)}.
```

The directly shared content includes the operational question, rational exponent two, passive-clipping entry point, and distinction between activation and useful mean work. Those are not presented here as an unrelated discovery.

| Compared feature | Quantitative conclusion of this account |
|---|---|
| Energy-bandwidth factor in the mean-work estimate | Removed by the order/relative-entropy comparison |
| Logarithmic gap in the necessary block size | Closed: every $`n=o(\delta^{-2})`$ has vanishing yield |
| Unspecified sufficiently small useful fraction | A rigorously constructed 25% fraction |
| Rational qutrit and one exponential tilt | Every fixed finite commensurate spectrum, including degeneracies, and every transverse diagonal $`C^2`$ path |

The companion investigation also considers irrational energy ratios. Those claims are outside the theorem proved here and are not used as proof dependencies. All fixed-lattice statements in this repository have self-contained proofs.

## The surviving statement

The [main theorem](../science/model.md#4-exact-threshold-theorem) combines a bound uniform over all unitaries and every subcritical block sequence with a constructive fixed-fraction upper bound. Its quantitative content is the constant-factor threshold for a general finite energy lattice. Published thermodynamic endpoints, concentration constructions, second-order scales, passivity deformations and the concurrent rational-qutrit argument remain explicitly credited.
