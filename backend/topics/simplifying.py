from random import randint

from sympy import simplify, parse_expr, latex

from Question import Question
from util import randint_not_zero


def generate():
	num_x_terms = randint(2, 3)
	num_y_terms = randint(2, 3)

	expression = ""

	for i in range(num_x_terms):
		coefficient = randint_not_zero(-10, 10)
		expression += f"{coefficient}*x +"

	for i in range(num_y_terms):
		coefficient = randint_not_zero(-10, 10)
		expression += f"{coefficient}*y +"

	expression = expression.rstrip(" +")

	# TODO: Convert 1x to x
	# TODO: Randomize the order of the x and y terms

	expression = parse_expr(expression, evaluate=False)

	answer = latex(simplify(expression))

	return Question(f"\\text{{Simplify}} {latex(expression)}", answer)
