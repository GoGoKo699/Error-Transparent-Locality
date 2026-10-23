# Interaction order and the necessary coupling budget

Exact error transparency requires cancellations between different interaction weights. Those cancellations impose a cost even when every native interaction has the optimal maximum weight. The [locality proof](locality.md) supplies the moment identities; this page turns them into quantitative lower bounds on the sum of absolute Pauli coefficients.

The general bounds allow arbitrary logical dimension. Their energy scale is the logical half-splitting $\omega$, not the norm of the trace-free logical Hamiltonian. These quantities coincide for a logical qubit but need not coincide in higher dimension. The finite examples attain the bound at $(d,t,r)=(3,1,4)$ and $(3,1,5)$. Higher-error and larger-locality formulas below are necessary bounds, with physical attainability left open unless an explicit construction is given.

## 1. Assumptions and a scalar witness

Use the fixed code, detection distance $d\ge2t+1$, exact transparency condition, and native Pauli expansion from the [model](model.md). Consistent scalar error-sector shifts are allowed. Write

```math
H=\sum_{Q}h_QQ=\sum_wH_w,\qquad
J=\sum_{Q\ne I}|h_Q|,
\qquad
\omega=\frac{\lambda_{\max}(h_L)-\lambda_{\min}(h_L)}{2}>0.
\tag{C1}
```

Let $A_w=[V^\dagger H_wV]_0$ and $A=[h_L]_0$. The established identities are

```math
A_w=0\ (w<d),\qquad
\sum_w A_w=A,\qquad
\sum_w w^jA_w=0\ (1\le j\le t).
\tag{C2}
```

Choose normalized eigenvectors $|+\rangle,|-\rangle$ of $h_L$ for its largest and smallest eigenvalues. Define the real linear functional

```math
\ell(B)=\frac{\langle+|B|+\rangle-\langle-|B|-\rangle}{2}.
```

It annihilates scalars, satisfies $\ell(A)=\omega$, and obeys $|\ell(V^\dagger QV)|\le1$ for every Hermitian tensor Pauli $Q$. The last statement follows because each expectation of $Q$ lies in $[-1,1]$.

Set $a_w=\ell(A_w)/\omega$. Then

```math
\sum_w a_w=1,\qquad
\sum_w w^ja_w=0\quad(1\le j\le t),
\qquad
\frac{J}{\omega}\ge\sum_w|a_w|.
\tag{C3}
```

The identity Pauli has zero witness and does not contribute to either side. Nonidentity terms with scalar compression still consume budget; they cannot weaken this inequality.

## 2. The exact finite moment bound

Let $\mathcal S$ be a finite set of positive weights containing every weight that can contribute to the chosen logical witness. The code-independent choice is $\mathcal S=\{d,d+1,\ldots,r\}$. Knowledge of the code or the available native Pauli axes can give a smaller set.

Define

```math
B_t(\mathcal S)=
\min_{\{a_w\}}
\left\{\sum_{w\in\mathcal S}|a_w|:
\sum_{w\in\mathcal S}a_ww^j=\delta_{j0},\ 0\le j\le t\right\}.
\tag{C4}
```

Every Hamiltonian in the stated model obeys

```math
\boxed{J\ge B_t(\mathcal S)\,\omega.}
\tag{C5}
```

This is the strongest lower bound obtained from these scalar moments alone. It is a relaxation of physical Hamiltonian synthesis: a feasible collection of weight masses need not come from a code and an error-transparent Hamiltonian.

### Polynomial dual

Finite-dimensional linear-programming duality gives

```math
B_t(\mathcal S)=
\max_{p}\left\{p(0):\deg p\le t,
\ |p(w)|\le1\ \text{for every }w\in\mathcal S\right\}.
\tag{C6}
```

The elementary weak-duality calculation is already useful. For any feasible masses and polynomial,

```math
p(0)=\sum_w a_wp(w)\le\sum_w|a_w|.
```

Thus a polynomial and a signed mass distribution with equal values are an exact optimality certificate. If $|\mathcal S|\le t$, a polynomial of degree at most $t$ vanishing on $\mathcal S$ but not at zero proves that the moment constraints are infeasible. This recovers the requirement for at least $t+1$ contributing weights.

### A finite formula without a numerical optimizer

When $|\mathcal S|\ge t+1$, an optimal basic solution has exactly $t+1$ nonzero masses. To see this, split each mass into positive and negative variables. A basic solution has at most $t+1$ nonzero variables, and both signs at the same weight can be canceled to reduce cost. Fewer than $t+1$ support weights are impossible by the preceding annihilating-polynomial argument.

