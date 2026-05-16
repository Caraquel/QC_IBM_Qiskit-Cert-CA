"""Practice code for Section 1: standard gates, phases, and Bell states."""

from __future__ import annotations

from pathlib import Path
import sys

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def state_after_single_qubit_gate(gate_name: str) -> Statevector:
    qc = QuantumCircuit(1)
    qc.x(0)
    getattr(qc, gate_name)(0)
    return Statevector.from_instruction(qc)


def phase_demo() -> None:
    print("Phase demo on |1>")
    expected = {
        "z": -1.0 + 0.0j,
        "s": 0.0 + 1.0j,
        "t": np.exp(1j * np.pi / 4),
    }

    for gate_name in ["z", "s", "t"]:
        state = state_after_single_qubit_gate(gate_name)
        amplitude = state.data[1]
        print(f"{gate_name.upper()}|1> amplitude on |1>: {amplitude}")
        assert np.allclose(amplitude, expected[gate_name])
    print()


def ry_probability_demo() -> None:
    qc = QuantumCircuit(1)
    qc.ry(np.pi / 2, 0)
    state = Statevector.from_instruction(qc)
    probabilities = state.probabilities_dict(decimals=4)

    print("RY(pi/2) on |0>")
    print(f"Statevector: {state.data}")
    print(f"Measurement probabilities: {probabilities}")
    assert np.isclose(probabilities["0"], 0.5)
    assert np.isclose(probabilities["1"], 0.5)
    print()


def bell_state_circuit() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    return qc


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


def bell_state_demo() -> None:
    qc = bell_state_circuit()
    state = Statevector.from_instruction(qc)
    probabilities = state.probabilities_dict(decimals=4)

    print("Bell state circuit")
    show_text_diagram(qc, "bell_state")
    print(f"Amplitudes: {state.to_dict(decimals=4)}")
    print(f"Probabilities: {probabilities}")

    assert np.isclose(probabilities["00"], 0.5)
    assert np.isclose(probabilities["11"], 0.5)
    assert np.isclose(probabilities.get("01", 0.0), 0.0)
    assert np.isclose(probabilities.get("10", 0.0), 0.0)
    print()


def save_visuals() -> None:
    try:
        import matplotlib.pyplot as plt
        from qiskit.visualization import plot_histogram, plot_state_qsphere
    except ImportError:
        print("Skipping visuals because matplotlib or qiskit.visualization is unavailable.")
        print()
        return

    output_dir = Path(__file__).with_name("outputs")
    output_dir.mkdir(exist_ok=True)

    state = Statevector.from_instruction(bell_state_circuit())
    probabilities = state.probabilities_dict()

    qsphere_figure = plot_state_qsphere(
        state,
        show_state_phases=True,
    )
    qsphere_figure.savefig(output_dir / "bell_state_qsphere.png", bbox_inches="tight")
    plt.close(qsphere_figure)

    histogram_figure = plot_histogram(
        probabilities,
        title="Bell-State Measurement Probabilities",
    )
    histogram_figure.savefig(output_dir / "bell_state_histogram.png", bbox_inches="tight")
    plt.close(histogram_figure)

    print(f"Saved visuals to: {output_dir}")
    print("On a qsphere, color represents the relative phase of each basis-state amplitude.")
    print()


def exercise_prompts() -> None:
    print("Practice prompts")
    print("1. Change ry(pi/2) to ry(pi/3) and predict the new measurement probabilities.")
    print("2. Apply T to |+> instead of |1> and inspect how the relative phase changes.")
    print("3. Add a final H gate to qubit 0 of the Bell circuit and predict the new state.")
    print()


def main() -> None:
    phase_demo()
    ry_probability_demo()
    bell_state_demo()
    save_visuals()
    exercise_prompts()


if __name__ == "__main__":
    main()
