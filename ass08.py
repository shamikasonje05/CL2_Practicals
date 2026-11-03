# Quantum Teleportation using Qiskit
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# q0 = Alice's message qubit, q1 = Alice's Bell half, q2 = Bob's Bell half
qc = QuantumCircuit(3, 1)

# Step 1: Prepare the state to teleport on q0 (any state works)
theta, phi = 1.1, 0.7
qc.ry(theta, 0)
qc.rz(phi, 0)
qc.barrier()

# Step 2: Create Bell pair (entanglement) between q1 and q2
qc.h(1)
qc.cx(1, 2)
qc.barrier()

# Step 3: Alice's Bell-basis measurement (CNOT + Hadamard)
qc.cx(0, 1)
qc.h(0)
qc.barrier()

# Step 4: Bob's corrections (controlled by Alice's qubits;
#         equivalent to measuring q0,q1 and sending 2 classical bits)
qc.cx(1, 2)   # X correction if q1 = 1
qc.cz(0, 2)   # Z correction if q0 = 1
qc.barrier()

# Step 5: Verify - undo the preparation on q2; it must give |0> always
qc.rz(-phi, 2)
qc.ry(-theta, 2)
qc.measure(2, 0)

print(qc.draw())

# Run on simulator
sim = AerSimulator()
counts = sim.run(transpile(qc, sim), shots=1024).result().get_counts()
print("Result:", counts)   # Expect {'0': 1024} -> teleportation successful