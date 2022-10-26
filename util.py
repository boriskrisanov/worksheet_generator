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
