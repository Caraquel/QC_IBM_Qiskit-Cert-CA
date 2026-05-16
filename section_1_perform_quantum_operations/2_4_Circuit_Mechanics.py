"""Practice code for Section 1: circuit mechanics, registers, and transpilation."""

from __future__ import annotations

from pathlib import Path
import sys

import numpy as np
from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister, transpile
from qiskit.quantum_info import Statevector


def build_register_demo() -> tuple[QuantumCircuit, QuantumCircuit]:
    data = QuantumRegister(2, "data")
    ancilla = QuantumRegister(1, "anc")
    readout = ClassicalRegister(3, "c")

    ideal = QuantumCircuit(data, ancilla, name="ideal_demo")
    ideal.h(data[0])
    ideal.cx(data[0], data[1])
    ideal.ry(np.pi / 3, ancilla[0])
    ideal.cz(data[1], ancilla[0])
    ideal.barrier()

    measured = QuantumCircuit(data, ancilla, readout, name="measured_demo")
    measured.compose(ideal, inplace=True)
    measured.measure(data[0], readout[0])
    measured.measure(data[1], readout[1])
    measured.measure(ancilla[0], readout[2])

    return ideal, measured


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


def mechanics_summary() -> None:
    ideal, measured = build_register_demo()
    state = Statevector.from_instruction(ideal)

    print("Register and circuit-property demo")
    show_text_diagram(measured, "register_mechanics")
    print(f"num_qubits: {measured.num_qubits}")
    print(f"num_clbits: {measured.num_clbits}")
    print(f"width: {measured.width()}")
    print(f"size: {measured.size()}")
    print(f"depth: {measured.depth()}")
    print(f"count_ops: {measured.count_ops()}")
    print(f"Ideal probabilities before measurement: {state.probabilities_dict(decimals=4)}")
    print()


def measure_all_demo() -> None:
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)

    measured = qc.measure_all(inplace=False)

    print("measure_all demo")
    show_text_diagram(measured, "measure_all")
    print(f"Original circuit clbits: {qc.num_clbits}")
    print(f"Measured circuit clbits: {measured.num_clbits}")
    print()


def transpilation_demo() -> None:
    _, measured = build_register_demo()
    transpiled = transpile(
        measured,
        basis_gates=["rz", "sx", "x", "cx", "measure"],
        optimization_level=1,
    )

    print("Transpilation demo")
    print(f"Original depth: {measured.depth()}")
    print(f"Transpiled depth: {transpiled.depth()}")
    print(f"Transpiled count_ops: {transpiled.count_ops()}")
    print()


def exercise_prompts() -> None:
    print("Practice prompts")
    print("1. Add another ClassicalRegister and measure the ancilla into a different readout bit.")
    print("2. Compare the circuit depth before and after adding barriers.")
    print("3. Change the basis gates in transpile() and inspect how the circuit decomposition changes.")
    print()


def main() -> None:
    mechanics_summary()
    measure_all_demo()
    transpilation_demo()
    exercise_prompts()


if __name__ == "__main__":
    main()

