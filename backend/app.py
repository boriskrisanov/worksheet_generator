from flask import Flask, request, send_file
from flask_cors import CORS

from Question import Question
from RightAngleTriangle import RightAngleTriangle
from topics import linear_equations, simultaneous_equations, factorising_quadratics, solving_quadratics, \
	pythagoras_theorem, right_angle_trig_missing_sides, right_angle_trig_missing_angles, simplifying, index_laws
from util import random_element

app = Flask(__name__)
CORS(app)


@app.route("/worksheet", methods=["POST"])
def index():
	# Get number of questions
	try:
		num_questions = request.json["questions"]
		num_questions = int(num_questions)
		assert num_questions >= 1
		assert num_questions <= 500
	except (ValueError, AssertionError, KeyError):
		return "Bad request: questions must be an integer between 1 and 500", 400

	# Get topics
	try:
		topics = request.json["topics"]
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
