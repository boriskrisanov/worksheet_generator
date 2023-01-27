from math import pi
from random import randint
from typing import Union

from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw

from util import save_pillow_image, create_circle_image


class Circle:
	def __init__(self, min_radius=2, max_radius=20):
		"""
		Generates a circle with a random radius
		"""
		self.radius = randint(min_radius, max_radius)
		self.diameter = self.radius * 2
		self.area = pi * self.radius ** 2
		self.circumference = pi * self.diameter

	def __str__(self):
		return f""" Circle(
						radius = {self.radius}
						diameter = {self.diameter}
						area = {self.area}
						circumference = {self.circumference}
					)
					"""

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

		# This function works by first drawing the circle on a transparent image and then overlaying it on a white image
		# with a margin and random offset applied. This is easier than drawing the circle directly on the final image because
		# the final image may not have equal width and height, and we would need to apply the random offsets to the radius
		# line, both of which make the code and calculations more confusing.

		# Everything position related, including the dimensions of the image, will be multiplied by this. This allows the
		# resolution/dimensions of the image to be changed without changing how the circle looks.
		scale_multiplier = 4

		# noinspection SpellCheckingInspection
		font = ImageFont.truetype("./fonts/NotoSansMath-Regular.ttf", 18 * scale_multiplier)

		circle_size = randint(150, 250)

		if diameter_label is None:
			diameter_label = str(round(self.diameter, 2))

		if radius_label is None:
			radius_label = str(round(self.radius, 2))

		circle_image = create_circle_image(
			scale_multiplier,
			circle_size,
			font,
			diameter_label,
			radius_label,
			show_diameter,
			show_radius,
		)

		width = 400 * scale_multiplier
		height = 300 * scale_multiplier

		final_image = Image.new("RGBA", (width, height), color="white")
		final_image_draw = ImageDraw(final_image)

		# Overlay the circle over the final image
		margin = 20 * scale_multiplier

		random_offset_x = randint(0, 30 * scale_multiplier)
		random_offset_y = randint(0, 30 * scale_multiplier)

		circle_pos = margin + random_offset_x, margin + random_offset_y

		final_image.paste(circle_image, circle_pos, circle_image)

		# Add "NOT TO SCALE" text
		final_image_draw.text((width / 2 + 60 * scale_multiplier, height - 290 * scale_multiplier), "NOT TO SCALE", "black", font)

		return save_pillow_image(final_image)
