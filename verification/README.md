# Exact verification

The universal interaction-order and coupling bounds are proved in the [scientific account](../science/README.md). These scripts independently certify the finite constructions, their normalizations, representative moment optima, and the control identities used in that account. All arithmetic is integer, rational, or complex rational. There are no numerical tolerances, sampled quantum trajectories, external packages, or optimization-solver dependencies.

## Run the complete certificate suite

From the repository root, using Python 3.10 or later:

```bash
python verification/run_all.py
```

The command runs five scientific checks and compares their JSON output with the committed records. It reads files without modifying them. Assertions are part of the checks; do not disable them with `-O` or `PYTHONOPTIMIZE`.

An individual script prints its full certificate, for example:

```bash
python verification/five_qubit.py
```

## Checks and their meaning

| Script | What is certified | Recorded result |
|---|---|---|
| [nine_qubit_projector.py](nine_qubit_projector.py) | The 256-element signed stabilizer group, a two-dimensional code, distance three, all 28 full identities $HEP=E\overline ZP$, and the weight-three/four logical contributions | [nine_qubit_projector.json](results/nine_qubit_projector.json) |
| [nine_qubit_css.py](nine_qubit_css.py) | An independent binary CSS derivation, all low-weight normalizers, literal logical-coset signs, sitewise cancellation, and 320 exact energy-plateau checks | [nine_qubit_css.json](results/nine_qubit_css.json) |
| [five_qubit.py](five_qubit.py) | The established canonical construction for each of three logical axes, all 48 full error identities, orthogonal and complete syndrome projectors, exact Pauli coefficients, and $H_L^2=I$ | [five_qubit.json](results/five_qubit.json) |
| [moment_bounds.py](moment_bounds.py) | Fifteen finite rational certificates: all moment constraints, all allowed-weight dual inequalities, matching primal and dual values, and one infeasibility witness | [moment_bounds.json](results/moment_bounds.json) |
| [control.py](control.py) | Incidence rank eight and its one-dimensional kernel, 19,008 exact phase-exponent identities, the sequencing counterexample, and an optimal pulse-order certificate over all 512 subsets | [control.json](results/control.json) |

The two nine-qubit verifiers use different representations. The full projector check multiplies signed Pauli polynomials. The CSS check reconstructs the binary spaces and diagonal energies directly from the printed support lists. Agreement checks both the physical operator statement and the simpler cancellation mechanism.

## Data and conventions

[nine_qubit.json](data/nine_qubit.json) contains the positive stabilizer generators, logical representatives, nine literal Hamiltonian terms, and binary supports of the CSS code. Site indices are one-based. The leftmost character of a Pauli or binary word is site one. The Hamiltonian term order matches the table in [the construction](../science/four_body_construction.md).

Every coefficient multiplies a **bare Hermitian tensor Pauli** with eigenvalues $\pm1$. A signed stabilizer-coset representative can have an additional minus sign. The five-qubit certificate records both coordinates explicitly; they must not be interchanged. In particular, its displayed logical $Z$ benchmark has sixteen bare coefficients equal to $-1/4$, even though ten signed-coset coefficients are $+1/4$.

The control certificate records the support associated with every matrix column and the optimal order as both support lists and indices. Its exact phase checks compare symbolic exponent coefficients for arbitrary total angle, rather than evaluating floating-point complex exponentials.

The full output records are deliberately committed alongside the scripts so that a reader can inspect the result without executing code and can detect a change in the reproduced certificate. They contain no random seeds or machine-dependent timestamps.

## What these checks do not establish

Finite certificates do not prove the universal theorem; its proof uses the Pauli twirl and a polynomial argument. Feasibility of a scalar moment problem does not establish a physical code or Hamiltonian attaining it. The checks also do not establish hardware synthesis cost, recovery-device fault tolerance, minimal block size, a universal four-body gate set, or experimental performance.
