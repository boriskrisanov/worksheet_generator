from math import sqrt, asin, degrees
from random import uniform, randint
from typing import Union

from PIL import Image, ImageDraw, ImageFont

from util import line_midpoint, save_pillow_image


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
					hidden_sides: Union[list[str], None] = None,
					hidden_angles: Union[list[str], None] = None,
					side_a_label: Union[str, None] = None,
					side_b_label: Union[str, None] = None,
					side_c_label: Union[str, None] = None,
					angle_a_label: Union[str, None] = None,
					angle_b_label: Union[str, None] = None,
	):
		"""
		Generates a WebP image of the triangle and returns a BytesIO object containing it.

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

		scale_multiplier = 4
		width = 400 * scale_multiplier
		height = 300 * scale_multiplier
		image = Image.new("RGB", (width, height), color="white")

		# Draw triangle

		margin_x = 60 * scale_multiplier
		margin_y = 30 * scale_multiplier

		triangle_length = randint(width // 2 + margin_x, width - margin_x)
		triangle_height = randint(height // 2 + margin_y, height - margin_y)

		point1 = (margin_x, height - triangle_height)
		point2 = (margin_x, height - margin_y)
		point3 = (triangle_length, height - margin_y)

		points = [point1, point2, point3, point1]
		draw = ImageDraw.Draw(image)
		draw.line(points, width=2 * scale_multiplier, fill="black")

		# Display side lengths

		# noinspection SpellCheckingInspection
		font = ImageFont.truetype("./fonts/NotoSansMath-Regular.ttf", 18 * scale_multiplier)

		side_a_midpoint = line_midpoint(point1, point2)
		side_b_midpoint = line_midpoint(point2, point3)
		side_c_midpoint = line_midpoint(point3, point1)

		if "a" not in hidden_sides:
			if not side_a_label:
				side_a_label = str(self.side_a)

			distance_from_edge = 10 * scale_multiplier + len(side_a_label) * 10 * scale_multiplier

			pos = (side_a_midpoint[0] - distance_from_edge, side_a_midpoint[1])
			draw.text(pos, side_a_label, "black", font)

		if "b" not in hidden_sides:
			if not side_b_label:
				side_b_label = str(self.side_b)
			draw.text(side_b_midpoint, side_b_label, "black", font)

		if "c" not in hidden_sides:
			if not side_c_label:
				side_c_label = str(self.side_c)

			pos = (side_c_midpoint[0], side_c_midpoint[1] - 30 * scale_multiplier)
			draw.text(pos, side_c_label, "black", font)

		# Display angles

		side_a_len = point2[1] - point1[1]
		side_b_len = point3[0] - point2[0]
		side_c_len = sqrt((side_a_len ** 2) + (side_b_len ** 2))

		radius = 40 * scale_multiplier

		if "a" not in hidden_angles:
			# B = sin^-1(a / c)
			angle = asin(side_a_len / side_c_len)
			angle = degrees(angle)

			start = (point3[0] - radius, point3[1] - radius)
			end = (point3[0] + radius, point3[1] + radius)

			draw.arc([start, end], 180, 180 + angle, (0, 0, 0), scale_multiplier)

			text_pos = line_midpoint(point3, side_a_midpoint)
			text_pos = line_midpoint(point3, text_pos)
			text_pos = (text_pos[0] - scale_multiplier, text_pos[1] - scale_multiplier)

			if not angle_a_label:
				angle_a_label = str(self.angle_a) + "°"

			distance_from_angle = 6 * scale_multiplier + len(angle_a_label) * 6 * scale_multiplier
			text_pos = (text_pos[0] - distance_from_angle, text_pos[1])
			draw.text(text_pos, angle_a_label, (0, 0, 0), font)

		if "b" not in hidden_angles:
			# A = sin^-1(b / c)
			angle = asin(side_b_len / side_c_len)
			angle = degrees(angle)

			start = (point1[0] - radius, point1[1] - radius)
			end = (point1[0] + radius, point1[1] + radius)

			draw.arc([start, end], 90 - angle, 90, (0, 0, 0), scale_multiplier)

			text_pos = line_midpoint(point1, side_b_midpoint)
			text_pos = line_midpoint(point1, text_pos)

			if not angle_b_label:
				angle_b_label = str(self.angle_b) + "°"

			text_pos = (text_pos[0] - 4 * len(angle_b_label) * scale_multiplier, text_pos[1])
			draw.text(text_pos, angle_b_label, (0, 0, 0), font)

		# Draw the 90deg angle

		pos2 = (point2[0], point2[1], point2[0] + 25 * scale_multiplier, point2[1] - 25 * scale_multiplier)
		draw.rectangle(pos2, None, (0, 0, 0), scale_multiplier)

		# Add "NOT TO SCALE" text
		draw.text((width / 2, height - 270 * scale_multiplier), "NOT TO SCALE", "black", font)

		# Save image
		return save_pillow_image(image)
