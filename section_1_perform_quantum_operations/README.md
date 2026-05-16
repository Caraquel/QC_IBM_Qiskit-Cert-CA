# Section 1: Perform Quantum Operations

This practice pack is organized around the Qiskit v2.x certification topics for Section 1.

## Files

- `1_Pauli_Operators.py`
  - Multi-qubit Pauli strings
  - Matrix construction with tensor products
  - Qiskit qubit-ordering checks
- `2_1_Standard_Gates.py`
  - Z, S, and T phase behavior
  - `ry` measurement probabilities
  - Bell-state construction
  - Optional qsphere and histogram output
- `2_2_Advanced_Circuits.py`
  - Reusable subcircuits
  - Parameterized layers
  - Controlled custom gates
- `2_3_Quantum_Operations_FeatureMaps.py`
  - `z_feature_map`
  - `zz_feature_map`
  - `pauli_feature_map`
  - Parameter assignment and encoded states
- `2_4_Circuit_Mechanics.py`
  - Registers
  - Circuit size, width, depth, and op counts
  - `measure_all`
  - Transpilation into a basis gate set

## Notebook Series

- `phase_2_standard_gates_and_rotations`
  - Focused notebook track for Section 1 Phase 2
  - Bloch-sphere intuition, rotation probabilities, Bell states, and exam drills

## Install

```bash
pip install -r requirements.txt
```

## Run

From the `section_1_perform_quantum_operations` folder:

```bash
python 1_Pauli_Operators.py
python 2_1_Standard_Gates.py
python 2_2_Advanced_Circuits.py
python 2_3_Quantum_Operations_FeatureMaps.py
python 2_4_Circuit_Mechanics.py
```

## Notes

- Qiskit labels Pauli strings in `q_(n-1) ... q_0` order, so `Pauli("IZ")` means `I ⊗ Z`.
- In current Qiskit 2.x releases, the function-based feature-map builders are the safer choice for new practice code.
- The scripts use `Statevector` for exact results so you can study behavior without needing a hardware backend.
