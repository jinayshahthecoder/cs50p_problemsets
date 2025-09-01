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