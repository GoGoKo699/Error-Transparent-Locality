# Control errors and faults during a pulse

For the [nine-term CSS construction](four_body_construction.md), the logical effect of a coefficient error can be calculated exactly. The quantity that controls the additional phase from a physical fault is the remaining signed coupling area incident on the faulty qubit. A correct final logical angle alone does not determine this quantity.

This account assumes a fixed code, the specified nine commuting Pauli supports, at most one instantaneous physical Pauli fault, and final ideal recovery. The exact channel formulas below concern a classical distribution of fault locations and times whose probabilities are independent of the logical input. They do not assume that a coherent superposition of fault times can be replaced by that distribution.

## 1. Logical rate and residual site incidence

Write the controlled Hamiltonian as

```math
H(t)=\sum_{S\in\mathcal S}h_S(t)Z_S,
\qquad h_S(t)\in\mathbb R,
\tag{C1}
```

where $\mathcal S$ is the nine-support family in the construction. Coefficients may be piecewise continuous or, more generally, integrable on $[0,T]$. All terms commute at all times, and every term has the same encoded action:

```math
Z_SV=VZ.
```

Define the logical rate, the residual incidence at site $i$, and their integrated areas by

```math
\begin{aligned}
a(t)&=\sum_Sh_S(t),
& b_i(t)&=\sum_{S\ni i}h_S(t),\\
A&=\int_0^Ta(t)\,dt,
& B_i(\tau)&=\int_\tau^Tb_i(t)\,dt.
\end{aligned}
\tag{C2}
```

The realized no-fault logical gate is $U_A=e^{-iAZ}$. If the intended gate is $U_\Theta=e^{-i\Theta Z}$, its ordinary angle calibration error is

```math
\Delta A=A-\Theta.
```

The exponent angle is used throughout: $e^{-i\Theta Z}$ rotates a Bloch vector through angle $2\Theta$.

## 2. Exact phase after one fault and recovery

**Proposition.** A single $X_i$ or $Y_i$ fault at time $\tau$, followed by final ideal recovery, produces

```math
\boxed{U_{i,\tau}=e^{-i[A-2B_i(\tau)]Z}.}
\tag{C3}
```

A $Z_i$ fault produces $U_A$.

To prove the statement, let $E=X_i$ or $Y_i$. Conjugation changes the sign of exactly the terms incident on site $i$:

```math
EZ_SE=(-1)^{\mathbf 1_{i\in S}}Z_S,
\qquad H(t)EV=EV[a(t)-2b_i(t)]Z.
```

The logical generator is $a(t)Z$ before the fault and $[a(t)-2b_i(t)]Z$ afterwards. Integration gives the full physical-space identity

```math
U(T,\tau)EU(\tau,0)V
=EVe^{-i[A-2B_i(\tau)]Z}.
\tag{C4}
```

Ideal recovery removes $E$. For $Z_i$, every conjugation sign is positive. The degeneracy between $X_5$ and $X_9$ is consistent with this derivation: every displayed support contains both sites or neither, so $b_5=b_9$ for every allowed coefficient vector.

The residual unitary relative to the **realized no-fault gate** is $e^{+2iB_i(\tau)Z}$. Relative to the **intended gate**, write it as $e^{-i\delta_i(\tau)Z}$ with

```math
\delta_i(\tau)=\Delta A-2B_i(\tau).
\tag{C5}
```

For a no-fault or $Z$ fault branch, $\delta=\Delta A$. Thus ordinary angle calibration and fault-dependent phase distortion are distinct contributions, with explicit signs.

For one deterministic branch, the entanglement infidelity, average gate infidelity, and diamond norm distance from the intended gate are

```math
\begin{aligned}
1-F_e&=\sin^2\delta,\\
1-F_{\mathrm{avg}}&=\frac23\sin^2\delta,\\
\|\mathcal U_{i,\tau}-\mathcal U_\Theta\|_\diamond
&=2|\sin\delta|.
\end{aligned}
\tag{C6}
```

