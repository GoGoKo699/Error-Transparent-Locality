#!/usr/bin/env python3
"""Full nine-qubit identities in exact complex-rational Pauli algebra."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import json,itertools
HERE = Path(__file__).resolve().parent
src=json.loads((HERE/'data/nine_qubit.json').read_text())
n=src['n']
def p(s):
 x=sum((c in 'XY')<<i for i,c in enumerate(s)); z=sum((c in 'YZ')<<i for i,c in enumerate(s)); return x,z,(x&z).bit_count()%4

def mul(a,b):
 return a[0]^b[0],a[1]^b[1],(a[2]+b[2]+2*(a[1]&b[0]).bit_count())%4

def prod(seq):
 a=(0,0,0)
 for b in seq:a=mul(a,b)
 return a

def sp(a,b):return ((a[0]&b[1]).bit_count()+(a[1]&b[0]).bit_count())%2

def add(d,a,c):
 x,z,ph=a
 if ph%2==0:d[(x,z,0)]+=c*((-1)**(ph//2))
 else:d[(x,z,1)]+=c*((-1)**((ph-1)//2))

S=[]
for word,eig in zip(src['stabilizer_generators'],[1]*8):
 a=p(word);S.append((a[0],a[1],(a[2]+(0 if eig==1 else 2))%4))
G=[prod([s for i,s in enumerate(S) if idx>>i&1]) for idx in range(1<<len(S))]
H=[(p(term['pauli']),F(term['coefficient'])) for term in src['hamiltonian_terms']]
L=p(src['logical_Z'])
assert all(not sp(a,b) for a in S for b in S)
assert len({a[:2] for a in G})==2**len(S)
assert all(a[:2]!=(0,0) or a[2]==0 for a in G)
assert all(not sp(L,s) for s in S)
assert L[:2] not in {s[:2] for s in G}
for name,E in [('I'*n,(0,0,0))]+[('I'*i+c+'I'*(n-i-1),p('I'*i+c+'I'*(n-i-1))) for i in range(n) for c in 'XYZ']:
 d=defaultdict(F)
 for a,c in H:
  for s in G:add(d,prod([a,E,s]),c)
 for s in G:add(d,prod([E,L,s]),F(-1))
 assert not {k:v for k,v in d.items() if v},name

normalizers={}
for w in (1,2,3):
 found=[]
 for inds in itertools.combinations(range(n),w):
  for chars in itertools.product('XYZ',repeat=w):
   word=['I']*n
   for i,c in zip(inds,chars):word[i]=c
   word=''.join(word);a=p(word)
   if all(not sp(a,b) for b in S):found.append(word)
 normalizers[w]=found
assert all(p(word)[:2] in {s[:2] for s in G} for w in (1,2) for word in normalizers[w])
assert any(p(word)[:2] not in {s[:2] for s in G} for word in normalizers[3])
weight_coefficients={}
for term in src['hamiltonian_terms']:
 w=sum(c!='I' for c in term['pauli'])
 weight_coefficients.setdefault(w,F(0))
 weight_coefficients[w]+=abs(F(term['coefficient']))
for w,alpha in [(3,4),(4,-3)]:
 d=defaultdict(F)
 for term,(a,c) in zip(src['hamiltonian_terms'],H):
  if sum(ch!='I' for ch in term['pauli'])==w:
   for s in G:add(d,mul(a,s),c)
 for s in G:add(d,mul(L,s),F(-alpha))
 assert not {k:v for k,v in d.items() if v},w
summary={'status':'PASS','arithmetic':'independent exact rational complex Pauli algebra','stabilizer_group_size':len(G),'dimension':2**n//len(G),'distance':3,'nondegenerate_single_error_code':not normalizers[1] and not normalizers[2],'lowweight_stabilizers':{w:normalizers[w] for w in (1,2)},'term_count':len(H),'maxweight':max(weight_coefficients),'l1_native_coefficient_cost':str(sum(weight_coefficients.values())),'l1_cost_by_weight':{w:str(c) for w,c in weight_coefficients.items()},'logical_target':src['logical_Z'],'all_28_full_action_identities':'H E P = E L P exactly','weight3_compression':'H_3 P = 4 L P','weight4_compression':'H_4 P = -3 L P','weight3_normalizer_count':len(normalizers[3])}
print(json.dumps(summary,indent=2))
