from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import random_clifford
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error
import matplotlib.pyplot as plt

# Set up a small gate-noise model
noise_model = NoiseModel()
error = depolarizing_error(0.01, 1)
noise_model.add_all_qubit_quantum_error(error, ["h", "s", "sdg"])
simulator = AerSimulator(noise_model=noise_model)

sequence_lengths = [0, 2, 4, 8, 16, 32]
number_of_sequences = 20
shots = 256
survival_probabilities = []

for length in sequence_lengths:
    circuits = []

    for _ in range(number_of_sequences):
        # Apply a random sequence of Clifford gates
        sequence = QuantumCircuit(1)
        for _ in range(length):
            clifford = random_clifford(1).to_circuit()
            sequence.compose(clifford, inplace=True)

        # Append the inverse so the ideal result returns to |0>
        circuit = QuantumCircuit(1, 1)
        circuit.compose(sequence, inplace=True)
        circuit.compose(sequence.inverse(), inplace=True)
        circuit.measure(0, 0)
        circuits.append(circuit)

    # Use the same gate set covered by the noise model
    circuits = transpile(circuits, basis_gates=["h", "s", "sdg"])
    results = simulator.run(circuits, shots=shots).result()

    zero_count = sum(result.get("0", 0) for result in results.get_counts())
    survival = zero_count / (number_of_sequences * shots)
    survival_probabilities.append(survival)

print("Sequence lengths:     ", sequence_lengths)
print("Survival probabilities:", [round(value, 3) for value in survival_probabilities])

plt.plot(sequence_lengths, survival_probabilities, "o-")
plt.xlabel("Sequence length")
plt.ylabel("Probability of measuring 0")
plt.title("Single-Qubit Randomized Benchmarking")
plt.ylim(0, 1.05)
plt.grid(True)
plt.show()