from math import sqrt
from random import uniform

from Question import Question
from util import generate_right_angle_triangle_image, random_element


def generate():
	a = round(uniform(1, 15), 1)
	b = round(uniform(1, 15), 1)
	# Side C must be greater than A and B
	c = round(uniform(max(a, b), 20), 1)

	missing_side = random_element(["a", "b", "c"])

	# Formula: c = sqrt(a^2 + b^2)

	if missing_side == "a":
		a = None
		answer = sqrt(c ** 2 - b ** 2)
	elif missing_side == "b":
		b = None
		answer = sqrt(c ** 2 - a ** 2)
	else:
		c = None
		answer = sqrt(a ** 2 + b ** 2)

	unit: str = random_element(["m", "cm"])

	if a:
		a = str(a) + unit
	if b:
		b = str(b) + unit
	if c:
		c = str(c) + unit

	image = generate_right_angle_triangle_image(a, b, c, missing_side)

	return Question("Find x.", f"x = {round(answer, 2)}", image)