For ordered nodes $w_0<\cdots<w_t$ in $\mathcal S$, the unique moment solution is evaluation at zero of the Lagrange basis:

```math
a_{w_j}=\prod_{k\ne j}\frac{-w_k}{w_j-w_k},
\qquad \mathrm{sign}(a_{w_j})=(-1)^j.
```

Consequently,

```math
B_t(\mathcal S)=
\min_{\substack{\{w_0,\ldots,w_t\}\subset\mathcal S}}
\sum_{j=0}^t\prod_{k\ne j}\frac{w_k}{|w_j-w_k|}.
\tag{C7}
```

This exact finite formula is convenient for small certificates. It is not a claim that enumerating all subsets is an efficient algorithm for arbitrarily large parameter sets.

## 3. Closed cost at the minimum interaction order

**Theorem C1.** Suppose $r=d+t$. Then every logical weight component is fixed:

```math
\boxed{
A_{d+j}=\alpha_j A,\qquad
\alpha_j=(-1)^j
\frac{(d)_{t+1}}{(d+j)j!(t-j)!},
\quad 0\le j\le t,
}
\tag{C8}
```

where $(d)_{t+1}=d(d+1)\cdots(d+t)$. Therefore

```math
\boxed{
J\ge B_t(d,d+t)\,\omega,
\qquad
B_t(d,d+t)=\sum_{k=0}^t2^k\binom{d+k-1}{k}.
}
\tag{C9}
```

**Proof of the operator identities.** For any polynomial $f$ of degree at most $t$, (C2) implies $\sum_w f(w)A_w=f(0)A$. Taking $f$ to be the Lagrange polynomial equal to one at $d+j$ and zero at the other $t$ allowed weights gives (C8). This step holds for matrices of every logical dimension.

**Proof of the closed sum.** The unique scalar masses are the $\alpha_j$. A dual polynomial interpolating their signs on the allowed weights is

```math
p_t(x)=\sum_{k=0}^t(-2)^k\binom{x-d}{k},
```

where the binomial coefficient denotes its polynomial extension. At $x=d+j$, the binomial theorem gives $p_t(d+j)=(1-2)^j=(-1)^j$. It is therefore feasible on all allowed weights, and its value at zero equals the primal cost:

```math
\sum_j|\alpha_j|=p_t(0)
=\sum_{k=0}^t2^k\binom{d+k-1}{k}.
```

Applying the witness bound proves (C9). No physical construction is required for this necessary bound. ∎

### Growth with the number of protected faults

At the minimum detection distance $d=2t+1$ and minimum allowed interaction order $r=3t+1$, the first values are:

| Protected weight $t$ | Detection distance $d$ | Interaction order $r$ | Necessary $J/\omega$ |
|---:|---:|---:|---:|
| 1 | 3 | 4 | 7 |
| 2 | 5 | 7 | 71 |
| 3 | 7 | 10 | 799 |
| 4 | 9 | 13 | 9439 |

Only the first row is accompanied here by a saturating physical construction. The remaining rows constrain any construction if it exists at that interaction order.

The growth is exponential:

```math
B_t(2t+1,3t+1)
\sim\frac65\sqrt{\frac{3}{4\pi t}}
\left(\frac{27}{2}\right)^t.
\tag{C10}
```

To derive this, write the sum in (C9) as $\sum_{k=0}^t T_k$ with $T_k=2^k\binom{2t+k}{k}$. Its largest term is $T_t=2^t\binom{3t}{t}$. The backward ratio is $T_{k-1}/T_k=k/[2(2t+k)]\le1/6$, and each fixed number of steps from the top approaches ratio $1/6$. Dominated summation gives $\sum_kT_k/T_t\to\sum_{j\ge0}6^{-j}=6/5$. Stirling's formula for $\binom{3t}{t}$ gives (C10).

This identifies a cost of insisting on the smallest interaction order: increasingly large positive and negative logical contributions must cancel to leave the desired logical splitting. It does not imply that every larger-order design is inexpensive or physically realizable.

## 4. Allowing a larger interaction order

Write $B_t(d,r)=B_t(\{d,\ldots,r\})$.

### One protected error

For $t=1$ and $r>d$, the exact moment optimum is

```math
\boxed{B_1(d,r)=\frac{r+d}{r-d}.}
\tag{C11}
```

