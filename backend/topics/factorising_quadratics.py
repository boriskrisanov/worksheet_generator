from random import randint

from sympy import symbols, Eq, EmptySet, Complexes, expand, latex

from backend.Question import Question
from backend.util import randint_not_zero


def coefficients():
	min = -10
	max = 20

	a = randint_not_zero(min, max)
	b = randint_not_zero(min, max)
	c = randint_not_zero(min, max)
	d = randint_not_zero(min, max)

	return a, b, c, d


def generate() -> Question:
	while True:
		# Keep generating equations until the equation has a solution

		should_equal_zero = bool(randint(0, 1))
		a, b, c, d, x = symbols("a, b, c, d, x")
		a, b, c, d = coefficients()

		# TODO: ax^2 + bx + c
		if should_equal_zero:
			solution = Eq((x + a) * (x + b), 0)
		else:
			solution = Eq((x + a) * (x + b), c)

		equation = expand(solution)

		if solution == EmptySet or solution == Complexes:
			# No solutions, generate a new equation
			continue

		equation = latex(equation)
		answer = latex(solution.args[0])
		question = Question(f"\\text{{Factorise}} \\: {equation}", answer)
		return question
