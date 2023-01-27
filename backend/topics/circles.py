import util
from Circle import Circle
from Question import Question


def _generate_circle_question_missing_area(radius: float, diameter: float, area: float, perimeter: float) -> Question:
	question = image_url = ""

	known_attribute = util.random_element(["radius", "diameter", "perimeter"])

	match known_attribute:
		case "radius":
			image_url = f"/question_images/circle?radius={radius}"
			question = f"\\text{{Shown below is a circle with a radius of {radius}. Calculate the area of the circle.}}"

		case "diameter":
			question = f"\\text{{Shown below is a circle with a diameter of {diameter}. Calculate the area of the circle.}}"
			image_url = f"/question_images/circle?diameter={diameter}"

		case "perimeter":
			question = f"\\text{{Shown below is a circle with a perimeter of {perimeter}. Calculate the area of the circle.}}"
			image_url = f"/question_images/circle"

	answer = f"{area}cm^2"
	return Question(question, answer, image_url)


def _generate_circle_question_missing_perimeter(radius: float, diameter: float, area: float, perimeter: float) -> Question:
	question = image_url = ""

	known_attribute = util.random_element(["radius", "diameter", "area"])

	match known_attribute:
		case "radius":
			image_url = f"/question_images/circle?radius={radius}"
			question = f"\\text{{Shown below is a circle with a radius of {radius}. Calculate the perimeter of the circle.}}"

		case "diameter":
			question = f"\\text{{Shown below is a circle with a diameter of {diameter}. Calculate the perimeter of the circle.}}"
			image_url = f"/question_images/circle?diameter={diameter}"

		case "area":
			question = f"\\text{{Shown below is a circle with an area of {area}. Calculate the perimeter of the circle.}}"
			image_url = f"/question_images/circle"

	answer = str(perimeter)
	return Question(question, answer, image_url)


def _generate_circle_question_missing_radius(radius: float, area: float, perimeter: float) -> Question:
	question = image_url = ""

	known_attribute = util.random_element(["perimeter", "area"])

	match known_attribute:
		case "perimeter":
			image_url = f"/question_images/circle"
			question = f"\\text{{Shown below is a circle with a perimeter of {perimeter}. Calculate the radius of the circle.}}"

		case "area":
			question = f"\\text{{Shown below is a circle with an area of {area}. Calculate the radius of the circle.}}"
			image_url = f"/question_images/circle"

	answer = str(radius)
	return Question(question, answer, image_url)


def _generate_circle_question_missing_diameter(diameter: float, area: float, perimeter: float) -> Question:
	question = image_url = ""

	known_attribute = util.random_element(["perimeter", "area"])

	match known_attribute:
		case "perimeter":
			image_url = f"/question_images/circle"
			question = f"\\text{{Shown below is a circle with a perimeter of {perimeter}. Calculate the diameter of the circle.}}"

		case "area":
			question = f"\\text{{Shown below is a circle with an area of {area}. Calculate the diameter of the circle.}}"
			image_url = f"/question_images/circle"

	answer = str(diameter)
	return Question(question, answer, image_url)


def generate():
	circle = Circle()
	rounded_radius = round(circle.radius, 2)
	rounded_diameter = round(circle.diameter, 2)
	rounded_area = round(circle.area, 2)
	rounded_perimeter = round(circle.circumference, 2)

	missing_attribute = util.random_element(["area", "perimeter", "radius", "diameter"])

	match missing_attribute:
		case "area":
			return _generate_circle_question_missing_area(rounded_radius, rounded_diameter, rounded_area, rounded_perimeter)

		case "perimeter":
			return _generate_circle_question_missing_perimeter(rounded_radius, rounded_diameter, rounded_area, rounded_perimeter)

		case "radius":
			return _generate_circle_question_missing_radius(rounded_radius, rounded_area, rounded_perimeter)

		case "diameter":
			return _generate_circle_question_missing_diameter(rounded_diameter, rounded_area, rounded_perimeter)
