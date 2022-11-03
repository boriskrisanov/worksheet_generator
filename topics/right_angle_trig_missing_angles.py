from Question import Question
from RightAngleTriangle import RightAngleTriangle
from util import random_element


def generate():
	triangle = RightAngleTriangle()

	sides = ["a", "b", "c"]
	hidden_side = random_element(sides)
	sides.remove(hidden_side)

	angles = ["a", "b"]

	missing_angle = random_element(angles)
	angles.remove(missing_angle)
	hidden_angles = angles

	answer = None
	angle_a_label = None
	angle_b_label = None

	match missing_angle:
		case "a":
			answer = triangle.angle_a
			angle_a_label = "x"
		case "b":
			answer = triangle.angle_b
			angle_b_label = "x"

	image = triangle.create_image([hidden_side], hidden_angles, None, None, None, angle_a_label, angle_b_label)

	return Question("Find x.", f"x = {round(answer, 1)}", image)
