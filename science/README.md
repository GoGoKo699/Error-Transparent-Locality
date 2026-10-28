# Scientific account

Error correction protects a logical state after a recoverable fault. A Hamiltonian gate faces an additional timing problem: a fault during the gate can change the logical evolution rate until recovery occurs. Exact error transparency asks for the same logical generator in the code and every protected error image. The resulting cancellations impose both an interaction-order constraint and a coupling-strength cost.

This account establishes a general constraint, realizes its first nontrivial equality case, and separates that result from the established error-transparent framework and from the resources of a complete hardware implementation.

## Reading route

| Account | Main content |
|---|---|
| [Model and resources](model.md) | Fixed code, detection distance, full error-sector identities, unknown fault time, maximum Pauli weight, and native coupling budget |
| [Locality theorem](locality.md) | Twirl-derived weight moments and the bound $r\ge d+t$ |
| [Coupling cost](coupling_cost.md) | Exact finite moment relaxation, closed minimum-locality budget, higher-locality bounds, and the established five-qubit benchmark |
| [Four-body construction](four_body_construction.md) | An explicit degenerate CSS $[[9,1,3]]$ code and nine commuting terms attaining $r=4$, $J=7\omega$ |
| [Control robustness](control_robustness.md) | Exact fault-dependent phase, coefficient calibration, classical noise mixtures, and simultaneous versus sequential pulses |
| [Physical interpretation](interpretation.md) | Why the cancellations cost strength, what the comparison establishes, and the boundaries of the resource claims |
| [Gate locality and syndrome readout](gate_readout_tradeoff.md) | At odd distance, minimum interaction order forces $r_S=d+1$; fixed-qubit proof and exact code comparison |
| [Equality family with reversible readout](minimum_readout_safe_gates.md) | Concatenated five-qubit codes attain $\ell=d+2$, $J/\omega=d+1$, and $r_S=\infty$ for each logical Pauli axis and one protected error |
| [Sparse exact protected gates](sparse_protected_gates.md) | At most $3n+1$ terms exist per axis; explicit recursion uses at most $4n$ with small rational coefficients; 75-term example at $n=25$ |

The [related-work account](../references/RELATED_WORK.md) gives the nearest precedents and their hypotheses. The [verification guide](../verification/README.md) provides reproducible exact certificates.

## Main statements and evidence

Let $d$ be the detection distance, $t$ the largest protected Pauli-error weight, $r$ the maximum Hamiltonian Pauli weight, and $\omega$ the logical half-splitting. The native coupling budget $J$ is the sum of the absolute nonidentity Pauli coefficients.

| Statement | Status and evidence |
|---|---|
| $r\ge d+t$, hence $r\ge3t+1$ for correction of all errors of weight at most $t$ | General proof; arbitrary logical dimension, degenerate or nondegenerate code; consistent scalar sector shifts allowed |
| At $r=d+t$, $J/\omega\ge\sum_{k=0}^t2^k\binom{d+k-1}{k}$ | General proof; physical saturation asserted only for a supplied construction |
| For one protected error, $J/\omega\ge(r+d)/(r-d)$ | Exact optimum of the scalar moment relaxation; physically attained here at $(d,r)=(3,4)$ and by the known benchmark at $(3,5)$ |
| Four-body, single-axis strict transparency on nine qubits with $J=7\omega$ | Explicit Hamiltonian, analytic proof, two independent exact certificates |
| Five-body canonical benchmark on five qubits with $J=4\omega$ | Prior construction, exact reconstruction, and coupling-bound optimality under the stated budget |
| For odd-distance stabilizer codes, $r=d+t$ implies $r_S=d+1$ | Joint proof from weight moments and the companion project's even-circuit theorem; nine-qubit witness checked exactly |
| On $[[5^m,1,3^m]]$ codes, all three axes attain $\ell=d+2$ and $J/\omega=d+1$ while $r_S=\infty$ | Explicit two-shell Hamiltonians and recursive proof for one protected error; exact signed checks at $m=1,2$ |
| The same resource equalities admit sparse native Pauli expansions | Exact support-reduction proof and constructive orbit recursion; finite exact signs and error identities checked independently |
| A fault at site $i$ and time $\tau$ produces recovered angle $A-2B_i(\tau)$ in the nine-support control family | Full propagator derivation; exact phase checks and explicit sequencing failure |

The higher-error entries $71,799,9439$ in the minimum-locality budget are necessary bounds. They are not claimed as realized gates. The explicit four-body gate is one continuous logical axis; universal control and minimal physical block size remain outside the established result.

## Logical dependencies

The locality proof uses only detection and the necessary compressed consequences of exact transparency. The construction separately proves the full physical-space identities, including preservation of the correctable error images. The coupling proof uses a spectral witness to translate operator moments into a signed scalar moment problem. Its lower bound becomes a physical optimum only when an actual Hamiltonian saturates it.

Control analysis then asks whether that Hamiltonian is maintained during a pulse. Commutation makes the fault-free product of sequential pulses exact, but does not by itself preserve the logical rate after a fault at an intermediate time. This distinction is essential to interpreting the resource comparison.
