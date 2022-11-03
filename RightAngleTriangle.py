from math import sqrt, asin, degrees
from random import uniform, randint
from uuid import uuid4

from PIL import Image, ImageDraw, ImageFont

from util import line_midpoint


class RightAngleTriangle:
	side_a: float
	side_b: float
	side_c: float

	# All angles are in degrees
	angle_a: float
	angle_b: float
	angle_c: float

	def __init__(self, min_side_len=2.0, max_side_len=16.0):
		# Generate side lengths
		self.side_a = uniform(min_side_len, max_side_len)

		# side_b = side_a ± 5
		min_side_b = self.side_a - 5
		max_side_b = self.side_a + 5
		self.side_b = uniform(min_side_b, max_side_b)

		self.side_c = sqrt(self.side_a ** 2 + self.side_b ** 2)

		# Generate angles
		self.angle_a = degrees(asin(self.side_a / self.side_c))
		self.angle_b = degrees(asin(self.side_b / self.side_c))
		self.angle_c = 90

	def get_opposite(self, angle: str):
		"""
		Returns the length of the side opposite to the angle
		:param: angle "a", "b", or "c"
		"""
		match angle:
			case "a":
				return self.side_b
			case "b":
				return self.side_a
			case "c":
				return self.side_c
			case _:
				raise Exception("Invalid angle")

	def get_adjacent(self, angle: str):
		"""
		Returns the length of the side adjacent to the angle
		:param: angle "a", "b", or "c"
		"""
		opp = self.get_opposite(angle)

		if opp == self.side_a:
			return self.side_b

		return self.side_a

	def get_hypotenuse(self):
		"""Returns the length of the hypotenuse"""
		return self.side_c

	def create_image(
					self,
					hidden_sides: list[str] = None,
					hidden_angles: list[str] = None,
					side_a_label: str = None,
					side_b_label: str = None,
					side_c_label: str = None,
					angle_a_label: str = None,
					angle_b_label: str = None,
	):
		"""
		Generates an image of the triangle and saves it in the static/question_images/ directory.

		The actual side length is generated randomly, which is why the "NOT TO SCALE" text is added.

		:param: hidden_sides The letters of the hidden sides. If a side is hidden, its length will not be displayed.
		:param: hidden_angles The letters of the hidden sides. If an angle is hidden, it will not be displayed.
		:param: side_a_label The label for side a (defaults to the length of side a and is only displayed if it isn't hidden)
		:param: side_b_label The label for side b (defaults to the length of side b and is only displayed if it isn't hidden)
		:param: side_c_label The label for side c (defaults to the length of side c and is only displayed if it isn't hidden)
		:param: angle_a_label The label for angle A (defaults to the size of angle A and is only displayed if it isn't hidden)
		:param: angle_b_label The label for angle B (defaults to the size of angle B and is only displayed if it isn't hidden)

		:returns: The URL of the image
		"""
		if not hidden_sides:
			hidden_sides = []

		if not hidden_angles:
			hidden_angles = []

		self.side_a = round(self.side_a, 1)
		self.side_b = round(self.side_b, 1)
		self.side_c = round(self.side_c, 1)

		self.angle_a = round(self.angle_a, 1)
		self.angle_b = round(self.angle_b, 1)

		width = 400
		height = 300
		image = Image.new("RGB", (width, height), color="white")

		# Draw triangle

		margin_x = 60
		margin_y = 30

		triangle_length = randint(width // 2 + margin_x, width - margin_x)
		triangle_height = randint(height // 2 + margin_y, height - margin_y)

		point1 = (margin_x, height - triangle_height)
		point2 = (margin_x, height - margin_y)
		point3 = (triangle_length, height - margin_y)

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

		if "a" not in hidden_sides:
			if not side_a_label:
				side_a_label = str(self.side_a)
			draw.text(side_a_midpoint, side_a_label, "black", font)

		if "b" not in hidden_sides:
			if not side_b_label:
				side_b_label = str(self.side_b)
			draw.text(side_b_midpoint, side_b_label, "black", font)

		if "c" not in hidden_sides:
			if not side_c_label:
				side_c_label = str(self.side_c)
			draw.text(side_c_midpoint, side_c_label, "black", font)

		# Display angles

		side_a_len = point2[1] - point1[1]
		side_b_len = point3[0] - point2[0]
		side_c_len = sqrt((side_a_len ** 2) + (side_b_len ** 2))

		radius = 40

		if "a" not in hidden_angles:
			# B = sin^-1(a / c)
			angle = asin(side_a_len / side_c_len)
			angle = degrees(angle)

			start = (point3[0] - radius, point3[1] - radius)
			end = (point3[0] + radius, point3[1] + radius)

			draw.arc([start, end], 180, 180 + angle, (0, 0, 0), 2)

			text_pos = line_midpoint(point3, side_a_midpoint)
			text_pos = line_midpoint(point3, text_pos)

			if not angle_a_label:
				angle_a_label = str(self.angle_a) + "°"

			draw.text(text_pos, angle_a_label, (0, 0, 0), font)

		if "b" not in hidden_angles:
			# A = sin^-1(b / c)
			angle = asin(side_b_len / side_c_len)
			angle = degrees(angle)

			start = (point1[0] - radius, point1[1] - radius)
			end = (point1[0] + radius, point1[1] + radius)

			draw.arc([start, end], 90 - angle, 90, (0, 0, 0), 2)

			text_pos = line_midpoint(point1, side_b_midpoint)
			text_pos = line_midpoint(point1, text_pos)

			if not angle_b_label:
				angle_b_label = str(self.angle_b) + "°"

			draw.text(text_pos, angle_b_label, (0, 0, 0), font)

		# Draw the 90deg angle

		pos = (point2[0], point2[1], point2[0] + 30, point2[1] - 30)
		draw.rectangle(pos, None, (0, 0, 0), 2)

		# Add "NOT TO SCALE" text
		draw.text((width / 2, height - 270), "NOT TO SCALE", "black", font)

		# Save image
		# TODO: Check if this file already exists

		image_url = f"/question_images/{uuid4()}.png"
		file_path = "static" + image_url

		image.save(file_path)

		# TODO: Delete the image after some time

		return image_url
