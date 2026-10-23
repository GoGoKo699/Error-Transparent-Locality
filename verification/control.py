#!/usr/bin/env python3
"""Exact incidence, fault-phase, and pulse-order checks for nine supports."""
from pathlib import Path
from fractions import Fraction as F
import json

HERE=Path(__file__).resolve().parent
src=json.loads((HERE/'data/nine_qubit.json').read_text())
terms=src['hamiltonian_terms'];n=src['n'];m=len(terms)
M=[[F(int(i in t['sites'])) for t in terms] for i in range(1,n+1)]
c=[F(t['coefficient']) for t in terms]

def rref(A):
 A=[row[:] for row in A];row=0;piv=[]
 for col in range(len(A[0])):
  hits=[i for i in range(row,len(A)) if A[i][col]]
  if not hits:continue
  k=hits[0];A[row],A[k]=A[k],A[row]
  scale=A[row][col];A[row]=[x/scale for x in A[row]]
  for i in range(len(A)):
   if i!=row and A[i][col]:
    scale=A[i][col];A[i]=[x-scale*y for x,y in zip(A[i],A[row])]
  piv.append(col);row+=1
  if row==len(A):break
 return A,piv

R,piv=rref(M)
assert len(piv)==8
assert all(sum(row[j]*c[j] for j in range(m))==0 for row in M)
assert sum(c)==1

def determinant(A):
 A=[row[:] for row in A];d=F(1)
 for k in range(len(A)):
  hit=next(i for i in range(k,len(A)) if A[i][k])
  if hit!=k:A[hit],A[k]=A[k],A[hit];d=-d
  v=A[k][k];d*=v
  for i in range(k+1,len(A)):
   f=A[i][k]/v
   A[i]=[x-f*y for x,y in zip(A[i],A[k])]
 return d

minor=determinant([row[:8] for row in M[:8]])
assert minor==8
index={tuple(t['sites']):j for j,t in enumerate(terms)}
eps=[F(0)]*m;eps[index[(3,4,6)]]=1;eps[index[(1,6,7)]]=-1
assert sum(eps)==0
assert [sum(M[i][j]*eps[j] for j in range(m)) for i in range(n)]==[-1,0,1,1,0,0,-1,0,0]
null=[]
for f in range(m):
 if f in piv:continue
 v=[F(0)]*m;v[f]=F(1)
 for i,p in enumerate(piv):v[p]=-R[i][f]
 null.append(v)
assert len(null)==1 and all(null[0][j]*c[0]==null[0][0]*c[j] for j in range(m))

# Optimal order among one monotone pulse per term: exact dynamic programming
# Prefix discrepancy is sufficient, because a pulse interpolates linearly
# between its endpoint incidence vectors.
vectors=[[int(2*c[j])*int(M[i][j]) for i in range(n)] for j in range(m)]
state={0:([0]*n,0,None)}
for bits in range(1,1<<m):
 j=(bits & -bits).bit_length()-1;prev=bits^(1<<j)
 prefix=[state[prev][0][i]+vectors[j][i] for i in range(n)]
 radius=max(map(abs,prefix))
 best=min((max(state[bits^(1<<k)][1],radius),k) for k in range(m) if bits>>k&1)
 state[bits]=(prefix,best[0],best[1])
bits=(1<<m)-1;order=[]
while bits:
 j=state[bits][2];order.append(j);bits^=1<<j
order=order[::-1]
optimal_value=state[(1<<m)-1][1]
# Verify the explicit optimal order printed in the scientific account.
order=[index[s] for s in [(3,5,7,9),(1,4,5,9),(1,2,3),(4,6,7,8),(5,8,9),(1,6,7),(1,3,6,8),(2,5,6,9),(3,4,6)]]
D=F(state[(1<<m)-1][1],2)
assert D==1
prefix=[0]*n;history=[prefix[:]]
for j in order:
 prefix=[prefix[i]+vectors[j][i] for i in range(n)];history.append(prefix[:])
