# From Preskill's QEC foundations to error-transparent locality

This bridge uses one external anchor: John Preskill, *Quantum Information*, Chapter 7, updated March 2026. The [author's course index](https://preskill.caltech.edu/ph229/index.html) links the [complete chapter](https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf). Page numbers below are the chapter's printed numbers; PDF viewer numbers are six larger.

Preskill supplies the foundations of correctability, distance, CSS codes, and stabilizers. The Hamiltonian, twirl, moment, coupling, and control arguments below are supplied locally. Their complete statements and proofs are in the [scientific account](../science/README.md). The [milestone map](MILESTONES.md) organizes a separate progression through those dependencies.

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

The five-qubit code in the last row is foundational input. Its canonical error-transparent Hamiltonian and coefficient accounting are developed in the [local benchmark](../science/coupling_cost.md#the-five-qubit-benchmark), with attribution to its original construction.

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
V^\dagger QV=q_QI_K,\qquad \operatorname{wt}(Q)<d.
```

The scalar can be nonzero. A low-weight stabilizer has scalar compression even though it acts nontrivially on the full physical Hilbert space. Setting every detectable compression to zero would incorrectly exclude degenerate codes.

Preskill's Eq. (7.17) translates to $V^\dagger E_b^\dagger E_aV=C_{ba}I_K$. Products of two weight-at-most-$t$ Paulis have weight at most $2t$, which explains the project's sufficient distance condition $d\ge2t+1$. The protected errors form a linear span: correcting a Pauli basis also corrects coherent combinations and channels whose Kraus operators lie in that span. The Hamiltonian theorem must nevertheless assume transparency separately.

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

| Error | Image of $|0\rangle$ | Image of $|1\rangle$ | Check eigenvalues |
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

Remove logical scalars with $[B]_0=B-\operatorname{tr}(B)I_K/K$, and define

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

The general [locality theorem](../science/locality.md#3-general-locality-theorem) uses a polynomial to express the same obstruction. If at most $t$ distinct positive weights can contribute, a degree-at-most-$t$ polynomial can vanish at all of them while having value one at zero. The moment equations would make its weighted logical sum equal to $A$, while its zeros make that sum vanish. This requires at least $t+1$ contributing weights at or above $d$, giving $r\ge d+t$. The theorem is independent of stabilizer structure and of the number of physical qubits.

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

The nine-qubit construction turns the abstract moments into a sitewise cancellation. Every displayed $Z$-type term has the same action on the code:

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
F_e=\frac{1+\operatorname{Re}\chi}{2},\qquad
1-F_{\rm avg}=\frac{1-\operatorname{Re}\chi}{3},\qquad
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
\mathcal D=\operatorname{rowspan}H_X,\qquad
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

The resulting capability is one continuous logical axis with strict transparency to all single-qubit errors, maximum Pauli weight four, and $J=7\omega$. A universal four-body gate set, the smallest block size, arbitrary control-error tolerance, and the cost of realizing the native interactions require additional results. The [scientific interpretation](../science/interpretation.md) and [source comparison](../references/RELATED_WORK.md) retain those boundaries.
