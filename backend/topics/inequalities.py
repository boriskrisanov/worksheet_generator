from sympy import symbols, solve, latex

import util
from Question import Question


def formats(difficulty: int) -> list:
	a = util.randint_not_zero(-10, 20)
	b = util.randint_not_zero(-10, 20)
	c = util.randint_not_zero(-10, 20)
	d = util.randint_not_zero(-10, 20)

	x = symbols("x")

	match difficulty:
		case 1:
			return [
				# ax > b
				a * x > b,
				a * x >= b,
				a * x < b,
				a * x <= b,
				# a > bx
				a > b * x,
				a >= b * x,
				a < b * x,
				a <= b * x,
				# ax + b > c
				a * x + b > c,
				a * x + b >= c,
				a * x + b < c,
				a * x + b <= c,
				# a + bx > c
				a + b * x > c,
				a + b * x >= c,
				a + b * x < c,
				a + b * x <= c,
				# a > bx + c
				a > b * x + c,
				a >= b * x + c,
				a < b * x + c,
				a <= b * x + c,
				# a > b + cx
				a > b + c * x,
				a >= b + c * x,
				a < b + c * x,
				a <= b + c * x
			]
		case 2:
			return [
				# ax + b > cx + d
				a * x + b > c * x + d,
				a * x + b >= c * x + d,
				a * x + b < c * x + d,
				a * x + b <= c * x + d,
				# a + bx > cx + d
				a + b * x > c * x + d,
				a + b * x >= c * x + d,
				a + b * x < c * x + d,
				a + b * x <= c * x + d,
				# ax + b > c + dx
				a * x + b > c + d * x,
				a * x + b >= c + d * x,
				a * x + b < c + d * x,
				a * x + b <= c + d * x,
				# a + bx > c + dx
				a + b * x > c + d * x,
				a + b * x >= c + d * x,
				a + b * x < c + d * x,
				a + b * x <= c + d * x
			]
		case 3:
			# TODO
			return []
		case _:
			raise Exception("Invalid difficulty")


def generate(difficulty: int) -> Question:
	inequality = util.random_element(formats(difficulty))
	solution = solve(inequality).args

	# TODO: Ignore anything with infinity
	# TODO: Format the answer properly

	question_text = latex(inequality) + "\\\\ \\text{State the range of values for which 𝑥 is valid.}"

	return Question(question_text, latex(solution))
