# Thirty milestones from QEC foundations to protected encoded control

The map has exactly thirty project-defined understanding targets. **M01–M12 build the background and preliminaries; M13–M30 connect the narrative and innovation.** Twelve background milestones assemble the code, error, dynamical, and operator tools. Eighteen narrative milestones follow their consequences through the locality and coupling theorems, the readout tradeoff, the optimal concatenated families, sparse descriptions, and protected logical strings. Each phase progresses from individual objects to their relationships and ends in a synthesis.

Error-Transparent Locality and Syndrome Reversibility Distance share one educational anchor: John Preskill, *Quantum Information*, Chapter 7, updated March 2026: [official PDF](https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf). The section pointers refer to that edition. Preskill supplies their common QEC foundations, including stabilizers and concatenation. The [local bridge](PRESKILL_BRIDGE.md) supplies the additional generator, twirl, moment, readout, synthesis, and lifting arguments for this map. The [companion readout bridge](https://github.com/GoGoKo699/Syndrome-Reversibility-Distance/blob/main/learning/PRESKILL_BRIDGE.md) develops the other project's measurement and recovery route from the same source. Research citations establish attribution and imported theorem dependencies; they are not additional educational anchors.

Dependencies point only to earlier milestones. The map connects the load-bearing ideas of the complete account; specialist calculations remain in the linked scientific sources. Interaction order is denoted by $\ell$ here to distinguish it from syndrome reversibility distance $r_S$.

## Phase I: Background and preliminaries

<a id="m01"></a>
### M01: An encoded state occupies a physical subspace

**Central question.** What is preserved when one logical system is represented by many physical qubits?

**Understanding target.** An isometry $V$ represents a logical state as $V|\psi\rangle$, with code projector $P=VV^\dagger$. Logical dimension and physical block size describe different spaces. Here $V$ is the encoder; Preskill also uses this letter for a recovery isometry in another setting.

**Earlier dependencies and story role.** None. This identifies the spaces on which errors, recovery, and Hamiltonians act.

**Conceptual connection.** Encoding preserves inner products while changing the physical operations that can distinguish logical states.

**Source pointers.** [Preskill §7.2][p72]; [bridge §3](PRESKILL_BRIDGE.md#3-notation-and-assumptions); [model §1](../science/model.md#1-encoded-space-and-detection-distance).

<a id="m02"></a>
### M02: Pauli support and coefficient signs carry different information

**Central question.** What does Pauli weight measure, and which phases affect a physical Hamiltonian?

**Understanding target.** Support records nonidentity sites and weight counts them. The native expansion uses bare Hermitian tensor Paulis with real coefficients. Signed logical representatives can have a negative bare sign. Preskill's real-Pauli convention must be translated before multiplying words or reading coefficients.

**Earlier dependencies and story role.** [M01](#m01). This fixes the physical operator coordinates used by every construction and cost statement.

**Conceptual connection.** Binary support can preserve commutation information while omitting a sign that changes a Hamiltonian.

**Source pointers.** [Preskill §§7.10.1–7.10.2][p7101]; [bridge §3](PRESKILL_BRIDGE.md#3-notation-and-assumptions); [model §4](../science/model.md#4-interaction-order-and-coupling-budget).

<a id="m03"></a>
### M03: Compression reveals logical action but can conceal leakage

**Central question.** What information is retained by $V^\dagger BV$?

**Understanding target.** Compression gives matrix elements between encoded states. A scalar compression has no logical contrast. The full map $BV$ also contains any component outside the code, so compressed equality alone cannot establish subspace preservation.

**Earlier dependencies and story role.** [M01](#m01), [M02](#m02). This prepares the distinction between quantities used in lower bounds and identities required of a physical construction.

**Conceptual connection.** Indistinguishability inside a subspace and invariance of that subspace are separate statements.

**Source pointers.** [Preskill §§7.2 and 7.4.3][p72]; [bridge §§3–4](PRESKILL_BRIDGE.md#3-notation-and-assumptions); [model §2](../science/model.md#2-exact-error-transparency).

<a id="m04"></a>
### M04: Correctability concerns an error space

**Central question.** Why can Pauli-error conditions protect coherent errors and channels?

**Understanding target.** An error moves the encoded information to the image of $EV$. The Knill–Laflamme condition $V^\dagger E_b^\dagger E_aV=C_{ba}I$ permits a common recovery for the linear span of the errors. Individual error images need not be orthogonal, and physical labels need not identify distinct encoded actions.

**Earlier dependencies and story role.** [M02](#m02), [M03](#m03). This gives all-Pauli certificates their meaning for general errors in the protected span.

**Conceptual connection.** Recovery separates error information from logical information; pairwise error products test whether that separation is possible.

**Source pointers.** [Preskill §§7.2–7.3][p72]; [bridge §§1 and 3](PRESKILL_BRIDGE.md#1-from-correctability-to-protected-motion); [model §1](../science/model.md#1-encoded-space-and-detection-distance).

<a id="m05"></a>
### M05: Distance and degeneracy determine what must be corrected

**Central question.** How can a low-weight Pauli be harmless even when it is not identity?

**Understanding target.** Detection distance $d$ makes every Pauli compression at weight below $d$ scalar. The scalar need not vanish. Products of two errors of weight at most $t$ have weight at most $2t$, giving correction when $d\ge2t+1$. Low-weight stabilizers and coincident error images are compatible with this condition.

**Earlier dependencies and story role.** [M03](#m03), [M04](#m04). This supplies the hypothesis that removes low interaction weights without assuming nondegeneracy.

**Conceptual connection.** A code protects logical distinctions rather than requiring every physical error to be distinguishable.

**Source pointers.** [Preskill §7.4][p74]; [bridge §3](PRESKILL_BRIDGE.md#3-notation-and-assumptions); [nine-qubit distance and degeneracy](../science/four_body_construction.md#distance-and-degeneracy).

<a id="m06"></a>
### M06: Stabilizers and logical cosets organize a code

**Central question.** How do checks distinguish detectable Paulis, stabilizers, and logical operators?

**Understanding target.** The stabilizer specifies the code; its Pauli centralizer contains the logical operators, and quotienting by stabilizers identifies logical classes. CSS checks translate commutation into binary orthogonality and basis states into coherent sums over classical cosets. A nontrivial logical class can have several signed physical representatives.

**Earlier dependencies and story role.** [M02](#m02), [M05](#m05). This connects the abstract code conditions to the explicit CSS example and later concatenated constructions.

**Conceptual connection.** A common logical action can be distributed over many physical supports, allowing their fault responses to cancel.

**Source pointers.** [Preskill §§7.6–7.8][p76] and [§§7.10.3–7.10.4][p7103]; [bridge §8](PRESKILL_BRIDGE.md#8-reading-the-nine-qubit-certificate); [four-body construction §§1–2](../science/four_body_construction.md#1-the-css-code).

<a id="m07"></a>
### M07: A recoverable fault can distort a logical trajectory

**Central question.** Why can final correction leave the wrong logical angle?

**Understanding target.** A Hamiltonian can have the intended generator on the code and a different generator on an error image. A fault at an unknown time then changes how long each rate acts. The restricted repetition-code example separates recovery of a bit flip from recovery of the accumulated phase.

**Earlier dependencies and story role.** [M03](#m03), [M04](#m04). This turns a static correction condition into the dynamical question addressed by the project.

**Conceptual connection.** Recoverable information can follow the wrong coherent evolution before it is recovered.

**Source pointers.** Anchor foundation: [Preskill §§7.2–7.3][p72]. Local step: [bridge §4](PRESKILL_BRIDGE.md#4-worked-repetition-code-example-restricted-noise-illustration); [model §3](../science/model.md#3-a-fault-at-an-unknown-time).

<a id="m08"></a>
### M08: Full intertwining specifies exact error transparency

**Central question.** Which generator identity removes the fault-time dependence?

**Understanding target.** Strict transparency is the full equality $HEV=EVh_L$ on every protected error image. It exponentiates to the intended logical propagator independently of the fault time. The lower bounds allow consistent scalar sector shifts, while the constructions set them to zero. Matching compressed energies can miss leakage between images.

**Earlier dependencies and story role.** [M03](#m03), [M05](#m05), [M07](#m07). This fixes the exact physical requirement before any resource is bounded.

**Conceptual connection.** An equality of maps controls an entire trajectory; an equality of diagonal blocks need not do so.

**Source pointers.** Anchor foundation: [Preskill §7.2][p72]. Local step: [bridge §§1, 3–4](PRESKILL_BRIDGE.md#1-from-correctability-to-protected-motion); [model §§2–3](../science/model.md#2-exact-error-transparency).

<a id="m09"></a>
### M09: Interaction order, coupling, support size, and precision are separate resources

**Central question.** What does it mean for one protected Hamiltonian to cost more than another?

**Understanding target.** $\ell$ is the largest individual Pauli weight, $J=\sum_{Q\ne I}|h_Q|$ is the native coefficient sum, and $\omega$ is half the logical spectral width. Neither operator norm, term count, coefficient bit length, geometric range, nor physical synthesis cost can replace these definitions. For higher logical dimension, $\omega$ need not equal the norm of the traceless generator.

**Earlier dependencies and story role.** [M02](#m02), [M08](#m08). This establishes a consistent scale for the later equality and sparsity statements.

**Conceptual connection.** Signed contributions can cancel in the logical rate while all consume native coupling budget.

**Source pointers.** Anchor foundation: [Preskill §7.10][p7101]. Local definitions: [bridge §6](PRESKILL_BRIDGE.md#6-locality-and-coefficient-budgets); [model §4](../science/model.md#4-interaction-order-and-coupling-budget).

<a id="m10"></a>
### M10: A local Pauli twirl measures interaction weight

**Central question.** How can conjugation by local errors expose the support of an interaction?

**Understanding target.** The one-site twirl $\mathcal R_i$ fixes a Pauli with identity at that site and kills any nonidentity label there. Thus $\mathcal W=\sum_i(\mathrm{Id}-\mathcal R_i)$ has eigenvalue $w$ on Paulis of weight $w$. Its power of order $j$ expands into conjugations by errors of weight at most $j$.

**Earlier dependencies and story role.** [M02](#m02), [M08](#m08). This supplies the operator mechanism relating the protected error set to interaction weights.

**Conceptual connection.** Pauli weight becomes an eigenvalue of a linear map on operators, enabling polynomial reasoning about locality.

**Source pointers.** Anchor foundation: [Preskill §7.10.1][p7101]. Local derivation: [bridge §5](PRESKILL_BRIDGE.md#5-pauli-twirl-and-weight-moments); [locality §2](../science/locality.md#2-the-pauli-weight-superoperator).

<a id="m11"></a>
### M11: Operator moments and scalar witnesses serve different proof roles

**Central question.** How does a physical intertwining identity become a bound on coefficients?

**Understanding target.** Scalar-free compression produces matrix-valued weight components $A_w$. Transparency gives vanishing moments, while distance removes weights below $d$. An extremal-eigenstate half-difference turns these operator equations into normalized signed masses. Polynomial interpolation constrains available weights; a bounded dual polynomial constrains their absolute sum.

**Earlier dependencies and story role.** [M03](#m03), [M05](#m05), [M09](#m09), [M10](#m10). This joins the algebraic tools needed for locality and coupling without identifying a scalar relaxation with a physical gate.

**Conceptual connection.** A separating linear functional preserves the desired logical energy contrast while making coefficient cost comparable to a scalar moment problem.

**Source pointers.** Anchor foundation: [Preskill §§7.2 and 7.4][p72]. Local derivation: [bridge §§5–6](PRESKILL_BRIDGE.md#5-pauli-twirl-and-weight-moments); [coupling §§1–2](../science/coupling_cost.md#1-assumptions-and-a-scalar-witness).

<a id="m12"></a>
### M12: The code, protected generator, and certificate form one framework

**Central question.** What must be established before a claimed resource optimum is meaningful?

**Understanding target.** A fixed code determines correction and logical cosets; a full generator identity determines protected motion; a declared native basis determines cost. The five-qubit code and concatenation provide reusable ingredients. A necessary moment bound, a construction attaining it, and an exact finite certificate answer distinct questions. Greater code distance alone does not increase a supplied Hamiltonian's protected error weight.

**Earlier dependencies and story role.** [M01](#m01)–[M11](#m11). This synthesizes the background into the framework used throughout the narrative.

**Conceptual connection.** Code capacity, dynamical protection, and implementation description must agree without being conflated.

**Source pointers.** [Preskill §§7.11 and 7.17][p711]; [bridge §§6 and 10](PRESKILL_BRIDGE.md#10-concatenation-parity-and-one-error-gates); [five-qubit benchmark](../science/coupling_cost.md#the-five-qubit-benchmark); [verification guide](../verification/README.md).

## Phase II: Narrative and innovation

<a id="m13"></a>
### M13: Vanishing weight moments force extra interaction order

**Central question.** Why must a nontrivial protected generator reach weight $d+t$?

**Understanding target.** With fewer than $t+1$ available weights, a polynomial of degree at most $t$ can vanish at every contributing weight while equaling one at zero. The moment equations would then make the nontrivial logical generator vanish. Hence $\ell\ge d+t$, and full correction gives $\ell\ge3t+1$. Missing coset weights can strengthen the argument.

**Earlier dependencies and story role.** [M08](#m08), [M10](#m10)–[M12](#m12). This is the first general consequence of the assembled framework.

**Conceptual connection.** Error protection requires enough distinct interaction weights to cancel multiple logical moments.

**Source pointers.** Anchor foundation: [Preskill §7.4][p74]. Local proof: [bridge §6](PRESKILL_BRIDGE.md#6-locality-and-coefficient-budgets); [locality §§3–5](../science/locality.md#3-general-locality-theorem).

<a id="m14"></a>
### M14: Minimum order fixes signed logical masses and coupling cost

**Central question.** What strength is necessarily spent on the cancellations required by transparency?

**Understanding target.** At $\ell=d+t$, interpolation fixes every $A_{d+j}$ as a multiple of $A$. The resulting lower bound is $J/\omega\ge\sum_{k=0}^t2^k\binom{d+k-1}{k}$. For $t=1$ and arbitrary $\ell>d$, the bound is $(\ell+d)/(\ell-d)$. At $d=3,\ell=4$, masses $4,-3$ force cost seven. Moment feasibility alone does not establish attainability.

**Earlier dependencies and story role.** [M09](#m09), [M11](#m11), [M13](#m13). This adds quantitative cost to the locality obstruction.

**Conceptual connection.** Interpolation determines both the required cancellations and an exact primal/dual cost certificate.

**Source pointers.** Anchor foundation: [Preskill §7.4][p74]. Local proof: [bridge §6](PRESKILL_BRIDGE.md#6-locality-and-coefficient-budgets); [coupling §§2–4](../science/coupling_cost.md#2-the-exact-finite-moment-bound).

<a id="m15"></a>
### M15: A nine-qubit CSS code realizes the four-body equality

**Central question.** How can different physical representatives produce the same protected logical motion?

**Understanding target.** The specified degenerate $[[9,1,3]]$ CSS code has nine commuting logical $Z$ representatives. Their signed site incidences vanish, proving full one-error transparency. Cubic mass four and quartic mass minus three attain $\ell=4$ and $J=7\omega$. Energy plateaus explain the diagonal action, while CSS coherence and quantum distance supply protection against all single-qubit Pauli errors.

**Earlier dependencies and story role.** [M06](#m06), [M08](#m08), [M14](#m14). This turns the necessary bound into a complete equality example for one logical axis.

**Conceptual connection.** Redundant physical representatives make destructive fault-response interference compatible with constructive logical action.

**Source pointers.** [Preskill §§7.7 and 7.10.4][p77]; [bridge §8](PRESKILL_BRIDGE.md#8-reading-the-nine-qubit-certificate); [four-body construction](../science/four_body_construction.md).

<a id="m16"></a>
### M16: Protection constrains the instantaneous pulse

**Central question.** Why do a correct final angle and commuting terms fail to certify fault-time protection?

**Understanding target.** For the nine supports, the no-fault rate is $a(t)=\sum_Sh_S(t)$ and the fault-sensitive incidence is $b_i(t)=\sum_{S\ni i}h_S(t)$. A fault at $\tau$ produces angle $A-2B_i(\tau)$. Exact protection requires incidence balance throughout. The incidence kernel fixes a common envelope; sequential terms can give a maximal logical error despite the exact no-fault product. Classical fault-time mixtures yield a calculable channel under the stated input-independent probabilities.

**Earlier dependencies and story role.** [M07](#m07), [M08](#m08), [M15](#m15). This specifies the control condition attached to the equality construction.

**Conceptual connection.** Endpoint calibration does not determine the generator experienced after an intermediate fault.

**Source pointers.** Anchor foundation: [Preskill §§7.2–7.3][p72]. Local derivation: [bridge §7](PRESKILL_BRIDGE.md#7-incidence-and-controls-with-unknown-fault-time); [control analysis](../science/control_robustness.md).

<a id="m17"></a>
### M17: Prescribed syndrome measurement introduces a separate invariant

**Central question.** When can measuring a code's original syndrome destroy information after a known product rotation?

**Understanding target.** The readout experiment applies a specified product unitary, measures the full original syndrome ideally, and allows an informed recovery. The imported support criterion defines $r_S$ by equal-support stabilizer/logical pairs; the circuit theorem identifies it with the minimum even logical-circuit weight. Logical circuits retain their local labels and have no proper nonempty normalizer subword. This experiment differs from the fault-during-gate model.

**Earlier dependencies and story role.** [M04](#m04), [M06](#m06), [M12](#m12). This introduces the independent code property needed for the joint constraint.

**Conceptual connection.** Correctability depends on the prescribed measurement as well as the code and the known physical transformation.

**Source pointers.** Anchor foundation: [Preskill §§7.2–7.3 and 7.10][p72]. Local bridge: [§9](PRESKILL_BRIDGE.md#9-the-same-code-in-a-syndrome-readout-experiment). Canonical joint statement and imported proof links: [gate/readout §1](../science/gate_readout_tradeoff.md#1-notation-and-hypotheses).

<a id="m18"></a>
### M18: Minimum gate order exposes the smallest even readout circuit

**Central question.** Why does attaining $\ell=d+t$ force $r_S=d+1$ at odd distance?

**Understanding target.** At odd $d\ge3$, with $t\ge1$ and $d\ge2t+1$, the moment equations force a nonzero logical contribution at weight $(d+1)$. Fixed qubits are first removed by a partial matrix element preserving full transparency, distance, and $r_S$. The resulting logical representative is an even circuit. Thus $r_S>d+1$ requires $\ell\ge d+t+1$. The nine-qubit code has $r_S=4$ with readout loss $3q^2-2q^3$, where $q=\sin^2(\theta/2)$ and $0\le\theta\le\pi/2$, for its specified four-site rotation.

**Earlier dependencies and story role.** [M13](#m13)–[M15](#m15), [M17](#m17). This joins the gate mechanism to the readout structure with all assumptions retained.

**Conceptual connection.** A weight sector required for protected evolution becomes a witness of measurement-induced information loss in a separate experiment.

**Source pointers.** Anchor foundation: [Preskill §§7.4 and 7.10][p74]. Local bridge: [§9](PRESKILL_BRIDGE.md#9-the-same-code-in-a-syndrome-readout-experiment); [joint proof and witness](../science/gate_readout_tradeoff.md#2-joint-theorem).

<a id="m19"></a>
### M19: Concatenation preserves a parity obstruction to readout loss

**Central question.** Which code family avoids every equal-support stabilizer/logical collision?

**Understanding target.** The iterated five-qubit code $Q_m=[[5^m,1,3^m]]$ has even-weight stabilizers and odd-weight nontrivial logical representatives. Hence $r_S=\infty$. The same odd-weight restriction leaves only $d,d+2,\ldots$ for nonscalar logical compression, strengthening the gate obstruction to $\ell\ge d+2t$. This is a property of this family, not of every code with infinite $r_S$.

**Earlier dependencies and story role.** [M06](#m06), [M12](#m12), [M13](#m13), [M18](#m18). This identifies a family on which both tasks can be studied at unbounded distance.

**Conceptual connection.** One parity structure prevents readout collisions and limits the interaction weights available to a gate.

**Source pointers.** [Preskill §§7.11 and 7.17][p717]; [bridge §10](PRESKILL_BRIDGE.md#10-concatenation-parity-and-one-error-gates); [family and parity proof](../science/minimum_readout_safe_gates.md#1-code-family-and-readout-property), [higher-error obstruction](../science/minimum_readout_safe_gates.md#6-scope-and-verification).

<a id="m20"></a>
### M20: Two logical weight classes attain the one-error family optimum

**Central question.** How can the additional locality required by parity be attained exactly?

**Understanding target.** Positive signed-coset averages at weights $d$ and $d+2$ have isotropic one-site label counts. Combining them with masses $(d+2)/2$ and $-d/2$ gives full one-error transparency for every logical Pauli axis. The resulting $\ell=d+2$, $J/\omega=d+1$ are optimal at that order. The guarantee remains $t=1$ even when the code corrects more errors.

**Earlier dependencies and story role.** [M14](#m14), [M19](#m19). This supplies an unbounded-distance equality family retaining infinite readout distance.

**Conceptual connection.** Local label balance is a concrete realization of the abstract first-moment cancellation.

**Source pointers.** [Preskill §§7.11 and 7.17][p717]; [bridge §10](PRESKILL_BRIDGE.md#10-concatenation-parity-and-one-error-gates); [recursive sums and full proof](../science/minimum_readout_safe_gates.md#3-recursive-normalized-sums).

<a id="m21"></a>
### M21: Sparse one-error synthesis preserves the optimum

**Central question.** Does an exponentially large dense expansion make exponentially many terms necessary?

**Understanding target.** Single-error transparency is a finite system of signed incidence equations. Nonnegative support reduction gives at most $3n+1$ terms. Translation orbits reduce the construction to four scalar constraints and give an explicit recursion with at most $4n$ terms and $O(\log n)$ coefficient bits. A 25-qubit example uses 75 terms at order eleven and cost ten. These support and precision guarantees are separate from physical synthesis and calibration.

**Earlier dependencies and story role.** [M09](#m09), [M16](#m16), [M20](#m20). This separates the dense construction from necessary description cost.

**Conceptual connection.** Linear dependence can remove physical terms while retaining every protected response and the forced signed masses.

**Source pointers.** Anchor foundation: [Preskill §7.17][p717]. Local bridge: [§10](PRESKILL_BRIDGE.md#10-concatenation-parity-and-one-error-gates); [sparse one-error construction](../science/sparse_protected_gates.md).

<a id="m22"></a>
### M22: Two-error protection requires resolving bottom-block patterns

**Central question.** Why is the total-weight moment bound too weak on $Q_2$?

**Understanding target.** At order thirteen, every contributing logical term has one of four bottom-block patterns. Two distinct patterns have total weight thirteen but different $R=\sum_bw_b^2$. The rows $(1,W,W^2,R)$ force signed masses $143/8,-117/4,243/16,-45/16$. Their exact responses give strict protection for all 2,776 errors through weight two and optimal axis cost $521/8$.

**Earlier dependencies and story role.** [M10](#m10), [M11](#m11), [M19](#m19), [M20](#m20). This introduces the block-resolved proof mechanism needed beyond one error.

**Conceptual connection.** Equal total interaction weight can conceal different internal structures and opposite unavoidable coefficient signs.

**Source pointers.** Anchor foundation: [Preskill §7.17][p717]. Local bridge: [§11](PRESKILL_BRIDGE.md#11-two-error-gates-and-sparse-response-preservation); [two-error construction and lower bound](../science/two_error_gates.md).

<a id="m23"></a>
### M23: Tree correlations sustain the two-error optimum at every depth

**Central question.** What fails when the depth-two construction is extended with uniform inactive-block padding?

**Understanding target.** In the uniform-promotion construction, active support pairs depend on their first divergence in the concatenation tree. Frontier-selected stabilizer padding supplies the required identity $\eta_{ij}=\rho_{ij}/(k-1)$. Uniform padding among inactive bottom blocks fails at larger depth. The four-pattern block moments give the arbitrary-Hamiltonian optimum $\ell=d+4$, $J/\omega=(4d^2+21d+8)/8$ for every $m\ge2$. The frontier rule is not a uniqueness theorem for all optimal gates.

**Earlier dependencies and story role.** [M19](#m19), [M22](#m22). This explains the new correlation needed to extend one explicit ensemble globally.

**Conceptual connection.** Multisite protection depends on joint responses, so matching single-site marginals cannot supply the missing pair information.

**Source pointers.** Anchor foundation: [Preskill §7.17][p717]. Local bridge: [§11](PRESKILL_BRIDGE.md#11-two-error-gates-and-sparse-response-preservation); [growing two-error proof](../science/growing_two_error_gates.md).

<a id="m24"></a>
### M24: Sparse two-error recursion must preserve complete class profiles

**Central question.** Which information must survive a sparse replacement of a recursive component?

**Understanding target.** Positive class certificates preserve each class's full two-error character vector. Pairwise child coupling suffices because an error touches at most two children; marginals alone do not suffice. Exact rational orbit reduction gives a reference algorithm with high polynomial degree. Separate finite certificates use 2,575 terms at 25 qubits and 69,125 at 125 qubits, with 125-bit and 1,458-bit native common denominators. Their support selection and exact verification are distinct operations.

**Earlier dependencies and story role.** [M09](#m09), [M21](#m21)–[M23](#m23). This makes the description and computational costs of the higher-error family explicit.

**Conceptual connection.** Response-preserving compression must retain the correlations used by the parent proof, even when the final gate constraints alone would allow more freedom.

**Source pointers.** Anchor foundation: [Preskill §7.17][p717]. Local bridge: [§11](PRESKILL_BRIDGE.md#11-two-error-gates-and-sparse-response-preservation); [sparse two-error synthesis](../science/sparse_two_error_synthesis.md).

<a id="m25"></a>
### M25: A third protected error forces an additional logical branch

**Central question.** Why do the patterns used through two errors no longer suffice?

**Understanding target.** On $Q_2$, order fifteen permits seven complete bottom-block patterns: four promotion classes, two padding classes, and an outer weight-five logical class. Weight-three errors can themselves be inner logical operators. A cubic active-count polynomial forces the weight-five branch to contribute $-3A/2$. The signed seven-class seed protects all 64,876 physical errors through weight three for each axis.

**Earlier dependencies and story role.** [M06](#m06), [M19](#m19), [M22](#m22). This identifies the additional mechanism required by three-error protection.

**Conceptual connection.** A physical error becomes a logical operation at an inner level, producing a constraint invisible to lower-order local counts.

**Source pointers.** Anchor foundation: [Preskill §§7.11 and 7.17][p717]. Local bridge: [§12](PRESKILL_BRIDGE.md#12-seven-patterns-and-the-three-error-coupling-bound); [three-error seed](../science/three_error_gates.md), [forced branch](../science/three_error_gates.md#why-the-outer-weight-five-branch-is-unavoidable).

<a id="m26"></a>
### M26: Cubic block moments determine the exact directional cost

**Central question.** How can optimality cover arbitrary Hamiltonians rather than just uniform class averages?

**Understanding target.** Every contributing order-fifteen logical word belongs to the seven patterns. The rows $(1,W,W^2,W^3,R,WR,S)$, with $S=\sum_bw_b^3$, form an invertible operator system forcing their masses. An exact dual and disjoint logical cosets give $J_{\min}=(2867/8)\sum_\alpha|\Omega_\alpha|$ in the fixed canonical logical Pauli frame. Scalar sector shifts, detectable terms, and competing logical terms cannot reduce the bound.

**Earlier dependencies and story role.** [M09](#m09), [M11](#m11), [M22](#m22), [M25](#m25). This closes the gap between a constructive ansatz and arbitrary-Hamiltonian optimality.

**Conceptual connection.** Resolving both block structure and logical direction turns a spectral lower bound into the physical coefficient norm selected by the native basis.

**Source pointers.** Anchor foundation: [Preskill §7.10.4][p7104]. Local bridge: [§12](PRESKILL_BRIDGE.md#12-seven-patterns-and-the-three-error-coupling-bound); [three-error moments and directional proof](../science/three_error_gates.md#5-block-moments-and-the-exact-coupling-lower-bound).

<a id="m27"></a>
### M27: Increment lifting transports strict protection to every depth

**Central question.** Why can a truncated tensor construction be exact on all protected error images?

**Understanding target.** Nested gates give increments $\Delta_a=L_a-L_{a-1}$ that annihilate error images of weight below $a$. Any tensor term whose total increment index exceeds the protected error weight has a vanishing factor. Keeping total degree at most three therefore gives exact full transparency. Compatible native signs and the seven-pattern moment dual attain $\ell=d+6$ and $J_3(d)=(4d^3+51d^2+170d+24)/24$ for every $m\ge2$, including the fixed-frame directional optimum. This truncation is not a time-evolution approximation.

**Earlier dependencies and story role.** [M08](#m08), [M19](#m19), [M25](#m25), [M26](#m26). This integrates the finite hierarchy into the arbitrary-depth three-error result.

**Conceptual connection.** Exact annihilation, rather than a small omitted norm, permits finite-degree lifting without losing the physical-space identity.

**Source pointers.** Anchor foundation: [Preskill §7.17][p717]. Local bridge: [§13](PRESKILL_BRIDGE.md#13-exact-increment-lifting-and-the-all-depth-optima); [all-depth three-error proof](../science/growing_three_error_gates.md).

<a id="m28"></a>
### M28: A pure logical string has its own minimum physical coset weight

**Central question.** Which distance controls a protected entangling generator on fixed product blocks?

**Understanding target.** On $Q_m^{\otimes M}$ with $m\ge2$, a specified nonidentity logical Pauli string $P$ of weight $p\ge1$ has minimum target-coset weight $D=pd$, while the ordinary code distance remains $d$. Total-degree-three products of active increments give strict protection. Projection onto that logical coefficient transfers the parity and seven-pattern lower bounds, proving $\ell_{\min}=D+6$ and $J_{\min}=|\Omega|J_3(D)$ for $h_L=\Omega P+cI$ with $\Omega\ne0$. No globally optimal mixed-string budget at one common order cap follows from this pure-string law.

**Earlier dependencies and story role.** [M06](#m06), [M26](#m26), [M27](#m27). This extends the single-block mechanism to specified multiqubit logical interactions.

**Conceptual connection.** A logical-coordinate projection isolates the required target resource even when arbitrary competing physical terms are allowed.

**Source pointers.** Anchor foundation: [Preskill §§7.10.4 and 7.17][p7104]. Local bridge: [§14](PRESKILL_BRIDGE.md#14-pure-logical-strings-entanglers-and-universal-control); [protected-string construction and optimum](../science/protected_entangling_gates.md#1-fixed-code-target-and-resource-model).

<a id="m29"></a>
### M29: Protected entanglers complete encoded control on unchanged blocks

**Central question.** How do local protected axes and a protected interaction produce universal encoded control?

**Understanding target.** Two $Q_2$ blocks admit a $ZZ$ generator with target minimum eighteen, order twenty-four, and cost $1789$. Its $\pi/4$ gate creates a maximally entangled state from $|++\rangle$. Six local Pauli controls and $ZZ$ generate all fifteen two-qubit Pauli directions. The product code still has $r_S=\infty$ by parity within each encoded block, including for even-global-weight targets. Every applied complete Hamiltonian must satisfy the full identity throughout the evolution.

**Earlier dependencies and story role.** [M16](#m16), [M19](#m19), [M27](#m27), [M28](#m28). This connects the protected generators to a complete encoded control capability in the declared native model.

**Conceptual connection.** Entanglement and Lie closure concern logical controllability; support parity separately controls reversibility of the prescribed readout.

**Source pointers.** Anchor foundation: [Preskill §7.10.4][p7104]. Local bridge: [§14](PRESKILL_BRIDGE.md#14-pure-logical-strings-entanglers-and-universal-control); [entangler and universal control](../science/protected_entangling_gates.md#5-the-first-protected-entangler), [product-code readout](../science/protected_entangling_gates.md#7-syndrome-readout-and-operational-scope).

<a id="m30"></a>
### M30: The complete result separates structural optima from implementation cost

**Central question.** What has the combined account established, and which comparisons remain outside it?

**Understanding target.** The general moment obstruction, attained examples, joint readout constraint, optimal $Q_m$ families through three errors, sparse descriptions, and pure-string control law form one account of fixed-code protected Hamiltonians. Analytical proofs establish universal and all-depth statements; exact response and moment certificates verify specified finite constructions without implying dense matrix enumeration. Interaction order, coupling, support size, coefficient bits, synthesis runtime, geometry, and recovery hardware remain distinct. Known-product-unitary readout and faults during a gate retain separate operational assumptions, so their coexistence is not a joint noisy-hardware threshold.

**Earlier dependencies and story role.** [M13](#m13)–[M29](#m29), with the framework of [M12](#m12). This integrates the full narrative, its evidence, and its physical boundaries.

**Conceptual connection.** An exact algebraic resource optimum is meaningful within its declared operations and access conditions; a complete implementation requires its additional costs and noise model to be specified.

**Source pointers.** Anchor foundations: [Preskill §§7.2, 7.10, and 7.17][p72]. Local synthesis: [bridge §§9–14](PRESKILL_BRIDGE.md#9-the-same-code-in-a-syndrome-readout-experiment); [scientific overview](../science/README.md), [physical meaning](../science/interpretation.md), [verification guide](../verification/README.md), [related work](../references/RELATED_WORK.md).

[p72]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=10
[p74]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=18
[p76]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=24
[p77]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=27
[p7101]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=33
[p7103]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=37
[p7104]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=39
[p711]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=40
[p717]: https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=54