assert all(x==0 for x in prefix)
assert max(abs(x) for row in history for x in row)==optimal_value

# Computational support of the CSS logical basis. Work with exponent
# coefficients in units of an arbitrary symbolic total angle Theta.
Dwords=src['D_words']
xmask=[int(ch=='X') for ch in src['logical_X']]
codewords=[(w,1) for w in Dwords]+[(''.join(str(int(b)^x) for b,x in zip(w,xmask)),-1) for w in Dwords]
def eig(word,sites):return (-1)**sum(int(word[i-1]) for i in sites)
for word,logical in codewords:
 assert all(eig(word,t['sites'])==logical for t in terms)

# Includes a balanced envelope, arbitrary unequal pulse coefficients,
# the canonical sequential implementation, and optimal reordered cycles.
schedules={
 'balanced_two_steps':[[2*x for x in c],[F(-1)*x for x in c]],
 'perturbed_two_steps':[[x+F(j-4,100) for j,x in enumerate(c)],[F(j%3-1,37) for j in range(m)]],
 'sequential_displayed':[[c[j] if k==j else F(0) for k in range(m)] for j in range(m)],
 'sequential_optimal':[[c[j] if k==j else F(0) for k in range(m)] for j in order],
}
checks=0
for name,steps in schedules.items():
 A=sum(sum(step) for step in steps)
 for k in range(len(steps)):
  for tau in (F(0),F(1,3),F(1)):
   before=[sum(step[j] for step in steps[:k])+tau*steps[k][j] for j in range(m)]
   after=[(1-tau)*steps[k][j]+sum(step[j] for step in steps[k+1:]) for j in range(m)]
   for i in range(n):
    B=sum(after[j]*M[i][j] for j in range(m))
    for word,logical in codewords:
     flipped=word[:i]+str(1-int(word[i]))+word[i+1:]
     actual=sum(before[j]*eig(word,terms[j]['sites'])+after[j]*eig(flipped,terms[j]['sites']) for j in range(m))
     predicted=logical*(A-2*B)
     assert actual==predicted,(name,k,tau,i,word)
     checks+=1

# Explicit sequencing counterexample: all integrated coefficients are c*Theta,
# fault immediately after first term at qubit3, then ideal correction.
remaining=c[:];remaining[0]=F(0)
B=sum(remaining[j]*M[2][j] for j in range(m))
assert B==-1
# Therefore faulted angle is 3*Theta and residual angle is 2*Theta.
# At Theta=pi/4 the residual channel is exactly logical Z.
res={'status':'PASS','arithmetic':'exact rational and integer','incidence_rank':len(piv),'incidence_nullity':len(null),'rank_witness':{'rows':'1 through8','columns':'first8 in displayed construction order','minor_determinant':str(minor)},'angle_invisible_perturbation':'Z346 minus Z167: sum coefficient0, incidence(-1,0,1,1,0,0,-1,0,0)','normalized_kernel_generator':[str(x) for x in c],'term_supports_in_column_order':[t['sites'] for t in terms],'incidence_matrix':[[int(x) for x in row] for row in M],'optimal_monotone_sequential_support_order':[terms[j]['sites'] for j in order],'optimal_monotone_sequential_order_1based':[j+1 for j in order],'minimum_prefix_discrepancy':str(D),'prefix_incidence_vectors':[[str(F(x,2)) for x in row] for row in history],'schedule_optimization':'all512 subsets, exact dynamic programming','full_computational_support_phase_checks':checks,'counterexample':{'schedule':'displayed construction order, each pulse area c_j*Theta','fault':'X_3 or Y_3 immediately after first pulse','B_over_Theta':str(B),'recovered_angle_over_Theta':'3','residual_angle_over_Theta':'2','at_Theta_pi_over_4':'exact logical Z error after ideal recovery'}}
print(json.dumps(res,indent=2))
