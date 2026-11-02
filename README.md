# Error-Transparent Locality

**Exact resource laws for logical Hamiltonians that keep working through physical faults at unknown times.**

A correctable fault during a gate can change the logical evolution rate until recovery. Exact error transparency removes this timing dependence: the physical Hamiltonian implements the same logical generator in the code and every protected error image. This repository proves general interaction-order and native coupling bounds, gives a sharp four-body witness, and constructs resource-optimal protected controls and entanglers on fixed concatenated five-qubit codes.

## Sister projects: Protected Gates and Syndrome Readout

| Sister repository | Central question |
|---|---|
| **[Error-Transparent Locality](https://github.com/GoGoKo699/Error-Transparent-Locality) (this repository)** | Which native interaction order and coupling budget let a logical gate tolerate faults at unknown times? |
| **[Syndrome Reversibility Distance](https://github.com/GoGoKo699/Syndrome-Reversibility-Distance)** | When does the original syndrome measurement preserve logical information after a known product unitary? |

The [shared gate/readout theorem](science/gate_readout_tradeoff.md) connects the two requirements on a fixed code. The gate and readout models retain separate assumptions.

## General resource bounds

Let a fixed code have detection distance $d$ and encoding $V$. A Hermitian, code-preserving Hamiltonian is transparent through Pauli-error weight $t$ when

```math
HEV=EV(h_L+c_E I)
\qquad\text{for every tensor Pauli }E\text{ with }\mathrm{wt}(E)\le t.
```

The lower bounds allow consistent scalar sector shifts $c_E$; the explicit constructions satisfy the strict identity with every $c_E=0$. This is a full physical-space equality, including preservation of each error image. With ideal final recovery, it preserves the intended logical evolution independently of the fault time.

Write $\ell$ for the largest weight of a nonzero native Pauli term, $J$ for the sum of absolute nonidentity **bare Hermitian Pauli coefficients**, and $\omega$ for half the spectral width of $h_L$. For nontrivial logical action, the general bounds are

```math
\boxed{\ell\ge d+t,\qquad
J\ge\left[\sum_{k=0}^{t}2^k\binom{d+k-1}{k}\right]\omega
\quad\text{when }\ell=d+t.}
```

Correction of all errors through weight $t$ requires $d\ge2t+1$, hence $\ell\ge3t+1$. For one protected error and any $\ell>d$, the exact scalar moment bound is $J/\omega\ge(\ell+d)/(\ell-d)$. These statements allow degenerate codes and arbitrary logical dimension. See the [model](science/model.md), [weight-moment proof](science/locality.md), and [coupling theorem](science/coupling_cost.md).

At $d=3,t=1$, a [nine-qubit CSS code](science/four_body_construction.md) attains $\ell=4$ and $J/\omega=7$ with nine commuting terms for one logical $Z$ axis. The established [canonical five-qubit construction](science/coupling_cost.md#the-five-qubit-benchmark) uses $\ell=5$, $J/\omega=4$, and sixteen terms per axis. These are optima at their respective interaction orders under the declared native budget. The four-body result establishes neither universal four-body control nor minimal block size. Attainment of the unrestricted order $\ell=d+t$ for $t>1$ remains open here.

## Optimal controls with reversible syndrome readout

For the concatenated five-qubit codes $Q_m=[[5^m,1,3^m]]$, put $n=5^m$ and $d=3^m$. Their stabilizers have even weight and their nontrivial logical Pauli representatives have odd weight. The resulting available-weight obstruction strengthens the gate bound to $\ell\ge d+2t$ whenever $2t+1\le d$.

Every logical Pauli axis attains this interaction order for $t=1,2,3$, with the following exact native coupling optima **for this code family at that order**:

| Protected Pauli-error weight | Depth | Minimum interaction order | Optimal axis budget $J_t(d)=J/\omega$ | Account |
|---:|---|---:|---|---|
| $t=1$ | $m\ge1$ | $d+2$ | $d+1$ | [Single-error controls](science/minimum_readout_safe_gates.md) |
| $t=2$ | $m\ge2$ | $d+4$ | $(4d^2+21d+8)/8$ | [Two-error optima](science/growing_two_error_gates.md) |
| $t=3$ | $m\ge2$ | $d+6$ | $(4d^3+51d^2+170d+24)/24$ | [Three-error optima](science/growing_three_error_gates.md) |

The higher-error coupling proofs resolve interaction weights inside code blocks and apply to arbitrary competing Hamiltonians, including consistent scalar sector shifts. A strict truncated tensor lifting carries the zero- through three-error hierarchy to every larger depth. In the fixed canonical one-qubit Pauli frame, the three-error result also gives the exact all-direction cost $J_{\min}=J_3(d)(|\Omega_X|+|\Omega_Y|+|\Omega_Z|)$ at $\ell=d+6$.

Native term count is a separate resource. The [single-error sparse recursion](science/sparse_protected_gates.md) uses at most $4n$ terms per axis with $O(\log n)$ coefficient bits; a separate support bound is $3n+1$. The [two-error sparse synthesis](science/sparse_two_error_synthesis.md) supplies a 69,125-term optimal gate on 125 qubits. The [scientific overview](science/README.md#construction-and-description-costs) compares the finite witnesses, coefficient sizes, and exact coverage certificates.

These codes also have syndrome reversibility distance $r_S=\infty$: every **known product unitary** is recoverable after full ideal measurement of the **original** stabilizer syndrome, with recovery informed of that unitary. For odd-distance stabilizer codes with $d\ge3$, $t\ge1$ and $d\ge2t+1$, attaining the unrestricted gate order $\ell=d+t$ forces $r_S=d+1$. Thus $r_S>d+1$ requires $\ell\ge d+t+1$. The coexistence of these guarantees does not establish a joint noisy threshold.

## Protected entanglers on fixed product codes

On $M$ fixed $Q_m$ blocks with $m\ge2$, prescribe a pure nonidentity logical Pauli string $P$ of logical weight $p$. Its minimum physical representative weight is $D=pd$, while the product code's ordinary distance remains $d$. For $h_L=\Omega P+cI$, $\Omega\ne0$, exact transparency through three physical errors has the sharp resource law

```math
\boxed{\ell_{\min}=D+6,\qquad
J_{\min}(\ell=D+6)=|\Omega|J_3(D).}
```

The [protected-string construction and lower bound](science/protected_entangling_gates.md) keep the code and original syndrome measurement fixed, with $r_S=\infty$. The first $ZZ$ entangler acts on a $[[50,2,9]]$ product code at $\ell=24$, $J/\omega=1789$. Together with protected local Pauli controls, it generates universal continuous encoded control in this model. The pure-string law does not assign a globally optimal sum of costs to an arbitrary mixed logical Hamiltonian at one common interaction-order cap.

The first entangler's compact dense specification contains **41,032,000,000 native terms**. This proves an exact resource optimum in interaction order and coupling budget; practical sparse synthesis and physical implementation require further work.

## Reading and learning routes

| Reader's aim | Start here |
|---|---|
| Follow the complete scientific argument | [Scientific overview and proof map](science/README.md) |
| Check definitions and general bounds | [Model](science/model.md) → [locality](science/locality.md) → [coupling cost](science/coupling_cost.md) |
| Inspect explicit controls and entanglers | [Construction catalog](science/README.md#construction-and-description-costs) and [protected logical strings](science/protected_entangling_gates.md) |
| Understand fault-sensitive control schedules | [Control robustness](science/control_robustness.md) and [physical interpretation](science/interpretation.md) |
| Study from the shared educational anchor | [Learning guide](learning/README.md), [Preskill bridge](learning/PRESKILL_BRIDGE.md), and [30 milestones](learning/MILESTONES.md) |
| Check attribution and nearest precedents | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

The shared educational anchor is **John Preskill, _Quantum Information_, Chapter 7, “Quantum Error Correction”**, in the author-hosted draft updated March 2026. This project's bridge selects relevant sections and translates notation and Pauli phases; its twelve background and eighteen narrative milestones lead through protected entanglers and universal encoded control. The [sister project's Preskill bridge](https://github.com/GoGoKo699/Syndrome-Reversibility-Distance/blob/main/learning/PRESKILL_BRIDGE.md) follows the readout argument with its own 30-milestone map.

## Reproduce the certificates

Only Python 3.10 or later and its standard library are required:

```bash
python verification/run_all.py
```

The [verification guide](verification/README.md) describes fourteen exact checks and their committed JSON records. They cover full error-image identities, code and stabilizer properties, coefficient normalization, moment primal/dual certificates, sparse constructions, recursive response coverage, entanglers, and control phases. No floating-point tolerance is used. Finite certificates support the stated instances; the general and arbitrary-depth conclusions use the analytical proofs.

## Physical scope

Interaction order counts qubits in one Pauli term. Native coupling budget counts absolute coefficients in a fixed basis. Neither specifies geometric range, term count, coefficient description size, or complete hardware cost.

Transparency must hold throughout a pulse. Even commuting terms can lose protection when applied sequentially: a correct fault-free final unitary can coexist with an incorrect logical evolution after an intermediate fault. The [control analysis](science/control_robustness.md) derives the exact phase and a bounded repeated-cycle approximation.

The model uses a fixed code and ideal final recovery. Multiple faults are protected while every accumulated error stays in the declared weight-limited set. State preparation, noisy syndrome extraction and recovery, efficient decoding, and synthesis of native many-body interactions require their own accounting.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## License

The repository retains the [MIT license](LICENSE).
