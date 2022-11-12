from sympy import symbols, Eq, EmptySet, Complexes, solveset, Reals, simplify, latex

from backend.Question import Question
from backend.util import randint_not_zero, random_element


def coefficients():
	min = -10
	max = 20

	a = randint_not_zero(min, max)
	b = randint_not_zero(min, max)
	c = randint_not_zero(min, max)
	d = randint_not_zero(min, max)

	return a, b, c, d


def formats():
	a, b, c, d, x = symbols("a b c d x")
	a, b, c, d = coefficients()

	return [
		Eq(a * x ** 2 + b * x + c, 0),
		Eq(a * x ** 2 + b * x + c, d),
	]


def generate() -> Question:
	while True:
		# Keep generating equations until the equation has a solution

		equation = random_element(formats())

		solution = solveset(equation, domain=Reals)

		if solution == EmptySet or solution == Complexes:
			# No solutions, generate a new equation
			continue

		answer = ""

		num_solutions = len(solution.args)
		if num_solutions == 1:
			solution = simplify(solution.args[0]).round(2)
			answer = f"x = {solution}"
		elif num_solutions == 2:
			solution1 = simplify(solution.args[0]).round(2)
			solution2 = simplify(solution.args[1]).round(2)
			answer = f"\\\\ x_1 = {solution1} \\\\ x_2 = {solution2}"

		equation = latex(equation)
		question = Question(f"{equation} \\\\ \\text{{Find the possible values of 𝑥.}}", answer)
		return question
