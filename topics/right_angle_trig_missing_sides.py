from Question import Question
from RightAngleTriangle import RightAngleTriangle
from util import random_element


def generate():
	triangle = RightAngleTriangle()

	sides = ["a", "b", "c"]
	angles = ["a", "b"]

	known_side = random_element(sides)
	known_angle = random_element(angles)

	angles.remove(known_angle)
	sides.remove(known_side)

	missing_side = random_element(sides)

	sides.remove(missing_side)

	answer = None

	match missing_side:
		case "a":
			answer = triangle.side_a
		case "b":
			answer = triangle.side_b
		case "c":
			answer = triangle.side_c

	side_a_label = None
	side_b_label = None
	side_c_label = None

	if missing_side == "a":
		side_a_label = "x"
	if missing_side == "b":
		side_b_label = "x"
	if missing_side == "c":
		side_c_label = "x"

	image = triangle.create_image(sides, angles, side_a_label, side_b_label, side_c_label)

	return Question("Find x.", f"x = {round(answer, 1)}", image)
