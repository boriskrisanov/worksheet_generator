from os import path, mkdir
from random import randint


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
