# Implementations of 16 Qubit Random Number Generator 

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create 16 qubits and 16 classical bits
qc = QuantumCircuit(16, 16)

# Apply Hadamard gate to all qubits
qc.h(range(16))

# Measure all qubits
qc.measure(range(16), range(16))

# Display the quantum circuit
print(qc.draw())

# Create simulator
simulator = AerSimulator()

# Run the circuit once
result = simulator.run(qc, shots=1).result()

# Get the measurement result
counts = result.get_counts()

# Get the 16-bit random number
binary = list(counts.keys())[0]

# Convert binary to decimal
decimal = int(binary, 2)

print("Random Binary Number :", binary)
print("Random Decimal Number:", decimal)