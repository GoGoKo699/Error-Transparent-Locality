# Error-Transparent Locality

**Exact interaction-order and coupling-strength limits for error-transparent logical Hamiltonians.**

A physical fault during a logical gate can change the rate of the encoded evolution until recovery occurs. An error-transparent Hamiltonian avoids that timing distortion by implementing the same logical generator in the code and every protected error image. This repository proves a general interaction-order constraint, derives the associated native coupling cost, and gives an explicit four-body construction that attains both bounds for arbitrary single-qubit errors.

## Main result

For a fixed code with detection distance $d$, a nontrivial logical Hamiltonian transparent to every tensor-Pauli error of weight at most $t$ must have maximum Pauli-term weight

```math
\boxed{r\ge d+t.}
```

Correcting all such errors requires $d\ge2t+1$, giving $r\ge3t+1$. The proof allows degenerate codes, arbitrary logical dimension, and consistent scalar energy shifts between error sectors.

Let $J$ be the sum of absolute nonidentity Pauli coefficients and $\omega$ the logical half-splitting. At the minimum allowed interaction order,

```math
J\ge\left[\sum_{k=0}^{t}2^k\binom{d+k-1}{k}\right]\omega.
```

For one protected error and any $r>d$, the exact scalar moment bound is

```math
J\ge\frac{r+d}{r-d}\,\omega.
```

The distance-three, four-body bound is $J\ge7\omega$. A nine-term commuting Hamiltonian on a degenerate CSS $[[9,1,3]]$ code attains it for a continuous logical $Z$ rotation. The established canonical five-qubit construction attains the corresponding five-body bound $J\ge4\omega$.

| Resource for one logical axis | Four-body construction | Known five-qubit benchmark |
|---|---:|---:|
| Data qubits | 9 | 5 |
| Maximum Pauli weight | 4 | 5 |
| Coupling budget $J/\omega$ | 7 | 4 |
| Nonzero Pauli terms | 9 | 16 |

The two examples establish exact optima at their respective interaction orders under the declared native budget. The four-body construction proves one logical axis. Higher-error saturation, universal four-body control, and minimal block size are not established.

## Connection to syndrome readout

For an odd-distance stabilizer code, attaining the protected-gate interaction order $r=d+t$ forces syndrome reversibility distance $r_S=d+1$. Thus $r_S>d+1$, including perfect product-unitary reversibility, requires at least $d+t+1$-body interactions under the same transparency assumptions. The [joint theorem and proof](science/gate_readout_tradeoff.md) connect this project to [Syndrome Reversibility Distance](https://github.com/GoGoKo699/Syndrome-Reversibility-Distance), handle fixed ancillary qubits, and give an exact four-site readout-loss witness on the nine-qubit code. Higher-error attainability and composition of the two noise models remain separate questions.

## Read the work

Start with the [scientific overview](science/README.md). The complete account is organized by topic:

- [Model and resource definitions](science/model.md)
- [General locality proof](science/locality.md)
- [Coupling bounds and the five-qubit comparison](science/coupling_cost.md)
- [Explicit four-body code and Hamiltonian](science/four_body_construction.md)
- [Control errors and faults during a pulse](science/control_robustness.md)
- [Physical interpretation and scope](science/interpretation.md)

The [related-work account](references/RELATED_WORK.md) states the closest antecedents and the precise comparison. The [bibliography](references/references.bib) supplies primary-source metadata. The protected-Hamiltonian framework and canonical five-qubit construction are prior work; the weight-moment obstruction, its coefficient consequences, and the supplied saturating witness are the results developed here.

## Learn the project

The [learning guide](learning/README.md) connects the research to one educational anchor: **John Preskill, _Quantum Information_, Chapter 7, “Quantum Error Correction”**, in the author-hosted draft updated March 2026. The [Preskill bridge](learning/PRESKILL_BRIDGE.md) identifies the relevant sections, translates notation and Pauli phase conventions, and develops the extra steps needed for this project.

The [30-milestone map](learning/MILESTONES.md) has two phases: **13 background milestones** establish the code, error, evolution, and resource language; **17 research milestones** build the moment obstruction, sharp single-error constructions, and control analysis. Each phase proceeds from local ingredients to a synthesis. The map follows the project's dependencies rather than the chapter's full table of contents.

## Reproduce the finite certificates

Only Python 3.10 or later and its standard library are required:

```bash
python verification/run_all.py
```

The [verification guide](verification/README.md) explains the six exact checks and links their committed JSON records. They cover full physical-space error identities, stabilizer signs, code distance, coupling normalization, finite primal/dual certificates, and control-phase formulas. No floating-point tolerance is used.

## Physical scope

Interaction order means the largest support of an individual Pauli term. It is distinct from geometric range and from the union of all term supports. Coupling budget is the absolute coefficient sum in a fixed native Pauli basis; it is distinct from an operator norm or a complete hardware cost.

The terms must maintain the transparency conditions throughout the gate. Commuting terms applied sequentially can have the correct fault-free final unitary while an intermediate fault creates a logical error. The control account derives this effect and a bounded sequential approximation.

The results assume a fixed code and ideal final recovery. State preparation, recovery-device faults, ancilla overhead, and synthesis of many-body interactions from different primitives require their own resource and noise accounting.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## License

The repository retains the [MIT license](LICENSE).
