# Exact verification

The universal interaction-order and coupling bounds are proved in the [scientific account](../science/README.md). These scripts independently certify the finite constructions, their normalizations, representative moment optima, and the control identities used in that account. All arithmetic is integer, rational, or complex rational. There are no numerical tolerances, sampled quantum trajectories, external packages, or optimization-solver dependencies.

## Run the complete certificate suite

From the repository root, using Python 3.10 or later:

```bash
python verification/run_all.py
```

The command runs eleven scientific checks and compares their JSON output with the committed records. It reads files without modifying them. Assertions are part of the checks; do not disable them with `-O` or `PYTHONOPTIMIZE`.

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
| [verify_gate_readout_tradeoff.py](verify_gate_readout_tradeoff.py) | Complete stabilizer/centralizer enumeration for the nine-qubit, five-qubit, and fixed-ancilla codes; exact support-collision distances, a four-site logical-$Z$ circuit, all fourteen proper subwords, rational transparency identities, and the $p_4$ polynomial | [verify_gate_readout_tradeoff.json](results/verify_gate_readout_tradeoff.json) |
| [verify_readout_safe_family.py](verify_readout_safe_family.py) | All three axes of the five- and twenty-five-qubit equality construction; signed stabilizer elimination, exact local-axis counts and full single-error identities; recursive resources through depth four; a two-error counterexample | [verify_readout_safe_family.json](results/verify_readout_safe_family.json) |
| [verify_sparse_gates.py](verify_sparse_gates.py) | Closed 75-term twenty-five-qubit gates on all three axes; exact recursive sparse gates through depth three; independent signed membership, shift symmetries, coefficient bounds and full error-image identities | [verify_sparse_gates.json](results/verify_sparse_gates.json) |
| [verify_two_error_gates.py](verify_two_error_gates.py) | Every Pauli error of weight at most two on all three axes; complete contributing block-pattern classification; exact primal/dual block-moment certificates; 2,575-term sparse optimal gates | [verify_two_error_gates.json](results/verify_two_error_gates.json) |
| [verify_growing_two_error.py](verify_growing_two_error.py) | All-depth polynomial response identities; frontier-padding probability recursion; growing block-moment primal/dual certificates; independent 125-qubit support and error-label classification | [verify_growing_two_error.json](results/verify_growing_two_error.json) |
| [verify_two_error_synthesis.py](verify_two_error_synthesis.py) | Positive 25-qubit class profiles; exact unequal pairwise coupling and recursive profiles; actual depth-two reference compilation; every signed term and all protected-error responses of the 69,125-term 125-qubit gate on all three axes | [Sparse synthesis certificate](results/verify_two_error_synthesis.json) |

The two nine-qubit verifiers use different representations. The full projector check multiplies signed Pauli polynomials. The CSS check reconstructs the binary spaces and diagonal energies directly from the printed support lists. Agreement checks both the physical operator statement and the simpler cancellation mechanism.

The [joint gate/readout theorem](../science/gate_readout_tradeoff.md) is supported by a standalone comparison script also included in the companion repository. Direct enumeration gives 2,848 support-collision pairs and $r_S=4$ for the nine-qubit code. The five-qubit code and its fixed-ancilla extension have zero collisions and $r_S=\infty$. The latter has a weight-four logical with a proper stabilizer subword, checking why arbitrary even logical weight is insufficient. The script verifies the complementary syndrome pairing and the polynomial $p_4(q)=3q^2-2q^3$ algebraically; the optimal-recovery interpretation follows from the written even-circuit theorem, not a numerical optimization.

The [concatenated equality family](../science/minimum_readout_safe_gates.md) has a separate exact certificate. At depth two, it expands all 28,000 terms for each of three axes, verifies every term's signed logical-coset membership using phase-aware binary elimination, and checks all 76 identity/single-Pauli intertwiners per axis. The two classes have 10,000 weight-nine and 18,000 weight-eleven terms, with single-error responses $13/25$ and $31/75$. The combination with masses $11/2$ and $-9/2$ has logical rate one and $J=10$. Direct enumeration for $X_1X_2$ on the logical-$Z$ Hamiltonian instead gives rate $1/5$, verifying the single-error scope. Recursive integer/rational checks extend through depth four; the arbitrary-depth distance, reversibility, and gate claims are proved in the scientific account.