The diamond norm convention here ranges from zero to two. A half-diamond distance is half the displayed quantity.

## 3. Unknown-time mixtures give an exact logical channel

For a classical distribution over the allowed branches, define

```math
\chi=\mathbb E[e^{-2i\delta}].
\tag{C7}
```

In the frame of the intended gate, the recovered channel preserves diagonal matrix elements and multiplies the off-diagonal element by $\chi$:

```math
\mathcal E_{\mathrm{rel}}(\rho)
=\begin{pmatrix}
\rho_{00}&\chi\rho_{01}\\
\chi^*\rho_{10}&\rho_{11}
\end{pmatrix}.
\tag{C8}
```

Let $p_{\mathrm{nf}}$ be the combined probability of no fault or a $Z$ fault, and let $p_i(\tau)$ be the probability density of an $X_i$ or $Y_i$ branch. With $p_{\mathrm{nf}}+\sum_i\int_0^Tp_i(\tau)d\tau=1$,

```math
\chi=e^{-2i\Delta A}\left[
p_{\mathrm{nf}}+
\sum_i\int_0^Tp_i(\tau)e^{4iB_i(\tau)}\,d\tau
\right].
\tag{C9}
```

The resulting metrics are exact:

```math
F_e=\frac{1+\mathrm{Re}\,\chi}{2},
\qquad
1-F_{\mathrm{avg}}=\frac{1-\mathrm{Re}\,\chi}{3},
\qquad
\|\mathcal E_{\mathrm{rel}}-\mathrm{Id}\|_\diamond=|1-\chi|.
\tag{C10}
```

For the last identity, the difference map has zero diagonal action and off-diagonal multiplier $\chi-1$. Up to a $Z$ rotation it is $|\chi-1|(\mathrm{Id}-\mathrm{Ad}_Z)/2$. Its diamond norm is $|\chi-1|$, attained on the state $|+\rangle$.

As an example, take constant incidence error $b_i(t)=\beta_i$ and condition on an $X_i$ or $Y_i$ fault with uniform time in $[0,T]$. Then

```math
\chi=e^{-2i\Delta A}e^{2i\beta_iT}\mathrm{sinc}(2\beta_iT),
\qquad \mathrm{sinc}(x)=\frac{\sin x}{x}.
\tag{C11}
```

At $\Delta A=0$ this gives

```math
1-F_e=\frac{1-\mathrm{sinc}(4\beta_iT)}2
=\frac43(\beta_iT)^2+O((\beta_iT)^4).
```

The complex number $\chi$ retains both the coherent phase and the dephasing caused by the unknown time.

## 4. Which coefficient changes preserve transparency?

Let $M_{iS}=\mathbf 1_{i\in S}$ be the site-incidence matrix and $c$ the coefficient vector of $H_\star$. Then $Mc=0$ and $\mathbf 1^Tc=1$.

For the **fixed nine supports**, $M$ has rank eight and

```math
\ker M=\mathrm{span}\{c\}.
\tag{C12}
```

For example, in the column order

```math
(346,167,589,123,2569,1368,4678,1459,3579),
```

the minor using the first eight rows and first eight columns has determinant $8$. The nonzero vector $c$ in the kernel completes the rank argument. This is a statement about this nine-dimensional control ansatz; it is not a classification of all four-local Hamiltonians on the code.

Consequently, the complete family of instantaneously transparent controls within this support is

```math
h_S(t)=g(t)c_S
\quad\text{for almost every }t,
\tag{C13}
```

with arbitrary real integrable common envelope $g$. Any pulse shape in this family remains transparent, and its area $\int_0^Tg(t)dt$ determines the logical angle. A common multiplicative calibration error therefore preserves transparency but can change the intended angle. Final error correction does not remove that logical overrotation.

For coefficient perturbations $h(t)=g(t)c+\epsilon(t)$,

```math
a(t)=g(t)+\mathbf 1^T\epsilon(t),
\qquad b(t)=M\epsilon(t).
\tag{C14}
```

