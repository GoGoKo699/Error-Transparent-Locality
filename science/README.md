# Scientific account

A fault during a Hamiltonian gate can change the logical evolution that accumulates before recovery. Exact error transparency asks for a fixed code to carry the same logical generator in every protected error image, so that the unknown fault time does not distort the gate. The scientific question is how much native interaction order and coupling strength this requirement costs, and which codes and Hamiltonians attain those costs.

There are two levels of result. General weight-moment obstructions apply to arbitrary fixed codes. Sharper code-family bounds are attained by protected local controls and logical Pauli-string entanglers on concatenated five-qubit codes. The latter codes also retain perfect syndrome reversibility in the separate known-product-unitary readout experiment.

## Model and general obstructions

Let $V$ encode a fixed code of detection distance $d$. A Hermitian, code-preserving Hamiltonian $H$ has logical action $h_L=V^\dagger HV$ and obeys

```math
HEV=EV(h_L+c_E I)
\qquad\text{for every tensor Pauli }E\text{ with }\operatorname{wt}(E)\le t.
```

The lower bounds permit consistent real scalar shifts, with $c_I=0$. All supplied constructions are strict, with every $c_E=0$. The identity holds into the full physical Hilbert space; logical compression alone would not exclude leakage from an error image. Ideal final recovery restores the intended logical evolution. Multiple faults are covered while every accumulated error remains in the protected set.

Use $\ell$ for maximum native Pauli-term weight, $J$ for the sum of absolute nonidentity bare Hermitian Pauli coefficients, and $\omega$ for half the spectral width of $h_L$. The foundational pages write interaction order as $r$; it is the same resource as $\ell$, distinct from syndrome reversibility distance $r_S$.

