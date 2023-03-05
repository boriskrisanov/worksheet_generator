import util
from Question import Question
from Triangle import Triangle


def generate() -> Question:
	missing_property = util.random_element(["side, angle"])
	missing_side = known_angle = answer = ""
	triangle = Triangle()

	print(f"Cosine rule: {triangle}")

	# if missing_property == "side":
	if True:
		known_sides = util.random_n_elements(["a", "b", "c"], 2)
		missing_side = util.list_difference(known_sides, ["a", "b", "c"])[0]
		known_angle = missing_side

		if missing_side == "a":
			answer = str(round(triangle.side_a, 2))

		if missing_side == "b":
			answer = str(round(triangle.side_b, 2))

		if missing_side == "c":
			answer = str(round(triangle.side_c, 2))

		angle_a_label = str(round(triangle.angle_a, 1)) if "a" == known_angle else ""
		angle_b_label = str(round(triangle.angle_b, 1)) if "b" == known_angle else ""
		angle_c_label = str(round(triangle.angle_c, 1)) if "c" == known_angle else ""

		side_a_label = "𝑥" if missing_side == "a" else str(round(triangle.side_a, 1)) if "a" in known_sides else ""
		side_b_label = "𝑥" if missing_side == "b" else str(round(triangle.side_b, 1)) if "b" in known_sides else ""
		side_c_label = "𝑥" if missing_side == "c" else str(round(triangle.side_c, 1)) if "c" in known_sides else ""

	else:
		pass

	return Question(
		"\\text{Find the value of 𝑥.}",
		answer,
		"/question_images/triangle?"
		f"angle_a={angle_a_label}&"
		f"angle_b={angle_b_label}&"
		f"angle_c={angle_c_label}&"
		f"side_a={side_a_label}&"
		f"side_b={side_b_label}&"
		f"side_c={side_c_label}"
	)