The first expression is the ordinary logical-rate calibration error. The second determines the additional phase after a physical fault. A perturbation preserves transparency exactly when it remains in $\ker M$ almost everywhere. Requiring both $M\epsilon=0$ and $\mathbf 1^T\epsilon=0$ forces $\epsilon=0$ within this ansatz.

### An error invisible to every no-fault logical-angle test

Add the control perturbation

```math
\Delta H(t)=\epsilon_0(t)(Z_{346}-Z_{167}).
\tag{C15}
```

Both terms act as logical $Z$, so the no-fault logical Hamiltonian remains exactly unchanged at every instant. Nevertheless,

```math
b_3=b_4=\epsilon_0,
\qquad b_1=b_7=-\epsilon_0,
```

and the other incidences vanish. Equation (C3) then gives nonzero fault-dependent phases. Ordinary logical-angle calibration alone cannot certify the cancellation needed for error transparency.

## 5. Quantitative bounds for imperfect cancellation

Define the largest remaining incidence area

```math
B_{\max}=\max_i\sup_{0\le\tau\le T}|B_i(\tau)|.
```

Relative to the realized no-fault gate, every single-fault branch obeys

```math
1-F_e\le\min\{1,4B_{\max}^2\},
\qquad
\|\mathcal E-\mathcal U_A\|_\diamond
\le\min\{2,4B_{\max}\}.
\tag{C16}
```

The same bounds hold for classical mixtures. Against the intended gate, the corresponding bounds are

```math
1-F_e\le\min\{1,(|\Delta A|+2B_{\max})^2\},
\qquad
\|\mathcal E-\mathcal U_\Theta\|_\diamond
\le\min\{2,2|\Delta A|+4B_{\max}\}.
\tag{C17}
```

These estimates preserve the signed incidence cancellations. A simpler bound is

```math
B_{\max}\le\int_0^T\|M\epsilon(t)\|_\infty\,dt.
```

If the nominal envelope has the intended area, a direct total-target bound also follows from

```math
\delta_i(\tau)
=\int_0^\tau\sum_S\epsilon_S(t)\,dt
+\int_\tau^T\sum_S(1-2M_{iS})\epsilon_S(t)\,dt.
```

Thus $|\delta_i(\tau)|\le\eta_1$, where $\eta_1=\int_0^T\sum_S|\epsilon_S(t)|dt$. Every branch then has $1-F_e\le\min\{1,\eta_1^2\}$ and diamond distance at most $\min\{2,2\eta_1\}$. This last estimate bounds ordinary angle error and fault-dependent phase together.

For a perturbation outside the nine-term family, a conservative comparison remains available. Take a calibrated nominal envelope, $\int_0^Tg(t)dt=\Theta$, and let $H_{\mathrm{actual}}(t)=g(t)H_\star+V_{\mathrm{err}}(t)$. Duhamel's formula on the intervals before and after a fixed Pauli fault yields an operator-norm difference at most $\int_0^T\|V_{\mathrm{err}}(t)\|dt$ between actual and nominal faulty propagators. Encoding and the same final ideal recovery therefore give

```math
\|\mathcal E_{\mathrm{actual}}-\mathcal U_\Theta\|_\diamond
\le\min\left\{2,2\int_0^T\|V_{\mathrm{err}}(t)\|\,dt\right\}.
\tag{C18}
```

This estimate does not require the perturbation to preserve the code. It also holds for mixtures with the same fixed classical branch probabilities in both comparisons. The incidence formulas provide the more specific exact answer when the perturbation changes only the stated coefficients.

## 6. Sequential commuting pulses can fail maximally

Apply each Pauli term separately with its correct signed pulse area $\Theta c_S$. Since the terms commute, the resulting no-fault physical unitary is exactly the simultaneous one, and every site's total integrated incidence is zero.

Take $Z_{346}$ as the first pulse, with area $\Theta$, and place an $X_3$ or $Y_3$ fault immediately after it. The remaining incidence area is $B_3=-\Theta$, so the recovered logical angle is

