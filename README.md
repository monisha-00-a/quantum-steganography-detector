# quantum-steganography-detector
A simple quantum simulation project using Qiskit to detect hidden or tampered data in a file. The program converts file content into quantum bits (qubits), simulates tampering by applying a quantum gate, and checks for differences using quantum fidelity

 #PURPOSE
 
To demonstrate quantum steganography detection in a beginner-friendly simulation. The project shows how quantum states can be used to detect hidden information or modifications in a dataset.

#METHODOLOGY

Read a text file (sample.txt).
Convert its content into a binary string.
Encode the bits into a quantum circuit (1 qubit per bit).
Create two circuits:
Clean circuit (original data)
Tampered circuit (simulated hidden data using a Z gate)
Simulate both circuits using Qiskit’s AerSimulator.
Compute quantum fidelity to check if the tampered circuit differs from the clean circuit.
Output whether hidden data is detected.
