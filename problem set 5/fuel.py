# Problem Set 5 Question 4
# To make a unit test code for PS3Q1

# Re-entering the same code in block and function format as stated
def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
             continue
    print(gauge(percentage))

def convert(fraction):
    x, y = fraction.split('/')
    if x.isdigit() == False or y.isdigit() == False:
        raise ValueError
    elif int(y) == 0:
        raise ZeroDivisionError
    elif int(x) > int(y):
        raise ValueError
    else:
        fuel = round(int(x) / int(y) * 100)
        return fuel

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"
    
if __name__ == "__main__":
    main()