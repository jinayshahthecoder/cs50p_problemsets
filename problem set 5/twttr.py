# Problem Set 5 Question 1
# To make a unit test code for PS2Q3

# Re-entering the same code in block and function format as stated
def main():
    inp = input("Input: ").strip()
    print(shorten(inp))

def shorten(username):
    out = ""
    for i in username:
        if i not in "aeiouAEIOU":
            out += i
    return out

if __name__ == "__main__":
    main()