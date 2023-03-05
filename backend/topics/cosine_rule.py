import util
from Question import Question
from Triangle import Triangle


def generate() -> Question:
	missing_property = util.random_element(["angle"])
	missing_side = known_angle = ""
	angle_a_label = angle_b_label = angle_c_label = ""
	side_a_label = side_b_label = side_c_label = ""
	answer = 0.0

	triangle = Triangle()

	print(f"Cosine rule: {triangle}")

	if missing_property == "side":
		known_sides = util.random_n_elements(["a", "b", "c"], 2)
		missing_side = util.list_difference(known_sides, ["a", "b", "c"])[0]
		known_angle = missing_side

		if missing_side == "a":
			answer = round(triangle.side_a, 2)

		if missing_side == "b":
			answer = round(triangle.side_b, 2)

		if missing_side == "c":
			answer = round(triangle.side_c, 2)

		angle_a_label = str(round(triangle.angle_a, 1)) if "a" == known_angle else ""
		angle_b_label = str(round(triangle.angle_b, 1)) if "b" == known_angle else ""
		angle_c_label = str(round(triangle.angle_c, 1)) if "c" == known_angle else ""

		side_a_label = "𝑥" if missing_side == "a" else str(round(triangle.side_a, 1)) if "a" in known_sides else ""
		side_b_label = "𝑥" if missing_side == "b" else str(round(triangle.side_b, 1)) if "b" in known_sides else ""
		side_c_label = "𝑥" if missing_side == "c" else str(round(triangle.side_c, 1)) if "c" in known_sides else ""

	else:
		missing_angle = util.random_element(["a", "b", "c"])

		angle_a_label = "𝑥" if "a" == missing_angle else ""
		angle_b_label = "𝑥" if "b" == missing_angle else ""
		angle_c_label = "𝑥" if "c" == missing_angle else ""

		side_a_label = str(round(triangle.side_a, 1))
		side_b_label = str(round(triangle.side_b, 1))
		side_c_label = str(round(triangle.side_c, 1))

		if missing_angle == "a":
			answer = round(triangle.angle_a, 2)

		elif missing_angle == "b":
			answer = round(triangle.angle_b, 2)

		elif missing_angle == "c":
			answer = round(triangle.angle_c, 2)

	return Question(
		"\\text{Find the value of 𝑥.}",
		str(answer),
		"/question_images/triangle?"
		f"angle_a={angle_a_label}&"
		f"angle_b={angle_b_label}&"
		f"angle_c={angle_c_label}&"
		f"side_a={side_a_label}&"
		f"side_b={side_b_label}&"
		f"side_c={side_c_label}"
	)