A matching primal witness uses only the endpoints,

```math
a_d=\frac{r}{r-d},\qquad
a_r=-\frac{d}{r-d},
```

and a dual witness is $p(x)=(r+d-2x)/(r-d)$. The line stays in $[-1,1]$ throughout the interval and has $p(0)=(r+d)/(r-d)$.

At $d=3$, the resulting lower bounds for $r=4,5,6,7$ are $7,4,3,5/2$. The present examples attain the first two values. Attainability at the other values is not established.

Equality at $r=4$ requires $A_3=4A$ and $A_4=-3A$. Equality at $r=5$ requires $A_3=(5/2)A$ and $A_5=-(3/2)A$, with no budget spent at weight four. These are two distinct resource optima, rather than an ordering of complete hardware implementations.

### Two protected errors

For $t=2$ and $r-d\ge2$, the exact discrete optimum is

```math
\boxed{
B_2(d,r)=1+\frac{2dr}{\lfloor(r-d)^2/4\rfloor}.
}
\tag{C12}
```

Let $m$ be either integer nearest $(d+r)/2$ and set $F=(m-d)(r-m)=\lfloor(r-d)^2/4\rfloor$. The three-node primal masses are

```math
\begin{aligned}
a_d&=\frac{mr}{(m-d)(r-d)},\\
a_m&=-\frac{dr}{(m-d)(r-m)},\\
a_r&=\frac{dm}{(r-d)(r-m)}.
\end{aligned}
```

They satisfy all three moment equations and have total absolute mass $1+2dr/F$. The matching quadratic is

```math
p(x)=1-\frac{2(x-d)(r-x)}{F}.
```

At every integer $w\in[d,r]$, the product $(w-d)(r-w)$ lies between zero and $F$, so $|p(w)|\le1$. Its value at zero is the same cost. When the interval width is odd, there are two nearest midpoint nodes; either gives a valid primal witness.

For example, $d=5$ gives moment costs $71,41,47/2,53/3$ at $r=7,8,9,10$. These are certified lower bounds, not a list of realized quantum gates.

### A simpler general bound

For arbitrary $t$, a readily evaluated dual witness is the Chebyshev polynomial

```math
p(x)=T_t\!\left(\frac{r+d-2x}{r-d}\right),
\qquad
B_t(d,r)\ge T_t\!\left(\frac{r+d}{r-d}\right).
\tag{C13}
```

It is bounded by one on the whole real interval. The exact discrete bound can be stronger because only integer Pauli weights constrain the polynomial. Formula (C7) or an exact primal/dual pair retains that discrete information.

## The five-qubit benchmark

