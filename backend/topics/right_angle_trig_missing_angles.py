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

	answer = None
	angle_a_label = ""
	angle_b_label = ""

	match missing_angle:
		case "a":
			answer = triangle.angle_a
			angle_a_label = "𝑥"
		case "b":
			answer = triangle.angle_b
			angle_b_label = "𝑥"

	side_a_label = ""
	side_b_label = ""
	side_c_label = ""

	if "a" in sides:
		side_a_label = round(triangle.side_a, 1)
	if "b" in sides:
		side_b_label = round(triangle.side_b, 1)
	if "c" in sides:
		side_c_label = round(triangle.side_c, 1)

	# TODO: Create image alt
	image = "/question_images/right_angle_triangle" \
					f"?side_a={side_a_label}" \
					f"&side_b={side_b_label}" \
					f"&side_c={side_c_label}" \
					f"&angle_a={angle_a_label}" \
					f"&angle_b={angle_b_label}"

	return Question("\\text{Find the value of 𝑥.}", f"x = {round(answer, 1)}", image)
