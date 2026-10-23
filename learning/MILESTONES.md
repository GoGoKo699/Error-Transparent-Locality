# Thirty milestones from QEC foundations to error-transparent control

This route has two phases: **M01–M13 build the background and preliminaries; M14–M30 assemble the scientific argument and its consequences.** Within each phase, individual mathematical objects lead to their relationships and then to a synthesis. The IDs are stable; dependencies refer only to earlier milestones.

The single educational anchor is John Preskill, *Quantum Information*, Chapter 7, updated March 2026: [official PDF](https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf). Section numbers below refer to that version. PDF links open at the relevant section's starting page. The [Preskill bridge](PRESKILL_BRIDGE.md) supplies the local notation and the additional mathematical tools required by this project. Preskill provides the QEC foundations; the twirl argument, error-transparent generator model, moment bounds, and control results are developed in the local scientific account.

A **central question** identifies the issue a milestone resolves. Its **understanding target** states the resulting concept or argument, rather than an exercise. The **story role** explains why that understanding is needed in the full account.

## Phase I — Background and preliminaries

<a id="m01"></a>
### M01 — An encoded state is a state in a subspace

**Central question.** What is preserved when one logical system is represented by many physical qubits?

**Understanding target.** The encoder is an isometry $V$, the code projector is $P=VV^\dagger$, and an arbitrary logical superposition is represented by $V|\psi\rangle$. The logical dimension and physical block size describe different objects. Here $V$ denotes the encoder; the anchor also uses that letter for a recovery isometry in a different setting.

**Earlier dependencies.** None; this is the entry point.

**Story role.** Establishes the spaces on which every later error, generator, and recovery map acts.

**Conceptual connection.** An encoding preserves inner products while changing which physical operations can distinguish logical states.

