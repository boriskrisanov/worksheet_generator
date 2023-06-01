from sympy import latex

from Equation import Equation
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
	match difficulty:
		case 1:
			return [
				"ax + b = c",
				"a + bx = c",
				"a + b = cx",
				"ax + bx = c",
				"ax = bx + c"
			]

		case 2:
			return [
				"ax + bx = cx + d",
				"ax = bx + cx + d",
				"ax + b/d = cx"
			]

		case 3:
			return [
				"(ax + b) / (cx) = dx + e",
				"(ax / b) + (cx / d) = (ex / f) + g"
			]


def sub_coefficients(difficulty: int, equation: str):
	a, b, c, d, e, f, g, h = coefficients(difficulty)

	equation = equation.replace("a", str(a))
	equation = equation.replace("b", str(b))
	equation = equation.replace("c", str(c))
	equation = equation.replace("d", str(d))
	equation = equation.replace("e", str(e))
	equation = equation.replace("f", str(f))
	equation = equation.replace("g", str(g))
	equation = equation.replace("h", str(h))

	return equation


def generate(difficulty=1) -> Question:
	while True:
		# Keep generating equations until the equation has a solution
		selected_format = random_element(formats(difficulty))
		selected_format = sub_coefficients(difficulty, selected_format)
		equation = Equation(selected_format)

		if equation.solve() is None:
			continue

		answer = latex("𝑥 = ") + str(equation.solve())

		equation_str = str(equation)
		question_str = f"{equation_str} \\\\ \\text{{Find the value of 𝑥.}}"
		question = Question(question_str, answer)
		return question
