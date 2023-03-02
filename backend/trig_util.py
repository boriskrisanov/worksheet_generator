"""
This file contains trigonometric functions that use degrees instead of radians
"""
import math


def sin(degrees: float):
	return math.sin(math.radians(degrees))


def cos(degrees: float):
	return math.cos(math.radians(degrees))


def tan(degrees: float):
	return math.tan(math.radians(degrees))


def arc_sin(degrees: float):
	return math.asin(math.radians(degrees))


def arc_cos(degrees: float):
	return math.acos(math.radians(degrees))


def arc_tan(degrees: float):
	return math.atan(math.radians(degrees))
