# Problem Set 7 Question 4
# To return the number of "um" in the given string input

# Importing count() to be tested
from um import count

# Calling all functions
def main():
    ...

# To count for
def test_countAlone():
    assert count("um") == 1
    assert count(" um ") == 1

# To count for number in letters (which should return 0)
def test_inWords():
    assert count("yummy") == 0
    assert count("umm mum") == 0
    assert count("um thats an album") == 1

# To count for case insensitive "um"s
def test_caseInsens():
    assert count("um what") == 1
    assert count("UM WHAT") == 1

# To execute the program
if __name__ == "__main__":
    main()