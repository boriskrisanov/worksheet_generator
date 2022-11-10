from sympy import symbols, Eq, EmptySet, Complexes, linsolve, latex

from backend.Question import Question
from backend.util import random_element, randint_not_zero


def coefficients():
	min = -10
	max = 20

	a = randint_not_zero(min, max)
	b = randint_not_zero(min, max)
	c = randint_not_zero(min, max)
	d = randint_not_zero(min, max)
	e = randint_not_zero(min, max)
	f = randint_not_zero(min, max)

	return a, b, c, d, e, f


def formats():
	a, b, c, d, e, f, x, y = symbols("a b c d e f x y")
	a, b, c, d, e, f = coefficients()

	return (
		[
			# ax + by = c
			Eq(a * x + b * y, c),
			# a + by = cx
			Eq(a + b * y, c * x),
			# ay = bx + c
			Eq(a * y, b * x + c)
		],
		[
			# dx + ey = f
			Eq(d * x + e * y, f),
			# d + ey = fx
			Eq(d + e * y, f * x),
			# dy = ex + f
			Eq(d * y, e * x + f)
		]
	)


def generate() -> Question:
	while True:
		# Keep generating equations until the equation has a solution
		selected_format = formats()

		equation1: Eq = random_element(selected_format[0])
		equation2: Eq = random_element(selected_format[1])

		x, y = symbols("x y")
		solution = linsolve([equation1, equation2], (x, y))

		if solution == EmptySet or solution == Complexes:
			# No solutions, generate a new equation
			continue

		equation = latex(equation1) + "\\\\" + latex(equation2)
		x = latex(solution.args[0][0])
		y = latex(solution.args[0][1])
		question = Question(equation + "\\\\ \\text{Find the value of 𝑥 and 𝑦.}", f"\\\\x = {x} \\\\ y = {y}")
		return question
