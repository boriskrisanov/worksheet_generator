from Equation import Equation


def test_solve():
	assert Equation("x = 1").solve().numeric_result == 1
	assert Equation("2x = 1").solve().numeric_result == 0.5
