# TO_DO - maybe use namedtuple to make this cleaner

from pprint import pprint
from typing import List, Tuple

import sympy
from sympy.abc import x

test_values = [(2, 1942), (4, 3402), (6, 5614)]


def buildBasisPolynomials(points: List[Tuple[int, int]]) -> List[sympy.poly]:
    basis_polynomials = []
    for current_index, value in enumerate(points):
        inner_index = -1
        current_eq = 1
        for x_y in points:
            inner_index += 1
            if current_index == inner_index:  # Can't work on the same pairing
                continue
            current_eq *= sympy.poly(
                (x - x_y[0]) / (value[0] - x_y[0])
            )  # Continue building lagrange basis for this value
        basis_polynomials.append(current_eq)
    return basis_polynomials


def buildPolynomial(points: List[Tuple[int, int]], basis_polynomials: List[sympy.poly]) -> sympy.poly:
    sum_polynomial = 0
    for x_y, polynomial in zip(points, basis_polynomials):
        sum_polynomial += x_y[1] * polynomial
    return sum_polynomial


def main() -> None:
    print("[+] Working from points:")
    for point in test_values:
        print(f"\t- {point}")

    print("[+] Building basis polynomials")
    basis_polynomials = buildBasisPolynomials(test_values)

    print("[+] Building polynomial from basis polynomials")
    recoveredPolynomial = buildPolynomial(test_values, basis_polynomials)
    secret = recoveredPolynomial.eval(0)
    print(f"[+] Secret value is {secret}")


if __name__ == "__main__":
    main()
