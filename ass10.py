# Implementing a 5 qubit Quantum Fourier Transform

from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import QFTGate
from qiskit_aer import AerSimulator

# Step 1: Create a circuit with 5 qubits and 5 classical bits
n = 5
qc = QuantumCircuit(n, n)

# Step 2: Prepare the input state |00001>
qc.x(0)

# Step 3: Apply the 5-qubit Quantum Fourier Transform
qc.append(QFTGate(n), range(n))

# Step 4: Measure all qubits
qc.measure(range(n), range(n))

# Step 5: Display the circuit
print("5-Qubit QFT Circuit:")
print(qc.draw())

# Step 6: Create a quantum simulator
simulator = AerSimulator()

# Step 7: Transpile the circuit
compiled_circuit = transpile(qc, simulator)

# Step 8: Execute the circuit
job = simulator.run(compiled_circuit, shots=1024)

# Step 9: Collect measurement results
result = job.result()
counts = result.get_counts()

# Step 10: Display the results
print("\nMeasurement Results:")
print(counts)