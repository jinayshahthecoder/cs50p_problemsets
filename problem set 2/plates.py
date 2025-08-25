# Problem Set 2 Question 4
# To check if custom made vanity plate complies with given set of rules

# main() takes the user input of given string and passes it onto is_valid
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Here is_valid() is a parent function for all child functions to make it better
def is_valid(s):
    if 2 <= len(s) <= 6 and val_start(s) and val_num(s) and val_punc(s) and val_end(s):
                    return True
    else:
        return False

# Functions below check if it complies with rules
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
    if end[len(end) - 1].isdigit():
            return True
    else:
            return False

# To execute the program
main()