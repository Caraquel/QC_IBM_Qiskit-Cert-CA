# Section 4: Run Quantum Circuits

This notebook series covers the core skills for preparing circuits for execution and running them on backend interfaces.

## Notebooks

- `4_1_Transpile_Circuits_for_Backends.ipynb`
  - Why transpilation is needed
  - Backend-aware circuit conversion
  - Optimization levels and basis gates
- `4_2_Run_Circuits_on_Simulated_Backends.ipynb`
  - Execute circuits with `GenericBackendV2`
  - Use `backend.run()` and inspect job results
  - Control shots and compare outcomes
- `4_3_Backend_Targets_and_Multiple_Circuits.ipynb`
  - Backend properties and targets
  - Running lists of circuits
  - Comparing transpiled outputs
- `4_4_Section_4_Exam_Drills.ipynb`
  - Short drills on transpilation and execution syntax
  - Backend and shot-count checks
  - Multi-circuit running exercises

## Recommended Order

1. `4_1_Transpile_Circuits_for_Backends.ipynb`
2. `4_2_Run_Circuits_on_Simulated_Backends.ipynb`
3. `4_3_Backend_Targets_and_Multiple_Circuits.ipynb`
4. `4_4_Section_4_Exam_Drills.ipynb`

## Notes

- The notebooks use `GenericBackendV2` so they are runnable locally without cloud setup.
- The focus is on the Qiskit 2.x SDK workflow for transpiling and running circuits.
- Result interpretation is kept basic here because deeper result analysis belongs in a later section.
