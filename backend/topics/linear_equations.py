import sympy
from sympy import symbols, Eq, Add, EmptySet, Rational, latex, solveset

from Question import Question
from util import random_element, randint_not_zero


def coefficients(difficulty: int):
	match difficulty:
		case 1:
			min = -5
			max = 10
		case 2:
			min = -10
			max = 20
		case _:
			min = -30
			max = 50

	a = randint_not_zero(min, max)
	b = randint_not_zero(min, max)
	c = randint_not_zero(min, max)
	d = randint_not_zero(min, max)
	e = randint_not_zero(min, max)
	f = randint_not_zero(min, max)
	g = randint_not_zero(min, max)
	h = randint_not_zero(min, max)

	return a, b, c, d, e, f, g, h


def formats(difficulty: int):
	x = symbols("x")
	a, b, c, d, e, f, g, h = coefficients(difficulty)

	match difficulty:
		case 1:
			return [
				# ax + b = c
				Eq(a * x + b, c),
				# a + bx = c
				Eq(a + b * x, c),
				# a + b = cx
				Eq(Add(a, b, evaluate=False), c * x),
				# ax + bx = c
				Eq(Add(a * x, b * x, evaluate=False), c),
				# ax = bx + c
				Eq(a * x, b * x + c)
			]

		case 2:
			return [
				# ax + bx = cx + d
				Eq(Add(a * x, b * x, evaluate=False), Add(c * x, d, evaluate=False)),
				# ax = bx + cx + d
				Eq(a * x, Add(b * x, c * x, evaluate=False) + d),
				# ax + b/d = cx
				Eq(a * x + Rational(b, d), c * x)
			]

		case 3:
			return [
				# (ax + b) / (cx) = dx + e
				Eq(a * x + b / (c * x), d * x + e),
				# (ax / b) + (cx / d) = (ex / f) + g
				Eq(Add(((a * x) / b), ((c * x) / d), evaluate=False), Add(((e * x) / f), g), evaluate=False)
				# (ax / b) + (cx / d) = (ex / f) + g
			]


def generate(difficulty=1) -> Question:
	while True:
		# Keep generating equations until the equation has a solution
		equation: Eq = random_element(formats(difficulty))
		solution = solveset(equation, domain=sympy.Reals)

		if solution == EmptySet:
			# No solutions, generate a new equation
			continue

		answer = "x = " + latex(solution.args[0])

		equation_str = latex(equation)
		question_str = f"{equation_str} \\\\ \\text{{Find the value of 𝑥.}}"
		question = Question(question_str, answer)
		return question
