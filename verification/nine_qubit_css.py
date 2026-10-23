#!/usr/bin/env python3
"""Exact, dependency-free certificate for the CSS four-local ET construction.
All site indices in the input are one-based. No floating-point arithmetic is used.
"""
from fractions import Fraction as F
from itertools import combinations, product
import json

n = 9
mask = lambda s: sum(1 << (i - 1) for i in s)
xs = [mask(s) for s in [(5,9),(1,2,4,6),(1,3,4,7),(2,3,4,5,8)]]
zs = [mask(s) for s in [(1,4,8),(2,6,8),(3,7,8),(2,3,4,5,9)]]
lx, lz = mask((1,4,5)), mask((3,4,6))
# (support, coefficient, stabilizer product bits in the A,B,C,D ordering)
terms = [
 ((3,4,6), F(1), 0),
 ((1,6,7), F(1), 5),
 ((5,8,9), F(3,2), 10),
 ((1,2,3), F(1,2), 3),
 ((2,5,6,9), F(-1,2), 8),
 ((1,3,6,8), F(-1), 1),
 ((4,6,7,8), F(-1,2), 4),
 ((1,4,5,9), F(-1,2), 11),
 ((3,5,7,9), F(-1,2), 14),
]
parity = lambda v: v.bit_count() % 2

def span(gens):
    out = [0]
    for g in gens:
        out += [v ^ g for v in out]
    return set(out)

X, Z = span(xs), span(zs)
assert len(X) == len(Z) == 16
assert all(parity(x & z) == 0 for x in xs for z in zs)
assert all(parity(lx & z) == 0 for z in zs)
assert all(parity(lz & x) == 0 for x in xs)
assert parity(lx & lz) == 1

# The only nonidentity normalizer element of weight <= 2 is a stabilizer X5 X9.
small_normalizers = []
for w in (1, 2):
    for sites in combinations(range(n), w):
        for labels in product('XYZ', repeat=w):
            x = sum((1 << i) for i, p in zip(sites, labels) if p in 'XY')
            z = sum((1 << i) for i, p in zip(sites, labels) if p in 'ZY')
            if any(parity(x & g) for g in zs) or any(parity(z & g) for g in xs):
                continue
            assert x in X and z in Z
            small_normalizers.append({'sites':[i+1 for i in sites], 'labels':''.join(labels)})
assert small_normalizers == [{'sites':[5,9], 'labels':'XX'}]
assert lx.bit_count() == lz.bit_count() == 3
assert lx not in X and lz not in Z

# Every bare, positive Z word equals Z_L times the specified positive stabilizer.
for support, coefficient, index in terms:
    zproduct = 0
    for j, generator in enumerate(zs):
        if (index >> j) & 1:
            zproduct ^= generator
    assert mask(support) == (lz ^ zproduct)
assert sum(c for _, c, _ in terms) == 1
incident = [sum(c for s,c,_ in terms if i in s) for i in range(1,n+1)]
assert incident == [F(0)] * n
positive_incident = [sum(c for s,c,_ in terms if i in s and c > 0) for i in range(1,n+1)]
negative_incident = [sum(-c for s,c,_ in terms if i in s and c < 0) for i in range(1,n+1)]
assert positive_incident == negative_incident
assert sum(c for s,c,_ in terms if len(s)==3) == 4
assert sum(c for s,c,_ in terms if len(s)==4) == -3
assert sum(abs(c) for _,c,_ in terms) == 7

# Direct exact classical plateau check, independent of the incidence proof.
C = [b for b in range(1 << n) if all(parity(b & z)==0 for z in zs)]
assert len(C) == 32 and X.issubset(C)
assert set(C) == X | {b ^ lx for b in X}
assert all(parity(b & lz) == 0 for b in X)
def energy(b):
    return sum(c * ((-1) ** parity(mask(s) & b)) for s,c,_ in terms)
for b in C:
    target = (-1) ** parity(lz & b)
    for delta in [0] + [1 << i for i in range(n)]:
        assert energy(b ^ delta) == target

out = {
    'exact_arithmetic': True,
    'independent_X_checks': 4,
    'independent_Z_checks': 4,
    'encoded_qubits': 1,
    'distance': 3,
    'nonidentity_normalizers_of_weight_at_most_two': small_normalizers,
    'all_terms_in_positive_logical_Z_coset': True,
    'coefficient_sum': '1',
    'sitewise_incident_coefficient_sums': [str(v) for v in incident],
    'positive_and_negative_incidence_masses': [str(v) for v in positive_incident],
    'weight_three_coefficient_sum': '4',
    'weight_four_coefficient_sum': '-3',
    'pauli_coupling_l1': '7',
    'classical_support_size': len(C),
    'classical_radius_one_plateau_checks': len(C) * (n+1),
    'full_operator_identity': 'H E P = E Z_L P for E=I and every single-site Pauli',
    'logical_axis_claimed': 'Z only',
}
print(json.dumps(out, indent=2))
