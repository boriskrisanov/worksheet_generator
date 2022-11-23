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

	answer = 0.0

	match missing_side:
		case "a":
			answer = triangle.side_a
		case "b":
			answer = triangle.side_b
		case "c":
			answer = triangle.side_c

	angle_a_label = angle_b_label = side_a_label = side_b_label = side_c_label = ""

	if known_angle == "a":
		angle_a_label = str(round(triangle.angle_a, 1))
	if known_angle == "b":
		angle_b_label = str(round(triangle.angle_b, 1))

	if missing_side == "a":
		side_a_label = "𝑥"
	if missing_side == "b":
		side_b_label = "𝑥"
	if missing_side == "c":
		side_c_label = "𝑥"

	match known_side:
		case "a":
			side_a_label = str(round(triangle.side_a, 1))
		case "b":
			side_b_label = str(round(triangle.side_b, 1))
		case "c":
			side_c_label = str(round(triangle.side_c, 1))

	image = "/question_images/right_angle_triangle" \
					f"?side_a={side_a_label}" \
					f"&side_b={side_b_label}" \
					f"&side_c={side_c_label}" \
					f"&angle_a={angle_a_label}" \
					f"&angle_b={angle_b_label}"
	# TODO: Create image alt

	return Question("\\text{Find the value of 𝑥.}", f"x = {round(answer, 1)}", image)
