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

[Quantum-Work-Activation](https://github.com/GoGoKo699/Quantum-Work-Activation) develops the same isolated mean-work block-size problem for near-Gibbs qutrits, with additional fixed-irrational and calibration results. Its inspected [one-third construction](https://github.com/GoGoKo699/Quantum-Work-Activation/blob/3fb4500d87acdb60746e10a9a5ae5917a2b698ec/science/achievability.md) and [two-copy boundary](https://github.com/GoGoKo699/Quantum-Work-Activation/blob/3fb4500d87acdb60746e10a9a5ae5917a2b698ec/science/calibration.md) are inherited ingredients with their own proofs. These are repository research results, not claims of peer-reviewed publication.

The directly shared content includes the operational question, rational exponent two, passive-clipping entry point and distinction between activation and useful mean work. QWA's earlier rational converse used an extensive energy-bandwidth factor and left a logarithmic gap. This repository's [bandwidth-free converse](../science/passive_clipping.md#4-the-uniform-work-bound) removes that loss. Combined with QWA's one-third construction, it gives

```math
N_f(\delta;\alpha)=\Theta(\delta^{-2}),
\qquad \alpha\gt1\text{ fixed rational},\quad0\lt f\le1/3.
```

**CWT supplies the inherited all-unitary necessity; QWA supplies the inherited one-third sufficiency.** Their combination is a reconciliation, not another discovery of either ingredient. The [qutrit account](../science/qutrit_transfer.md#2-the-fixed-rational-reconciliation) verifies the transversality and fixed-lattice hypotheses. The general CWT quarter-yield result retains the broader scope of arbitrary fixed finite commensurate spectra, degeneracies and transverse diagonal $`C^2`$ paths.

The additional joint step is a finite entropy comparison between actual detuned work and harmonic work on the same matched input. It yields $`N_{1/10}(\delta;2+\nu\delta^{3/2})=\Theta(\delta^{-2})`$ for fixed $`\beta,\nu\gt0`$, after checking the actual equal-entropy Gibbs benchmark. The [full local account](../science/qutrit_transfer.md) states and proves that implication; QWA's [matched-detuning account](https://github.com/GoGoKo699/Quantum-Work-Activation/blob/main/science/matched_detuning.md) develops the complementary spectral-arithmetic perspective.

QWA's order-$`\delta`$ example with $`N_{1/10}=2`$ remains intact. The new matched path theorem supplies neither a full crossover law nor a classification by the rational/irrational status of each moving parameter. QWA's fixed-irrational conclusions retain their own hypotheses and are not used as proof dependencies here.

## The surviving statement

The [main theorem](../science/model.md#4-exact-threshold-theorem) combines a bound uniform over all unitaries and every subcritical block sequence with a constructive fixed-fraction upper bound. Its quantitative content is the constant-factor threshold for a general finite energy lattice. Published thermodynamic endpoints, concentration constructions, second-order scales, passivity deformations and the concurrent rational-qutrit argument remain explicitly credited.
