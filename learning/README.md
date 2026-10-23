# Learning Error-Transparent Locality

The central question is how demanding the same logical evolution before and after a correctable error constrains the physical Hamiltonian. The learning route starts with the meaning of a code and a correctable error, then follows the argument from Pauli-weight moments to a four-body construction and its control requirements.

## One educational anchor

The selected source is **John Preskill, _Quantum Information_, Chapter 7, “Quantum Error Correction”**, in the author-hosted prepublication draft updated March 2026. The [official course index](https://preskill.caltech.edu/ph229/index.html) links the [complete chapter](https://www.preskill.caltech.edu/ph219/chap7_26_6A.pdf). The repository links to that draft; it does not redistribute it.

The core reading is §§7.2–7.4 for exact correction, its interpretations, and distance; §§7.6–7.8 for classical linear codes and CSS codes; and §§7.9–7.11 for code bounds, stabilizers, and the five-qubit code. This is a targeted route through one source. The research references remain attribution and comparison sources, rather than additional educational anchors.

Begin with the [Preskill-to-project bridge](PRESKILL_BRIDGE.md). It translates the source's notation and assumptions, including its stabilizer convention for $Y$, into the repository's Hermitian Pauli basis. It also supplies the steps beyond the chapter that the locality, coupling, and control arguments need. The [bibliography](../references/references.bib) records the source version under `Preskill2026QEC`.

## The 30-milestone route

The [milestone map](MILESTONES.md) defines exactly 30 understanding targets in two phases. Their allocation follows this project's proof dependencies.

| Phase | Milestones | Direction |
|---|---|---|
| Background and preliminaries | M01–M13 | Encoded states and Pauli operators → correctability, distance, and code structure → logical evolution, resource definitions, and a complete model |
| Research narrative | M14–M30 | Exact transparency and weight moments → locality and coupling bounds → saturating examples and fault-time control → synthesis of the full result |

Within each phase, local facts come before the global argument they support. Each milestone states a central question, an understanding target, earlier dependencies, its role in the story, a conceptual connection, and pointers to the authoritative scientific account and relevant anchor or bridge sections.

## Reading routes

For the learning route, read the bridge alongside M01–M13, then follow M14–M30 into the linked scientific pages. Familiar material can be located through the map's dependency and source pointers.

For a direct research route, start with the [scientific overview](../science/README.md), then read the [model](../science/model.md), [locality proof](../science/locality.md), and [coupling argument](../science/coupling_cost.md). The [four-body construction](../science/four_body_construction.md) shows how the bounds are attained for one logical axis; the [control analysis](../science/control_robustness.md) explains what must remain true during a pulse.

The [verification guide](../verification/README.md) connects finite exact calculations to the claims they check. The universal theorem rests on its analytical proof; finite certificates establish the printed examples and specified identities. The [physical interpretation](../science/interpretation.md) and [related-work account](../references/RELATED_WORK.md) complete the scientific context.
