from Circle import Circle
from Question import Question
from util import random_bool


def generate():
	# TODO: Finding area/perimeter when given radius/diameter
	circle = Circle()
	rounded_radius = round(circle.radius, 2)
	rounded_diameter = round(circle.diameter, 2)
	rounded_area = round(circle.area, 2)

	show_radius = random_bool()

	if show_radius:
		question = f"\\text{{Shown below is a circle with a radius of {rounded_radius}. Calculate the area of the circle.}}"
		image_url = f"/question_images/circle?radius={rounded_radius}"
	else:
		question = f"\\text{{Shown below is a circle with a diameter of {rounded_diameter}. Calculate the area of the circle.}}"
		image_url = f"/question_images/circle?diameter={rounded_diameter}"

	answer = f"{rounded_area}cm^2"

	return Question(question, answer, image_url)
