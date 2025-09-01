# Problem Set 5 Question 3
# To make a unit test code for PS2Q4

# Importing is_valid() from plates.py
from plates import is_valid

# Calling all functions
def main():
    test_len()
    test_start()
    test_zero()
    test_numbers()
    test_punc()
    test_end()

# To test for correct length
def test_len():
    assert is_valid("CS") == True
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False

# To test for correct starting characters
def test_start():
    assert is_valid("10MARK") == False
    assert is_valid("MARK10") == True

# To test for correct zero placement
def test_zero():
    assert is_valid("MARK04") == False
    assert is_valid("MARK40") == True

# To test for correct number placement
def test_numbers():
    assert is_valid("M4RK10") == False
    assert is_valid("MAR400") == True

# To test for use of improper symbols
def test_punc():
    assert is_valid("PI3.14") == False
    assert is_valid("PI314") == True
    assert is_valid("PI3!14") == False

# To test for correct ending character
def test_end():
    assert is_valid("HEL4A") == False
    assert is_valid("HEL44") == True

if __name__ == "__main__":
    main()