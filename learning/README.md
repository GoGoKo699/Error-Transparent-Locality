# Learning Error-Transparent Locality

The central question is how demanding the same logical evolution before and after a correctable error constrains the physical Hamiltonian. The route starts with encoded states and correction, then follows Pauli-weight moments into interaction and coupling bounds. It connects those bounds to syndrome readout, optimal gates through three physical errors on concatenated codes, sparse descriptions, and protected entanglers on fixed product codes.

## One educational anchor

The selected source is **John Preskill, _Quantum Information_, Chapter 7, “Quantum Error Correction”**, in the author-hosted prepublication draft updated March 2026. The [official course index](https://preskill.caltech.edu/ph229/index.html) links the [complete chapter](https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf). The repository links to that draft; it does not redistribute it.

The core reading is §§7.2–7.4 for exact correction, its interpretations, and distance; §§7.6–7.8 for classical linear codes and CSS codes; §§7.9–7.11 for code bounds, stabilizers, and the five-qubit code; and §7.17 for concatenation. This is a targeted route through one source. The research references remain attribution and comparison sources, rather than additional educational anchors.

Begin with the [Preskill-to-project bridge](PRESKILL_BRIDGE.md). It translates the source's notation and assumptions, including its stabilizer convention for $Y$, into the repository's Hermitian Pauli basis. Its worked example explains why correcting a fault need not correct the angle accumulated during a gate. The later sections supply the additional moment, readout, sparse-synthesis, and tensor-lifting steps needed for the final results. The [bibliography](../references/references.bib) records the source version under `Preskill2026QEC`.

## The 30-milestone route

The [milestone map](MILESTONES.md) defines exactly 30 understanding targets in two phases. Their allocation follows this project's proof dependencies.

| Phase | Milestones | Direction |
|---|---|---|
| Background and preliminaries | M01–M12 | Encoded states and Pauli operators → correction and logical dynamics → twirls, resource definitions, and the proof framework |
| Narrative and innovation | M13–M30 | Moment bounds and the four-body example → the gate/readout tradeoff → optimal one-, two-, and three-error families → protected logical strings and the full resource comparison |

Within each phase, local facts come before the global argument they support. Each milestone states a central question, an understanding target, earlier dependencies, its role in the story, a conceptual connection, and pointers to the authoritative scientific account and relevant anchor or bridge sections.

## Reading routes

For the learning route, read the bridge alongside M01–M12, then follow M13–M30 into the linked scientific pages. Twelve background milestones assemble the common QEC and operator framework. Eighteen narrative milestones connect the successive constraints and constructions into the complete account. The allocation leaves specialist calculations in their canonical sources while keeping the final contributions visible.

For a direct research route, start with the [scientific overview](../science/README.md), then read the [model](../science/model.md), [locality proof](../science/locality.md), and [coupling argument](../science/coupling_cost.md). The [four-body construction](../science/four_body_construction.md) and [control analysis](../science/control_robustness.md) give the first exact example. The [gate/readout theorem](../science/gate_readout_tradeoff.md) leads to the concatenated families. The [all-depth three-error account](../science/growing_three_error_gates.md) and [protected logical strings](../science/protected_entangling_gates.md) complete the gate constructions; their sparse descriptions and finite certificates have separate resource statements.

The [verification guide](../verification/README.md) connects finite exact calculations to the claims they check. The universal theorem rests on its analytical proof; finite certificates establish the printed examples and specified identities. The [physical interpretation](../science/interpretation.md) and [related-work account](../references/RELATED_WORK.md) complete the scientific context.
