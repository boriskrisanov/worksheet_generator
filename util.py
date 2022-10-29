from os import path, mkdir
from random import randint
from typing import Union
from uuid import uuid4

from PIL import ImageDraw, ImageFont, Image


def random_element(array: list):
	"""Returns a random element from the array"""
	if not len(array):
		return None
	index = randint(0, len(array) - 1)
	return array[index]


def randint_not_zero(min: int, max: int):
	"""Returns a random non-zero integer >= min and <= max"""
	n = randint(min, max)
	while n == 0:
		n = randint(min, max)
	return n


def create_question_images_dir():
	"""Creates the directory static/question_images/ if it doesn't exist"""
	if not path.exists("static/question_images/"):
		mkdir("static/question_images/")


def line_midpoint(point1: tuple[float, float], point2: tuple[float, float]):
	"""Returns the coordinates of the midpoint of the line"""
	x = (point1[0] + point2[0]) / 2
	y = (point1[1] + point2[1]) / 2
	return x, y


def generate_right_angle_triangle_image(
				side_a: Union[str, None] = None,
				side_b: Union[str, None] = None,
				side_c: Union[str, None] = None,
				missing_side: Union[str, None] = None,
				missing_side_label: Union[str] = "x",
):
	"""
	Generates an image of a right angle triangle and saves it in the static/question_images/ directory.

	The labels will only be displayed if they are defined.

	The actual side length is generated randomly, which is why the "NOT TO SCALE" text is added.

	:param side_a The label for side A
	:param side_b The label for side B
	:param side_c The label for side C
	:param missing_side: "a", "b" or "c"
	:param missing_side_label: What the missing side will be labelled as (defaults to "x")
	:returns: The URL of the image
	"""
	width = 400
	height = 300
	image = Image.new("RGB", (width, height), color="white")

	# Draw triangle

	margin = 50

	triangle_length = randint(width // 2 + margin, width - margin)
	triangle_height = randint(height // 2 + margin, height - margin)

	point1 = (margin, height - triangle_height)
	point2 = (margin, height - margin)
	point3 = (triangle_length, height - margin)

	points = [point1, point2, point3, point1]
	draw = ImageDraw.Draw(image)
	draw.line(points, width=4, fill="black")

	# Display side lengths

	font = ImageFont.truetype("arial.ttf", 18)

	side_a_midpoint = line_midpoint(point1, point2)
	side_b_midpoint = line_midpoint(point2, point3)
	side_c_midpoint = line_midpoint(point3, point1)

	side_a_midpoint = (side_a_midpoint[0] - 48, side_a_midpoint[1])
	side_b_midpoint = (side_b_midpoint[0] - 20, side_b_midpoint[1] + 10)
	side_c_midpoint = (side_c_midpoint[0], side_c_midpoint[1] - 40)

	if side_a:
		draw.text(side_a_midpoint, side_a, (0, 0, 0), font)
	if side_b:
		draw.text(side_b_midpoint, side_b, (0, 0, 0), font)
	if side_c:
		draw.text(side_c_midpoint, side_c, (0, 0, 0), font)

	# Label missing side

	if missing_side:
		if missing_side == "a":
			missing_side_midpoint = side_a_midpoint
		elif missing_side == "b":
			missing_side_midpoint = side_b_midpoint
		else:
			missing_side_midpoint = side_c_midpoint

		draw.text(missing_side_midpoint, missing_side_label, (0, 0, 0), font)

	# Add "NOT TO SCALE" text
	draw.text((width / 2, height - 270), "NOT TO SCALE", (0, 0, 0), font)

	# TODO: Draw the 90deg angle to show that this is a right angle triangle

	# Save image
	# TODO: Check if this file already exists

	image_url = f"/question_images/{uuid4()}.png"
	file_path = "static" + image_url

	image.save(file_path)

	# TODO: Delete the image after some time

	return image_url
