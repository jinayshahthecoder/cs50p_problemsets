# Problem Set 5 Question 4
# To make a unit test code for PS3Q1

# Importing convert(), gauge() from fuel.py and importing pytest for raised Errors
from fuel import convert, gauge
import pytest

# Calling all functions
def main():
    test_conversionZero()
    test_conversionNotDigit()
    test_gaugePercent()

# To test for correct conversions
def test_conversionFraction():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("0/1") == 0
    assert convert("8/10") == 80

# To test if ZeroDivisionError is raised
def test_conversionZero():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")

# To test if ValueError is raised
def test_conversionNotDigit():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("9/3")

# To test for correct gauge percentage
def test_gaugePercent():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(25) == "25%"

if __name__ == "__main__":
    main()