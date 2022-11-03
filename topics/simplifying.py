from random import randint

from sympy import symbols, simplify, pretty, parse_expr

from Question import Question
from util import randint_not_zero


def generate():
	num_x_terms = randint(2, 3)
	num_y_terms = randint(2, 3)

	x, y = symbols("x y")

	expression = ""

	for i in range(num_x_terms):
		coefficient = randint_not_zero(-10, 10)
		expression += f"{coefficient}*x +"

	for i in range(num_y_terms):
		coefficient = randint_not_zero(-10, 10)
		expression += f"{coefficient}*y +"

	expression = expression.rstrip(" +")

	expression = parse_expr(expression, evaluate=False)

	answer = simplify(expression)
	answer = pretty(answer)

	return Question(f"Simplify {pretty(expression)}", answer)
