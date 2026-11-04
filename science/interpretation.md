# Physical interpretation and boundaries

The [two thresholds](model.md) describe different uses of collective control. A single population inversion makes some work possible. Recovering a fixed fraction requires rearranging enough probability mass to matter on the scale of the available thermodynamic resource.

## 1. Two ways a likelihood can become large

The perturbation changes a one-copy log-likelihood by order $`\delta`$. Across $`n`$ copies, an extreme pair of occupation patterns can accumulate a difference of order $`n\delta`$. It can overcome a fixed Gibbs penalty $`\beta g`$ when $`n`$ is of order $`\delta^{-1}`$. These are the rare activation witnesses.

Typical likelihood fluctuations instead have size $`\delta\sqrt n`$, and the mean likelihood drift has size $`n\delta^2`$. Both become order one on the larger scale $`n\sim\delta^{-2}`$. The [clipping argument](passive_clipping.md) turns this explanation into an upper bound valid for every unitary, rather than relying on a particular extraction recipe.

At blocks with $`n\delta`$ tending to a sufficiently large fixed constant, available work is of order $`\delta`$ but extractable work is exponentially small in $`1/\delta`$. At $`n=\lceil C/\delta^2\rceil`$, the [type construction](useful_work.md) extracts at least a quarter of the available work for a fixed sufficiently large $`C`$.

The construction is deliberately conservative. Its constants prove a scale law; they are not estimates of laboratory-ready block sizes or optimized controls.

## 2. What the resource statement does and does not charge

| Resource or task | Treatment |
|---|---|
| Copies controlled in one block | The quantity bounded above and below |
| Work | Mean system-energy decrease under cyclic driving |
| Input information | The state and Hamiltonian are known |
| Control | Arbitrary global unitary; an explicit permutation suffices |
| Gate count and driving duration | Not bounded |
| Bath, catalyst or auxiliary entropy sink | Absent |
| Independent repetitions of an allowed block | Permitted; their mean work adds |
| Reliable or deterministic work, fluctuations, charging power | Separate questions not determined by the mean-work theorem |

A unitary on a block can be difficult to synthesize even when its existence is explicit. Conversely, allowing a large gate arity does not by itself imply that a useful fraction is extracted. The result constrains the joint block, not the number of experimental samples needed to estimate an extremely small mean.

## 3. Diagonality is essential

Let $`H=\mathrm{diag}(0,1)`$, let $`q`$ be its positive-temperature Gibbs state, and let $`\rho_\delta=U_\delta qU_\delta^\dagger`$ with a real rotation by angle $`\delta`$. Its entropy equals that of $`q`$, and

```math
W_1(\rho_\delta)=w_\infty(\delta)
=(q_0-q_1)\sin^2\delta.
```

A single copy gives the entire available work. Thus the diagonal hypothesis cannot be removed from the inverse-square threshold.

## 4. The transverse derivative fixes the exponent

A pure temperature path $`p_\delta=q_{\beta+\delta}`$ is completely passive. A non-Gibbs but tangent path such as the qutrit family
$`p_\delta\propto e^{-\beta H+\delta^2 A}`$ has $`v=0`$ at the origin. Applying the established qutrit result with parameter $`\delta^2`$ gives first activation of order $`\delta^{-2}`$ and useful-work blocks of order $`\delta^{-4}`$. The nonzero transverse first derivative is therefore a substantive assumption.

## 5. Fixed temperature and fixed energy lattice

At $`\beta=0`$, the local entropy inverse used in the model is singular and the clipping interval is empty. For $`H=\mathrm{diag}(0,1,2)`$ and
$`p_\delta=(1/3-\delta,1/3+2\delta,1/3-\delta)`$, one copy already yields $`3\delta`$ of work. The theorem is explicitly at fixed positive inverse temperature.

For a fixed commensurate Hamiltonian, all product energies retain the same lower gap bound $`g`$. An incommensurate spectrum can have increasingly small many-copy differences, so the proof does not extend by replacing a rational energy ratio with a nearby irrational one. A Hamiltonian varying with $`\delta`$ can likewise invalidate uniform constants. Arithmetic dependence is the related subject of [Quantum-Work-Activation](https://github.com/GoGoKo699/Quantum-Work-Activation); its irrational-spectrum conclusions are not required or established here.

## 6. Meaning of the strengthened converse

An inverse-square sufficient scale already appears in collective concentration and finite-size thermodynamic reasoning. The quantitative issue addressed here is whether a global unitary could harvest a useful mean from rare spectra at any smaller block scale. The [relative-entropy comparison](passive_clipping.md) rules out every subcritical sequence, including blocks only logarithmically below $`\delta^{-2}`$.

The scope and attribution of that statement are detailed in [related work](../references/RELATED_WORK.md). The same theorem does not certify an optimal crossover constant, a high-yield limit approaching one, or an efficient physical implementation.
