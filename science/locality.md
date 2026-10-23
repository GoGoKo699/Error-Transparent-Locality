# Error moments impose an interaction-order bound

The assumptions and resource definitions are in the [model](model.md). The central observation is that exact error transparency cancels the first several moments of the interaction weight after logical compression. Code distance removes the low-weight terms. Polynomial interpolation then turns these two facts into a lower bound.

## 1. Logical weight components

Write $H=\sum_w H_w$. For a logical operator $B$, define its scalar-free part by $[B]_0=B-\mathrm{tr}(B)I_K/K$. Let

```math
A_w=[V^\dagger H_wV]_0,
\qquad A=[h_L]_0=\sum_w A_w.
\tag{L1}
```

Nontrivial logical evolution means $A\ne0$. Detection distance gives

```math
A_w=0\qquad(w\lt d).
\tag{L2}
```

The terms $H_w$ need not preserve the code separately. Only their compressed scalar-free parts appear in the argument; the complete Hamiltonian obeys the full transparency condition.

## 2. The Pauli-weight superoperator

For each physical qubit define the complete Pauli twirl on observables,

```math
\mathcal R_i(B)=\frac14\left(B+X_iBX_i+Y_iBY_i+Z_iBZ_i\right),
\qquad
\mathcal W=\sum_{i=1}^n(\mathrm{Id}-\mathcal R_i).
\tag{L3}
```

If a tensor Pauli has identity at site $i$, $\mathcal R_i$ leaves it unchanged; otherwise the twirl sends it to zero. Thus every Pauli of weight $w$ is an eigenoperator of $\mathcal W$ with eigenvalue $w$, and

```math
\mathcal W^j(H)=\sum_w w^j H_w.
\tag{L4}
```

Each factor in $\mathcal W$ is a linear combination of the identity map and one-site Pauli conjugations. Expanding $\mathcal W^j$ gives a real linear combination of maps $B\mapsto E^\dagger BE$ with $\mathrm{wt}(E)\le j$. Repeated sites can reduce that weight. Pauli product phases cancel in conjugation. The expansion coefficients sum to zero for $j\ge1$, because every conjugation fixes $I$ whereas $\mathcal W^j(I)=0$.

From transparency, including the allowed scalar shifts,

```math
V^\dagger E^\dagger HEV=h_L+\lambda_E I_K.
```

Consequently the scalar-free compression of $\mathcal W^j(H)$ vanishes for $1\le j\le t$. This proves the moment identities

```math
\boxed{\sum_w w^j A_w=0,\qquad j=1,\ldots,t.}
\tag{L5}
```

This is an algebraic use of a depolarizing twirl, not an instruction to apply noise to the computer. Equivalently, the scalar-free compression of $e^{-s\mathcal W}(H)$ has its first $t$ derivatives at $s=0$ equal to zero. Different interaction weights decay at different rates under this mathematical map; exact transparency requires their logical responses to cancel.

## 3. General locality theorem

**Theorem L1.** Let a fixed code of detection distance $d$ carry a Hermitian, code-preserving Hamiltonian that is transparent to every Pauli of weight at most $t$, allowing consistent scalar sector shifts as in (M2). If its logical action is nontrivial, its maximum interaction order satisfies

```math
\boxed{r\ge d+t.}
\tag{L6}
```

**Proof.** If $r\lt d$, equation (L2) already makes $A=0$. Otherwise suppose $d\le r\lt d+t$ and form

```math
q(x)=\prod_{a=d}^{r}\left(1-\frac{x}{a}\right).
```

The polynomial has degree at most $t$, constant coefficient one, and a zero at every integer weight where $A_w$ can be nonzero. Expanding it and applying (L5) gives

```math
\sum_w q(w)A_w=\sum_w A_w=A.
```

But each summand on the left vanishes, either by (L2) or by a root of $q$. Hence $A=0$, a contradiction. ∎

For correction of every error on at most $t$ qubits, $d\ge2t+1$ yields the immediate consequence $r\ge3t+1$. The result is independent of the number of physical qubits and the number of Hamiltonian terms.

For a time-dependent fixed-code protocol satisfying the transparency condition at every instant, the same proof applies at each time when the logical generator is nontrivial. It does not constrain a general circuit whose intermediate states leave the fixed code or whose error correction changes the relevant generator.

## 4. The single-error case in one equation

When $t=1$, summing over the three nonidentity Paulis at every site gives the equivalent identity

```math
\sum_{i=1}^n\sum_{a=X,Y,Z} a_i H_w a_i=(3n-4w)H_w.
\tag{L7}
```

Transparency makes the scalar-free compression of the left-hand side equal to $3nA$. Therefore $\sum_w wA_w=0$. On a distance-three code, a Hamiltonian with only weights at most three would have $3A_3=0$ and hence no nontrivial logical action. At weight four the two equations are

```math
A_3+A_4=A,\qquad 3A_3+4A_4=0,
```

so necessarily

```math
A_3=4A,\qquad A_4=-3A.
\tag{L8}
```

The four-body construction achieves precisely this cancellation. The opposite signs are also the source of its unavoidable coupling cost.

## 5. Available weights can strengthen the bound

The proof uses distinct available weights, not their contiguity. If the only possible nonzero logical components lie at positive weights in a finite set $\mathcal S$, and $|\mathcal S|\le t$, then

```math
q(x)=\prod_{w\in\mathcal S}(1-x/w)
```

repeats the contradiction. A nontrivial transparent generator therefore needs at least $t+1$ distinct contributing weights.

For a specified stabilizer logical axis, physical Pauli terms in its stabilizer coset compress to that axis; Paulis outside the normalizer have zero compression. Restricting the available coset weights can thus strengthen the code-independent bound. The five-qubit benchmark has logical coset weights three and five, so it cannot use the four-body equality mechanism. The nine-qubit construction has both three- and four-body representatives of its logical $Z$.

The [coupling analysis](coupling_cost.md) extracts quantitative consequences of the same moments. The finite scripts verify coefficient identities and the explicit examples; the universal theorem is established by the argument above, not by enumeration of small codes.
