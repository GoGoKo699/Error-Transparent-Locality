#!/usr/bin/env python3
"""Exact five-qubit canonical error-transparent Hamiltonians, no dependencies.
Pauli coefficients and full operator products use Gaussian rational arithmetic.
"""
from fractions import Fraction as F
from itertools import combinations, product
import json

N = 5
STABILIZERS = ['IXZZX', 'XIXZZ', 'ZXIXZ', 'ZZXIX']
LOGICALS = {'X': 'XXXXX', 'Y': 'YYYYY', 'Z': 'ZZZZZ'}

# Standard bare Hermitian Pauli is i^(x.z) X^x Z^z.
def bits(word):
    return (sum(1<<i for i,p in enumerate(word) if p in 'XY'),
            sum(1<<i for i,p in enumerate(word) if p in 'YZ'))
def word(key):
    x,z=key
    return ''.join('IXZY'[((x>>i)&1)+2*((z>>i)&1)] for i in range(N))
def wt(key): return (key[0]|key[1]).bit_count()
def comm(a,b): return ((a[0]&b[1]).bit_count()+(a[1]&b[0]).bit_count())%2

def pmul(a,b):
    x,z=a; u,v=b; key=(x^u,z^v)
    phase=((x&z).bit_count()+(u&v).bit_count()+2*(z&u).bit_count()-(key[0]&key[1]).bit_count())%4
    return key,phase

def rotate(c,k):
    a,b=c
    return [(a,b),(-b,a),(-a,-b),(b,-a)][k%4]
def gmul(c,d):
    a,b=c;u,v=d
    return (a*u-b*v,a*v+b*u)
def addterm(out,key,c):
    a,b=out.get(key,(F(0),F(0)))
    value=(a+c[0],b+c[1])
    if value==(0,0):out.pop(key,None)
    else:out[key]=value

def mul(A,B):
    out={}
    for a,c in A.items():
        for b,d in B.items():
            key,k=pmul(a,b);addterm(out,key,rotate(gmul(c,d),k))
    return out

def add(A,B,scale=F(1)):
    out=dict(A)
    for key,(a,b) in B.items():addterm(out,key,(scale*a,scale*b))
    return out

def atom(key,coef=F(1)): return {key:(F(coef),F(0))}
I=atom((0,0))
generators=[bits(s) for s in STABILIZERS]
assert all(comm(g,h)==0 for g in generators for h in generators)

# Signed stabilizer group; all products are exact literal bare Pauli expansions.
group=[I]
for g in generators:
    group += [mul(s,atom(g)) for s in group]
assert len({next(iter(s)) for s in group})==16
P={}
for s in group:P=add(P,s,F(1,16))
assert mul(P,P)==P
assert P.get((0,0))==(F(1,16),F(0))

assert comm(bits(LOGICALS['X']),bits(LOGICALS['Z'])) == 1
assert all(bits(w) not in {next(iter(s)) for s in group} for w in LOGICALS.values())

errors=[(0,0)]+[bits('I'*i+p+'I'*(N-i-1)) for i in range(N) for p in 'XYZ']
syndromes=[tuple(comm(e,g) for g in generators) for e in errors]
assert len(set(syndromes))==16
syndrome_projectors=[mul(mul(atom(e),P),atom(e)) for e in errors]
Q={}
for pe in syndrome_projectors:Q=add(Q,pe)
assert Q==I
for i,q in enumerate(syndrome_projectors):
    assert mul(q,q)==q
    for p in syndrome_projectors[:i]:assert mul(q,p)=={}

# Distance lower bound, directly checking all weight-one and weight-two Paulis.
small_normalizers=[]
for k in (1,2):
    for sites in combinations(range(N),k):
        for labels in product('XYZ',repeat=k):
            p=['I']*N
            for i,label in zip(sites,labels):p[i]=label
            b=bits(''.join(p))
            if all(comm(b,g)==0 for g in generators):small_normalizers.append(word(b))
assert not small_normalizers

results={}
for axis,Lword in LOGICALS.items():
    L=bits(Lword)
    assert all(comm(L,g)==0 for g in generators)
    LP=mul(atom(L),P)
    H={}
    for e in errors:H=add(H,mul(mul(atom(e),LP),atom(e)))
    assert mul(H,P)==LP
    for e in errors:
        assert mul(mul(H,atom(e)),P)==mul(mul(atom(e),atom(L)),P)
    assert mul(H,H)==I
    assert all(c[1]==0 for c in H.values())
    assert len(H)==16
    signed_coset=[]
    for s in group:
        ls=mul(atom(L),s)
        assert len(ls)==1
        p,c=next(iter(ls.items()))
        assert c in [(F(1),F(0)),(F(-1),F(0))]
        weight=wt(p)
        expected=F(1)-F(weight,4)
        assert H[p][0]==expected*c[0]
        signed_coset.append({'pauli':word(p),'coset_sign':str(c[0]),'weight':weight,'signed_coset_coefficient':str(expected),'bare_coefficient':str(H[p][0])})
    assert sum(x['weight']==3 for x in signed_coset)==10
    assert sum(x['weight']==5 for x in signed_coset)==6
    assert sum(abs(c[0]) for c in H.values())==4
    h3={p:c for p,c in H.items() if wt(p)==3}
    h5={p:c for p,c in H.items() if wt(p)==5}
    assert mul(h3,P)=={p:(F(5,2)*c[0],F(5,2)*c[1]) for p,c in LP.items()}
    assert mul(h5,P)=={p:(F(-3,2)*c[0],F(-3,2)*c[1]) for p,c in LP.items()}
    assert all(comm(a,b)==0 for a in H for b in H)
    results[axis]={
      'logical_pauli':Lword,
      'terms':sorted(signed_coset,key=lambda t:(t['weight'],t['pauli'])),
      'weight_three_terms':10,'weight_five_terms':6,
      'weight_three_logical_coefficient':'5/2','weight_five_logical_coefficient':'-3/2',
      'maximum_locality':5,'pauli_l1':'4','full_error_transparency_identities':16,
      'global_square_is_identity':True,'terms_pairwise_commute':True,
    }

out={
 'exact_arithmetic':True,'n':5,'k':1,'distance':3,'code_nondegenerate':True,
 'stabilizer_generators':STABILIZERS,
 'syndrome_projectors_sum_to_identity':True,
 'construction':'H_L = sum_{E in {I,X_i,Y_i,Z_i}} E L P E',
 'provenance':'Canonical protected Hamiltonian, known prior construction; coupling-budget optimality is the new derived comparison.',
 'axes':results,
}
print(json.dumps(out,indent=2))
