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


def arc_sin(value: float):
	return math.degrees(math.asin(value))


def arc_cos(value: float):
	return math.degrees(math.acos(value))


def arc_tan(value: float):
	return math.degrees(math.atan(value))