```math
A-2B_3=3\Theta.
\tag{C19}
```

The residual rotation relative to the intended gate is $e^{-2i\Theta Z}$. At $\Theta=\pi/4$, it is a logical $Z$ error up to phase, with entanglement infidelity one and diamond distance two. Faults before or after the whole sequence are transparent, while an intermediate fault can fail maximally. This is not a product-formula approximation error: the no-fault product is exact.

### Why pointwise cancellation is necessary

Suppose every $X_i$ or $Y_i$ fault time gives the same logical channel as the realized no-fault gate. Equation (C3) requires $e^{2iB_i(\tau)Z}$ to be scalar, so

```math
B_i(\tau)\in\frac\pi2\mathbb Z
\quad\text{for every }\tau.
```

Integrability makes $B_i$ continuous, and $B_i(T)=0$. Hence $B_i$ vanishes identically, and $b_i(t)=0$ almost everywhere. The converse follows directly from (C3).

Exact transparency for every unknown fault time is therefore equivalent to instantaneous incidence balance. Integrated cancellation at the endpoints is insufficient. For the fixed nine-support family, (C12) further implies that every nonzero transparent instantaneous Hamiltonian has all nine terms present in their common ratio. This is a statement about the generator in this model, not a lower bound on the resources of an arbitrary hardware implementation.

## 7. A controlled approximation by repeated sequential cycles

The phase error of a sequential implementation can still be bounded. Divide the desired angle into $N$ identical cycles, applying each term once per cycle with signed area $(\Theta/N)c_S$. Every completed cycle has zero integrated incidence. Only the unfinished cycle containing a fault contributes to $B_i(\tau)$.

For a pulse order $\pi$, define its prefix discrepancy by

```math
D(\pi)=\max_{i,k}
\left|\sum_{\ell\le k}M_{i,\pi(\ell)}c_{\pi(\ell)}\right|.
\tag{C20}
```

If each individual pulse's accumulated area is monotone between its endpoints, then

```math
B_{\max}\le\frac{|\Theta|}{N}D(\pi).
\tag{C21}
```

For these nine coefficients, the minimum discrepancy among orders with one pulse per term is exactly one. An attaining support order is

```math
(3579,1459,123,4678,589,167,1368,2569,346).
```

Its prefix incidence entries all lie in $[-1,1]$. For the matching lower bound, every completed-pulse prefix is a half-integer vector, and the $3/2$ pulse on support $589$ changes three incidence entries by $3/2$. If $D<1$, every prefix entry would lie in $\{-1/2,0,1/2\}$, which cannot accommodate that change.

For this order, $B_{\max}=|\Theta|/N$, giving the conditional single-fault bounds

```math
1-F_e\le\min\{1,4\Theta^2/N^2\},
\qquad
\|\mathcal E-\mathcal U_\Theta\|_\diamond
\le\min\{2,4|\Theta|/N\}.
\tag{C22}
```

When $|\Theta|/N\le\pi/4$, the exact worst-case values are $\sin^2(2|\Theta|/N)$ and $2\sin(2|\Theta|/N)$, respectively. A continuous prefix trajectory reaches the discrepancy endpoint. At larger per-cycle angles it also passes through a maximally damaging phase.

This calculation concerns the phase conditional on at most one fault in a specified schedule. It does not assign a duration, amplitude, or total fault-probability cost to increasing the number of cycles.

## 8. Reproduction and scope

The exact control checks use rational and integer arithmetic. They verify the rank and kernel of the incidence matrix, the pulse-order optimum over all 512 subsets, the maximal-failure example, and the phase-exponent identity on every computational support word of both logical basis states for balanced, perturbed, and sequential schedules. The verification data retain an explicit term order to prevent index ambiguities; see [Verification](../verification/README.md).

The results establish exact sensitivity to specified coefficient errors and pulse schedules for the demonstrated logical axis. They do not establish a universal gate set, fault tolerance of the final recovery hardware, or protection against arbitrary control errors.
