from Question import Question
from RightAngleTriangle import RightAngleTriangle
from util import random_element


def generate():
	triangle = RightAngleTriangle()

	missing_side = random_element(["a", "b", "c"])

	side_a_label = None
	side_b_label = None
	side_c_label = None

	answer = None

	match missing_side:
		case "a":
			side_a_label = "x"
			answer = triangle.side_a
		case "b":
			side_b_label = "x"
			answer = triangle.side_b
		case "c":
			side_c_label = "x"
			answer = triangle.side_c

	image = triangle.create_image([], ["a", "b"], side_a_label, side_b_label, side_c_label)

	return Question("Find x.", f"x = {round(answer, 2)}", image)
