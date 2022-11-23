from math import pi
from random import randint
from typing import Union

from PIL import Image, ImageDraw, ImageFont

from util import save_pillow_image, line_midpoint


class Circle:
	def __init__(self, min_radius=2, max_radius=20):
		"""
		Generates a circle with a random radius
		"""
		self.radius = randint(min_radius, max_radius)
		self.diameter = self.radius ** 2
		self.area = pi * self.radius ** 2
		self.circumference = pi * self.diameter

	def create_image(
					self,
					show_diameter=True,
					show_radius=True,
					diameter_label: Union[str, None] = None,
					radius_label: Union[str, None] = None
	):
		"""
		Generates a WebP image of the circle and returns a BytesIO object containing it

		:param show_diameter: Whether the diameter should be shown (If set to False, both the diameter line and the label will
		be hidden. If you want to show the line but not display anything on it, set this to True and set
		diameter_label to an empty string)

		:param show_radius: Whether the radius should be shown (If set to False, both the radius line and the label will
		be hidden. If you want to show the line but not display anything on it, set this to True and set
		radius_label to an empty string). If show_diameter is True, this argument will be ignored.

		:param diameter_label: The text next to the diameter line. This will only be displayed if show_diameter is True.
		If this is None, the actual diameter of the circle will be used.

		:param radius_label: The text next to the radius line. This will only be displayed if show_radius is True.
		If this is None, the actual radius of the circle will be used.
		"""

		scale_multiplier = 4

		width = 400 * scale_multiplier
		height = 300 * scale_multiplier

		image = Image.new("RGB", (width, height), color="white")
		draw = ImageDraw.Draw(image)
		# noinspection SpellCheckingInspection
		font = ImageFont.truetype("./fonts/NotoSansMath-Regular.ttf", 18 * scale_multiplier)

		# Draw circle
		random_offset = randint(0, 20 * scale_multiplier)
		margin = 20 * scale_multiplier
		start = (margin + random_offset, margin + random_offset)
		end = ((width - 100 * scale_multiplier) - margin - random_offset, height - margin - random_offset)
		pos = (start, end)
		center = line_midpoint((start[0], start[1]), (end[0], end[1]))
		draw.arc(pos, 0, 360, "black", 2 * scale_multiplier)

		# Add "NOT TO SCALE" text
		draw.text((width / 2 + 60 * scale_multiplier, height - 290 * scale_multiplier), "NOT TO SCALE", "black", font)

		# Draw radius
		if show_radius and not show_diameter:
			if not radius_label:
				radius_label = str(round(self.radius, 2))

			top_right = end[0], start[0]
			line_end = line_midpoint(top_right, end)
			draw.line((center, line_end), "black", 2 * scale_multiplier)

			label_pos = line_midpoint(center, line_end)

		# Save image
		return save_pillow_image(image)
