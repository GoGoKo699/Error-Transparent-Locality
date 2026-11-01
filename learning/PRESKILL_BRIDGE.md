# From Preskill's QEC foundations to error-transparent locality

This bridge uses one external anchor: John Preskill, *Quantum Information*, Chapter 7, updated March 2026. The [author's course index](https://preskill.caltech.edu/ph229/index.html) links the [complete chapter](https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf). Page numbers below are the chapter's printed numbers; PDF viewer numbers are six larger.

Preskill supplies the foundations of correctability, distance, CSS codes, stabilizers, and concatenation. The Hamiltonian, twirl, moment, coupling, and control arguments below are supplied locally. Sections 9–14 connect them to the separate syndrome-readout experiment, optimal concatenated families through three physical errors, sparse synthesis, and protected logical strings. Their complete statements and proofs are in the [scientific account](../science/README.md). The [milestone map](MILESTONES.md) organizes a progression through those dependencies.

## 1. From correctability to protected motion

Error correction asks whether the logical state can be recovered after a specified family of physical errors. A gate introduces another question: while the state occupies an error image, does it accumulate the intended logical evolution?

Suppose an encoder $V$ maps a logical state $|\psi\rangle$ to $V|\psi\rangle$. A code-preserving Hamiltonian satisfies

```math
HV=Vh_L.
```

The matrix $h_L$ is the generator seen by the encoded information. An instantaneous error $E$ moves that information to $EV|\psi\rangle$. Correctability says that the information is still recoverable. It does not by itself determine what $H$ does to $EV|\psi\rangle$ during the remaining gate time.

Exact error transparency adds the full map identity

```math
HEV=EVh_L.
```

The same $h_L$ then acts in the error image. Expanding an exponential in powers of $H$ gives $e^{-iHs}EV=EVe^{-ih_Ls}$, so a fault at time $\tau$ obeys

```math
e^{-iH(T-\tau)}E e^{-iH\tau}V
=EVe^{-ih_LT}.
```

An ideal final recovery removes the correctable error, leaving the intended evolution independently of $\tau$. This is the operational reason for imposing the generator identity. A final-time gate identity alone leaves the intermediate dynamics unspecified.

The [model](../science/model.md#2-exact-error-transparency) states the assumptions, including a fixed code, the protected error set, and the full physical-space equality. The earlier error-transparent and protected-Hamiltonian frameworks are attributed in [Related work](../references/RELATED_WORK.md).

## 2. Targeted Preskill sections

| Chapter location | Printed pages | Foundation used here |
|---|---:|---|
| [§7.2](https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=10), especially Eq. (7.17) | 4–7 | Correctable error spans; recovery; degeneracy |
| [§§7.3.1–7.3.3](https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=14) | 8–10 | Distinguishability, environmental information, reference decoupling |
| [§7.4](https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=18), especially §§7.4.1 and 7.4.3 | 12–14 | Pauli weight, distance, detection |
| [§§7.6–7.8](https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=24) | 18–24 | Binary linear codes and CSS encodings |
| [§7.9](https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=31) | 25–26 | Code-parameter constraints: Hamming, no-cloning, and Singleton bounds |
| [§§7.10.1–7.10.2](https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=33) | 27–31 | Stabilizers, phases, symplectic notation |
| [§§7.10.3–7.10.4](https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=37) | 31–34 | CSS checks and encoded Pauli operators |
| [§7.11](https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=40) | 34–37 | The five-qubit code underlying the comparison |
| [§7.17](https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf#page=54) | 48–50 | Inner and outer encodings; concatenation and multiplicative distance bounds |

The five-qubit code is foundational input. Its canonical error-transparent Hamiltonian and coefficient accounting are developed in the [local benchmark](../science/coupling_cost.md#the-five-qubit-benchmark), with attribution to its original construction. Section 7.17 supplies the concatenation framework. The exact parity, response, coupling, and tensor-lifting results for the family below are local derivations, not theorems attributed to that chapter.

## 3. Notation and assumptions

### Translating the conventions

| Preskill's chapter | This repository |
|---|---|
| Code projector $\Pi$ | $P=VV^\dagger$ |
| $V$ in §7.2 denotes a recovery isometry | $V$ denotes the encoder; recovery is stated separately |
| $[[n,k,d]]$ | Logical dimension $K=2^k$ for these codes; the general theorem allows any $K\ge2$ |
| §7.10.1, Eq. (7.116): $Y_{\rm P}=ZX=i\sigma_y$ | $Y=\sigma_y$ is Hermitian, with $Y^2=I$ |
| §7.10.2: $(\alpha\mid\beta)=Z(\alpha)X(\beta)$ | $\alpha$ lists $Z$ support and $\beta$ lists $X$ support; literal Pauli phases are retained |

The $Y$ conversion matters in a Hamiltonian calculation. If a word contains $m$ sites with both bits set, its Hermitian representative is $(-i)^m Z(\alpha)X(\beta)$. Binary labels retain commutation and support information, but coefficient signs require the phase as well. Conjugation is always $E^\dagger B E$; the shorter $EBE$ is valid for the repository's Hermitian Paulis, not for Preskill's anti-Hermitian $Y_{\rm P}$.

### Compression, detection, and correction

For any physical operator $B$, its compression is $V^\dagger BV$, a matrix on the logical space. The detection condition becomes

```math
V^\dagger QV=q_QI_K,\qquad \mathrm{wt}(Q)\lt d.
```

The scalar can be nonzero. A low-weight stabilizer has scalar compression even though it acts nontrivially on the full physical Hilbert space. Setting every detectable compression to zero would incorrectly exclude degenerate codes.

Preskill's Eq. (7.17) translates to $V^\dagger E_b^\dagger E_aV=C_{ba}I_K$. Products of two Paulis of weight at most $t$ have weight at most $2t$, which explains the project's sufficient distance condition $d\ge2t+1$. The protected errors form a linear span: correcting a Pauli basis also corrects coherent combinations and channels whose Kraus operators lie in that span. The Hamiltonian theorem must nevertheless assume transparency separately.

Compression also does not certify invariance. The equality $V^\dagger HV=h_L$ discards the component $(I-P)HV$. Code preservation requires that component to vanish. Likewise,

```math
V^\dagger E^\dagger HEV=h_L
```

examines only a diagonal block associated with $EV$. It can miss transfers to other error images. A full transparency certificate checks $HEV-EVh_L=0$ before any projection. Section 4 gives an explicit failure of the compressed-only check.

### Scalar shifts and degeneracy

The lower bounds also permit

```math
HEV=EVh_L+\lambda_EEV,\qquad \lambda_I=0.
```

For one error branch this adds only the phase $e^{-i\lambda_E(T-\tau)}$. In a coherent error superposition it can change relative syndrome amplitudes, but the transformed error remains in the correctable span, and ideal recovery still returns the same logical evolution. The strict construction sets every $\lambda_E$ to zero.

These shifts are not independently adjustable when error images overlap. For example, if $EV=FV$, the two identities require $\lambda_E=\lambda_F$. In the project's code, $X_5X_9$ is a stabilizer, so $X_5V=X_9V$. Equal error actions do not imply loss of logical information; they impose consistency rather than a requirement to distinguish the two physical faults.

## 4. Worked repetition-code example (restricted-noise illustration)

The following complete calculation isolates the timing issue with only eight basis states. Encode

```math
V|0\rangle=|000\rangle,\qquad V|1\rangle=|111\rangle
```

and protect only $\{I,X_1,X_2,X_3\}$. The checks $Z_1Z_2$ and $Z_2Z_3$ distinguish its four error images:

| Error | Image of $\lvert0\rangle$ | Image of $\lvert1\rangle$ | Check eigenvalues |
|---|---|---|---|
| $I$ | $000$ | $111$ | $(+,+)$ |
| $X_1$ | $100$ | $011$ | $(-,+)$ |
| $X_2$ | $010$ | $101$ | $(-,-)$ |
| $X_3$ | $001$ | $110$ | $(+,-)$ |

Measuring the checks and applying the indicated $X_i$ recovers any encoded superposition after one protected error.

### A correctable fault can still change a gate

The simple Hamiltonian $H_{\rm bare}=\omega Z_1$, with $\omega>0$, implements $h_L=\omega Z$ on the code. After an $X_1$ error, however, $X_1Z_1X_1=-Z_1$, so the logical rate changes sign. A fault at $\tau$ followed by final recovery gives

```math
U_{\rm recovered}
=e^{-i\omega(2\tau-T)Z},
```

instead of $e^{-i\omega TZ}$. Recovery repairs the bit flip; it cannot infer and undo an unknown accumulated logical angle merely from that syndrome.

Now choose

```math
H_{\rm maj}
=\frac{\omega}{2}(Z_1+Z_2+Z_3-Z_1Z_2Z_3).
```

For a computational word of Hamming weight $m$, its energy is

```math
\frac{\omega}{2}\bigl[3-2m-(-1)^m\bigr]
=
\begin{cases}
+\omega,&m=0,1,\\
-\omega,&m=2,3.
\end{cases}
```

Every image of $|0\rangle$ in the table therefore has energy $+\omega$, and every image of $|1\rangle$ has energy $-\omega$. It follows directly that $H_{\rm maj}EV=EV\omega Z$ for all four protected errors. The two logical phases remain correct throughout a fault at any time.

This is a restricted-noise example. It does not correct $Z_1$, which already acts as a logical $Z$ and has weight one. Its unrestricted detection distance is therefore one. Its three-body generator and budget $J=2\omega$ do not conflict with the distance-three, all-single-Pauli bound $r\ge4$, $J\ge7\omega$.

### Matching every compressed block still can fail

Add the Hermitian operator

```math
D=\kappa\bigl(|100\rangle\langle010|
+|010\rangle\langle100|\bigr),
\qquad H'=H_{\rm maj}+D .
```

It annihilates the code, so $H'$ preserves the code and has the same $h_L$. It also has zero compression in each of the four error images in the table:

```math
V^\dagger E^\dagger D EV=0
\quad(E=I,X_1,X_2,X_3).
```

All four compressed logical Hamiltonians therefore look correct. But

```math
H'X_1V|0\rangle
=\omega|100\rangle+\kappa|010\rangle.
```

The second term leaves the $X_1$ image; full transparency fails.

The logical damage can also be seen explicitly. After an $X_1$ fault, let $s$ be the remaining duration. In a frame removing the intended logical evolution, an input $\alpha|0\rangle+\beta|1\rangle$ becomes

```math
\alpha\bigl[\cos(\kappa s)|100\rangle
-i\sin(\kappa s)|010\rangle\bigr]
+\beta|011\rangle.
```

Ideal recovery maps the first two physical states to logical $|0\rangle$ with different syndrome records, while $|011\rangle$ maps to logical $|1\rangle$ with the $X_1$ record. Discarding that record multiplies the logical coherence $\alpha\beta^*$ by $\cos(\kappa s)$. This example makes the distinction concrete: equal diagonal logical blocks can coexist with a logical-state-dependent motion between error images.

## 5. Pauli twirl and weight moments

The [locality account](../science/locality.md#2-the-pauli-weight-superoperator) supplies a mathematical map that extracts interaction weight. It is a proof device, with no physical twirling procedure assumed.

For site $i$, define

```math
\mathcal R_i(B)=\frac14(B+X_iBX_i+Y_iBY_i+Z_iBZ_i),
\qquad
\mathcal W=\sum_i(\mathrm{Id}-\mathcal R_i).
```

Consider $Q=X_1Z_3$ on three qubits. At site one, the four conjugations give $Q,Q,-Q,-Q$, so $\mathcal R_1(Q)=0$. Site three also gives zero. At site two, every conjugation leaves $Q$ unchanged. Thus $\mathcal W(Q)=2Q$.

The same argument works for every tensor Pauli: each occupied site contributes one copy, and each identity site contributes zero. Grouping a Hamiltonian by weight,

```math
H=\sum_wH_w,\qquad
\mathcal W^j(H)=\sum_w w^jH_w.
```

Remove logical scalars with $[B]_0=B-\mathrm{tr}(B)I_K/K$, and define

```math
A_w=[V^\dagger H_wV]_0,\qquad
A=[h_L]_0=\sum_wA_w .
```

Distance supplies $A_w=0$ below $d$. Transparency supplies a different constraint. Its compressed consequence is

```math
V^\dagger E^\dagger HEV=h_L+\lambda_EI_K.
```

Each power $\mathcal W^j$ expands into conjugations by products of at most $j$ one-site Paulis. Such products have weight at most $j$, even when sites repeat; irrelevant product phases cancel in conjugation. The expansion coefficients sum to zero, since $\mathcal W^j$ annihilates the identity. Therefore, after scalar-free logical compression, every copy of $h_L$ cancels and every $\lambda_EI_K$ disappears. For $1\le j\le t$ this gives

```math
\sum_w w^jA_w=0.
```

These are operator-valued weight moments. They are necessary consequences of full transparency, not a replacement for it. In particular, $H_w$ need not preserve the code separately. Only the complete $H$ has the assumed full intertwining property.

The two ingredients now have distinct jobs: distance eliminates low weights; transparency makes the first $t$ moments of the remaining logical contributions vanish.

## 6. Locality and coefficient budgets

### The first nontrivial case

For $d=3,t=1$, a Hamiltonian using weights no larger than three has only $A_3$ available for nontrivial logical action. The moment condition says $3A_3=0$, which rules out a nonzero $A$.

Allowing weight four gives two equations,

```math
A_3+A_4=A,\qquad 3A_3+4A_4=0,
```

and hence $A_3=4A$, $A_4=-3A$. The desired logical generator is a cancellation between larger contributions of opposite sign.

The general [locality theorem](../science/locality.md#3-general-locality-theorem) uses a polynomial to express the same obstruction. If at most $t$ distinct positive weights can contribute, a polynomial of degree at most $t$ can vanish at all of them while having value one at zero. The moment equations would make its weighted logical sum equal to $A$, while its zeros make that sum vanish. This requires at least $t+1$ contributing weights at or above $d$, giving $r\ge d+t$. The theorem is independent of stabilizer structure and of the number of physical qubits.

### Why cancellation costs strength

Write the native expansion as $H=\sum_Qh_QQ$ and define

```math
J=\sum_{Q\ne I}|h_Q|,
\qquad
\omega=\frac{\lambda_{\max}(h_L)-\lambda_{\min}(h_L)}2.
```

Choose logical eigenstates $|+\rangle,|-\rangle$ at the largest and smallest energies. Their half-difference functional,

```math
\ell(B)=\frac{\langle+|B|+\rangle-\langle-|B|-\rangle}{2},
```

has $\ell(A)=\omega$. Every physical Hermitian Pauli has expectations between $-1$ and $1$, so $|\ell(V^\dagger QV)|\le1$. Consequently the native budget spent at weight $w$ is at least $|\ell(A_w)|$.

For the cubic/quartic solution this yields

```math
J\ge|\ell(4A)|+|\ell(-3A)|=7\omega.
```

This argument also works when $K>2$; it uses half the spectral width, which need not equal the norm of the trace-free logical Hamiltonian in higher dimension. An identity term is excluded from $J$ because it changes no logical energy differences. Other terms with scalar compression still consume physical coupling budget.

### From the example to a moment optimization

The dimensionless numbers $a_w=\ell(A_w)/\omega$ satisfy

```math
\sum_wa_w=1,\qquad
\sum_ww^ja_w=0\ (1\le j\le t),\qquad
J/\omega\ge\sum_w|a_w|.
```

These are signed masses, not probabilities. Positive weights could not have a vanishing first moment if every nonzero mass were positive. Minimizing their absolute sum is the [finite moment relaxation](../science/coupling_cost.md#2-the-exact-finite-moment-bound).

A useful lower-bound certificate is a polynomial $p$ of degree at most $t$ with $|p(w)|\le1$ at every allowed weight. The moment equations imply

```math
p(0)=\sum_wa_wp(w)\le\sum_w|a_w|.
```

For allowed weights three and four, $p(w)=7-2w$ takes values $+1,-1$, and $p(0)=7$. The masses $(4,-3)$ attain that value. The full account develops general duality, interpolation formulas, and higher-error bounds.

This optimization is a relaxation: signed masses alone do not specify a quantum code, the Pauli phases, or the full error-image identities. Physical attainability needs a construction. The supplied four-body example attains seven; the established five-qubit, five-body benchmark attains four. Higher-error entries in the moment table are necessary bounds, not demonstrated gates.

Finally, $J$ counts strengths in a declared physical Pauli basis. It is not the operator norm, geometric range, number of data qubits, or complete implementation cost. For the one-axis common-envelope realization, it constrains integrated native strength; synthesis, preparation, and recovery have separate costs. The [interpretation](../science/interpretation.md#why-minimum-interaction-order-costs-coupling-strength) states that comparison precisely.

## 7. Incidence and controls with unknown fault time

The nine-qubit construction turns the abstract moments into a sitewise cancellation. Every displayed $Z$ type term has the same action on the code:

```math
Z_SV=VZ.
```

For coefficients $h_S(t)$, define the no-fault logical rate and the signed rate incident on site $i$ by

```math
a(t)=\sum_Sh_S(t),\qquad
b_i(t)=\sum_{S\ni i}h_S(t).
```

An $X_i$ or $Y_i$ fault reverses precisely the incident terms, giving the full identity

```math
H(t)EV=EV[a(t)-2b_i(t)]Z.
```

Therefore the code rate and error-image rate agree exactly when $b_i(t)=0$. For the ideal coefficient vector $c$, site three illustrates the cancellation:

```math
c_{346}+c_{123}+c_{1368}+c_{3579}
=1+\tfrac12-1-\tfrac12=0.
```

Summing the site equations counts every term once per occupied site:

```math
\sum_i\sum_{S\ni i}c_S
=\sum_S|S|c_S
=3(4)+4(-3)=0.
```

The global first-moment equation is thus implied by all the site equations. Its converse is false. A global cancellation can conceal a nonzero incidence at a particular faulty qubit.

### A correct no-fault angle does not certify transparency

The perturbation $\epsilon(t)(Z_{346}-Z_{167})$ has zero logical action on the code. Both terms are cubic, so it also preserves the logical weight sums. Yet it changes $b_3$ by $\epsilon(t)$ and $b_1$ by $-\epsilon(t)$, among other entries. Its response to a fault can change even though every no-fault logical-rate test remains unchanged.

For the fixed nine supports, the [control analysis](../science/control_robustness.md#4-which-coefficient-changes-preserve-transparency) proves that the incidence matrix $M_{iS}=\mathbf1_{i\in S}$ has rank eight and kernel spanned by $c$. Instantaneously transparent controls in this ansatz must therefore have the form $h(t)=g(t)c$ almost everywhere. A common amplitude error preserves that cancellation but can still overrotate the logical qubit.

### The remaining pulse area controls the fault

In the control notation, $A$ is now a scalar pulse area, not the matrix $A=[h_L]_0$ of Sections 5–6. Set

```math
A=\int_0^Ta(t)\,dt,\qquad
B_i(\tau)=\int_\tau^Tb_i(t)\,dt.
```

Integrating the logical rate before and after the fault gives the recovered gate

```math
U_{i,\tau}=e^{-i[A-2B_i(\tau)]Z}
```

for $X_i$ and $Y_i$. A $Z_i$ fault commutes with the Hamiltonian and leaves the no-fault angle $A$.

Against an intended exponent angle $\Theta$, define $\Delta A=A-\Theta$ and $\delta_i(\tau)=\Delta A-2B_i(\tau)$. The exponent convention matters: $e^{-i\Theta Z}$ rotates a Bloch vector through $2\Theta$. For a deterministic branch the residual unitary is $e^{-i\delta Z}$, giving

```math
1-F_e=\sin^2\delta,\qquad
1-F_{\rm avg}=\tfrac23\sin^2\delta,\qquad
\|\mathcal U-\mathcal U_\Theta\|_\diamond=2|\sin\delta|.
```

The diamond norm convention ranges from zero to two. The [full derivation and conventions](../science/control_robustness.md#2-exact-phase-after-one-fault-and-recovery) are local additions, not results assigned to Preskill's chapter.

For a classical distribution of fault branches, independent of the logical input, let $\chi=\mathbb E[e^{-2i\delta}]$. In the intended-gate frame the recovered channel preserves populations and sends $\rho_{01}\mapsto\chi\rho_{01}$. The [channel calculation](../science/control_robustness.md#3-unknown-time-mixtures-give-an-exact-logical-channel) gives

```math
F_e=\frac{1+\mathrm{Re}\,\chi}{2},\qquad
1-F_{\rm avg}=\frac{1-\mathrm{Re}\,\chi}{3},\qquad
\|\mathcal E_{\rm rel}-\mathrm{Id}\|_\diamond=|1-\chi|.
```

These formulas retain both coherent angle bias and dephasing from an unknown time. They do not replace a coherent superposition of fault times by a classical mixture.

### Why commuting sequential pulses need separate analysis

Commutation guarantees the same final fault-free unitary when the terms are applied sequentially with their correct areas. A fault inserted between pulses changes which signs apply to the remaining areas.

For example, apply the $Z_{346}$ pulse first with area $\Theta$, then insert $X_3$. The total integrated incidence is zero, but the remaining incidence is $B_3=-\Theta$. Recovery therefore gives angle $3\Theta$. At $\Theta=\pi/4$ the residual is a logical $Z$ up to phase, with entanglement infidelity one. This is possible even though the ideal no-fault product formula is exact.

For integrable controls, $B_i(\tau)$ is continuous and $B_i(T)=0$. Equality with the no-fault logical channel for every $\tau$ requires $B_i(\tau)\in(\pi/2)\mathbb Z$. Continuity forces $B_i$ to vanish throughout, hence $b_i(t)=0$ almost everywhere. This explains the need for instantaneous cancellation.

Repeated sequential cycles provide a controlled approximation. A completed balanced cycle contributes zero; only the portion of the cycle containing the fault matters. The [pulse-order result](../science/control_robustness.md#7-a-controlled-approximation-by-repeated-sequential-cycles) supplies an order with $B_{\max}\le|\Theta|/N$ when the pulses have monotone accumulated areas, producing conditional infidelity of order $N^{-2}$ and diamond distance of order $N^{-1}$. Those are single-fault phase bounds. Total performance also depends on pulse durations and the resulting fault probability.

## 8. Reading the nine-qubit certificate

The [construction page](../science/four_body_construction.md) provides the actual code and Hamiltonian. Its parameters $[[9,1,3]]$ do not identify it with Preskill's nine-qubit example; the stabilizer checks must be used explicitly.

To translate the CSS description, let $H_Z$ and $H_X$ be its binary check matrices. The project uses

```math
\mathcal C=\ker H_Z,\qquad
\mathcal D=\mathrm{rowspan}\,H_X,\qquad
\mathcal D\subseteq\mathcal C.
```

These correspond to $C_1$ and $C_2$ in Preskill's §7.7. The two matrices each have rank four. Hence $\dim\mathcal C=5$, $\dim\mathcal D=4$, and $\mathcal C/\mathcal D$ has two cosets. Their coherent sums give one encoded qubit:

```math
|0_L\rangle=\frac14\sum_{b\in\mathcal D}|b\rangle,\qquad
|1_L\rangle=X_{145}|0_L\rangle.
```

The normalization follows from $|\mathcal D|=16$. The CSS commutation condition is $H_XH_Z^T=0$. The [distance argument](../science/four_body_construction.md#distance-and-degeneracy) then examines normalizers, including the weight-two stabilizer $X_5X_9$. Degeneracy must be retained when deciding whether a low-weight commuting Pauli is a damaging logical operator.

The logical-coset table proves that every Hamiltonian term acts as the same logical $Z$. One representative calculation is

```math
Z_{1368}=Z_{346}Z_{148}
=\overline Z\,Z_{148},
```

where $Z_{148}$ is a positive stabilizer. Since all these words contain only $Z$ operators, this multiplication introduces no additional Pauli phase. The full table is what fixes the signs of the literal coefficients.

Three logically separate checks then complete the result:

| Check | What it establishes |
|---|---|
| Code rank, normalizer, and distance | A two-dimensional code corrects the full single-qubit error set |
| Common logical coset and sitewise incidence cancellation | The full identities $H_\star EP=E\overline ZP$ hold, including error-image preservation |
| Cubic mass four, quartic mass minus three, absolute coefficient sum seven | The constructed axis attains the locality and coupling lower bounds |

The energy-plateau description in the construction makes the diagonal Hamiltonian visible on computational words. The CSS superpositions and the distance check supply the quantum coherence and phase-error protection. Plateau energies alone would establish neither.

The [verification guide](../verification/README.md) describes two independent exact representations of the nine-qubit certificate: signed Pauli-projector multiplication and binary CSS/energy calculations. These certify the finite example. The universal theorem rests on the mathematical moment argument, and the scalar moment optimum alone does not certify a physical Hamiltonian.

The resulting capability of this nine-qubit construction is one continuous logical axis with strict transparency to all single-qubit errors, maximum Pauli weight four, and $J=7\omega$. A universal four-body gate set, the smallest block size, arbitrary control-error tolerance, and the cost of realizing these native interactions require additional results. The later protected universal controls use the different, explicitly stated interaction orders below. The [scientific interpretation](../science/interpretation.md) and [source comparison](../references/RELATED_WORK.md) retain those boundaries.

## 9. The same code in a syndrome-readout experiment

The gate problem constrains evolution after a protected fault. The syndrome-readout problem asks what information survives a prescribed measurement after a known physical transformation. Its operational order is fixed: apply a specified product unitary, measure the full original stabilizer syndrome ideally, and then allow an arbitrary recovery informed of both the unitary and the outcome. Those access and measurement assumptions are part of the statement.

For a stabilizer code, write $S$ for the phase-free stabilizer group and $N$ for its Pauli centralizer. The readout project's [support criterion](https://github.com/GoGoKo699/Syndrome-Reversibility-Distance/blob/main/science/support_criterion.md) uses

```math
r_S=\min_{\substack{g\in S,\ L\in N\setminus S\\
\mathrm{supp}(g)=\mathrm{supp}(L)}}
\mathrm{wt}(gL),\qquad \min\varnothing=\infty.
```

Equal support allows a stabilizer and a logically nontrivial term to enter the same measurement-conditioned expansion. The support criterion and its converse establish the recoverability consequence; equality of supports by itself is not a replacement for that proof. Its [circuit characterization](https://github.com/GoGoKo699/Syndrome-Reversibility-Distance/blob/main/science/support_criterion.md#4-equivalent-characterization-by-even-logical-circuits) identifies $r_S$ with the smallest even logical-circuit weight. A logical circuit is a nontrivial normalizer word with no proper nonempty normalizer subword, keeping its actual local Pauli labels. These are imported research-level ingredients. Preskill's correctability and stabilizer sections provide their language, while the cited readout account supplies these theorems.

The [joint gate/readout theorem](../science/gate_readout_tradeoff.md#2-joint-theorem) combines that circuit result with the weight moments. For a stabilizer code encoding at least one qubit, odd $d\ge3$, $t\ge1$, and $d\ge2t+1$, a nontrivial exactly transparent generator obeys

```math
\ell=d+t\ \Longrightarrow\ r_S=d+1,
\qquad
r_S>d+1\ \Longrightarrow\ \ell\ge d+t+1.
```

The proof has three dependencies. First remove fixed physical qubits. After local Pauli-basis changes, an encoder factors as $V_{\rm red}\otimes|a\rangle$ on those sites. The partial matrix element $H_{\rm red}=\langle a|H|a\rangle$, rather than a partial trace, retains the full transparency identity and cannot increase Pauli order. Distance and $r_S$ are unchanged. Second, at minimum order every allowed weight $d,\ldots,d+t$ must have nonzero logical contribution; otherwise the annihilating-polynomial contradiction applies. Thus a logical representative of weight $(d+1)$ exists. Third, on the reduced code it has no proper normalizer subword: a stabilizer subword would remove at least two sites and violate distance; a logical subword would leave a forbidden weight-one normalizer. It is therefore an even circuit. Parity and distance give $r_S=d+1$.

The fixed-qubit step matters. Appending a fixed qubit to the five-qubit code creates a weight-four logical representative by multiplying a weight-three logical by the extra stabilizer. It does not create a circuit or change $r_S=\infty$.

For the nine-qubit construction, $Z_{1368}$ is an even circuit. The [explicit equal-support witness](../science/gate_readout_tradeoff.md#3-the-distance-three-comparison) gives $r_S=4$. Rotating its four sites about $Z$ by a common angle $\theta$ gives, with $q=\sin^2(\theta/2)$ and $0\le\theta\le\pi/2$,

```math
e_{\rm opt}=\varepsilon_{\rm opt}
=3q^2-2q^3=\frac3{16}\theta^4+O(\theta^6).
```

Here $e_{\rm opt}$ is optimal entanglement infidelity and $\varepsilon_{\rm opt}$ is optimal half-diamond error in that readout experiment. The known rotation can still cause information loss because the measurement is prescribed. This formula does not describe an unknown-time gate fault, and the two models do not automatically compose.

## 10. Concatenation, parity, and one-error gates

Preskill §7.17 defines concatenation by replacing each qubit of an outer encoding with an inner encoded qubit. Applying that construction repeatedly to the five-qubit code gives

```math
Q_m=[[5^m,1,3^m]],\qquad n=5^m,\quad d=3^m.
```

The [local distance proof](../science/minimum_readout_safe_gates.md#1-code-family-and-readout-property) establishes equality: a nontrivial outer logical uses at least three active inner blocks, and each costs at least the inner distance; minimum representatives attain the product. The same induction proves that every stabilizer has even weight and every nontrivial logical representative has odd weight. At the seed, stabilizers have weight zero or four and logical representatives have weight three or five. Lifting through disjoint blocks preserves these parities, as does multiplication by commuting stabilizers.

Equal-support stabilizer/logical pairs are therefore impossible, giving $r_S=\infty$ under the readout model of Section 9. Odd logical weights also strengthen the gate obstruction. Protecting errors through weight $t$ needs at least $t+1$ contributing logical weights, so

```math
\ell\ge d+2t
```

when $2t+1\le d$. This uses the particular family's coset parity; infinite $r_S$ alone does not establish this full bound for every code.

For one-error protection, let $T^{(0)}$ and $T^{(1)}$ be normalized averages of positive signed representatives of one logical axis at weights $d$ and $d+2$. A positive signed representative $Q$ obeys $QV_m=V_m\alpha$, even when its bare Hermitian sign is negative. The recursive averages have coefficient mass $d/(3n)$ and $(d+2)/(3n)$, respectively, for each specified nonidentity local label at each specified site. Thus

```math
H_\alpha=\frac{d+2}{2}T^{(0)}-\frac d2T^{(1)}
```

has coefficient sum one and zero signed mass on every local label. Conjugation by a single-site Pauli reverses two of those labels, leaving the logical response one. This proves the full identity $H_\alpha EV_m=EV_m\alpha$, not only its compression. The disjoint weights and positive class coordinates give

```math
\ell=d+2,\qquad J/\omega=d+1.
```

The parity obstruction proves minimum order, and the one-error coupling bound proves minimum cost at that order. The construction supplies each of $X,Y,Z$. It protects one physical error even when the larger-distance code corrects many more. The [full account](../science/minimum_readout_safe_gates.md) gives a correctable weight-two error that this one-error Hamiltonian does not treat transparently.

The dense expansion is a description choice. The [sparse one-error construction](../science/sparse_protected_gates.md) writes transparency as normalization plus $3n$ local incidence equations. With the two weight-class signs fixed, nonnegative support reduction leaves at most $3n+1$ native terms and retains the forced masses, hence the optimum. A separate explicit recursion uses translation orbits to reduce the constraints to normalization and three axis counts. It produces at most four orbits, hence $4n$ terms, with rational coefficients of $O(\log n)$ bits and no exponentially large candidate list. The general $3n+1$ reduction has a weaker coefficient-size guarantee. At 25 qubits, a three-orbit certificate gives 75 terms, order eleven, and cost ten.

Sparsity does not remove the need to hold the complete protected combination during a pulse. In the declared relative coefficient-error model, the residual sector-rate difference is bounded by $2\eta J$. Exact coefficient bit length and this algebraic sensitivity bound are different from an experimental calibration guarantee.

## 11. Two-error gates and sparse response preservation

An error on two physical sites probes pair responses that one-site incidence balance cannot determine. Divide $Q_2$ into five bottom five-qubit blocks. A contributing logical normalizer word has the following possible block weights at order thirteen:

| Class | Bottom-block pattern, up to permutation | $W=\sum_bw_b$ | $R=\sum_bw_b^2$ | Forced signed mass |
|---|---|---:|---:|---:|
| $A_0$ | $(3,3,3,0,0)$ | 9 | 27 | $143/8$ |
| $A_1$ | $(5,3,3,0,0)$ | 11 | 43 | $-117/4$ |
| $A_2$ | $(5,5,3,0,0)$ | 13 | 59 | $243/16$ |
| $F$ | $(3,3,3,4,0)$ | 13 | 43 | $-45/16$ |

An active logical factor has weight three or five; an inactive stabilizer factor has weight zero or four. This exhausts the contributing patterns at that order. The positive normalized class averages have exact responses whose combination with the displayed masses is one for every physical error through weight two. The [finite construction](../science/two_error_gates.md) therefore has $\ell=13$ and $J/\omega=521/8$ for each axis.

The additional lower-bound tool is a bottom-block twirl $\mathcal W_b$. Its square counts $w_b^2$ on a Pauli word and expands into conjugations by errors of weight at most two. Transparency consequently forces the scalar-free $R$ moment to vanish, alongside the $W$ and $W^2$ moments. The four rows $(1,W,W^2,R)$ determine the four operator masses. Detectable terms compress to zero, stabilizers to scalars, and scalar error-sector shifts disappear, so the argument applies to arbitrary Hermitian competitors. The absolute masses sum to $521/8$. Total weights alone merge $A_2$ and $F$, hiding their opposite signs and giving a weaker bound.

At larger depth the [two-error construction](../science/growing_two_error_gates.md) uses a logical-support tree with $k=d/3$ active bottom blocks. For its uniform-promotion ensemble, write $\rho_{ij}$ for the probability that two specified blocks are active, and $\eta_{ij}$ for the probability that block $i$ is padded by a stabilizer while block $j$ is active. Selecting an inactive frontier subtree uniformly, then a bottom block within it, gives

```math
\eta_{ij}=\frac{\rho_{ij}}{k-1}.
```

This is the pair correlation required for that ensemble's two-error cancellation. Uniform selection among all inactive bottom blocks fails at depths above two because pair probabilities depend on the first divergence in the tree. The four-pattern block moments and the construction attain, for every $m\ge2$,

```math
\ell=d+4,\qquad
J/\omega=J_2(d)=\frac{4d^2+21d+8}{8}.
```

The scalar total-weight bound is smaller by $5d/8$. The frontier rule is sufficient for this explicit ensemble; the increment construction in Section 13 provides another optimum with different positive components.

Sparse recursion needs more than a sparse final gate. Each positive component must preserve its complete character response vector $f_T(E)=\mathbb E_{Q\sim T}[\chi(E,Q)]$ through weight two. Splitting a final sparse gate into classes does not automatically give the required individual class profiles. The [positive base certificates](../science/sparse_two_error_synthesis.md#1-positive-class-certificates-at-twenty-five-qubits) check these profiles separately.

When at most two errors touch child factors, exact pairwise product marginals of the child distributions suffice; one-child marginals alone do not. The [rational coupling construction](../science/sparse_two_error_synthesis.md#2-pairwise-coupling-is-sufficient) supplies those product marginals even for unequal rational distributions. Translation-orbit response reduction then gives an exact reference algorithm with polynomial bit complexity and high polynomial degree. This is a theoretical complexity statement, not a fast large-depth runtime guarantee.

Separate exact final certificates use 2,575 native terms at 25 qubits and 69,125 at 125 qubits. Their collected native common denominators have 125 and 1,458 bits. The latter has order 31 and cost $3491/8$. Numerical searches selected finite supports; independent integer and rational calculations check the supplied coefficients, signed logical membership, and every protected response. Support count, exact coefficient size, the search procedure, and physical many-body synthesis remain different costs.

## 12. Seven patterns and the three-error coupling bound

A third physical error can be a nontrivial logical Pauli of a bottom five-qubit block. Its conjugation therefore constrains which outer logical branches occur. On $Q_2$, minimum permitted order is fifteen. The [three-error seed](../science/three_error_gates.md) uses seven complete bottom-block patterns:

| Class | Bottom-block pattern, up to permutation | Forced signed mass at $d=9$ |
|---|---|---:|
| $A_0$ | $(3,3,3,0,0)$ | $715/16$ |
| $A_1$ | $(5,3,3,0,0)$ | $-1755/16$ |
| $A_2$ | $(5,5,3,0,0)$ | $3645/32$ |
| $A_3$ | $(5,5,5,0,0)$ | $-1485/32$ |
| $F_0$ | $(3,3,3,4,0)$ | $-675/32$ |
| $F_1$ | $(5,3,3,4,0)$ | $675/32$ |
| $B_5$ | $(3,3,3,3,3)$ | $-3/2$ |

For a bottom weight $w\in\{0,3,4,5\}$, the cubic polynomial

```math
p(w)=\frac{4w^3-33w^2+68w}{15}
```

is zero on stabilizer weights and one on nontrivial logical weights. Thus $\sum_bp(w_b)$ counts active outer logical factors. Its scalar-free compression vanishes by the allowed degree-three twirl moments. It equals three on the first six classes and five on $B_5$. Combining this relation with normalization forces $C_{B_5}=-3A/2$. The outer weight-five branch cannot be omitted and repaired by reweighting the other six classes.

For the full lower bound set $W=\sum_bw_b$, $R=\sum_bw_b^2$, and $S=\sum_bw_b^3$. Degree at most three in bottom-block twirls supplies the rows

```math
(1,W,W^2,W^3,R,WR,S).
```

Their right-hand side is $(A,0,0,0,0,0,0)$, where $A=[h_L]_0$. Classification of all normalizer words at the order cap gives exactly the seven columns above. The matrix has determinant $2,949,120$, and its unique operator solution has the displayed masses. The [exact dual](../science/three_error_gates.md#5-block-moments-and-the-exact-coupling-lower-bound) takes their signs on all seven columns, certifying the same coupling lower bound. No symmetry of a competing Hamiltonian is assumed.

All normalized class atoms act as the same positive logical axis, so their conjugation characters establish the full physical-space error-image action. The finite certificate checks all 64,876 physical errors through weight three separately for each axis using exact factorization. The dense seed has 1,480,960 native words per axis and a common coefficient denominator of 3,200,000, of bit length 22. These are construction properties, not term-count or hardware precision optima.

The canonical logical Pauli frame is selected by the three physical normalizer cosets. Partitioning each pattern by those disjoint cosets sharpens the norm bound: for $A=\sum_\alpha\Omega_\alpha\alpha$,

```math
J_{\min}=\frac{2867}{8}\sum_{\alpha=X,Y,Z}|\Omega_\alpha|
\qquad(\ell=15).
```

The logical half-splitting is $\omega=(\sum_\alpha\Omega_\alpha^2)^{1/2}$, so the ratio to $\omega$ depends on direction. Changing logical coordinate labels does not freely rotate the prescribed native physical Pauli basis.

## 13. Exact increment lifting and the all-depth optima

The [lifting theorem](../science/growing_three_error_gates.md#1-a-strict-transparency-lifting-theorem) starts with a nested hierarchy of strict child gates $L_{s,\beta}$ through protected weight $s=0,1,2,3$. Define $L_{-1,\beta}=0$ and

```math
\Delta_{a,\beta}=L_{a,\beta}-L_{a-1,\beta}.
```

If an error $E$ has weight below $a$, both terms have the same full action on its image. Therefore

```math
\Delta_{a,\beta}EV=0
\qquad\text{when }a>\mathrm{wt}(E).
```

For one positive signed outer weight-three logical representative, tensor the three active child increment polynomials and keep total increment degree at most $t$. Then average over the ten such outer representatives, retaining their signs. Inactive children carry physical identity. This gives the parent $L'_{t,\alpha}$.

To prove strict protection, first take the full tensor product of active $L_{t,\beta}$ factors. It has the correct full action on any parent error image of total weight at most $t$. Expanding each factor into increments, an omitted term has total index above $t$. At least one active child's index exceeds the error weight in that child, so its increment annihilates the corresponding image. Every omitted tensor term is therefore exactly zero there. This proves the full physical-space intertwiner; truncation is in a finite hierarchy index and introduces no approximation to time evolution. The interaction order is at most $3D+2t$ when the child distance is $D$.

For the supplied seed, contributions in the seven patterns have compatible coefficient signs $(+,-,+,-,-,+,-)$. These signs survive lifting through total degree three, so repeated native words add without cancellation. The increment coefficient budgets are

```math
b_0(d)=1,\qquad b_1(d)=d,\qquad
b_2(d)=\frac{d(4d+13)}8,\qquad
b_3(d)=\frac{d(4d^2+39d+107)}{24}.
```

Cubing their generating polynomial under $d\mapsto3d$ gives the same four coefficient formulas. Summing the increments gives the optimal axis budgets:

| Protected physical weight | Depth | Minimum order on $Q_m$ | Exact axis budget at that order |
|---:|---|---|---|
| 1 | $m\ge1$ | $d+2$ | $J_1(d)=d+1$ |
| 2 | $m\ge2$ | $d+4$ | $J_2(d)=(4d^2+21d+8)/8$ |
| 3 | $m\ge2$ | $d+6$ | $J_3(d)=(4d^3+51d^2+170d+24)/24$ |

For the three-error lower bound at every depth, the seven bottom-weight patterns remain exhaustive. The same moment rows as in Section 12, now with variable $d$, have the same nonzero determinant. Their forced masses have the construction's signs, and their absolute sum is $J_3(d)$. The arbitrary-Hamiltonian proof allows consistent scalar sector shifts. Resolving logical cosets also gives $J_{\min}=J_3(d)\sum_\alpha|\Omega_\alpha|$ in the fixed canonical frame.

The lifting constructs another optimal two-error realization as part of the hierarchy. Its positive promotion and padding components need not equal those of the earlier uniform-promotion/frontier ensemble. The earlier pair-correlation condition concerned that ensemble and does not preclude this different construction.

The recursive description is short, but its dense native expansion grows rapidly. A safe common native denominator obeys $q_2=3,200,000$ and $q_m=10q_{m-1}^3$, giving bit lengths 22, 69, 208, and 627 at depths two through five, or $O(d)$. These are upper bounds on exact description size, not minimal denominators or physical control precision. A separate response-preserving support argument gives at most

```math
D_3(n)=1+3n+9\binom n2+27\binom n3=O(n^3)
```

native terms per axis in principle. It does not supply a practical sparse three-error compiler or an explicit sparse 125-qubit word list. At 125 qubits, eleven complete response profiles cover all 8,649,376 protected errors; the certificate checks those profiles and their coverage rather than a dense native contraction for every error. The all-depth physical-space conclusion follows from the lifting proof.

## 14. Pure logical strings, entanglers, and universal control

On the unchanged product code $Q_m^{\otimes M}$, $m\ge2$, consider a specified logical Pauli string $P_L$ of logical weight $p\ge1$. Its minimum physical representative weight is $D=pd$: each active encoded block needs a nontrivial representative of weight at least $d$, and minimum representatives attain the product. Its weight parity is $p\bmod2$. The ordinary distance of the complete product code is still $d$, since a logical operation can act on one block.

The [protected-string construction](../science/protected_entangling_gates.md) tensors the increments only on active encoded blocks and retains total degree at most three:

```math
H_{P_L}=\sum_{\substack{a_i\ge0\ (i\in A(P_L))\\\sum_i a_i\le3}}
\bigotimes_{i\in A(P_L)}\Delta_{a_i,(P_L)_i},
```

with physical identity on inactive blocks. The omitted-term argument of Section 13 applies to every physical error of total weight at most three, including errors on different encoded blocks and entangled logical inputs. Thus $H_{P_L}EV=EVP_L$ as a full map.

The increment-budget polynomial has an additional additive identity:

```math
B(x,z)=\sum_{a=0}^3b_a(x)z^a,
\qquad B(x,z)B(y,z)=B(x+y,z)\pmod{z^4}.
```

Consequently $p$ active factors have total budget at most $\sum_{a=0}^3b_a(pd)=J_3(D)$ by the triangle inequality. The matching lower bound projects any competing logical operator onto its specified Pauli coefficient with $\pi_{P_L}(A)=2^{-M}\mathrm{Tr}(P_LA)$. Other logical cosets, scalar terms, and detectable terms have zero target projection. Target weights start at $D$ in steps of two, so the projected moments force order at least $D+6$. At that order, the same seven bottom-block patterns and their moment dual apply with $d$ replaced by $D$. They give the reverse cost inequality. Hence, for $h_L=\Omega P_L+cI$ with $\Omega\ne0$,

```math
\ell_{\min}=pd+6,\qquad
J_{\min}(\ell=pd+6)=|\Omega|J_3(pd).
```

This is the pure-string law. It does not assign a globally optimal sum of these budgets to an arbitrary mixed logical Hamiltonian at one common order cap: a lower-weight component can exploit extra allowed locality under a cap chosen for a higher-weight one.

For two $Q_2$ blocks, $P_L=ZZ$ has $D=18$, minimum order 24, and unit-strength budget 1789. Eighteen ordered class pairs specify its dense expansion of 41,032,000,000 words, with collected common denominator 32,000,000,000 of bit length 35. The finite verifier covers all 540,376 physical errors through weight three for each of the nine two-block Pauli axes by complete child response profiles. It does not enumerate that dense word list. Three active $Q_2$ blocks give $D=27$, order 33, and cost $40175/8$; two $Q_3$ blocks give $D=54$, order 60, and cost $32824$.

The two-block logical gate $e^{-i\pi ZZ/4}$ takes $|++\rangle$ to a state with either one-qubit reduced density matrix $I/2$. The six local Pauli generators together with $ZZ$ generate all fifteen nonidentity two-qubit Pauli directions under commutators, hence the full two-qubit unitary Lie algebra after removing global phase. These are protected continuous encoded controls in the declared native Hamiltonian model. At every instant, the applied complete combination must satisfy strict transparency; sequential individual native terms do not inherit this guarantee.

The product code also retains $r_S=\infty$. Each stabilizer has even-weight restriction in every encoded block, while a nontrivial logical string has odd-weight restriction in at least one block. Their supports cannot coincide. An even global logical weight such as $ZZ$ therefore does not create a readout collision; its single-block logical subword also prevents the relevant word from being an even logical circuit.

The resulting picture separates exact encoded control, prescribed-measurement reversibility, and implementation. Gate protection concerns accumulated physical errors within the stated weight set and ideal final recovery. Readout concerns each specified known product unitary followed by ideal original-syndrome measurement and informed recovery. Their coexistence on a fixed code supplies no joint noisy-hardware threshold. Geometric range, many-body synthesis, state preparation, recovery-device faults, efficient decoding, and practical large-depth sparse three-error compilation remain outside the proved resource optima.
