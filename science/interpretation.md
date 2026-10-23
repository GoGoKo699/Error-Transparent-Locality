# Physical meaning and scope

## Why equal logical rates require extra interaction weight

The code distance removes all low-weight nontrivial logical action. Exact error transparency adds another requirement: conjugating the physical generator by any protected error must leave its logical energy differences unchanged. A single-site Pauli twirl weighs a term in proportion to the number of sites on which that term acts. Matching the logical action before and after errors therefore forces signed cancellations between interaction weights.

For a distance-three code and all single-qubit errors, the first moment must vanish. At maximum interaction order four, the logical contributions are uniquely fixed to $4h_L$ from cubic terms and $-3h_L$ from quartic terms, after removing scalars. The desired generator is their difference. A purely cubic generator has nothing at another weight with which to cancel its nonzero first moment.

The [general proof](locality.md) repeats this logic for the first $t$ moments. At least $t+1$ distinct contributing weights are needed above the distance threshold. This explains the necessary order $d+t$ without assuming any particular stabilizer presentation or number of physical qubits.

## Why minimum interaction order costs coupling strength

The absolute strengths required to produce $4h_L$ and $-3h_L$ cannot cancel in a native coupling budget. Their sum is at least seven times the logical half-splitting. The [explicit nine-qubit Hamiltonian](four_body_construction.md) uses only terms that achieve maximal logical contrast, and its coefficient signs implement exactly this cancellation. It attains the cost as well as the interaction-order bound.

Allowing order five changes the endpoint masses to $5/2$ and $-3/2$, reducing the required budget to four. The [canonical five-qubit protected Hamiltonian](coupling_cost.md#the-five-qubit-benchmark), already present in earlier work, attains this second optimum. The comparison demonstrates a real tradeoff between maximum native interaction order and the sum of native strengths. The data-qubit counts and term counts are separate resources: the exhibited four-body construction uses nine qubits and nine terms; the benchmark uses five qubits and sixteen terms for one axis.

For a fixed-axis implementation with an instantaneous budget $J(t)\le J_{\max}$ and required exponent angle $\Theta$, the one-error bound implies

```math
|\Theta|\le\int_0^T\omega(t)dt
\le\frac{r-d}{r+d}J_{\max}T,
```

provided the generator remains exactly transparent throughout and the logical evolution stays on that axis. Thus the native model gives a gate-duration lower bound

```math
T\ge\frac{r+d}{r-d}\frac{|\Theta|}{J_{\max}}.
```

Here $\Theta$ is a chosen accumulated angle for the path, not a unique label for the final channel modulo its phase periodicity. A monotone common envelope attains the integrated-strength relation for the supplied saturating examples. This comparison does not assign a hardware cost to making a four- or five-body interaction available in the first place.

At minimum interaction order for higher error weights, the moment cost grows rapidly. The [closed expression and its asymptotic](coupling_cost.md#growth-with-the-number-of-protected-faults) quantify the price of insisting on the smallest order. They do not prove that any high-error equality case is physically attainable.

## What a control calibration must test

For the nine-support Hamiltonian, the no-fault logical rate is the sum of all coefficients. The rate after an $X_i$ or $Y_i$ error differs by twice the signed coefficient sum incident on site $i$. These are different calibration observables.

Consequently, a perturbation can preserve every no-fault logical-angle test while introducing a phase that depends on the fault time. The [control analysis](control_robustness.md) gives such a perturbation explicitly. Within these nine supports, exact instantaneous transparency permits only a common rescaling of the displayed coefficient vector. Matching the final integrated areas is insufficient.

Sequential application of the commuting terms illustrates this distinction sharply. Its fault-free final unitary is exactly correct, but a fault between pulses can create a full logical error. Repeated cycles can bound this conditional phase error, at the cost of more pulses. Without pulse durations, switching costs, and a physical noise model, that approximation does not establish a better total error rate.

## Boundaries of the comparison

The theorem concerns a fixed subspace code and a generator satisfying specified sector-intertwining identities. Its locality is tensor-Pauli weight. It does not impose geometric locality or constrain arbitrary circuits, moving encodings, measurement-assisted gates, or generalized autonomous schemes whose correction dynamics mixes syndrome sectors.

The native budget also excludes state preparation, syndrome extraction, final recovery, and synthesis of higher-body terms from other controls. Those costs can dominate an implementation. The result identifies an exact algebraic resource requirement before those additional costs are specified.

The [literature comparison](../references/RELATED_WORK.md) distinguishes this setting from an earlier five-body discussion using a common active subsystem, syndrome-dependent logical-rate deformation, bosonic squeezing-order bounds, and energy-penalty protection. These are different hypotheses or resource definitions, and their results are not contradicted by a sum of four-body terms on a nine-qubit block.

The established scientific conclusion is a general weight-moment obstruction with an exactly attained single-error case and an explicit strength tradeoff. Higher-error attainability, the smallest block supporting the four-body optimum, universal four-body logical control, and a complete hardware realization require additional results.
