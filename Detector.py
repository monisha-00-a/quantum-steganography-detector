# ============================================================
# Quantum Steganography Detector (File-based Simulation)
# ============================================================
# This program demonstrates how hidden or tampered data could
# be detected in a quantum environment. It reads a text file,
# converts the first few bits into quantum states (qubits),
# simulates a hidden/tampered version, and compares them
# using quantum fidelity.
# ============================================================

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import state_fidelity
import os
import random

# ------------------------------------------------------------
# Convert text into binary string
# ------------------------------------------------------------
def text_to_bits(text):
    return ''.join(format(ord(c), '08b') for c in text)

# ------------------------------------------------------------
# Create a quantum circuit based on bit string
# ------------------------------------------------------------
def make_quantum_circuit(bit_string, tampered=False):
    n = len(bit_string)
    qc = QuantumCircuit(n)

    # Encode each bit as a qubit
    for i, bit in enumerate(bit_string):
        if bit == '1':
            qc.x(i)  # |1⟩ for bit 1, |0⟩ for bit 0

    # Optional tampering: flip a random qubit
    if tampered and n > 0:
        tamper_index = random.randint(0, n - 1)
        qc.z(tamper_index)
        print(f"[Tampering] Hidden data added at qubit {tamper_index}")

    qc.save_statevector()  # save state for simulation
    return qc

# ------------------------------------------------------------
# Main Detector Function
# ------------------------------------------------------------
def main():
    print("=== Quantum Steganography Detector ===\n")

    filename = "sample.txt"

    # Create demo file if not present
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write("Hello Quantum World!")

    # Read file content
    with open(filename, "r") as f:
        data = f.read()

    print(f"📂 Reading file: {filename}")
    print(f"🧾 File content: {data}\n")

    # Convert to binary
    bit_string = text_to_bits(data)
    print(f"Original binary string length: {len(bit_string)} bits")

    # ⚙️ Limit number of qubits to prevent memory crash
    max_bits = 8
    bit_string = bit_string[:max_bits]
    print(f"Simulating first {max_bits} bits only...\n")

    # Create clean and tampered circuits
    normal_circuit = make_quantum_circuit(bit_string, tampered=False)
    tampered_circuit = make_quantum_circuit(bit_string, tampered=True)

    # Initialize simulator
    simulator = AerSimulator(method="statevector")

    # Run circuits
    normal_state = simulator.run(normal_circuit).result().get_statevector()
    tampered_state = simulator.run(tampered_circuit).result().get_statevector()

    # Compare states using fidelity
    fidelity = state_fidelity(normal_state, tampered_state)
    print(f"🔍 Fidelity between clean and tampered states: {fidelity:.4f}")

    # Decision
    if fidelity < 0.95:
        print("⚠️ Hidden or tampered data detected in file (simulated)!")
    else:
        print("✅ File is clean (no hidden data detected).")

    print("\n=== Detection Complete ===")

# ------------------------------------------------------------
# Run program
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
