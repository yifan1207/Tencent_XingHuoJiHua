import numpy as np
import itertools
import tensorcircuit as tc
# Grover 算法 TensorCircuit 示例


def grover_oracle(c, n):
    c.multicontrol(*range(n + 1), unitary=tc.gates.x(), ctrl=[1 for _ in range(n)])
    return c
    # answer bitstring is in ctrl


def grover_reflection(c, n):
    for i in range(n):
        c.H(i)
        c.X(i)
    c.multicontrol(*range(n), unitary=tc.gates.z(), ctrl=[1 for _ in range(n - 1)])
    for i in range(n):
        c.X(i)
        c.H(i)
    return c
def grover_algorithm(n, r):
    c = tc.Circuit(n + 1)
    c.X(n)
    for i in range(n + 1):
        c.H(i)
    for j in range(r):
        c = grover_oracle(c, n)
        c = grover_reflection(c, n)
    return c
n = 6
np.pi / 4 * np.sqrt(2**n)
c = grover_algorithm(6, 6)
c.sample()