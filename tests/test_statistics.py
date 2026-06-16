from utils.statistics import four_parameter_logistic


def test_four_parameter_logistic_runs():
    y = four_parameter_logistic([1, 10, 100], bottom=0, top=100, ic50=50, hill_slope=1)
    assert len(y) == 3
