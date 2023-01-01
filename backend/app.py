from flask import Flask, request, send_file
from flask_cors import CORS

from Circle import Circle
from Question import Question
from RightAngleTriangle import RightAngleTriangle
from Triangle import Triangle
from topics import linear_equations, simultaneous_equations, factorising_quadratics, solving_quadratics, \
	pythagoras_theorem, right_angle_trig_missing_sides, right_angle_trig_missing_angles, simplifying, index_laws, circles, \
	expanding_brackets
from util import random_element

app = Flask(__name__)
CORS(app)


@app.route("/worksheet", methods=["POST"])
def index():
	# Get number of questions
	try:
		num_questions_str: str = request.json["questions"]  # type: ignore
		num_questions = int(num_questions_str)
		assert num_questions >= 1
		assert num_questions <= 500
	except (ValueError, AssertionError, KeyError):
		return "Bad request: questions must be an integer between 1 and 500", 400

	# Get topics
	try:
		topics = request.json["topics"]  # type: ignore
	except KeyError:
		return "Bad request: select at least one topic", 400

	questions: list[Question] = []

	for i in range(num_questions):
		selected_topic: dict[str, str] = random_element(topics)
		try:
			difficulty = int(selected_topic["difficulty"])
		except KeyError:
			difficulty = 1
		except ValueError:
			return "Bad request: difficulty must be an integer", 400

		try:
			name = selected_topic["name"]
		except KeyError:
			return "Bad request", 400

		match name:
			case "linear_equations":
				questions.append(linear_equations.generate(difficulty))
			case "simultaneous_equations":
				questions.append(simultaneous_equations.generate())
			case "factorising_quadratics":
				questions.append(factorising_quadratics.generate())
			case "solving_quadratics":
				questions.append(solving_quadratics.generate())
			case "pythagoras_theorem":
				questions.append(pythagoras_theorem.generate())
			case "right_angle_trig_missing_sides":
				questions.append(right_angle_trig_missing_sides.generate())
			case "right_angle_trig_missing_angles":
				questions.append(right_angle_trig_missing_angles.generate())
			case "simplifying":
				questions.append(simplifying.generate())
			case "index_laws":
				questions.append(index_laws.generate(difficulty))
			case "circles":
				questions.append(circles.generate())
			case "expanding_brackets":
				questions.append(expanding_brackets.generate(difficulty))

	questions_json = [question.json() for question in questions]

	return {
		"questions": questions_json
	}


@app.route("/question_images/right_angle_triangle", methods=["GET"])
def right_angle_triangle_question_image():
	hidden_sides = []
	hidden_angles = []

	side_a = request.args.get("side_a")
	side_b = request.args.get("side_b")
	side_c = request.args.get("side_c")

	angle_a = request.args.get("angle_a")
	angle_b = request.args.get("angle_b")

	if not side_a:
		hidden_sides.append("a")
	if not side_b:
		hidden_sides.append("b")
	if not side_c:
		hidden_sides.append("c")

	if not angle_a:
		hidden_angles.append("a")
	if not angle_b:
		hidden_angles.append("b")

	triangle = RightAngleTriangle()

	image = triangle.create_image(hidden_sides, hidden_angles, side_a, side_b, side_c, angle_a, angle_b)

	return send_file(image, "image/webp")


@app.route("/question_images/triangle", methods=["GET"])
def triangle_question_image():
	side_a_label = request.args.get("side_a")
	side_b_label = request.args.get("side_b")
	side_c_label = request.args.get("side_c")

	angle_a_label = request.args.get("angle_a")
	angle_b_label = request.args.get("angle_b")
	angle_c_label = request.args.get("angle_c")

	triangle = Triangle()
	image = triangle.create_image(
		side_a_label,
		side_b_label,
		side_c_label,

		angle_a_label,
		angle_b_label,
		angle_c_label,

		show_angle_a=angle_a_label is not None,
		show_angle_b=angle_b_label is not None,
		show_angle_c=angle_c_label is not None
	)

	return send_file(image, "image/webp")


@app.route("/question_images/circle", methods=["GET"])
def circle_question_image():
	show_diameter = show_radius = False

	diameter = request.args.get("diameter")
	if diameter:
		show_diameter = True

	radius = request.args.get("radius")
	if radius:
		show_radius = True

	circle = Circle()
	image = circle.create_image(show_diameter, show_radius, diameter, radius)

	return send_file(image, "image/webp")
