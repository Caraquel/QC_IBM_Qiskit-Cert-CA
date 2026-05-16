"""Practice code for Section 1: Pauli operators and matrix representations."""

from __future__ import annotations

import numpy as np
from qiskit.quantum_info import Pauli


I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI_MAP = {"I": I, "X": X, "Y": Y, "Z": Z}


def manual_tensor_product(label: str) -> np.ndarray:
    """Build a Pauli-string matrix by hand using Kronecker products."""
    result = PAULI_MAP[label[0]]
    for symbol in label[1:]:
        result = np.kron(result, PAULI_MAP[symbol])
    return result


def print_matrix(name: str, matrix: np.ndarray) -> None:
    print(f"{name} =")
    print(np.array_str(matrix, precision=2, suppress_small=True))
    print()


def compare_qiskit_and_manual(label: str) -> None:
    qiskit_matrix = Pauli(label).to_matrix()
    manual_matrix = manual_tensor_product(label)
    print(f"Label: {label}")
    print_matrix("Qiskit", qiskit_matrix)
    print_matrix("Manual", manual_matrix)
    print(f"Matches: {np.allclose(qiskit_matrix, manual_matrix)}")
    print("-" * 60)


def ordering_demo() -> None:
    print("Qiskit ordering demo")
    print("Pauli('IZ') means I kron Z, where the rightmost symbol acts on qubit 0.")
    print("Pauli('ZI') means Z kron I.")
    print("-" * 60)

    pauli_iz = Pauli("IZ").to_matrix()
    pauli_zi = Pauli("ZI").to_matrix()

    print_matrix("Pauli('IZ')", pauli_iz)
    print_matrix("Pauli('ZI')", pauli_zi)
    print(f"Are they equal? {np.allclose(pauli_iz, pauli_zi)}")
    print()


def tensor_operator_demo() -> None:
    left = Pauli("I")
    right = Pauli("Z")
    tensored = left ^ right
    print("Tensor-product operator demo")
    print(f"(Pauli('I') ^ Pauli('Z')).to_label() = {tensored.to_label()}")
    print()


def self_checks() -> None:
    assert np.allclose(Pauli("IZ").to_matrix(), np.kron(I, Z))
    assert np.allclose(Pauli("ZI").to_matrix(), np.kron(Z, I))
    assert not np.allclose(Pauli("IZ").to_matrix(), Pauli("ZI").to_matrix())
    assert (Pauli("I") ^ Pauli("Z")).to_label() == "IZ"
    assert np.allclose(Pauli("XYZ").to_matrix(), manual_tensor_product("XYZ"))


def exercise_prompts() -> None:
    print("Practice prompts")
    print("1. Predict the 4x4 matrix for Pauli('XY') before running it.")
    print("2. Replace 'XYZ' in self_checks() with 'YZI' and verify the matrix by hand.")
    print("3. Explain why Pauli('IZ') and Pauli('ZI') are different even though both contain I and Z.")
    print()


def main() -> None:
    ordering_demo()
    for label in ["I", "X", "Y", "Z", "IZ", "ZI", "XY", "XYZ"]:
        compare_qiskit_and_manual(label)
    tensor_operator_demo()
    self_checks()
    print("Self-checks passed.")
    print()
    exercise_prompts()


if __name__ == "__main__":
    main()
