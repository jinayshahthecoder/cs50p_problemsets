# Problem Set 5 Question 1
# To make a unit test code for PS2Q3

# Importing shorten() from twttr.py
from twttr import shorten

# Calling all functions
def main():
    test_lowerVowel()
    test_upperVowel()
    test_numbers()
    test_punc()
    test_cons()

# Defining assertion functions to return true/false values for input in shorten()

# To test for all lowercase vowels
def test_lowerVowel():
    assert shorten("aeiou") == ""

# To test for all uppercase vowels
def test_upperVowel():
    assert shorten("AEIOU") == ""

# To test for all numbers in case of a mistake
def test_numbers():
    assert shorten("9876543210") == "9876543210"

# To test for punctuations in case of a mistake
def test_punc():
    assert shorten(";:,.!?") == ";:,.!?"

# To test for all consonants in case of a mistake
def test_cons():
    assert shorten("bcdfghjklmnpqrstvwxyz") == "bcdfghjklmnpqrstvwxyz"

if __name__ == "__main__":
    main()