The canonical protected Hamiltonian is established prior work. In particular, [Young, Sarovar, and Blume-Kohout (2013), Eq. (22) and Appendix A.1](https://arxiv.org/html/1307.5893v3) construct the syndrome-independent logical operators used here. The purpose of this benchmark is to put that known construction on the same native coupling scale and show that it saturates (C11). Its existence is not a new result.

Take the standard five-qubit code with positive generators

```math
S_1=IXZZX,\quad S_2=XIXZZ,\quad
S_3=ZXIXZ,\quad S_4=ZZXIX,
```

and logical representatives $L_X=XXXXX$, $L_Y=YYYYY$, and $L_Z=ZZZZZ$. Let $\mathcal G$ be the signed stabilizer group and $P=\frac1{16}\sum_{S\in\mathcal G}S$. The sixteen errors $\mathcal E=\{I,X_i,Y_i,Z_i\}$ have distinct syndromes, and their rank-two images partition the full 32-dimensional Hilbert space.

For any one of these logical axes, the canonical Hamiltonian is

```math
H_L^{\rm can}=\sum_{E\in\mathcal E}ELPE.
\tag{C14}
```

Orthogonality of the error images immediately gives $H_L^{\rm can}EP=ELP$. Since the images fill the full Hilbert space, $(H_L^{\rm can})^2=I$ as well. Thus its logical half-splitting and its full operator norm are both one, even though its native Pauli coefficient budget is larger.

Expanding $P$ and using the single-error twirl gives the exactly normalized expression

```math
H_L^{\rm can}
=\sum_{S\in\mathcal G}\left(1-\frac{\mathrm{wt}(LS)}{4}\right)LS.
\tag{C15}
```

Each nontrivial logical Pauli coset contains ten weight-three and six weight-five representatives. The coefficients in these **signed coset coordinates** are therefore $+1/4$ and $-1/4$, respectively. Consequently,

```math
(H_L^{\rm can})_3P=\frac52LP,\qquad
(H_L^{\rm can})_5P=-\frac32LP,
\qquad J=\frac{10+6}{4}=4.
\tag{C16}
```

At $d=3,r=5$, (C11) says $J\ge4\omega$. The known five-qubit Hamiltonian attains that lower bound. For the displayed choice $L=L_Z$, all sixteen **bare Hermitian Pauli coefficients** are $-1/4$; the ten cubic bare words act as minus $L_Z$ on the code. The machine-readable certificate records both conventions explicitly, avoiding a sign ambiguity when reproducing the Hamiltonian.

The same finite certificate verifies the canonical $X$, $Y$, and $Z$ axes separately. The four-body construction in this repository establishes only its specified logical axis; this comparison does not extend its gate set.

| Resource at unit logical half-splitting | Nine-qubit construction | Canonical five-qubit benchmark |
|---|---:|---:|
| Physical data qubits during the gate | 9 | 5 |
| Maximum Pauli weight | 4 | 5 |
| Absolute native coupling sum $J$ | 7 | 4 |
| Nonzero Pauli terms for the compared axis | 9 | 16 |
| Cubic logical contribution | $4L$ | $(5/2)L$ |
| Highest-weight logical contribution | $-3L$ | $-(3/2)L$ |
| Saturates its coupling lower bound | Yes | Yes |

Both columns assume their required native interactions are available and preserve the transparency conditions throughout the gate. The comparison charges maximum interaction order, total strength, term count, and data-qubit count separately. Neither column is declared preferable for every hardware platform. In particular, neither the operator norm nor commuting ideal terms can be substituted for the stated native coupling budget.

## 5. Code-specific obstructions to saturation

The moment bound is necessary. Code structure and the full error-sector identities can prevent its saturation.

First, missing logical weights strengthen the moment problem. The five-qubit code has only weights three and five in its three nontrivial logical Pauli cosets. At maximum weight four it therefore has only one possible nontrivial weight component, and the first-moment identity forbids a nonzero transparent generator. At weight five the two available weights produce exactly the endpoint solution in (C16). The nine-qubit construction instead supplies both cubic and quartic logical representatives.

Second, the dual polynomial gives a precise equality condition. Put $f_Q=\ell(V^\dagger QV)$. For an optimal dual polynomial $p$,

```math
\omega p(0)=\sum_Qh_Q f_Qp(\mathrm{wt}(Q))\le J.
```

If equality holds, every nonidentity Pauli with a nonzero coefficient must satisfy

```math
|f_Q|=1,\qquad |p(\mathrm{wt}(Q))|=1,
\qquad h_Qf_Qp(\mathrm{wt}(Q))>0.
\tag{C17}
```

Terms with scalar or zero logical witness cannot consume any budget in a saturating Hamiltonian. For an encoded qubit with a stabilizer logical Pauli as the target, $|f_Q|=1$ means that $Q$ belongs to that logical Pauli's stabilizer coset. Its coefficient sign must match both its literal coset sign and the dual contact sign.

For the single-error interval bound, the dual line touches magnitude one only at weights $d$ and $r$. Thus saturation requires the target coset to furnish both endpoint weights, and all budget must be spent there. This condition is not sufficient: the signed coefficients must also satisfy every full identity $HEV=EVh_L$ (or the allowed scalar-shift version). An optimal solution of the scalar moment LP alone is not a quantum construction.

## 6. Exact certificates and interpretation

The finite moment certificates use rational Lagrange masses and rational dual polynomials. Their verification checks the complete moment equations, every dual inequality on the allowed finite weight set, and equality of primal and dual values. They require no floating-point optimizer. The five-qubit certificate checks full Pauli-polynomial operator products, projector orthogonality and completeness, code distance, every relevant error identity, and $(H_L^{\rm can})^2=I$.

The universal inequalities are proved above. The finite certificates document specific instances and normalizations; they do not replace the proof or imply unrestricted attainability. Exact file locations and commands are listed in [Verification](../verification/README.md).

For a common-envelope implementation of a fixed axis, the bound also limits the integrated native strength needed for a specified logical rotation parameter. This is a statement within the generator model. Circuit compilation, changing encodings, ancillary gadgets, measurements during the gate, and imperfect recovery have separate resource and fault models. The [control analysis](control_robustness.md) explains why matching only the final ideal unitary does not preserve the unknown-fault-time guarantee.
