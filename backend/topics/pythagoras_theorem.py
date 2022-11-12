from backend.Question import Question
from backend.RightAngleTriangle import RightAngleTriangle
from backend.util import random_element


def generate():
	triangle = RightAngleTriangle()

	missing_side = random_element(["a", "b", "c"])

	side_a_label = round(triangle.side_a, 1)
	side_b_label = round(triangle.side_b, 1)
	side_c_label = round(triangle.side_c, 1)

	answer = None

	match missing_side:
		case "a":
			side_a_label = "𝑥"
			answer = triangle.side_a
		case "b":
			side_b_label = "𝑥"
			answer = triangle.side_b
		case "c":
			side_c_label = "𝑥"
			answer = triangle.side_c

	image = "/question_images/right_angle_triangle" \
					f"?side_a={side_a_label}" \
					f"&side_b={side_b_label}" \
					f"&side_c={side_c_label}"
	# TODO: Create image alt

	return Question("\\text{Find 𝑥.}", f"x = {round(answer, 1)}", image)
