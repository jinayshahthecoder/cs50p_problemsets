from twttr import shorten

def main():
    test_lowerVowel()
    test_upperVowel()
    test_numbers()
    test_punc()

def test_lowerVowel():
    assert shorten("aeiou") == ""

def test_upperVowel():
    assert shorten("AEIOU") == ""

def test_numbers():
    assert shorten("9876543210") == "9876543210"

def test_punc():
    assert shorten(";:,.!?") == ";:,.!?"

if __name__ == "__main__":
    main()