**Pointers.** Anchor: [Preskill §7.2][p72]. Local bridge: [§3, notation and assumptions](PRESKILL_BRIDGE.md#3-notation-and-assumptions). Scientific account: [Model §1](../science/model.md#1-encoded-space-and-detection-distance).

<a id="m02"></a>
### M02 — Pauli words, support, and physical coefficients

**Central question.** What does a term's Pauli weight measure, and which phase conventions affect a Hamiltonian?

**Understanding target.** Tensor Paulis form an operator basis; support records the nonidentity sites and weight counts them. This repository expands Hamiltonians in bare Hermitian words with real coefficients. A signed stabilizer product can differ from its printed bare word. The anchor's real-Pauli convention in §7.10 must be translated before multiplying words or reading coefficients.

**Earlier dependencies.** [M01](#m01).

**Story role.** Fixes the native interaction resource and prevents sign ambiguities in the explicit constructions.

**Conceptual connection.** A basis convention changes coefficient coordinates, while the underlying physical operator remains the same.

**Pointers.** Anchor: [Preskill §7.4][p74] and [§7.10.1][p7101]. Local bridge: [§3](PRESKILL_BRIDGE.md#3-notation-and-assumptions). Scientific account: [Model §4](../science/model.md#4-interaction-order-and-coupling-budget) and [verification conventions](../verification/README.md#data-and-conventions).

<a id="m03"></a>
### M03 — Compression exposes logical information

**Central question.** What does an operator reveal when it is restricted to the encoded subspace?

**Understanding target.** The compression $V^\dagger QV$ describes the part of $Q$ visible between encoded states. A scalar compression has no logical contrast. Compression alone does not determine whether $Q$ takes a state out of the code; the full action $QV$ contains that additional information.

**Earlier dependencies.** [M01](#m01), [M02](#m02).

**Story role.** Supplies the distinction between the compressed quantities used in lower bounds and the full identities required of a construction.

**Conceptual connection.** Logical indistinguishability is a statement about matrix elements; preservation of a subspace is a statement about the entire output vector.

**Pointers.** Anchor: [Preskill §7.2][p72] and [§7.4.3][p743]. Local bridge: [§3](PRESKILL_BRIDGE.md#3-notation-and-assumptions). Scientific account: [Model §§1–2](../science/model.md#1-encoded-space-and-detection-distance).

<a id="m04"></a>
### M04 — Error images retain the encoded information

**Central question.** Where does the logical state reside after a recoverable physical error?

**Understanding target.** An error $E$ sends encoded states into the image of $EV$. A suitable recovery preserves the logical amplitudes while extracting error information. Its syndrome basis can involve linear combinations of the chosen error operators, so their individual images need not be orthogonal. Distinct physical error labels need not always produce distinct images; that distinction becomes important for degeneracy.

**Earlier dependencies.** [M01](#m01), [M03](#m03).

**Story role.** Identifies the additional subspaces on which a logical Hamiltonian must act consistently.

**Conceptual connection.** Recovery transfers information about the error to an auxiliary degree of freedom while retaining the logical state.

**Pointers.** Anchor: [Preskill §7.2][p72] and [§7.3][p73]. Local bridge: [§1, from correctability to protected motion](PRESKILL_BRIDGE.md#1-from-correctability-to-protected-motion). Scientific account: [Model §§2–3](../science/model.md#2-exact-error-transparency).

<a id="m05"></a>
### M05 — Correctability concerns an error space

**Central question.** Why can conditions on finitely many Pauli errors protect more general physical noise?

**Understanding target.** The Knill–Laflamme condition constrains every error pair through $V^\dagger E_a^\dagger E_bV$. Its scalar matrix elements permit one recovery to correct the linear span of the chosen errors, including channel Kraus operators in that span. Error probabilities are not required to specify this exact correctability statement.

**Earlier dependencies.** [M02](#m02), [M03](#m03), [M04](#m04).

**Story role.** Explains why the later all-Pauli certificates have a physical meaning beyond a list of discrete fault labels.

**Conceptual connection.** Pairwise operator products encode whether the environment or a syndrome measurement can acquire logical information.

**Pointers.** Anchor: [Preskill §§7.2–7.3][p72]. Local bridge: [§1](PRESKILL_BRIDGE.md#1-from-correctability-to-protected-motion). Scientific account: [Model §1](../science/model.md#1-encoded-space-and-detection-distance).

<a id="m06"></a>
### M06 — Distance converts local ignorance into correction

**Central question.** How does detection distance determine the error weights a code can correct?

**Understanding target.** Distance $d$ makes all Pauli compressions below weight $d$ scalar. Products of two errors of weight at most $t$ have weight at most $2t$, giving the sufficient condition $d\ge2t+1$. Error detection, correction of unknown-location errors, and correction of located errors impose different requirements.

**Earlier dependencies.** [M02](#m02), [M03](#m03), [M05](#m05).

**Story role.** Provides the lower-weight cutoff used in the interaction-order proof.

**Conceptual connection.** A local property of each error product becomes a guarantee for the entire protected error family.

**Pointers.** Anchor: [Preskill §§7.4.1–7.4.3][p741]. Local bridge: [§3](PRESKILL_BRIDGE.md#3-notation-and-assumptions). Scientific account: [Model §1](../science/model.md#1-encoded-space-and-detection-distance) and [Locality §1](../science/locality.md#1-logical-weight-components).

<a id="m07"></a>
### M07 — Degeneracy is compatible with exact recovery

**Central question.** How can two different physical errors have the same correctable action?

**Understanding target.** Correctability does not demand a distinct syndrome for every physical error label. Errors may agree on the code because their product acts trivially there. This possibility must be distinguished from two errors whose product is a nontrivial logical operator.

**Earlier dependencies.** [M04](#m04), [M05](#m05), [M06](#m06).

**Story role.** Removes an unnecessary nondegeneracy assumption before the explicit nine-qubit code is introduced.

**Conceptual connection.** Equality of encoded actions is an equivalence relation on physical error representatives.

**Pointers.** Anchor: [Preskill §7.2][p72] and [§7.10.1][p7101]. Local bridge: [§3](PRESKILL_BRIDGE.md#3-notation-and-assumptions). Scientific account: [the construction's distance and degeneracy discussion](../science/four_body_construction.md#distance-and-degeneracy).

<a id="m08"></a>
### M08 — Stabilizers separate checks from logical operations

**Central question.** How can a code and its encoded Pauli operators be specified algebraically?

**Understanding target.** Independent commuting checks specify a common eigenspace. Their normalizer contains the Pauli operations preserving it; quotienting by stabilizer action identifies logical representatives. Generator signs, independence, and logical anticommutation are separate facts to establish.

**Earlier dependencies.** [M02](#m02), [M03](#m03), [M07](#m07).

**Story role.** Provides the language for finite code certificates and for dressing one logical operator with many physical representatives.

**Conceptual connection.** A logical coset can contain operators with different supports and weights but the same encoded action.

**Pointers.** Anchor: [Preskill §§7.10.1–7.10.4][p7101]. Local bridge: [§3](PRESKILL_BRIDGE.md#3-notation-and-assumptions) and [§8, reading the nine-qubit certificate](PRESKILL_BRIDGE.md#8-reading-the-nine-qubit-certificate). Scientific account: [Construction §1](../science/four_body_construction.md#1-the-css-code).

<a id="m09"></a>
### M09 — CSS structure connects binary parity and coherence

**Central question.** How do classical parity constraints organize a quantum code?

**Understanding target.** Binary support rows encode separate $X$ and $Z$ checks, and their orthogonality ensures commutation. Row spaces, kernels, and cosets describe both computational supports and coherent superpositions over those supports. Classical bit protection alone does not establish protection of quantum phases.

**Earlier dependencies.** [M02](#m02), [M06](#m06), [M08](#m08).

**Story role.** Prepares the compact code description and the later energy-plateau interpretation.

**Conceptual connection.** The same binary linear algebra describes parity measurements and the coherent sums that preserve quantum information.

**Pointers.** Anchor: [Preskill §§7.6–7.7][p76], [§7.8][p78], and the general CSS discussion in [§7.10.3][p7103]. Local bridge: [§8](PRESKILL_BRIDGE.md#8-reading-the-nine-qubit-certificate). Scientific account: [Construction §§1 and 5](../science/four_body_construction.md#1-the-css-code).

<a id="m10"></a>
### M10 — A logical gate has a trajectory

**Central question.** Why can recovery repair a state error while leaving a gate-angle error?

**Understanding target.** A Hamiltonian implements continuous evolution, so a fault separates a gate into evolution before and after the fault. Even when both endpoint states are recoverable, unequal logical rates in the code and error image can produce a fault-time-dependent angle. Exponent angles and Bloch-vector rotation angles differ by a factor of two.

**Earlier dependencies.** [M04](#m04), [M05](#m05), [M08](#m08).

**Story role.** Introduces the dynamical question that ordinary static correctability leaves unanswered.

**Conceptual connection.** Correcting the error representative and correcting the accumulated logical evolution are distinct requirements.

**Pointers.** Anchor: [Preskill §7.2][p72] and [§7.10.4][p7104] for recovery and encoded operators. The dynamical extension is local: [Bridge §1](PRESKILL_BRIDGE.md#1-from-correctability-to-protected-motion) and [Model §3](../science/model.md#3-a-fault-at-an-unknown-time).

<a id="m11"></a>
### M11 — State the resources before comparing controls

**Central question.** Which quantities distinguish a small interaction from an inexpensive logical gate?

**Understanding target.** Maximum Pauli weight $r$, physical block size $n$, number of terms, native coefficient budget $J$, and logical half-splitting $\omega$ are separate quantities. The chosen Pauli basis fixes $J$; a scalar energy shift does not change $\omega$. Preparation, recovery, geometric range, and hardware synthesis require additional accounting.

**Earlier dependencies.** [M02](#m02), [M06](#m06), [M10](#m10).

**Story role.** Defines the comparison in which an interaction-order optimum can differ from a coupling-strength optimum.

**Conceptual connection.** Code-parameter bounds constrain an encoding, whereas the native budget constrains a specified generator acting on it.

**Pointers.** Anchor: [Preskill §7.4.1][p741] and [§7.9][p79] for code parameters. The Hamiltonian resources are local: [Bridge §6](PRESKILL_BRIDGE.md#6-locality-and-coefficient-budgets) and [Model §4](../science/model.md#4-interaction-order-and-coupling-budget).

<a id="m12"></a>
### M12 — A general proof and a finite certificate answer different questions

**Central question.** What evidence establishes a universal bound, and what establishes one explicit example?

**Understanding target.** An analytic argument must cover all objects satisfying its hypotheses. An exact certificate can establish a particular code's dimension, distance, signs, and operator identities. Checking projected energies alone does not verify a full error-sector identity, and enumerating small codes does not prove a universal lower bound.

**Earlier dependencies.** [M03](#m03), [M06](#m06), [M08](#m08), [M09](#m09).

**Story role.** Establishes the evidence standard used by the theorem and the saturating construction.

**Conceptual connection.** Two representations of the same example can independently test its operator algebra and its binary structure.

**Pointers.** Anchor: [Preskill §§7.10.1–7.10.3][p7101] for the code algebra. The evidence distinction is local: [Bridge §8](PRESKILL_BRIDGE.md#8-reading-the-nine-qubit-certificate), [Verification: checks and their meaning](../verification/README.md#checks-and-their-meaning), and [the scientific dependency summary](../science/README.md#logical-dependencies).

<a id="m13"></a>
### M13 — Synthesis: the precise protected-evolution problem

**Central question.** What complete mathematical problem emerges from the QEC foundations?

**Understanding target.** A fixed encoded subspace must correct every specified low-weight error while a physical Hamiltonian implements a nontrivial logical motion. The question concerns both behavior after a fault at an unknown time and the native resources required for that behavior. Code assumptions, gate requirements, and resource definitions remain separately visible.

**Earlier dependencies.** [M05](#m05), [M06](#m06), [M07](#m07), [M09](#m09), [M10](#m10), [M11](#m11), [M12](#m12).

**Story role.** Completes the background phase by assembling the global task before its specific proof machinery is introduced.

**Conceptual connection.** The error-correction condition supplies the protected information; an additional dynamical condition must supply the protected motion.

**Pointers.** Anchor: [Preskill §7.2][p72], [§7.4.1][p741], and [§7.10.4][p7104]. Local bridge: [§1](PRESKILL_BRIDGE.md#1-from-correctability-to-protected-motion) and [§3](PRESKILL_BRIDGE.md#3-notation-and-assumptions). Scientific account: [Model](../science/model.md).

## Phase II — Narrative and innovation

<a id="m14"></a>
### M14 — Exact error transparency is a full intertwining identity

**Central question.** Which generator condition removes dependence on the time of a protected fault?

**Understanding target.** The strict relation $HEV=EVh_L$ specifies the full action on each error image. Exponentiation gives the same logical gate before and after any protected fault. Consistent additive scalar sector shifts preserve logical energy differences; a syndrome-dependent multiplication of the logical rate is a different condition.

**Earlier dependencies.** [M03](#m03), [M04](#m04), [M10](#m10), [M13](#m13).

**Story role.** States the hypothesis whose consequences the rest of the argument develops.

**Conceptual connection.** Intertwining is the dynamical counterpart of carrying the same logical information in several correctable images.

**Pointers.** Anchor: [Preskill §7.2][p72] supplies the error-image background. The ET condition and exponentiation are local: [Bridge §1](PRESKILL_BRIDGE.md#1-from-correctability-to-protected-motion) and [Model §§2–3](../science/model.md#2-exact-error-transparency).

<a id="m15"></a>
### M15 — A local Pauli twirl reads an interaction's weight

**Central question.** How can an operation on observables distinguish identity from nonidentity at one site?

**Understanding target.** The average $\mathcal R_i(B)=(B+X_iBX_i+Y_iBY_i+Z_iBZ_i)/4$ retains the identity component at site $i$. Summing $\mathrm{Id}-\mathcal R_i$ over sites produces a superoperator whose eigenvalue on a weight-$w$ Pauli is $w$. This is a mathematical device, not an added physical noise process.

**Earlier dependencies.** [M02](#m02), [M03](#m03), [M14](#m14).

**Story role.** Supplies a local algebraic operation that exposes the resource counted by the theorem.

**Conceptual connection.** Pauli conjugation signs convert support information into an eigenvalue of a linear map on operators.

**Pointers.** Anchor: [Preskill §7.4][p74] for Pauli expansion and weight. The twirl construction is supplied by [Bridge §5](PRESKILL_BRIDGE.md#5-pauli-twirl-and-weight-moments) and [Locality §2](../science/locality.md#2-the-pauli-weight-superoperator).

<a id="m16"></a>
### M16 — Protected errors force vanishing weight moments

**Central question.** Why does exact transparency constrain several moments of the logical weight components?

**Understanding target.** Powers of the weight superoperator are linear combinations of conjugations by errors of bounded weight. Their coefficients sum to zero, so transparency makes their scalar-free logical compression vanish. The resulting equations are $\sum_w w^jA_w=0$ for $1\le j\le t$, even if individual $H_w$ do not separately preserve the code.

**Earlier dependencies.** [M03](#m03), [M06](#m06), [M14](#m14), [M15](#m15).

**Story role.** Converts the physical protection requirement into the algebraic constraints shared by both resource bounds.

**Conceptual connection.** Consistent scalar sector energies disappear under the same scalar-free compression that detects nontrivial logical motion.

**Pointers.** Anchor: [Preskill §7.2][p72] and [§7.4.1][p741] supply correctability and distance, not this moment theorem. Local tools: [Bridge §5](PRESKILL_BRIDGE.md#5-pauli-twirl-and-weight-moments). Scientific account: [Locality §§1–2](../science/locality.md#1-logical-weight-components).

<a id="m17"></a>
### M17 — An annihilating polynomial gives the locality bound

**Central question.** Why must a nontrivial transparent generator reach weight at least $d+t$?

**Understanding target.** Distance eliminates logical components below $d$. If fewer than $t+1$ remaining weights are available, a polynomial of degree at most $t$ can vanish on all of them while remaining nonzero at zero. The moment equations then force the total logical generator to be scalar, contradicting nontrivial evolution.

**Earlier dependencies.** [M06](#m06), [M11](#m11), [M16](#m16).

**Story role.** Establishes the general obstruction independently of stabilizer form, degeneracy, or block size.

**Conceptual connection.** Polynomial interpolation turns missing low-weight logical action and equal error-sector action into one contradiction.

**Pointers.** Anchor: [Preskill §7.4.1][p741] supplies the distance premise. The polynomial argument is local: [Bridge §6](PRESKILL_BRIDGE.md#6-locality-and-coefficient-budgets) and [Locality §3](../science/locality.md#3-general-locality-theorem), Theorem L1.

<a id="m18"></a>
### M18 — The first sharp case requires a costly cancellation

**Central question.** What does the general argument force when one correctable fault meets a four-body generator?

**Understanding target.** For $d=3,t=1,r=4$, the only nontrivial weight components obey $A_3=4A$ and $A_4=-3A$. A spectral witness normalized by logical half-splitting bounds each physical Pauli's logical contrast by one, giving $J\ge7\omega$. Signed logical contributions cancel; their absolute native strengths do not.

**Earlier dependencies.** [M11](#m11), [M16](#m16), [M17](#m17).

**Story role.** Identifies the two exact values an explicit four-body construction must attain.

**Conceptual connection.** A locality equality case becomes a quantitative strength constraint through the extremal logical eigenstates.

**Pointers.** Anchor: [Preskill §7.4.1][p741] provides the distance interpretation. Local tools: [Bridge §6](PRESKILL_BRIDGE.md#6-locality-and-coefficient-budgets). Scientific account: [Locality §4](../science/locality.md#4-the-single-error-case-in-one-equation) and [Coupling §1](../science/coupling_cost.md#1-assumptions-and-a-scalar-witness).

<a id="m19"></a>
### M19 — Moment duality describes the larger strength problem

**Central question.** How do weight moments determine necessary coupling costs beyond the first case?

**Understanding target.** The scalar moment relaxation minimizes total absolute signed mass; its dual maximizes a polynomial's value at zero subject to bounds at allowed weights. Matching primal and dual witnesses certify a moment optimum. At $r=d+t$, interpolation fixes the logical components and yields the closed cost, while physical attainability remains a separate question.

**Earlier dependencies.** [M12](#m12), [M16](#m16), [M17](#m17), [M18](#m18).

**Story role.** Extends the cancellation mechanism into a resource framework without mistaking an optimization relaxation for a physical gate.

**Conceptual connection.** The same polynomial idea supplies both an impossibility witness and a quantitative strength witness.

**Pointers.** Anchor: [Preskill §7.4.1][p741] fixes the meaning of distance; interpolation and optimization are local additions. Read [Bridge §6](PRESKILL_BRIDGE.md#6-locality-and-coefficient-budgets) and [Coupling §§2–4](../science/coupling_cost.md#2-the-exact-finite-moment-bound).

<a id="m20"></a>
### M20 — The nine-qubit CSS code supplies the required logical space

**Central question.** Which features of the displayed code establish exact correction of a single arbitrary qubit error?

**Understanding target.** Four independent $X$ checks and four independent $Z$ checks define one encoded qubit. The syndrome columns rule out nontrivial weight-one and weight-two logical operators; the sole weight-two normalizer is the stabilizer $X_5X_9$. The displayed anticommuting weight-three logical representatives complete the distance-three certificate.

**Earlier dependencies.** [M06](#m06), [M07](#m07), [M08](#m08), [M09](#m09), [M18](#m18).

**Story role.** Supplies a concrete code on which the abstract optimum can be tested.

**Conceptual connection.** Repeated syndrome columns can certify benign degeneracy when their associated operator is a stabilizer.

**Pointers.** Anchor: [Preskill §7.7][p77], [§7.10.2][p7102], and [§7.10.4][p7104]. Local bridge: [§8](PRESKILL_BRIDGE.md#8-reading-the-nine-qubit-certificate). Scientific account: [Construction §1](../science/four_body_construction.md#1-the-css-code).

<a id="m21"></a>
### M21 — Nine physical terms share one logical action

**Central question.** How can different cubic and quartic Pauli supports cooperate to implement the same logical operator?

**Understanding target.** Each displayed $Z_S$ equals the chosen logical $\overline Z$ times a positive stabilizer. The coefficients sum to one, while their signed sum at every physical site is zero. These two statements respectively determine the code action and cancel the sign changes induced by a local bit or $Y$ fault.

**Earlier dependencies.** [M02](#m02), [M08](#m08), [M18](#m18), [M20](#m20).

**Story role.** Reveals the explicit mechanism behind the resource-saturating Hamiltonian.

**Conceptual connection.** Logical equivalence supplies freedom to choose physical supports; site incidence determines whether that freedom preserves motion after errors.

**Pointers.** Anchor: [Preskill §7.10.4][p7104] supplies logical-representative equivalence. The weighted incidence construction is local: [Bridge §7](PRESKILL_BRIDGE.md#7-incidence-and-controls-with-unknown-fault-time) and [Construction §§2–3](../science/four_body_construction.md#2-the-hamiltonian).

<a id="m22"></a>
### M22 — Coherent energy plateaus realize both equalities

**Central question.** Why does the diagonal construction protect a quantum rotation and attain both lower bounds?

**Understanding target.** The CSS supports form coherent cosets with opposite logical energies. Sitewise balance makes each energy constant over all single-bit neighbors; $Z$ faults commute with the generator. Together these facts establish the full identities for all 28 protected Pauli branches. The cubic and quartic masses are exactly $4$ and $-3$, giving $r=4$ and $J=7\omega$ for one logical axis.

**Earlier dependencies.** [M09](#m09), [M14](#m14), [M18](#m18), [M20](#m20), [M21](#m21).

**Story role.** Joins the code, Hamiltonian, and general bounds into an attained physical optimum.

**Conceptual connection.** A classical diagonal energy description becomes full quantum protection only with the code's coherence and phase-error correction.

**Pointers.** Anchor: [Preskill §7.7][p77] for coherent CSS cosets. Local bridge: [§8](PRESKILL_BRIDGE.md#8-reading-the-nine-qubit-certificate). Scientific account: [Construction §§3–5](../science/four_body_construction.md#3-sitewise-cancellation-proves-full-transparency).

<a id="m23"></a>
### M23 — The five-qubit benchmark exposes a genuine resource tradeoff

**Central question.** What changes when maximum native interaction order increases from four to five?

**Understanding target.** The perfect five-qubit code's sixteen error images fill its Hilbert space. Its established canonical protected Hamiltonian has ten cubic and six quintic signed-coset terms, with logical masses $5/2$ and $-3/2$. It attains $J=4\omega$ at $r=5$. Block size, number of terms, and interaction order must remain visible alongside strength.

**Earlier dependencies.** [M04](#m04), [M08](#m08), [M11](#m11), [M19](#m19), [M22](#m22).

**Story role.** Places the four-body optimum against a normalized, established comparison rather than treating one resource as the entire implementation cost.

**Conceptual connection.** Permitting a wider separation between contributing weights reduces the cancellation strength required by the first moment.

**Pointers.** Anchor: [Preskill §7.11][p711] covers the code, not its canonical ET Hamiltonian. That extension is in [Bridge §6](PRESKILL_BRIDGE.md#6-locality-and-coefficient-budgets) and [the five-qubit benchmark](../science/coupling_cost.md#the-five-qubit-benchmark), including its prior attribution.

<a id="m24"></a>
### M24 — Saturation depends on the code and the allowed controls

**Central question.** Why does a sharp moment bound not guarantee a saturating Hamiltonian for every code?

**Understanding target.** Missing logical weights can make the moment constraints infeasible. Equality also confines each nonzero physical term to a dual contact weight with maximal logical contrast and compatible sign. These necessary conditions still leave the full error-sector identities to establish. A fixed-axis native-budget statement does not bound arbitrary circuits or moving-code protocols.

**Earlier dependencies.** [M11](#m11), [M14](#m14), [M19](#m19), [M22](#m22), [M23](#m23).

**Story role.** Delimits the sense in which the two certified resource optima are sharp.

**Conceptual connection.** Logical coset structure controls which scalar weight distributions can correspond to physical operators.

**Pointers.** Anchor: [Preskill §7.9][p79] and [§7.10.4][p7104] for code constraints and logical representatives. Local bridge: [§6](PRESKILL_BRIDGE.md#6-locality-and-coefficient-budgets). Scientific account: [Coupling §5](../science/coupling_cost.md#5-code-specific-obstructions-to-saturation) and [interpretation boundaries](../science/interpretation.md#boundaries-of-the-comparison).

<a id="m25"></a>
### M25 — A coefficient error creates a calculable fault-dependent phase

**Central question.** Which part of a pulse determines the extra logical angle after a fault?

**Understanding target.** For arbitrary integrable coefficients on the fixed nine supports, the logical rate is $a(t)=\sum_Sh_S(t)$ and the site incidence is $b_i(t)=\sum_{S\ni i}h_S(t)$. An $X_i$ or $Y_i$ fault at time $\tau$ produces recovered angle $A-2B_i(\tau)$, where $B_i$ is the remaining incidence area. Ordinary angle calibration and fault-dependent distortion are distinct.

**Earlier dependencies.** [M10](#m10), [M14](#m14), [M21](#m21), [M22](#m22).

**Story role.** Turns the exact construction into a direct description of sensitivity to specified control errors.

**Conceptual connection.** The static incidence cancellation becomes an integrated phase mismatch along a faulty trajectory.

**Pointers.** Anchor: [Preskill §7.2][p72] supplies recovery language; the trajectory formula is local. Read [Bridge §7](PRESKILL_BRIDGE.md#7-incidence-and-controls-with-unknown-fault-time) and [Control §§1–2](../science/control_robustness.md#1-logical-rate-and-residual-site-incidence).

<a id="m26"></a>
### M26 — Classical uncertainty in fault time produces a logical channel

**Central question.** How does a distribution of faulty trajectories combine coherent phase error with dephasing?

**Understanding target.** For fixed classical branch probabilities independent of the input state, $\chi=\mathbb E[e^{-2i\delta}]$ is the exact multiplier of logical off-diagonal coherence. Its real part controls the stated fidelities, while $|1-\chi|$ is the diamond distance from the target-frame identity channel. A coherent superposition of histories is not automatically this classical mixture.

**Earlier dependencies.** [M05](#m05), [M10](#m10), [M25](#m25).

**Story role.** Connects the trajectory result to operational channel quantities under an explicit stochastic model.

**Conceptual connection.** Averaging phase factors preserves information about both systematic rotation and uncertainty in rotation angle.

**Pointers.** Anchor: [Preskill §7.2][p72] for channel-based recovery. The coherence and metric formulas are supplied locally by [Bridge §7](PRESKILL_BRIDGE.md#7-incidence-and-controls-with-unknown-fault-time) and [Control §§2–3](../science/control_robustness.md#2-exact-phase-after-one-fault-and-recovery).

<a id="m27"></a>
### M27 — Transparency requires more than logical-angle calibration

**Central question.** Which coefficient variations preserve the full protection of the nine-support gate?

**Understanding target.** The incidence matrix has rank eight and kernel spanned by the nominal coefficient vector. Exact transparency within this support therefore permits a common envelope and no independent coefficient deformation. A perturbation can leave the no-fault logical rate unchanged while producing nonzero incidence. Continuity removes apparent global-phase exceptions to pointwise cancellation.

**Earlier dependencies.** [M14](#m14), [M21](#m21), [M25](#m25), [M26](#m26).

**Story role.** Identifies what a control calibration must preserve to retain the proved guarantee.

**Conceptual connection.** The sum of coefficients and their sitewise sums are different linear observables of the same control vector.

**Pointers.** Anchor: [Preskill §7.10.4][p7104] supplies equality of logical representatives. The control-kernel classification is local: [Bridge §7](PRESKILL_BRIDGE.md#7-incidence-and-controls-with-unknown-fault-time), [Control §4](../science/control_robustness.md#4-which-coefficient-changes-preserve-transparency), and [pointwise necessity](../science/control_robustness.md#why-pointwise-cancellation-is-necessary).

<a id="m28"></a>
### M28 — Exact ideal sequencing can still distort a faulty gate

**Central question.** Why do commuting pulse terms fail to preserve transparency when applied one at a time?

**Understanding target.** Correct total pulse areas give the correct no-fault unitary but need not balance the remaining incidence at intermediate times. The explicit first-pulse fault gives angle $3\Theta$ instead of $\Theta$. Repeated cycles with monotone pulse areas bound the conditional phase through prefix discrepancy; the displayed order attains the optimal value one. More cycles alone do not establish a lower total fault probability.

**Earlier dependencies.** [M11](#m11), [M25](#m25), [M27](#m27).

**Story role.** Separates the algebraic native-control result from an implementation that merely reproduces the final ideal gate.

**Conceptual connection.** Endpoint equality constrains a completed path; an unknown-time fault probes its unfinished portions.

**Pointers.** Anchor: [Preskill §7.2][p72] remains the recovery foundation; pulse discrepancy is a local addition. Read [Bridge §7](PRESKILL_BRIDGE.md#7-incidence-and-controls-with-unknown-fault-time) and [Control §§6–7](../science/control_robustness.md#6-sequential-commuting-pulses-can-fail-maximally).

<a id="m29"></a>
### M29 — Assemble the evidence without enlarging the claims

**Central question.** Which conclusions follow from the universal proofs, the finite certificates, and the comparison of hypotheses?

**Understanding target.** The theorem covers its declared fixed-code generator model; exact operator and CSS certificates establish the supplied equality case. The known five-qubit benchmark and related protected-Hamiltonian frameworks require explicit attribution and hypothesis comparison. Physical attainment of higher-error moment optima, universal four-body control, minimal block size, and complete hardware performance are separate unresolved claims.

**Earlier dependencies.** [M12](#m12), [M17](#m17), [M19](#m19), [M22](#m22), [M23](#m23), [M24](#m24), [M28](#m28).

**Story role.** Integrates the different evidence types before the final scientific synthesis.

**Conceptual connection.** A change in the protected object, error family, or resource definition changes what a theorem can be compared against.

**Pointers.** Anchor: [Preskill §7.9][p79] and [§7.11][p711] provide examples of code bounds and constructions. Local bridge: [§8](PRESKILL_BRIDGE.md#8-reading-the-nine-qubit-certificate). Scientific account: [verification limits](../verification/README.md#what-these-checks-do-not-establish), [related work](../references/RELATED_WORK.md), and [interpretation boundaries](../science/interpretation.md#boundaries-of-the-comparison).

<a id="m30"></a>
### M30 — Synthesis: code, generator, resources, and control form one argument

**Central question.** What complete explanation connects QEC foundations to the attained error-transparent resource frontier?

**Understanding target.** The connected argument runs from detectable low-weight operators and full error-sector evolution to vanishing weight moments, then to the interaction-order and coupling bounds. The nine-qubit construction attains the first case; the established five-qubit benchmark exhibits the strength tradeoff; the control analysis specifies when those guarantees survive a pulse. Each conclusion retains its own assumptions and evidence.

**Earlier dependencies.** [M13](#m13), [M17](#m17), [M18](#m18), [M19](#m19), [M22](#m22), [M23](#m23), [M24](#m24), [M25](#m25), [M26](#m26), [M27](#m27), [M28](#m28), [M29](#m29).

**Story role.** Completes the narrative phase by unifying the theorem, its sharp example, its physical interpretation, and its boundaries.

**Conceptual connection.** Protection of logical information, protection of logical motion, and the resources of realizing that motion are related requirements with distinct mathematical content.

**Pointers.** Anchor: [Preskill §7.2][p72], [§7.4.1][p741], and [§7.10.4][p7104] are the foundational return points. Local bridge: [the complete bridge](PRESKILL_BRIDGE.md). Scientific account: [main statements and evidence](../science/README.md#main-statements-and-evidence) and [Physical meaning and scope](../science/interpretation.md).

[p72]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=10
[p73]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=14
[p74]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=18
[p741]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=19
[p743]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=20
[p76]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=24
[p77]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=27
[p78]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=29
[p79]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=31
[p7101]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=33
[p7102]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=36
[p7103]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=37
[p7104]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=39
[p711]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=40
