# Problem Set 5 Question 2
# To make a unit test code for PS1Q2

# Importing value() from bank.py
from bank import value

# Calling all functions
def main():
    test_hello()
    test_startHey()
    test_startElse()

# To test for input "hello"
def test_hello():
    assert value("hello") == "$0"
    assert value("hello, newman") == "$0"

# To test for input "hey" or any input starting with h that isn't hello
def test_startHey():
    assert value("hey") == "$20"
    assert value("how's the weather today?") == "$20"

# To test for any other greeting
def test_startElse():
    assert value("what's up?") == "$100"
    assert value("what's happening?") == "$100"

if __name__ == "__main__":
    main()