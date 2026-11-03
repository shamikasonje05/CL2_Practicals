from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, pauli_error

# Create 3-qubit repetition code for logical 0 = 000
circuit = QuantumCircuit(3, 3)

# Create 10% bit-flip noise
noise_model = NoiseModel()
bit_flip_error = pauli_error([("X", 0.1), ("I", 0.9)])
noise_model.add_all_qubit_quantum_error(bit_flip_error, ["id"])

# Apply identity gates where noise can occur
for qubit in range(3):
    circuit.id(qubit)

# Measure all qubits
circuit.measure(range(3), range(3))

print(circuit.draw())

# Run noisy simulation
simulator = AerSimulator(noise_model=noise_model)
counts = simulator.run(circuit, shots=1000).result().get_counts()

# Majority-vote error correction
decoded_counts = {"0": 0, "1": 0}

for measured_bits, count in counts.items():
    decoded_bit = "0" if measured_bits.count("1") < 2 else "1"
    decoded_counts[decoded_bit] += count

corrected_bit = max(decoded_counts, key=decoded_counts.get)

print("Original logical bit: 0")
print("Noisy measurement counts:", counts)
print("Decoded counts:", decoded_counts)
print("Corrected logical bit:", corrected_bit)