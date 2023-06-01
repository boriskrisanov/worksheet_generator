import random
from dataclasses import dataclass
from io import BytesIO
from math import sqrt, degrees
from random import randint
from typing import Optional

from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw
from sympy.geometry.line import Line

import util
from trig_util import *

# Draws extra lines and info on the triangle image to make debugging easier
# TODO: Maybe this should be an environment variable
DEBUG_TRIANGLE_DRAW = False


@dataclass
class Triangle:
	side_a: float
	side_b: float
	side_c: float

	# All angles are in degrees
	angle_a: float
	angle_b: float
	angle_c: float

	def __init__(self, min_side_len=5.0, max_side_len=16.0):
		# When a triangle is generated, it might be mathematically incorrect or have small side lengths/angles.
		# The loop will keep running until a good triangle is generated, at which point we will break out of the loop.
		while True:
			self.side_a = random.uniform(min_side_len, max_side_len)
			self.angle_a = random.uniform(20, 100)

			self.angle_b = random.uniform(20, 100)
			self.side_b = sin(self.angle_b) / (sin(self.angle_a) / self.side_a)

			self.angle_c = 180 - self.angle_a - self.angle_b

			try:
				self.side_c = sqrt(self.side_a ** 2 + self.side_b ** 2 - 2 * self.side_a * self.side_b * cos(self.angle_c))
			except ValueError:
				continue

			if self.angle_a < 10 or self.angle_b < 10 or self.angle_c < 10 \
							or self.side_a < 2 or self.side_b < 2 or self.side_c < 2 \
							or self.side_a > 30 or self.side_b > 30 or self.side_c > 30:
				# Bad triangle, generate a new one
				continue

			break

	def create_image(
					self,

					side_a_label: Optional[str],
					side_b_label: Optional[str],
					side_c_label: Optional[str],

					angle_a_label: Optional[str],
					angle_b_label: Optional[str],
					angle_c_label: Optional[str],

					show_angle_a=False,
					show_angle_b=False,
					show_angle_c=False,
	) -> BytesIO:
		# TODO: Fix angle arcs sometimes not being draw correctly
		"""
		:param side_a_label: What side A will be labeled as. If this is None, the actual length of the side will be used. To
		not display anything, set this to an empty string.

		:param side_b_label: What side B will be labeled as. If this is None, the actual length of the side will be used. To
		not display anything, set this to an empty string.

		:param side_c_label: What side C will be labeled as. If this is None, the actual length of the side will be used. To
		not display anything, set this to an empty string.

		:param angle_a_label:
		:param angle_b_label:
		:param angle_c_label:

		:param show_angle_c:
		:param show_angle_b:
		:param show_angle_a:
		"""
		if show_angle_a and angle_a_label is None:
			angle_a_label = str(round(self.angle_a, 2))
		if show_angle_b and angle_b_label is None:
			angle_b_label = str(round(self.angle_b, 2))
		if show_angle_c and angle_c_label is None:
			angle_c_label = str(round(self.angle_c, 2))

		scale_multiplier = 4
		width = 400 * scale_multiplier
		height = 300 * scale_multiplier

		image = Image.new("RGB", (width, height), color="white")
		draw = ImageDraw(image)
		# noinspection SpellCheckingInspection
		font = ImageFont.truetype("./fonts/NotoSansMath-Regular.ttf", 18 * scale_multiplier)

		region_layouts = [
			# (x1, y1, x2, y2)
			[
				(width / 4, 0, width / 4 + 200 * scale_multiplier, 100 * scale_multiplier),
				(0, height * 0.65, 150 * scale_multiplier, height - 10 * scale_multiplier),
				(0.65 * width, 0.65 * height, width - 10 * scale_multiplier, height - 10 * scale_multiplier)
			]
		]

		layout = util.random_element(region_layouts)
		r1 = (round(layout[0][0]), round(layout[0][1]), round(layout[0][2]), round(layout[0][3]))
		r2 = (round(layout[1][0]), round(layout[1][1]), round(layout[1][2]), round(layout[1][3]))
		r3 = (round(layout[2][0]), round(layout[2][1]), round(layout[2][2]), round(layout[2][3]))

		# Pick a random point from each region
		p1 = (randint(r1[0], r1[2]), randint(r1[1], r1[3]))
		p2 = (randint(r2[0], r2[2]), randint(r2[1], r2[3]))
		p3 = (randint(r3[0], r3[2]), randint(r3[1], r3[3]))

		# Draw the triangle

		draw.line([p1, p2, p3, p1], width=2 * scale_multiplier, fill="black")

		# Label sides
		# TODO: Make sure that the position is correct. Right now, the text sometimes appears inside the line
		#  or inside the triangle. It needs to always appear outside the triangle. It also sometimes appears outside the
		#  image and isn't visible.

		side_a_midpoint = util.line_midpoint(p1, p2)
		side_b_midpoint = util.line_midpoint(p2, p3)
		side_c_midpoint = util.line_midpoint(p3, p1)

		if side_a_label is None:
			side_a_label = ""
		if side_b_label is None:
			side_b_label = ""
		if side_c_label is None:
			side_c_label = ""

		draw.text(side_a_midpoint, side_a_label, "black", font)
		draw.text(side_b_midpoint, side_b_label, "black", font)
		draw.text(side_c_midpoint, side_c_label, "black", font)

		# Draw angles

		angle_arc_radius = 40 * scale_multiplier

		side_a_line = Line(p1, p2)
		side_b_line = Line(p3, p2)
		side_c_line = Line(p3, p1)

		if DEBUG_TRIANGLE_DRAW:
			draw.text(p1, "p1 (b)", "red", font)
			draw.text(p2, "p2 (c)", "red", font)
			draw.text(p3, "p3 (a)", "red", font)

			draw.text(side_a_midpoint, "A", "red", font)
			draw.text(side_b_midpoint, "B", "red", font)
			draw.text(side_c_midpoint, "C", "red", font)

		if show_angle_a:
			p3_horizontal = Line(p3, (width, p3[1]))
			# draw.line((p3, p3_horizontal.p2.args[0], p3[1]), "blue", 4)  # debug
			start_angle = p3_horizontal.angle_between(side_b_line)
			start_angle = degrees(float(start_angle))

			arc_angle = 360 - degrees(p3_horizontal.angle_between(side_c_line))

			start = (p3[0] - angle_arc_radius, p3[1] - angle_arc_radius)
			end = (p3[0] + angle_arc_radius, p3[1] + angle_arc_radius)

			# We always need the clockwise angle between p3_horizontal and side B because that's what ImageDraw.arc() uses.
			# If p2 is above p3, angle_between() returns the counterclockwise angle because it's smaller,
			# so we subtract it from 360 to get the clockwise angle if that's the case.
			if p2[1] < p3[1]:
				start_angle = 360 - start_angle

			draw.arc([start, end], start_angle, arc_angle, "black", scale_multiplier)

			# TODO: Improve text positioning
			# text_pos = util.line_midpoint(p3, util.line_midpoint(p1, p2))
			# text_pos[0] + 10 * scale_multiplier, text_pos[1] + 10 * scale_multiplier
			draw.text(p3, str(angle_a_label), "black", font)

		if show_angle_b:
			p1_horizontal = Line(p1, (width, p1[1]))
			start_angle = p1_horizontal.smallest_angle_between(side_c_line)
			start_angle = degrees(start_angle)

			arc_angle = degrees(p1_horizontal.angle_between(side_a_line))

			start = (p1[0] - angle_arc_radius, p1[1] - angle_arc_radius)
			end = (p1[0] + angle_arc_radius, p1[1] + angle_arc_radius)

			# draw.line((p1, (width, p1[1])), "black", 2 * scale_multiplier)

			draw.arc([start, end], start_angle, arc_angle, "black", scale_multiplier)
			# draw.rectangle((start, end), None, "red")

			# TODO: Improve text positioning
			# text_pos = util.line_midpoint(p1, util.line_midpoint(p2, p3))
			# text_pos[0] - 10 * scale_multiplier, text_pos[1] - 30 * scale_multiplier
			draw.text(p1, str(angle_b_label), "black", font)

		if show_angle_c:
			p2_horizontal = Line(p2, (width, p2[1]))

			start_angle = p2_horizontal.angle_between(side_a_line)
			start_angle = degrees(float(start_angle)) + 180

			arc_angle = degrees(side_a_line.angle_between(side_b_line))

			if p2[1] > p3[1]:
				arc_angle -= degrees(side_a_line.smallest_angle_between(p2_horizontal))
			if p2[1] < p3[1]:
				arc_angle -= degrees(side_a_line.smallest_angle_between(p2_horizontal))

			start = (p2[0] - angle_arc_radius, p2[1] - angle_arc_radius)
			end = (p2[0] + angle_arc_radius, p2[1] + angle_arc_radius)

			# draw.arc([start, end], 0, start_angle, "orange", scale_multiplier)  # debug
			draw.arc([start, end], start_angle, arc_angle, "black", scale_multiplier)

			# TODO: Improve text positioning
			# text_pos = util.line_midpoint(p2, util.line_midpoint(p1, p3))
			# text_pos[0] - 40 * scale_multiplier, text_pos[1] - 20 * scale_multiplier
			draw.text(p2, str(angle_c_label), "black", font)

		return util.save_pillow_image(image)
