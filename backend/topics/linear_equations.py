from sympy import symbols, Eq, Add, solveset, EmptySet, Complexes, Rational, latex

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

	return a, b, c, d


def formats(difficulty: int):
	a, b, c, d, x = symbols("a b c d x")
	a, b, c, d = coefficients(difficulty)

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


def generate(difficulty=1) -> Question:
	while True:
		# Keep generating equations until the equation has a solution
		equation: Eq = random_element(formats(difficulty))
		solution = solveset(equation)

		if solution == EmptySet or solution == Complexes:
			# No solutions, generate a new equation
			continue

		equation_str = latex(equation)
		question_str = f"{equation_str} \\\\ \\text{{Find the value of 𝑥.}}"
		answer = "x = " + latex(solution.args[0])
		question = Question(question_str, answer)
		return question
