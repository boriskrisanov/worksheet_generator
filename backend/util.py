from io import BytesIO
from random import randint, uniform

from PIL import ImageDraw, Image
from PIL.ImageFont import FreeTypeFont
from sympy import symbols, Eq, solve


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


def random_bool():
	"""Returns a random boolean"""
	return bool(randint(0, 1))


def line_midpoint(point1: tuple[float, float], point2: tuple[float, float]):
	"""Returns the coordinates of the midpoint of the line"""
	x = (point1[0] + point2[0]) / 2
	y = (point1[1] + point2[1]) / 2
	return x, y


def save_pillow_image(image: Image.Image):
	"""
	Returns a BytesIO object with the image encoded as WebP
	"""

	buffer = BytesIO()

	image.save(buffer, format="WEBP", lossless=True)
	buffer.seek(0)

	return buffer


def create_circle_image(
				scale_multiplier: int,
				size: int,
				font: FreeTypeFont,
				diameter_label: str,
				radius_label: str,
				show_diameter=True,
				show_radius=True,
) -> Image.Image:
	width = height = size * scale_multiplier
	image = Image.new("RGBA", (width, height))
	draw = ImageDraw.Draw(image)

	# Draw circle
	start = (0, 0)
	end = (width, height)
	pos = (start, end)
	center = line_midpoint((start[0], start[1]), (end[0], end[1]))
	draw.arc(pos, 0, 360, "black", 2 * scale_multiplier)

	if show_radius and not show_diameter:
		# Draw radius line
		r = size * scale_multiplier
		x = uniform(0, r)
		y_symbol = symbols("y")
		equation = Eq(
			(x - (r / 2)) ** 2 + (y_symbol - (r / 2)) ** 2,
			(r ** 2) / 4
		)
		solution = solve(equation)
		y = solution[randint(0, 1)]

		draw.line((center, (x, y)), "black", 2 * scale_multiplier)

		# Label radius
		label_pos = line_midpoint(center, (x, y))
		draw.text(label_pos, radius_label, "black", font)

	if show_diameter:
		# Draw diameter line
		r = size * scale_multiplier
		x = uniform(0, r)
		y_symbol = symbols("y")
		equation = Eq(
			(x - (r / 2)) ** 2 + (y_symbol - (r / 2)) ** 2,
			(r ** 2) / 4
		)
		solution = solve(equation)
		y = solution[randint(0, 1)]

		d = x - center[0], y - center[1]
		p2 = center[0] - d[0], center[1] - d[1]

		draw.line((center, (x, y)), "black", 2 * scale_multiplier)
		draw.line((center, p2), "black", 2 * scale_multiplier)

		# Label radius
		label_pos = (center[0], center[1] + 20 * scale_multiplier)
		draw.text(label_pos, diameter_label, "black", font)

	# TODO: Fix label text being drawn inside the line when it is vertical

	return image
