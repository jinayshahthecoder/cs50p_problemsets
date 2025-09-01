# Problem Set 5 Question 3
# To make a unit test code for PS2Q4

# Re-entering the same code as stated in question
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 1 < len(s) <= 6 and val_start(s) and val_num(s) and val_punc(s) and val_end(s):
                    return True
    else:
        return False

def val_start(start):
    if start[0:2].isalpha():
        return True
    else:
        return False

def val_num(nonzero):
    for i in nonzero:
        if i.isdigit():
            break
    if i != "0":
        return True

def val_punc(punc):
    if punc.isalnum():
            return True
    else:
            return False

def val_end(end):
    if end.isalpha():
        return True
    else:
        if end[len(end) - 1].isdigit():
                return True
        else:
                return False
    
if __name__ == "__main__":
    main()