| General statement for nontrivial logical action | Assumptions and authoritative proof |
|---|---|
| $\ell\ge d+t$ | [Weight moments and interpolation](locality.md); arbitrary logical dimension and degenerate codes allowed |
| $\ell\ge3t+1$ when all errors through weight $t$ are correctable | Combine $d\ge2t+1$ with the same theorem |
| At $\ell=d+t$, $J/\omega\ge\sum_{k=0}^t2^k\binom{d+k-1}{k}$ | [Closed minimum-order coupling bound](coupling_cost.md#3-closed-cost-at-the-minimum-interaction-order) |
| For $t=1$ and $\ell>d$, $J/\omega\ge(\ell+d)/(\ell-d)$ | [Exact scalar moment optimum](coupling_cost.md#one-protected-error) |
| For odd-distance stabilizer codes, $\ell=d+t$ implies $r_S=d+1$ | [Gate/readout theorem](gate_readout_tradeoff.md), with $1\le t$ and $2t+1\le d$; includes fixed stabilized ancillas |

The scalar moment problem is a necessary relaxation. Its feasible masses and optimum do not by themselves supply a physical Hamiltonian. At the unrestricted minimum distances and orders, the higher-error costs $71,799,9439$ are necessary bounds without supplied saturating gates. The family optima below occur at their stronger code-specific orders.

The [nine-qubit four-body construction](four_body_construction.md) realizes the first unrestricted equality case: $d=3,t=1,\ell=4,J/\omega=7$ for one logical $Z$ axis. Its nine commuting terms obey full error-image identities. The [canonical five-qubit benchmark](coupling_cost.md#the-five-qubit-benchmark), which is prior work, realizes $\ell=5,J/\omega=4$ with sixteen terms for each axis. The four-body witness does not establish universal four-body control or minimal block size.

| Foundation | What to read for |
|---|---|
| [Model and resources](model.md) | Detection distance, scalar shifts, unknown fault time, full intertwiners, and native resource definitions |
| [Locality theorem](locality.md) | Pauli twirls, vanishing weight moments, interpolation, and restrictions on available logical weights |
| [Coupling cost](coupling_cost.md) | Operator-to-scalar witness, finite primal/dual certificates, closed bounds, and the five-qubit comparison |
| [Four-body construction](four_body_construction.md) | Literal code generators, logical operators, bare coefficients, and sitewise cancellation proof |

## Sharp controls on a readout-reversible code family

The family $Q_m=[[5^m,1,3^m]]$ has even-weight stabilizers and odd-weight nontrivial logical representatives. Put $n=5^m$ and $d=3^m$. The available-weight argument gives $\ell\ge d+2t$ for every nontrivial transparent generator when $2t+1\le d$. Each logical Pauli axis attains the following exact resources:

| Protected error weight | Depth | Minimum order | Optimal axis coupling at that order |
|---:|---|---:|---|
| $t=1$ | $m\ge1$ | $d+2$ | $J_1(d)=d+1$ |
| $t=2$ | $m\ge2$ | $d+4$ | $J_2(d)=(4d^2+21d+8)/8$ |
| $t=3$ | $m\ge2$ | $d+6$ | $J_3(d)=(4d^3+51d^2+170d+24)/24$ |

Here $J_t(d)$ denotes $J/\omega$ for one axis. The coupling lower bounds apply to arbitrary Hamiltonians in the fixed-code model, including consistent scalar sector shifts. For two and three errors, resolving the weights inside bottom code blocks gives stronger bounds than the scalar total-weight relaxation. Seven complete block patterns determine the three-error optimum and force an outer weight-five logical contribution.

A strict truncated tensor lifting acts on the nested zero-, one-, two- and three-error hierarchy. An increment of index greater than the local error weight annihilates that error image. Consequently every omitted tensor term vanishes on the protected images, making the lifting exact. Compatible native coefficient signs preserve the coupling optimum at every depth. For a general one-qubit direction in the fixed canonical Pauli frame,

```math
J_{\min}=J_3(d)\bigl(|\Omega_X|+|\Omega_Y|+|\Omega_Z|\bigr)
\quad\text{for }h_L=\Omega_X X+\Omega_Y Y+\Omega_Z Z+cI,
\quad \ell=d+6.
```

The earlier two-error construction uses uniform active promotions and correlated inactive-frontier padding. Uniform padding over inactive bottom blocks fails for that ensemble beyond depth two. The increment lifting supplies different optimal two-error ensembles with hierarchy-dependent promotions; the frontier condition is not a uniqueness theorem for all optimal gates.

| Construction or proof | Scientific role |
|---|---|
| [Single-error family](minimum_readout_safe_gates.md) | Distance and parity proof, two signed weight classes, exact gate identities, and minimum-order coupling equality |
| [Sparse single-error gates](sparse_protected_gates.md) | Positive support reduction, explicit translation-orbit recursion, and controlled coefficient sizes |
| [Twenty-five-qubit two-error gate](two_error_gates.md) | Four-class seed, full error responses, sparse witness, and block-moment lower bound |
| [Growing two-error family](growing_two_error_gates.md) | Correlated frontier-padding construction, pair identities, and all-depth optimal budget |
| [Sparse two-error synthesis](sparse_two_error_synthesis.md) | Positive component profiles, exact pairwise child coupling, reference compiler, and finite 125-qubit certificate |
| [Twenty-five-qubit three-error gate](three_error_gates.md) | Seven-class seed, forced outer logical branch, full three-error responses, and all-direction optimum |
| [Growing three-error optima](growing_three_error_gates.md) | Strict increment lifting, sign preservation, arbitrary-Hamiltonian block-moment dual, and all-depth exact costs |

## Protected entanglers and universal encoded control

Keep $M$ product blocks of $Q_m$ fixed, with $m\ge2$. For a prescribed nonidentity logical Pauli string $P$ of logical weight $p$, its target coset has minimum physical weight $D=pd$. The ordinary distance of the full product code is still $d$. The [pure-string theorem](protected_entangling_gates.md) gives

```math
h_L=\Omega P+cI,\quad\Omega\ne0
\quad\Longrightarrow\quad
\ell_{\min}=D+6,\qquad
J_{\min}(\ell=D+6)=|\Omega|J_3(D)
```

for exact transparency through three physical Pauli errors. The lower bound projects arbitrary competing Hamiltonians onto the target logical coefficient and uses the complete block moments with $d$ replaced by $D$. Other logical cosets, detectable terms, stabilizers, and scalar shifts cannot evade it. The construction tensors the active-block increments with total increment index at most three and uses physical identity on idle blocks.

Six protected single-logical-qubit Pauli controls together with protected $ZZ$ generate all fifteen nonidentity two-qubit Pauli directions, hence $\mathfrak{su}(4)$. The larger pure-string family supplies every logical Pauli direction on a fixed product register. These are universal continuous encoded controls in the native Hamiltonian model, maintaining strict transparency throughout the evolution. The pure-string optimum does not imply that adding the individual optimum costs gives the optimum for an arbitrary mixed logical Hamiltonian at one common order cap.

## Construction and description costs

Interaction order, coupling budget, native term count, and exact coefficient size answer different questions. The finite examples make those distinctions explicit:

| Code and protected target | $t$ | $\ell$ | $J/\omega$ | Supplied native description |
|---|---:|---:|---:|---|
| $[[9,1,3]]$, logical $Z$ | 1 | 4 | $7$ | Nine commuting terms |
| $[[5,1,3]]$, each Pauli axis; canonical benchmark | 1 | 5 | $4$ | Sixteen terms per axis |
| $[[25,1,9]]$, each Pauli axis | 1 | 11 | $10$ | Sparse 75-term example, three bare coefficient values |
| $[[25,1,9]]$, each Pauli axis | 2 | 13 | $521/8$ | Sparse 2,575-term example, 125-bit common native denominator |
| $[[125,1,27]]$, each Pauli axis | 2 | 31 | $3491/8$ | Sparse 69,125-term example in 553 orbits, 1,458-bit common native denominator |
| $[[25,1,9]]$, each Pauli axis | 3 | 15 | $2867/8$ | Seven dense classes, 1,480,960 terms per axis, denominator 3,200,000 (22 bits) |
| $[[125,1,27]]$, each Pauli axis | 3 | 33 | $40175/8$ | Exact dense increment recursion, safe denominator bound of 69 bits |
| $[[625,1,81]]$, each Pauli axis | 3 | 87 | $824723/8$ | Same recursion, safe denominator bound of 208 bits |
| $[[50,2,9]]$, logical $ZZ$ | 3 | 24 | $1789$ | Eighteen ordered dense class pairs, 41,032,000,000 native terms, collected denominator 32,000,000,000 (35 bits) |
| $[[250,2,27]]$, logical $ZZ$ | 3 | 60 | $32824$ | Exact product-increment construction |

For one error, at most $3n+1$ terms per axis exist; an explicit recursion uses at most $4n$ with $O(\log n)$ coefficient bits. For two errors, positive component certificates and pairwise coupling give a general reference compiler, but its high polynomial degree does not establish fast large-depth synthesis. The 125-qubit sparse witness is independently checked, with substantial exact coefficient complexity.

For a single-block three-error axis, positive support reduction gives an $O(n^3)$ term-existence bound using $1+3n+9\binom n2+27\binom n3$ response coordinates. A practical sparse three-error compiler is not supplied. The direct dense recursion has safe coefficient denominator bounds of $O(d)$ bits, separate from its rapidly growing native expansion. The finite term counts and denominator sizes above are construction resources, not optima in term count, coefficient precision, or hardware cost. In particular, the 41-billion-term entangler is not a practical synthesis claim.

## Syndrome readout and control schedules

The complementary readout experiment applies a specified known product unitary, performs full ideal measurement of the original stabilizer syndrome, and permits recovery informed of the unitary and outcome. The [support/circuit invariant in Syndrome Reversibility Distance](https://github.com/GoGoKo699/Syndrome-Reversibility-Distance) determines whether that measurement loses logical information. Per-block parity prevents stabilizer/logical equal-support collisions on $Q_m$ and its product codes, giving $r_S=\infty$ even for entangled logical inputs. An even global target such as $ZZ$ does not change that per-block argument.

The [gate/readout theorem](gate_readout_tradeoff.md) links the two resource questions. At odd distance, an unrestricted minimum-order gate forces $r_S=d+1$; the nine-qubit witness has $r_S=4$, while the five-qubit benchmark has $r_S=\infty$. The gate and readout models retain their own ordering, recovery knowledge, and ideality assumptions. Their coexistence is not a composed noise threshold.

The [control account](control_robustness.md) independently tests whether a protected generator is maintained during a pulse. In the nine-support family it derives the recovered angle $A-2B_i(\tau)$ after a fault at site $i$ and time $\tau$, identifies calibration errors invisible to fault-free angle tests, and proves a failure of sequential commuting pulses. Repeated cycles bound the conditional phase error, without assigning a total noise or hardware advantage. The [physical interpretation](interpretation.md) relates these results to gate duration and native resource accounting.

## Proof dependencies and reproducibility

| Conclusion | Load-bearing argument | Evidence and limits |
|---|---|---|
| General interaction-order and coupling bounds | Detection removes weights below $d$; Pauli twirls give vanishing moments; interpolation and a spectral witness yield the bounds | Analytical proof; finite scalar primal/dual identities supplement it |
| Strict physical gates | Signed logical-coset membership plus exact conjugation responses | Full error-image identities, rather than logical compression alone |
| Sharper family and target-string optima | Parity restricts available weights; complete block patterns and target projection give arbitrary-Hamiltonian lower bounds | Exact primal/dual polynomial identities; constructions attain the stated order and budget |
| Arbitrary-depth protected control | Increment annihilation and sign-compatible truncated tensor lifting | Analytical induction; finite child-response profiles verify representative depths |
| Sparse descriptions | Positive response-preserving support reduction and explicit orbit or pairwise coupling constructions | Separate existence, constructive, and finite-witness guarantees |

Run the fourteen standard-library exact checks with Python 3.10 or later:

```bash
python verification/run_all.py
```

The [verification guide](../verification/README.md) identifies each program and committed JSON record. Among the complete coverage certificates, the sparse 125-qubit two-error check covers all 70,126 protected physical errors on each axis; the 25-qubit three-error check covers all 64,876 on each axis; eleven complete child-response profiles cover all 8,649,376 on 125 qubits; and the 50-qubit entangler check covers all 540,376 for each of nine logical axis products. Profile coverage does not mean enumerating a dense native expansion or multiplying a full Hilbert-space matrix. No floating-point tolerance is used.

All resource claims concern fixed codes and native Hermitian Pauli generators with ideal final recovery. Geometric range, noisy recovery and syndrome extraction, efficient decoding, and synthesis from different hardware primitives require additional accounting. The [related-work account](../references/RELATED_WORK.md) and [bibliography](../references/references.bib) distinguish inherited error-transparent methods and code ingredients from the resource laws and constructions developed here.

For the educational route, start with the [learning guide](../learning/README.md), the selected [Preskill bridge](../learning/PRESKILL_BRIDGE.md), and the [30-milestone map](../learning/MILESTONES.md).
