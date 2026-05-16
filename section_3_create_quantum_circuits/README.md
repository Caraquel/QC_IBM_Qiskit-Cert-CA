# Section 3: Create Quantum Circuits

This notebook series covers the core circuit-construction skills needed for Qiskit v2.x certification practice.

## Notebooks

- `3_1_Construct_Basic_Circuits.ipynb`
  - Build circuits with qubit and classical-bit counts
  - Add gates and inspect circuit data
  - Use `Statevector.from_instruction()` for exact checks
- `3_2_Registers_Bits_and_Measurements.ipynb`
  - Work with `QuantumRegister`, `ClassicalRegister`, and ancillas
  - Measure selected qubits into selected classical bits
  - Inspect circuit width and register structure
- `3_3_Parameters_Compose_and_Inverse.ipynb`
  - Use `Parameter` and `ParameterVector`
  - Compose subcircuits and bind parameters
  - Build inverses and verify cancellation
- `3_4_Section_3_Exam_Drills.ipynb`
  - Short prediction drills for circuit-construction questions
  - Register and parameter exercises
  - Circuit-output checks

## Recommended Order

1. `3_1_Construct_Basic_Circuits.ipynb`
2. `3_2_Registers_Bits_and_Measurements.ipynb`
3. `3_3_Parameters_Compose_and_Inverse.ipynb`
4. `3_4_Section_3_Exam_Drills.ipynb`

## Notes

- The notebooks use the current `QuantumCircuit` construction model from Qiskit 2.x.
- `Statevector` is used where exact, backend-free verification is useful.
- The content is intended for VS Code notebook execution.
