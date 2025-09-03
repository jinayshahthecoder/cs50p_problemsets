# Problem Set 7 Question 1
# To output Boolean based on user inputted IPv4 Address

# Importing validate() to be tested
from numb3rs import validate

# Calling all functions
def main():
    test_range()
    test_dots()
    test_extras()
    test_str()

# To test for valid range
def test_range():
    assert validate("0.1.255.245") == True
    assert validate("256.257.-1.-2") == False
    assert validate("250.100.001.2") == False

# To test for extra periods
def test_dots():
    assert validate(".1.1.1.1") == False
    assert validate("1.1.1.1.") == False
    assert validate("1.2.3.4") == True

# To test for extra values
def test_extras():
    assert validate("1.2.3.4.5") == False
    assert validate("200.201.202.203") == True

# To test for string input
def test_str():
    assert validate("h.t.t.p") == False

# To execute the program
if __name__ == "__main__":
    main()