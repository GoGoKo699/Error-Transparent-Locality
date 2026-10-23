#!/usr/bin/env python3
"""Exact primal/dual certificates for the finite error-moment LP.
No external packages. This verifies moment relaxations, not code attainability.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb, prod
import json


def peval(p,x):
    out=F(0)
    for a in reversed(p):out=out*x+a
    return out

def padd(p,q):
    n=max(len(p),len(q));out=[F(0)]*n
    for i,a in enumerate(p):out[i]+=a
    for i,a in enumerate(q):out[i]+=a
    while len(out)>1 and not out[-1]:out.pop()
    return out

def pmul(p,q):
    out=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):out[i+j]+=a*b
    return out

def lagrange_basis(nodes,j):
    p=[F(1)];den=F(1)
    for k,x in enumerate(nodes):
        if k==j:continue
        p=pmul(p,[-F(x),F(1)]);den*=nodes[j]-x
    return [a/den for a in p]

def solve(W,t):
    W=tuple(sorted(set(W)))
    assert all(w>0 for w in W)
    if len(W)<=t:
        annihilator=[F(1)]
        for w in W:annihilator=pmul(annihilator,[-F(w),F(1)])
        assert all(peval(annihilator,w)==0 for w in W)
        assert peval(annihilator,0)!=0
        return {'feasible':False,'allowed_weights':W,'t':t,'annihilator_coefficients':[str(x) for x in annihilator]}
    candidates=[]
    for nodes in combinations(W,t+1):
        basis=[lagrange_basis(nodes,j) for j in range(t+1)]
        masses=[peval(p,0) for p in basis]
        assert all(sum(a*F(w)**j for a,w in zip(masses,nodes))==(1 if j==0 else 0) for j in range(t+1))
        cost=sum(abs(a) for a in masses)
        candidates.append((cost,nodes,masses,basis))
    cost,nodes,masses,basis=min(candidates,key=lambda c:(c[0],c[1]))
    dual=[F(0)]
    for a,p in zip(masses,basis):dual=padd(dual,[(1 if a>0 else -1)*b for b in p])
    assert all(abs(peval(dual,w))<=1 for w in W)
    assert peval(dual,0)==cost
    assert all(peval(dual,w)==(1 if a>0 else -1) for a,w in zip(masses,nodes))
    return {'feasible':True,'allowed_weights':W,'t':t,'optimal_cost':str(cost),
            'primal_support':nodes,'primal_masses':[str(a) for a in masses],
            'dual_polynomial_coefficients_ascending':[str(a) for a in dual],
            'dual_values_on_allowed_weights':[str(peval(dual,w)) for w in W],
            'interpretation':'Exact moment-relaxation optimum; no physical-code attainability is asserted.'}

records=[]
for d,r,t in [(3,4,1),(3,5,1),(3,6,1),(3,7,1),(5,7,2),(5,8,2),(5,9,2),(5,10,2),(7,10,3),(7,11,3),(7,12,3),(9,13,4)]:
    result=solve(range(d,r+1),t)
    B=F(result['optimal_cost'])
    if t==1:assert B==F(r+d,r-d)
    if t==2:assert B==1+F(2*d*r,((r-d)**2)//4)
    if r==d+t:
        assert B==sum(2**k*comb(d+k-1,k) for k in range(t+1))
        expected=[(-1)**j*F(prod(range(d,d+t+1)),(d+j)*prod(range(1,j+1))*prod(range(1,t-j+1))) for j in range(t+1)]
        assert [F(a) for a in result['primal_masses']]==expected
    records.append({'d':d,'r':r,**result})

# Code-specific missing-weight examples: they strengthen the generic interval bound.
records.append({'label':'five-qubit odd-weight coset at r=4',**solve([3],1)})
records.append({'label':'five-qubit logical coset at r=5',**solve([3,5],1)})
records.append({'label':'illustrative sparse allowed set, not a code claim',**solve([5,7,9],2)})

out={'exact_arithmetic':True,'moment_constraints':'sum_w a_w w^j = delta_{j0}, j=0,...,t',
     'dual':'maximize p(0), degree(p)<=t, |p(w)|<=1 for every allowed weight',
     'records':records}
print(json.dumps(out,indent=2))
