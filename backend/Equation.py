import re
from dataclasses import dataclass
from typing import Any

import sympy.parsing
from sympy import EmptySet


@dataclass
class MathResult:
	result: Any
	numeric_result: float | list[float]
	rounded_numeric_result: float | list[float]

	def __init__(self, result: Any):
		equation_has_one_solution = type(result) is list and len(result) == 1

		if equation_has_one_solution:
			# Set the result to the first array element since there is only one result
			self.result = result[0]
			self.numeric_result = float(self.result)
			self.rounded_numeric_result = round(self.numeric_result, 2)
		else:
			# Equation has multiple solutions, keep the result as an array
			self.result = result
			self.numeric_result = [float(r) for r in result]
			self.rounded_numeric_result = [round(r, 2) for r in self.numeric_result]

		print(f"MathResult: {str(self)}")

	def __str__(self):
		return sympy.latex(self.result)


class Equation:
	def __init__(self, equation: str):
		self.equation = equation
		self.left = equation.split("=")[0]
		self.right = equation.split("=")[1]

	def __str__(self):
		return self.equation

	def solve(self):
		left2 = self.left
		right2 = self.right

		# Replace 1x with x
		left2 = re.sub(pattern="1([Aa-zZ])", repl="\\1", string=left2)
		right2 = re.sub(pattern="1([Aa-zZ])", repl="\\1", string=right2)

		# Replace -1x with -x
		left2 = re.sub(pattern="-1([Aa-zZ])", repl="-\\1", string=left2)
		right2 = re.sub(pattern="-1([Aa-zZ])", repl="-\\1", string=right2)

		# Add a multiplication sign between letters and coefficients so that sympy can parse it
		# (for example, 4x will be replaced with 4*x).

		left2 = re.sub(pattern="(\\d+)([Aa-zZ])", repl="\\1*\\2", string=left2)
		right2 = re.sub(pattern="(\\d+)([Aa-zZ])", repl="\\1*\\2", string=right2)

		left_parsed = sympy.parsing.parse_expr(left2)
		right_parsed = sympy.parsing.parse_expr(right2)

		sympy_equation = sympy.Eq(left_parsed, right_parsed)
		solution = sympy.solvers.solve(sympy_equation)

		if solution == EmptySet:
			return None

		return MathResult(solution)
