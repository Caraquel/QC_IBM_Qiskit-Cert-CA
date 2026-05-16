"""Practice code for Section 1: feature maps and data encoding."""

from __future__ import annotations

from pathlib import Path
import sys

import numpy as np
from qiskit.circuit.library import pauli_feature_map, z_feature_map, zz_feature_map
from qiskit.quantum_info import Statevector


FEATURES_2 = [0.2, 0.4]
FEATURES_3 = [0.2, 0.4, 0.8]


def show_text_diagram(circuit, stem: str) -> None:
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


def summarize_feature_map(name: str, circuit, values: list[float]) -> None:
    encoded = circuit.assign_parameters(values)
    state = Statevector.from_instruction(encoded)

    print(name)
    show_text_diagram(encoded, name.replace(" ", "_"))
    print(f"Depth: {encoded.depth()}")
    print(f"Operation counts: {encoded.count_ops()}")
    print(f"Probabilities: {state.probabilities_dict(decimals=4)}")
    print("-" * 60)


def z_feature_map_demo() -> None:
    circuit = z_feature_map(feature_dimension=3, reps=1)
    summarize_feature_map("z_feature_map", circuit, FEATURES_3)


def zz_feature_map_demo() -> None:
    circuit = zz_feature_map(feature_dimension=3, reps=1, entanglement="linear")
    summarize_feature_map("zz_feature_map", circuit, FEATURES_3)


def pauli_feature_map_demo() -> None:
    circuit = pauli_feature_map(
        feature_dimension=2,
        reps=1,
        paulis=["Z", "ZZ", "XX"],
        entanglement="full",
    )
    summarize_feature_map("pauli_feature_map", circuit, FEATURES_2)


def custom_data_map_demo() -> None:
    def custom_phi(x):
        if len(x) == 1:
            return x[0]
        return (np.pi - x[0]) * (np.pi - x[1]) / 2

    circuit = zz_feature_map(
        feature_dimension=2,
        reps=1,
        entanglement="full",
        data_map_func=custom_phi,
    )
    summarize_feature_map("zz_feature_map with custom data_map_func", circuit, FEATURES_2)


def exercise_prompts() -> None:
    print("Practice prompts")
    print("1. Change the entanglement pattern in zz_feature_map from 'linear' to 'full'.")
    print("2. Add 'YY' to the pauli_feature_map paulis list and compare count_ops().")
    print("3. Bind two different classical feature vectors and compare the resulting probabilities.")
    print()


def main() -> None:
    print("Feature-map note: current Qiskit 2.x practice code uses function-based builders.")
    print()
    z_feature_map_demo()
    zz_feature_map_demo()
    pauli_feature_map_demo()
    custom_data_map_demo()
    exercise_prompts()


if __name__ == "__main__":
    main()


