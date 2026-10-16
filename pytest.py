
from student import calculate_grade

def test_grade_A():
    assert calculate_grade(95) == "A"

def test_grade_B():
    assert calculate_grade(80) == "B"

def test_grade_C():
    assert calculate_grade(65) == "C"

def test_grade_D():
    assert calculate_grade(55) == "D"

def test_grade_F():
    assert calculate_grade(40) == "F"

def test_boundary_marks():
    assert calculate_grade(90) == "A"
    assert calculate_grade(75) == "B"
    assert calculate_grade(60) == "C"
    assert calculate_grade(50) == "D"
    assert calculate_grade(39) == "F"
