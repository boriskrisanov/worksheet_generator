from sympy import symbols, latex, expand

import util
from Question import Question


def formats(difficulty: int) -> list:
	x = symbols("x")

	b = util.randint_not_zero(-5, 15)
	a = util.randint_not_zero(-5, 15)
	c = util.randint_not_zero(-5, 15)
	d = util.randint_not_zero(-5, 15)
	e = util.randint_not_zero(-5, 15)
	f = util.randint_not_zero(-5, 15)

	match difficulty:
		case 1:
			# TODO
			pass

		case 2:
			return [
				(a * x + b) * (c * x + d),  # (ax + b)(cx + d)
				(a * x + b) * (c + d * x),  # (ax + b)(c + dx)
				(a + b * x) * (c + d * x),  # (a + bx)(c + dx)
				(a + b * x) * (c * x + d)  # (a + bx)(cx + d)
			]

		case 3:
			return [
				(a * x + b) * (c * x + d) * (e * x + f),  # (ax + b)(cx + d)(ex + f)
				(a + b * x) * (c * x + d) * (e * x + f),  # (a + bx)(cx + d)(ex + f)
				(a * x + b) * (c + d * x) * (e * x + f)  # (ax + b)(c + dx)(ex + f)
				# TODO: Add more formats
			]

	return []


def generate(difficulty: int) -> Question:
	chosen_format = util.random_element(formats(difficulty))
	question = "\\text{Expand and simplify: } " + latex(chosen_format)

	answer = latex(expand(chosen_format))

	return Question(question, answer)
