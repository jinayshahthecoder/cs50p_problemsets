# Problem Set 5 Question 4
# To make a unit test code for PS3Q1

from fuel import convert, gauge
import pytest

def main():
    test_conversionZero()
    test_conversionNotDigit()
    test_gaugePercent()

def test_conversionZero():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")

def test_conversionNotDigit():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_gaugePercent():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(25) == "25%"