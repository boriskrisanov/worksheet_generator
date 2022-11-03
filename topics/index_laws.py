from random import randint

from sympy import parse_expr, pretty, simplify, latex

from Question import Question
from util import random_element


def generate():
	num_terms = randint(2, 4)

	expression = ""

	for i in range(num_terms):
		exponent = randint(-5, 5)
		sign = random_element(["+", "-"])
		expression += f"x**{exponent} {sign}"

	expression = expression.rstrip("+")
	expression = expression.rstrip("-")

	question = parse_expr(expression, evaluate=False)
	answer = simplify(question)

	question = f"Simplify {pretty(question)}"
	answer = latex(answer)

	return Question(question, answer)
