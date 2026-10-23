# A four-body logical rotation attaining both bounds

This construction encodes one qubit into nine and corrects arbitrary single-qubit errors. Four three-body and five four-body commuting Pauli terms implement a logical $Z$ rotation without timing distortion from a protected fault. The terms simultaneously attain the [interaction-order bound](locality.md) and the [coupling bound](coupling_cost.md).

Use one-based site indices and write $Z_{346}=Z_3Z_4Z_6$, with identities on the other sites; use the same convention for $X$. All coefficients below multiply literal Hermitian Pauli words, without hidden stabilizer-product phases.

## 1. The CSS code

Take the simultaneous $+1$ eigenspace of the following eight generators:

| $X$ stabilizers | $Z$ stabilizers |
|---|---|
| $X_{59}$ | $A=Z_{148}$ |
| $X_{1246}$ | $B=Z_{268}$ |
| $X_{1347}$ | $C=Z_{378}$ |
| $X_{23458}$ | $D=Z_{23459}$ |

The four $X$ checks and four $Z$ checks are separately independent, and their binary support row spaces are orthogonal. The generators therefore commute and leave a two-dimensional code. Logical representatives are

```math
\overline X=X_{145},\qquad \overline Z=Z_{346}.
\tag{F1}
```

They commute with every generator and anticommute with each other.

### Distance and degeneracy

The $Z$ check column at a site is the syndrome of its $X$ error; the $X$ check column is the syndrome of its $Z$ error. In the row order above these columns are

| Site | $Z$ check column | $X$ check column |
|---:|:---:|:---:|
| 1 | 1000 | 0110 |
| 2 | 0101 | 0101 |
| 3 | 0011 | 0011 |
| 4 | 1001 | 0111 |
| 5 | 0001 | 1001 |
| 6 | 0100 | 0100 |
| 7 | 0010 | 0010 |
| 8 | 1110 | 0001 |
| 9 | 0001 | 1000 |

Every column is nonzero. The $X$ check columns are all distinct. The only repeated $Z$ check column occurs at sites five and nine. A Pauli normalizer of weight at most two must therefore be the identity or $X_5X_9$, and the latter is a stabilizer. Mixed $X/Z$ support cannot evade the two independent syndrome tests. There is no nontrivial logical operator of weight one or two, while (F1) gives weight-three logical operators. The code has parameters $[[9,1,3]]$.

The code is degenerate: $X_5$ and $X_9$ have the same encoded action up to their stabilizer product. Nondegeneracy is not needed for correction or for the locality theorem.

## 2. The Hamiltonian

Define

```math
\begin{aligned}
H_\star={}&Z_{346}+Z_{167}+\frac32Z_{589}+\frac12Z_{123}\\
&-\frac12Z_{2569}-Z_{1368}-\frac12Z_{4678}
-\frac12Z_{1459}-\frac12Z_{3579}.
\end{aligned}
\tag{F2}
```

All nine terms commute globally. Each term is a positive representative of the same logical $Z$:

| Pauli term | Coefficient $c_S$ | Pauli term equals $\overline Z$ times |
|---|---:|---|
| $Z_{346}$ | $1$ | $I$ |
| $Z_{167}$ | $1$ | $AC$ |
| $Z_{589}$ | $3/2$ | $BD$ |
| $Z_{123}$ | $1/2$ | $AB$ |
| $Z_{2569}$ | $-1/2$ | $D$ |
| $Z_{1368}$ | $-1$ | $A$ |
| $Z_{4678}$ | $-1/2$ | $C$ |
| $Z_{1459}$ | $-1/2$ | $ABD$ |
| $Z_{3579}$ | $-1/2$ | $BCD$ |

This table proves $Z_SP=\overline ZP$ for every displayed support. The coefficient sum is one, giving $H_\star P=\overline ZP$.

## 3. Sitewise cancellation proves full transparency

The essential second identity is

```math
\sum_{S\ni i}c_S=0\qquad\text{for every site }i=1,\ldots,9.
\tag{F3}
```

The positive and absolute negative coefficient masses incident on the sites are equal component by component. Their common vector is

```math
\left(\frac32,\frac12,\frac32,1,\frac32,2,1,\frac32,\frac32\right).
```

Conjugating by $X_i$ reverses exactly the $Z$ terms containing $i$. Hence

```math
X_iH_\star X_iP
=\left(\sum_Sc_S-2\sum_{S\ni i}c_S\right)\overline ZP
=\overline ZP.
```

Multiplication by $X_i$ gives $H_\star X_iP=X_i\overline ZP$. The same signs arise for $Y_i$, while every $Z_i$ commutes with $H_\star$. Thus

```math
\boxed{H_\star EP=E\overline ZP}
\quad(E=I,X_i,Y_i,Z_i).
\tag{F4}
```

The derivation establishes a full physical-space equality. It includes preservation of the relevant error images, rather than only their projected logical energies.

For $H(t)=g(t)H_\star$ and $\Theta=\int_0^Tg(t)\,dt$, a single protected fault at any time obeys

```math
U(T,\tau)EU(\tau,0)P
=Ee^{-i\Theta\overline Z}P.
```

An ideal recovery at the end returns the intended rotation. Linearity covers arbitrary single-qubit error operators and their channel Kraus representations.

## 4. Saturated resources

The cubic coefficients add to four and the quartic coefficients to minus three:

```math
(H_\star)_3P=4\overline ZP,
\qquad (H_\star)_4P=-3\overline ZP.
```

Their total absolute sum is seven. Scaling by $\Omega$ gives logical half-splitting $|\Omega|$, maximum interaction order four, and $J=7|\Omega|$. This saturates both general bounds in the $d=3,t=1,r=4$ case.

## 5. Energy plateaus and quantum coherence

Let $\mathcal C\subset\mathbb F_2^9$ be the kernel of the four $Z$ check rows, and let $\mathcal D\subset\mathcal C$ be the row space of the four $X$ checks. They have sizes 32 and 16. A logical basis is

```math
|0_L\rangle=\frac14\sum_{b\in\mathcal D}|b\rangle,
\qquad |1_L\rangle=X_{145}|0_L\rangle.
```

Their computational supports partition $\mathcal C$. On each support word every monomial in (F2) has the same sign as $\overline Z$. The incidence identities make the energy unchanged by flipping any one bit. The diagonal Hamiltonian therefore has an energy plateau of $+1$ around the support of $|0_L\rangle$ and another of $-1$ around the support of $|1_L\rangle$, each including all radius-one neighbors.

A bit or $Y$ fault moves amplitude within a plateau, preserving the accumulated logical phase. A $Z$ fault changes relative computational phases and commutes with the gate. The CSS coherence and the quantum distance condition are what make this classical energy description compatible with correction of the full single-qubit Pauli set.

## 6. Control requirements and reproduction

The terms must act concurrently, or their coefficients must preserve the necessary cancellations at every instant. Global commutation alone does not protect a sequential implementation. The [control analysis](control_robustness.md) derives the exact residual logical angle when the incidence conditions are imperfect and shows why a correct final pulse area is insufficient.

The established gate family is rotation about this one logical axis. The locality and coupling optimality statements do not assert a minimal number of qubits, a minimal number of terms, a universal four-body gate set, or a complete hardware advantage.

The machine-readable construction and independent exact projector verification are documented in [Verification](../verification/README.md). No floating-point tolerance is used to certify (F4), the stabilizer dimension, or the code distance.