The [sparse construction](../science/sparse_protected_gates.md) has an exact standard-library generator, [sparse_pauli.py](sparse_pauli.py), and a separate verifier. The generator couples finite seed distributions, reduces three- and four-dimensional integer count vectors with rational arithmetic, then expands cyclic translation orbits. It avoids the dense Pauli list and numerical optimization. The verifier checks the closed 75-term form from [sparse_25_qubit.json](data/sparse_25_qubit.json) for every axis, with bare coefficients $2/25$, $7/50$, and $9/50$. It also checks the general recursion through depths one, two, and three, independently verifies coordinate-shift automorphisms of the signed code, and certifies every no-error/single-Pauli intertwiner and the rational denominator bounds. Term count, coefficient complexity, and physical interaction synthesis remain separate resources.

The [two-error account](../science/two_error_gates.md) has independent factorized and explicit sparse checks. The main program constructs the signed five-qubit group using literal Pauli multiplication, exhausts its 1,024 physical labels to classify every inner normalizer, and checks all 2,776 protected errors on each of three axes. Its four-class moment matrix has unique masses $143/8,-117/4,243/16,-45/16$; the exact dual row $(521/8,-12,1/2,1/8)$ proves the refined coupling certificate. The helper [two_error_sparse.py](two_error_sparse.py) independently expands [103 stored cyclic-orbit seeds](data/two_error_sparse_orbits.json) into 2,575 terms per axis, checks every signed full-code logical membership, and evaluates all protected error responses using integer contractions over a common denominator. The stored sparse coefficients have a 125-bit common denominator; no numerical optimizer is required to reproduce the certificate.

The [growing two-error theorem](../science/growing_two_error_gates.md) is checked at three levels. Exact polynomial arithmetic verifies the response cancellations and coupling formula for arbitrary active-block count. Rational hierarchy calculations through depths two to six check every first-divergence category and the block-moment dual. Independent enumeration of all 10,000 depth-three support trees confirms active/padding correlations and detects the failure of uniform inactive-leaf padding. Finally, the script enumerates and classifies all 70,126 weight-at-most-two physical error labels on 125 qubits. This last check establishes category coverage; it is not a dense native-Pauli expansion or a large Hilbert-space matrix calculation. Full error-image transparency at all depths follows from the signed-coset construction and the written probability proof.

The [sparse two-error synthesis](../science/sparse_two_error_synthesis.md) has a separate [exact verifier](verify_two_error_synthesis.py). It expands all 69,125 terms for each logical axis and checks their actual signed logical-coset memberships. Exact bitset correlations check 562 translation-orbit equations; independent coverage assigns all 70,126 protected physical errors to these orbits. Literal site-by-site character sums cross-check the bitset formula. The verifier also checks every positive 25-qubit class profile, rational pairwise marginal and tensor-response identities with unequal 127-bit denominators, the recursive class profiles through depth six, and an actual depth-two reference compilation. The explicit 125-qubit coefficients have a 1,458-bit common denominator. Reproducing the certificate requires no numerical optimizer.

## Data and conventions

[nine_qubit.json](data/nine_qubit.json) contains the positive stabilizer generators, logical representatives, nine literal Hamiltonian terms, and binary supports of the CSS code. Site indices are one-based. The leftmost character of a Pauli or binary word is site one. The Hamiltonian term order matches the table in [the construction](../science/four_body_construction.md).

Every coefficient multiplies a **bare Hermitian tensor Pauli** with eigenvalues $\pm1$. A signed stabilizer-coset representative can have an additional minus sign. The five-qubit certificate records both coordinates explicitly; they must not be interchanged. In particular, its displayed logical $Z$ benchmark has sixteen bare coefficients equal to $-1/4$, even though ten signed-coset coefficients are $+1/4$.

The control certificate records the support associated with every matrix column and the optimal order as both support lists and indices. Its exact phase checks compare symbolic exponent coefficients for arbitrary total angle, rather than evaluating floating-point complex exponentials.

The full output records are deliberately committed alongside the scripts so that a reader can inspect the result without executing code and can detect a change in the reproduced certificate. They contain no random seeds or machine-dependent timestamps.

## What these checks do not establish

Finite certificates do not prove the universal theorem; its proof uses the Pauli twirl and a polynomial argument. Feasibility of a scalar moment problem does not establish a physical code or Hamiltonian attaining it. The checks also do not establish hardware synthesis cost, recovery-device fault tolerance, minimal block size, a universal four-body gate set, or experimental performance.
