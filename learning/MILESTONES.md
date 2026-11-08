# Thirty milestones for Collective Work Thresholds

How many nearly thermal systems must be controlled together before their extractable work becomes useful? This map connects the state of one system to the distinction between a first population inversion and a fixed fraction of the available mean work.

The allocation is **12 background/preliminaries milestones and 18 narrative/innovation milestones**. The background must join five kinds of information: quantum states and allowed operations, spectral ordering, entropy, concentration, and integer occupation counts. The longer narrative then needs both sides of the result: a bound on every unitary and a concrete permutation that attains a useful fraction. It also needs the smaller activation threshold, the entropy comparison for the specified matched detuning, and the assumptions that separate this task from other work-extraction problems. This is why the proof mechanisms receive more space than the foundations.

Each phase proceeds from local objects to their global use. The background ends by assembling the operational question; the narrative ends by integrating the two thresholds, their proofs, resources, and limits. These are common understanding targets. The canonical science pages retain the full calculations and specialist details.

The sole educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [Watrous bridge](WATROUS_BRIDGE.md#the-selected-anchor) gives the source edition, targeted sections, notation translations, and locally supplied thermodynamic steps. The sections cited below support the question at hand; they are not a requirement to read the book in order. Research references remain in the [related-work account](../references/RELATED_WORK.md).

## Background and preliminaries — 12 milestones

### M01: Populations and energy

**Central question.** What information specifies one input system and its mean energy?

**Understanding target.** Interpret the Hamiltonian, a diagonal density operator, its probabilities, and $`\mathrm{Tr}(\rho H)`$. Distinguish an energy eigenvector from an energy value: several basis states may share one energy.

**Dependencies and story role.** None. This establishes the objects whose probabilities and energies will later be rearranged.

**Conceptual connection.** A classical probability vector is also the spectrum of this quantum state; the energy basis supplies its physical meaning.

**Source pointers.** Watrous §2.1; [states, spectra, and work](WATROUS_BRIDGE.md#states-spectra-and-work); [model §1](../science/model.md#1-fixed-system-and-admissible-operations).

### M02: Independent copies form one controlled block

**Central question.** How do one-copy probabilities and energies combine?

**Understanding target.** Explain why a product string has probability equal to a product of populations and energy equal to a sum of one-copy energies. Distinguish independent preparation from a control operation that may act jointly on all copies.

**Dependencies and story role.** M01. The single-system description becomes the growing block on which work is optimized.

**Conceptual connection.** Tensor products become ordinary products and sums in the energy basis, making quantum rearrangement accessible to probability and counting.

**Source pointers.** Watrous §2.1; [state bridge](WATROUS_BRIDGE.md#states-spectra-and-work); [block Hamiltonian and state](../science/model.md#1-fixed-system-and-admissible-operations).

### M03: Cyclic driving and mean work

**Central question.** What can the permitted operation change, and what is counted as work?

**Understanding target.** Explain why a cyclic unitary can lower mean system energy while preserving the state spectrum. Distinguish this operation from a unitary required to commute with the Hamiltonian, and distinguish mean work from a guaranteed battery output.

**Dependencies and story role.** M01–M02. This fixes the optimization before introducing any bound or protocol.

**Conceptual connection.** Spectral invariance constrains the state, while unrestricted driving can change its alignment with energy.

**Source pointers.** [State and work bridge](WATROUS_BRIDGE.md#states-spectra-and-work); [admissible operations](../science/model.md#1-fixed-system-and-admissible-operations); [resource accounting](../science/interpretation.md#2-what-the-resource-statement-does-and-does-not-charge).

### M04: Passivity as an ordering statement

**Central question.** When has a state already exhausted all work accessible to a unitary?

**Understanding target.** Relate passivity to placing larger populations at lower energies. Explain why a basis permutation attains the unrestricted unitary minimum, why ties give no positive gain, and why degeneracies do not require equal populations.

**Dependencies and story role.** M01–M03. The optimization becomes an ordered assignment of probabilities to energies.

**Conceptual connection.** Majorization and doubly stochastic mixing justify reducing a quantum optimization to rearrangement.

**Source pointers.** Watrous §§4.3.1–4.3.2; [sorting bridge](WATROUS_BRIDGE.md#states-spectra-and-work); [passivity in the model](../science/model.md#1-fixed-system-and-admissible-operations).

### M05: Gibbs states remain passive across copies

**Central question.** Why is a Gibbs state the equilibrium reference for this task?

**Understanding target.** Explain how $`q_j\propto e^{-\beta E_j}`$ orders populations when $`\beta\gt0`$, and why its product probabilities depend only on total energy with the same inverse temperature. Distinguish changing temperature from introducing a nonthermal direction.

**Dependencies and story role.** M02–M04. This identifies the reference family around which the project studies weak departures.

**Conceptual connection.** Exponential weights turn energy additivity into passivity at every copy number.

**Source pointers.** [Entropy and equilibrium bridge](WATROUS_BRIDGE.md#entropy-and-the-available-work); [Gibbs reference](../science/model.md#1-fixed-system-and-admissible-operations); [temperature paths](../science/interpretation.md#4-the-transverse-derivative-fixes-the-exponent).

### M06: Entropy is an invariant constraint

**Central question.** What does a unitary preserve beyond normalization?

**Understanding target.** Interpret entropy as a function of the state's populations, with unitary invariance and product additivity. Explain why equal entropy is a necessary condition for unitary conversion but does not make two finite-copy states unitarily equivalent.

**Dependencies and story role.** M03–M05. This supplies the invariant constraint used to define the available-work benchmark.

**Conceptual connection.** Entropy retains part of the spectral constraint; the next step turns that information into an energy bound.

**Source pointers.** Watrous §§5.1–5.2; [entropy bridge](WATROUS_BRIDGE.md#entropy-and-the-available-work); [available work](../science/model.md#3-available-work-and-its-quadratic-coefficient).

### M07: Relative entropy and likelihood ratios

**Central question.** How can a logarithmic comparison of states constrain energy?

**Understanding target.** Interpret $`D(p\Vert q)=\sum_jp_j\ln(p_j/q_j)`$ and its nonnegativity, asymmetry, and product additivity. Explain how a Gibbs reference converts positivity into an energy bound at fixed entropy. Keep the project's natural logarithms consistent with the book's base-two convention, and recognize how data processing and binary Pinsker control an occupation change.

**Dependencies and story role.** M01, M02, M06. This supplies the information quantity used in both normalization and the converse.

**Conceptual connection.** Relative entropy is an average log-likelihood; when the reference is Gibbs, its logarithm contains the Hamiltonian.

**Source pointers.** Watrous §§5.1–5.2, including Theorems 5.15 and 5.38; [entropy and logarithm conventions](WATROUS_BRIDGE.md#entropy-and-the-available-work); [Gibbs relative-entropy identity](../science/model.md#3-available-work-and-its-quadratic-coefficient).

### M08: Separate a temperature change from nonthermality

**Central question.** Which part of a small population change can generate thermodynamic work?

**Understanding target.** Explain the score $`f_j=p'_{0,j}/q_j`$ and its projection away from the energy direction. Interpret the residual vector $`u`$ and coefficient $`v`$; identify why $`v\gt0`$ excludes a purely tangent temperature perturbation.

**Dependencies and story role.** M05–M07. This identifies the local perturbation to which the theorem applies.

**Conceptual connection.** A covariance projection removes the first-order change that can be absorbed into another Gibbs state.

**Source pointers.** [Temperature-direction bridge](WATROUS_BRIDGE.md#removing-the-temperature-direction); [nonthermal direction](../science/model.md#2-the-nonthermal-direction); [tangent-path boundary](../science/interpretation.md#4-the-transverse-derivative-fixes-the-exponent).

### M09: The available work is quadratic

**Central question.** What is the correct work scale near equilibrium?

**Understanding target.** Connect the equal-entropy reference $`q_{\beta_\delta}`$ and the local relative-entropy expansion to $`w_\infty(\delta)=v\delta^2/(2\beta)+o(\delta^2)`$. Explain why comparing only with the original-temperature Gibbs state would retain an unwanted temperature component.

**Dependencies and story role.** M06–M08. This fixes the normalization against which finite-block work must be measured.

**Conceptual connection.** The quadratic information cost of the transverse displacement becomes a quadratic energy resource.

**Source pointers.** Watrous §5.2 for relative entropy; [local projection bridge](WATROUS_BRIDGE.md#removing-the-temperature-direction); [coefficient and derivation](../science/model.md#3-available-work-and-its-quadratic-coefficient).

### M10: Sums of small likelihood changes

**Central question.** Why do extreme and typical product populations suggest different copy scales?

**Understanding target.** Distinguish an extreme log-likelihood difference of order $`n\delta`$ from fluctuations of order $`\delta\sqrt n`$ and mean drift of order $`n\delta^2`$. Explain what independence and bounded increments contribute to concentration.

**Dependencies and story role.** M02, M07–M09. This supplies the statistical vocabulary for the gap between possible and useful work.

**Conceptual connection.** The same one-copy perturbation has a linear extreme range and a smaller typical fluctuation scale.

**Source pointers.** Watrous §1.2.2; [concentration bridge](WATROUS_BRIDGE.md#concentration-as-the-state-changes); [two likelihood scales](../science/interpretation.md#1-two-ways-a-likelihood-can-become-large).

### M11: Energy lattices and occupation types

**Central question.** How can exponentially many strings be described without listing them?

**Understanding target.** Interpret an integer occupation vector, its energy, and its multinomial multiplicity. Distinguish one string's probability from the total mass of its type. Explain why a fixed commensurate spectrum retains a positive lower gap bound in every product block.

**Dependencies and story role.** M01–M02, M05. This adds the discrete framework needed for activation witnesses and collective transport.

**Conceptual connection.** Copy counts turn spectral rearrangement into integer geometry, while multiplicities turn individual probabilities into macroscopic mass.

**Source pointers.** [Types-to-work bridge](WATROUS_BRIDGE.md#turning-types-into-useful-work); [energy lattice](../science/model.md#1-fixed-system-and-admissible-operations); [type multiplicities](../science/useful_work.md#4-an-exact-factorial-bound-for-the-type-multiplicities).

### M12: Assemble the two-threshold question

**Central question.** What exactly must a block achieve before its work counts as useful?

**Understanding target.** Put the known input, fixed Hamiltonian, permitted unitary, and quadratic work benchmark into one operational question. Distinguish $`N_{\mathrm{act}}`$ from $`N_f`$ and explain why a fixed-state infinite-copy result does not determine their behavior as the input approaches Gibbs.

**Dependencies and story role.** M01–M11. This integrates the background into the project rather than adding another prerequisite.

**Conceptual connection.** Spectral possibility, probability mass, and thermodynamic normalization must be considered in the same joint limit.

**Source pointers.** [Theorem and resources bridge](WATROUS_BRIDGE.md#the-theorem-its-resources-and-its-boundaries); [threshold definitions](../science/model.md#4-exact-threshold-theorem); [inherited thermodynamic endpoint](../references/RELATED_WORK.md#alicki-fannes).

## Narrative and innovation — 18 milestones

### M13: A concrete population inversion

**Central question.** Which qutrit occupation patterns first make a profitable swap possible?

**Understanding target.** Use the log-weight $`-\beta E+\delta A`$ to compare two strings. Explain how the parity constraint and a strict inversion make the first activating block the smallest odd integer strictly greater than $`\beta/\delta`$.

**Dependencies and story role.** M04, M10–M12. The narrative starts with an individual swap whose energy and probability gain are visible.

**Conceptual connection.** An integer occupation constraint determines exact onset, while equality of populations yields zero work.

**Source pointers.** [Complete three-copy swap](WATROUS_BRIDGE.md#a-complete-three-copy-swap); [exact qutrit onset](../science/qutrit.md#1-exact-first-activation).

### M14: The general activation scale

**Central question.** Why does first activation have inverse-linear order for every allowed energy lattice?

**Understanding target.** Combine the passive lower window with an integer direction that preserves copy number and energy, plus a fixed correction supplying one positive energy gap. Explain how transversality makes that direction profitable at order $`\delta^{-1}`$ copies.

**Dependencies and story role.** M08, M10–M13. The local qutrit mechanism becomes a general finite-spectrum existence statement.

**Conceptual connection.** A rational nullspace and a Bezout correction convert a nonthermal derivative into an admissible pair of product types.

**Source pointers.** [Early-inversion bridge](WATROUS_BRIDGE.md#why-the-first-inversion-comes-earlier); [passive window](../science/activation.md#1-a-passive-lower-window); [integer witness](../science/activation.md#2-an-integer-witness-for-activation).

### M15: A normalized clipped reference

**Central question.** Can a reference retain ordinary populations while limiting dangerous likelihood excursions?

**Understanding target.** Explain the clipped log-likelihood relative to the fixed reference $`q=q_\beta`$, the condition $`0\lt a\lt\beta g/2`$, and the normalized state $`\sigma_i=q_i e^{F_i}/Z_c`$. Identify why its normalization cannot be omitted from a relative-entropy argument.

**Dependencies and story role.** M05, M07, M10–M12. This introduces the local object from which the all-unitary converse is built.

**Conceptual connection.** The fixed energy gap permits bounded likelihood changes without reversing the equilibrium order across energy shells.

**Source pointers.** [Clipping bridge](WATROUS_BRIDGE.md#clipping-a-likelihood-without-paying-for-bandwidth); [finite passive-reference lemma](../science/passive_clipping.md#1-a-finite-passive-reference-lemma).

### M16: Three observables share one minimizing order

**Central question.** Why does sorting the state once control both physical energy and logarithmic energy?

**Understanding target.** Explain the common spectral ordering of $`H`$, $`K=-\ln\sigma`$, and $`B=K-\kappa H`$. Account for ties within degenerate energy shells and identify the one permutation that minimizes all three expectations.

**Dependencies and story role.** M04, M11, M15. The reference becomes an energy comparison valid beyond a chosen swap.

**Conceptual connection.** Majorization-based rearrangement can compare observables when their spectral orders are compatible; arbitrary observables need not have this property.

**Source pointers.** Watrous §§4.3.1–4.3.2; [ordering bridge](WATROUS_BRIDGE.md#clipping-a-likelihood-without-paying-for-bandwidth); [common spectral order](../science/passive_clipping.md#common-spectral-order).

### M17: Relative entropy bounds every unitary

**Central question.** How does information loss become a bound on extractable mean energy?

**Understanding target.** Connect $`W_K=D(p\Vert\sigma)-D(p^\downarrow\Vert\sigma)`$ to the common-order inequality and obtain $`W_H\le D(p\Vert\sigma)/\kappa`$. Explain why the resulting coefficient contains neither the dimension nor the maximum energy.

**Dependencies and story role.** M06–M07, M15–M16. This is the central finite-system comparison used in the converse.

**Conceptual connection.** Entropy invariance removes the state-entropy term, and relative-entropy positivity bounds the remaining spectral rearrangement.

**Source pointers.** Watrous §5.2; [clipping-to-energy bridge](WATROUS_BRIDGE.md#clipping-a-likelihood-without-paying-for-bandwidth); [lemma and proof](../science/passive_clipping.md#1-a-finite-passive-reference-lemma).

### M18: Normalization leaves two controlled tails

**Central question.** Which rare events determine the information cost of clipping?

**Understanding target.** Explain why the upper likelihood excess is averaged under the input law, while the lower-tail normalization correction is bounded under the Gibbs law. Follow the sign cancellations that produce the tail bound without assuming $`Z_c`$ is close to one.

**Dependencies and story role.** M07, M15, M17. The abstract relative-entropy bound is reduced to explicit probability estimates.

**Conceptual connection.** A normalized comparison state couples two probability laws; controlling only one tail would miss part of its cost.

**Source pointers.** [Clipping bridge](WATROUS_BRIDGE.md#clipping-a-likelihood-without-paying-for-bandwidth); [exact normalization and tails](../science/passive_clipping.md#2-exact-control-of-normalization-and-tails).

### M19: Concentration while the input approaches Gibbs

**Central question.** How can a tail estimate remain useful when both the state and copy number change?

**Understanding target.** Apply bounded-increment concentration under each product law, including its different mean. Explain how likelihood range $`O(\delta)`$ and drift $`O(n\delta^2)`$ lead to exponential suppression in $`1/(n\delta^2)`$, and how integrating a tail controls its excess expectation.

**Dependencies and story role.** M10, M18. This converts the finite reference construction into a uniform estimate along the joint limit.

**Conceptual connection.** The effective fluctuation parameter is the total squared perturbation, not copy number alone.

**Source pointers.** Watrous §1.2.2; [concentration bridge and local one-sided derivation](WATROUS_BRIDGE.md#concentration-as-the-state-changes); [product likelihood proof](../science/passive_clipping.md#3-product-likelihoods-near-equilibrium).

### M20: A uniform bound without an extensive factor

**Central question.** Why does the converse survive the exponentially growing product space?

**Understanding target.** Apply the finite lemma to $`H_n`$ using the same gap bound $`g`$. Explain the form $`W_n\le A(1+Bs)e^{-c_0/s}`$ with $`s=n\delta^2`$, and the order of quantifiers: fixed constants, all sufficiently small perturbations, and every block with $`s\le s_0`$.

**Dependencies and story role.** M11, M17–M19. The local comparison and concentration estimates become the global all-unitary bound.

**Conceptual connection.** The gap controls the cost of spectral reordering even though the total energy bandwidth grows with the block.

**Source pointers.** [Converse bridge](WATROUS_BRIDGE.md#clipping-a-likelihood-without-paying-for-bandwidth); [uniform work bound](../science/passive_clipping.md#4-the-uniform-work-bound); [bandwidth comparison](../science/passive_clipping.md#5-why-the-energy-bandwidth-factor-matters).

### M21: Positive work can remain a vanishing resource fraction

**Central question.** What does the converse say after a block has already activated?

**Understanding target.** Divide the work bound by the quadratic available work and explain why every $`n\delta^2\to0`$ sequence has vanishing yield. Relate this to exponentially weak work at a fixed factor beyond the activation witness, while preserving the qualification at the exact first activating integer.

**Dependencies and story role.** M09, M12–M14, M20. This integrates activation and necessity into the physical separation of the two scales.

**Conceptual connection.** Existence of a profitable pair does not imply that enough probability mass can be moved to recover a fixed fraction.

**Source pointers.** [Normalized converse](../science/passive_clipping.md#4-the-uniform-work-bound); [work beyond the witness scale](../science/activation.md#3-work-at-a-fixed-factor-beyond-the-witness-scale); [exact-onset qualification](../science/qutrit.md#3-why-exact-onset-needs-a-qualification).

### M22: Choose a collective transport direction

**Central question.** Which type displacement can turn the thermodynamic endpoint into a finite operation?

**Understanding target.** Explain the choice $`m\approx\alpha n(p_\delta-q_{\beta_\delta})`$ with $`\alpha=3/4`$ and its bounded integer correction. Identify why rounding the energy downward preserves a useful lower bound on the probability ratio, through the forward and reverse relative entropies.

**Dependencies and story role.** M07–M09, M11–M12. The sufficiency argument starts with one transport direction toward the equal-entropy endpoint.

**Conceptual connection.** A continuous thermodynamic displacement must respect exact copy counts and the discrete energy lattice before it can describe a permutation.

**Source pointers.** [Types-to-work bridge](WATROUS_BRIDGE.md#turning-types-into-useful-work); [bounded rounding](../science/useful_work.md#3-bounded-integer-rounding-with-the-energy-rounded-downward); [probability ratio](../science/useful_work.md#the-individual-probability-ratio).

### M23: Destination multiplicity is a capacity constraint

**Central question.** Why are profitable individual moves insufficient to define the collective transport?

**Understanding target.** Explain why every selected source string needs a distinct destination. Relate the multiplicity ratio to a linear probability gain, a quadratic counting cost, and a finite error uniform over types within $`K\sqrt n`$ of the mean.

**Dependencies and story role.** M11, M22. The proposed displacement acquires a verified capacity bound across an entire typical set.

**Conceptual connection.** Counting available states supplies the reversible matching constraint that thermodynamic energy differences alone do not provide.

**Source pointers.** [Construction bridge](WATROUS_BRIDGE.md#turning-types-into-useful-work); [exact factorial and multiplicity bounds](../science/useful_work.md#4-an-exact-factorial-bound-for-the-type-multiplicities).

### M24: Reserve disjoint energy residues with substantial mass

**Central question.** How can source and destination regions be separated without losing almost all input probability?

**Understanding target.** For a lattice energy drop $`gw`$ with integer $`w`$, explain the upper-half selection modulo $`2w`$ in lattice units, the typical-set probability bound, and the Fourier argument for residue mixing. Identify why positivity, a zero energy label, and the gcd condition suffice even with degenerate levels.

**Dependencies and story role.** M10–M11, M22–M23. The transport gains a source region of nonvanishing total probability.

**Conceptual connection.** Finite-group mixing reconciles arithmetic separation with a probability-mass requirement.

**Source pointers.** [Types-to-work bridge](WATROUS_BRIDGE.md#turning-types-into-useful-work); [source mass lemma](../science/useful_work.md#5-finite-sufficient-condition-lemma-and-actual-source-mass); [uniform modulo estimate](../science/useful_work.md#uniform-modulo-mixing-for-those-moduli).

### M25: Assemble one unitary and count its actual work

**Central question.** When do all the proposed injections form a single valid work-extracting operation?

**Understanding target.** Explain why different source types have different target types and no target is also a selected source. Combine their disjoint transpositions and obtain energy drop times source mass times $`1-e^{-R}`$, where $`R`$ is the pair's log-probability ratio. The target populations must be subtracted.

**Dependencies and story role.** M03–M04, M22–M24. The local capacity and mass estimates become an actual unitary on the supplied copies.

**Conceptual connection.** Reversible matching and correct probability accounting jointly certify mean work without an auxiliary entropy sink.

**Source pointers.** [Construction bridge](WATROUS_BRIDGE.md#turning-types-into-useful-work); [finite extraction certificate and disjointness](../science/useful_work.md#5-finite-sufficient-condition-lemma-and-actual-source-mass).

### M26: One fixed inverse-square block scale gives quarter yield

**Central question.** Why can the constructive constants be chosen once for all sufficiently small perturbations?

**Understanding target.** Explain the order of choices: fix a sufficiently large $`C`$, set $`n=\lceil C/\delta^2\rceil`$, then restrict the perturbation interval. Connect the multiplicity margin, positive energy drop, finite set of moduli, and probability mass to the quarter-yield guarantee.

**Dependencies and story role.** M09, M22–M25. This assembles the constructive upper bound matching the necessary scale.

**Conceptual connection.** Controlled integer discontinuities are compatible with a uniform asymptotic statement; the conservative constant need not be optimal.

**Source pointers.** [Construction bridge](WATROUS_BRIDGE.md#turning-types-into-useful-work); [explicit constant and interval choice, §6](../science/useful_work.md); [bounded possible energy drops](../science/useful_work.md#positive-work-drop-and-a-finite-set-of-possible-moduli).

### M27: What finite qutrit calculations establish

**Central question.** How can a finite calculation illuminate the theorem without replacing its proof?

**Understanding target.** Explain sorting type populations against energy-shell capacities, preserving exact ties, and evaluating work through a positive sum. Interpret finite checks of the detuning sandwich and actual thermodynamic benchmark. Distinguish exact integer counting from rounded probability arithmetic and observed numerical agreement from a uniform theorem or crossover law.

**Dependencies and story role.** M04, M11, M13, M21, M26. The general result reconnects to a fully specified example and its finite evidence.

**Conceptual connection.** Spectral rearrangement gives both an analytical characterization and a computational route, with different guarantees.

**Source pointers.** [Small complete swap](WATROUS_BRIDGE.md#a-complete-three-copy-swap); [finite rearrangement and numerical meaning](../science/qutrit.md#4-finite-rearrangement); [near-tie behavior](../science/qutrit.md#3-why-exact-onset-needs-a-qualification).

### M28: Entropy bounds the cost of changing the energy objective

**Central question.** How can the same input be compared under harmonic and detuned Hamiltonians without a shrinking-gap assumption?

**Understanding target.** For a matched top-level tilt, explain $`t=\delta-\beta\epsilon`$, $`W_\epsilon=W_0+\epsilon L`$ and $`D(\sigma\Vert P)=\delta L-\beta W_\epsilon`$. Connect marginal entropy, binary data processing and Pinsker to $`D\ge2L^2/n`$ and the exact uniform sandwich. Explain why the proof measurement adds no feedback resource to the operation.

**Dependencies and story role.** M03, M06–M07, M20–M21. The information toolkit controls a change of physical objective after the fixed-lattice converse has been established.

**Conceptual connection.** A small one-copy spectral change can have extensive energy effect, but entropy constrains how much occupation a useful unitary can move.

**Source pointers.** Watrous §§5.1–5.2; [entropy-comparison bridge](WATROUS_BRIDGE.md#comparing-actual-and-harmonic-work-by-entropy); [finite all-unitary comparison](../science/qutrit_transfer.md#3-an-entropy-comparison-for-the-actual-matched-state).

### M29: Combine inherited bounds using the actual benchmark

**Central question.** Which fixed-rational result transfers to the specified matched detuning, and why does the order-delta example survive?

**Understanding target.** Credit CWT's log-free converse and QWA's one-third construction separately. Verify that their fixed-rational combination gives $`N_f=\Theta(\delta^{-2})`$ for $`0\lt f\le1/3`$. For $`\epsilon=\nu\delta^{3/2}`$, connect the actual benchmark, the harmonic-to-actual ratio tending to one and the vanishing normalized comparison error to $`N_{1/10}=\Theta(\delta^{-2})`$. Retain the order-$`\delta`$ two-copy counterexample without inferring a full crossover law.

**Dependencies and story role.** M08–M09, M12, M20–M21, M26–M28. The inherited results and new finite comparison become one correctly normalized consequence.

**Conceptual connection.** Transferring a work bound and transferring a recovered fraction require different checks because the Hamiltonian also defines the benchmark.

**Source pointers.** [Fixed-rational attribution](../science/qutrit_transfer.md#2-the-fixed-rational-reconciliation); [actual normalization](../science/qutrit_transfer.md#4-normalize-by-the-actual-hamiltonian); [matched-path threshold](../science/qutrit_transfer.md#5-the-specified-matched-detuning-threshold); [two-copy boundary](../science/qutrit_transfer.md#6-keep-the-order-delta-two-copy-boundary); [related-work comparison](../references/RELATED_WORK.md#concurrent-work).

### M30: Integrate the thresholds, assumptions and scientific ownership

**Central question.** How do spectral opportunity, probability mass and thermodynamic normalization fit into one account of collective work?

**Understanding target.** Explain the general fixed-lattice activation scale $`\Theta(\delta^{-1})`$ and quarter-yield scale $`\Theta(\delta^{-2})`$, together with the fixed-rational qutrit corollary and the specified matched-detuning result. Distinguish the moving path's two-copy activation from its useful-yield threshold. Identify which assumptions support spectral alignment, transverse quadratic normalization and a uniform gap, and how coherence or a tangent perturbation changes the conclusion. State inherited ownership and separate block size from gate complexity, duration, reliable work and a full crossover function.

**Dependencies and story role.** M12–M29. This integrates the entire narrative, its assumptions and the limits of the transferred conclusion.

**Conceptual connection.** Rare or low-gap spectral opportunities and probability-weighted usefulness are different operational questions; spectral order, information and integer transport connect them only under checked hypotheses.

**Source pointers.** [Theorem and resources bridge](WATROUS_BRIDGE.md#the-theorem-its-resources-and-its-boundaries); [exact general theorem](../science/model.md#4-exact-threshold-theorem); [physical boundaries](../science/interpretation.md); [matched qutrit account](../science/qutrit_transfer.md); [attribution](../references/RELATED_WORK.md#the-surviving-statement).
