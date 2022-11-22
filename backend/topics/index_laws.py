from random import randint

from Question import Question
from util import random_element, randint_not_zero


def difficulty_1():
	operator = random_element(["*", "/"])

	a = randint_not_zero(-5, 10)
	b = randint_not_zero(-5, 10)

	if operator == "*":
		question = f"x^{{{a}}} \\times x^{{{b}}}"
		answer_exponent = a + b
	else:
		question = f"\\frac{{x^{{{a}}}}} {{x^{{{b}}}}}"
		answer_exponent = a - b

	answer = f"x^{{{answer_exponent}}}"

	if answer == "x^{0}":
		answer = "1"
	if answer == "x^{1}":
		answer = "x"

	return question, answer


def difficulty_2():
	a = randint_not_zero(-5, 10)
	b = randint_not_zero(-5, 10)
	c = randint_not_zero(-5, 10)
	d = randint_not_zero(-5, 10)
	e = randint_not_zero(-5, 10)

	question = answer = ""

	match randint(0, 2):
		case 0:
			question = f"(x^{{{a}}}y^{{{b}}}x^{{{c}}}y^{{{d}}})^{{{e}}}"
			answer = f"x^{{{a * e + c * e}}}y^{{{b * e + d * e}}}"
		case 1:
			question = f"(x^{{{a}}}y^{{{b}}})^{{{c}}}"
			answer = f"x^{{{a * c}}}y^{{{b * c}}}"
		case 2:
			question = f"(x^{{{a}}}y^{{{b}}}z^{{{c}}})^{{{d}}}"
			answer = f"x^{{{a * d}}}y^{{{b * d}}}z^{{{c * d}}}"

	return question, answer


def generate(difficulty):
	question = answer = ""

	match difficulty:
		case 1:
			question, answer = difficulty_1()
		case 2:
			question, answer = difficulty_2()
		case 3:
			pass
			# TODO: Difficulty 3

	question = "\\text{Simplify} \\:" + question

	return Question(question, answer)
