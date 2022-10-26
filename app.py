from flask import Flask, request

from Question import Question
from topics import linear_equations, simultaneous_equations
from util import random_element

app = Flask(__name__)


@app.route("/worksheet", methods=["GET"])
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

	questions_json = [question.json() for question in questions]

	return {
		"questions": questions_json
	}
