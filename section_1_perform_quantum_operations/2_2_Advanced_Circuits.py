"""Practice code for Section 1: advanced circuit construction patterns."""

from __future__ import annotations

from pathlib import Path
import sys

import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector
from qiskit.quantum_info import Statevector


def build_parameterized_layer(theta: ParameterVector) -> QuantumCircuit:
    layer = QuantumCircuit(3, name="theta_layer")
    for qubit, angle in enumerate(theta):
        layer.ry(angle, qubit)
    layer.cx(0, 1)
    layer.cx(1, 2)
    layer.rz(theta[0] - theta[2], 2)
    return layer


def show_text_diagram(circuit: QuantumCircuit, stem: str) -> None:
    diagram = str(circuit.draw("text"))
    encoding = (sys.stdout.encoding or "").lower()
    if "utf" in encoding:
        print(diagram)
        return

    output_dir = Path(__file__).with_name("outputs")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / f"{stem}_diagram.txt"
    output_path.write_text(diagram, encoding="utf-8")
    print(f"Diagram saved to: {output_path}")


def parameterized_circuit_demo() -> None:
    theta = ParameterVector("theta", 3)
    layer = build_parameterized_layer(theta)

    qc = QuantumCircuit(3)
    for qubit in range(3):
        qc.h(qubit)
    qc.compose(layer, inplace=True)
    qc.barrier()
    qc.compose(layer.inverse(), inplace=True)

    bound = qc.assign_parameters([np.pi / 6, np.pi / 4, np.pi / 3])
    state = Statevector.from_instruction(bound)

    print("Parameterized layer demo")
    show_text_diagram(bound, "parameterized_layer")
    print(f"Depth: {bound.depth()}")
    print(f"Parameters remaining: {len(bound.parameters)}")
    print(f"Probabilities: {state.probabilities_dict(decimals=4)}")
    print()


def reusable_subcircuit_demo() -> None:
    bell_block = QuantumCircuit(2, name="bell_block")
    bell_block.h(0)
    bell_block.cx(0, 1)

    qc = QuantumCircuit(4)
    qc.compose(bell_block, qubits=[0, 1], inplace=True)
    qc.compose(bell_block, qubits=[2, 3], inplace=True)

    state = Statevector.from_instruction(qc)

    print("Reusable subcircuit demo")
    show_text_diagram(qc, "reusable_subcircuits")
    print(f"Non-zero amplitudes: {state.to_dict(decimals=4)}")
    print()


def controlled_custom_gate_demo() -> None:
    swap_like = QuantumCircuit(2, name="swap_like")
    swap_like.cx(0, 1)
    swap_like.cx(1, 0)
    swap_like.cx(0, 1)

    controlled_gate = swap_like.to_gate().control(1)

    qc = QuantumCircuit(3)
    qc.x(0)
    qc.x(1)
    qc.append(controlled_gate, [0, 1, 2])

    state = Statevector.from_instruction(qc)

    print("Controlled custom gate demo")
    show_text_diagram(qc, "controlled_custom_gate")
    print(f"Final state: {state.to_dict()}")
    print()


def exercise_prompts() -> None:
    print("Practice prompts")
    print("1. Add a second parameterized layer and compare the depth.")
    print("2. Replace the controlled swap-like gate with a controlled Bell block and inspect the state.")
    print("3. Compose the inverse of bell_block after the two Bell pairs and verify that you return to |0000>.")
    print()


def main() -> None:
    parameterized_circuit_demo()
    reusable_subcircuit_demo()
    controlled_custom_gate_demo()
    exercise_prompts()


if __name__ == "__main__":
    main()
