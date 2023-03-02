import util
from Question import Question
from Triangle import Triangle


def generate() -> Question:
	triangle = Triangle()
	missing_property = util.random_element(["side", "angle"])

	angle_a_label = angle_b_label = angle_c_label = ""
	side_a_label = side_b_label = side_c_label = ""
	answer = 0.0

	known_sides: list[str] = []
	known_angles: list[str] = []

	if missing_property == "side":
		known_angles.extend(util.random_n_elements(["a", "b", "c"], 2))
		# TODO: Fix type issues
		known_sides.extend(util.random_element(known_angles))  # type: ignore
		missing_side = util.list_difference(known_sides, known_angles)[0]  # type: ignore

		angle_a_label = str(round(triangle.angle_a, 2)) if "a" in known_angles else ""
		angle_b_label = str(round(triangle.angle_b, 2)) if "b" in known_angles else ""
		angle_c_label = str(round(triangle.angle_c, 2)) if "c" in known_angles else ""

		side_a_label = "𝑥" if missing_side == "a" else str(round(triangle.side_a, 2)) if "a" in known_sides else ""
		side_b_label = "𝑥" if missing_side == "b" else str(round(triangle.side_b, 2)) if "b" in known_sides else ""
		side_c_label = "𝑥" if missing_side == "c" else str(round(triangle.side_c, 2)) if "c" in known_sides else ""

		match missing_side:
			case "a":
				answer = round(triangle.side_a, 2)
			case "b":
				answer = round(triangle.side_b, 2)
			case "c":
				answer = round(triangle.side_c, 2)

	elif missing_property == "angle":
		known_angles.extend(util.random_element(["a", "b", "c"]))
		known_sides.extend(util.random_n_elements(["a", "b", "c"], 2))
		missing_angle = util.list_difference(known_sides, known_angles)[0]

		side_a_label = str(round(triangle.side_a, 2)) if "a" in known_sides else ""
		side_b_label = str(round(triangle.side_b, 2)) if "b" in known_sides else ""
		side_c_label = str(round(triangle.side_c, 2)) if "c" in known_sides else ""

		angle_a_label = "𝑥" if missing_angle == "a" else str(round(triangle.angle_a, 2)) if "a" in known_angles else ""
		angle_b_label = "𝑥" if missing_angle == "b" else str(round(triangle.angle_b, 2)) if "b" in known_angles else ""
		angle_c_label = "𝑥" if missing_angle == "c" else str(round(triangle.angle_c, 2)) if "c" in known_angles else ""

		match missing_angle:
			case "a":
				answer = round(triangle.angle_a, 2)
			case "b":
				answer = round(triangle.angle_b, 2)
			case "c":
				answer = round(triangle.angle_c, 2)

	print(f"Sine rule: {triangle}")

	return Question(
		"\\text{Find the value of 𝑥.}",
		f"x = {answer}",
		"/question_images/triangle?"
		f"side_a={side_a_label}&"
		f"side_b={side_b_label}&"
		f"side_c={side_c_label}&"
		f"angle_a={angle_a_label}&"
		f"angle_b={angle_b_label}&"
		f"angle_c={angle_c_label}"
	)
