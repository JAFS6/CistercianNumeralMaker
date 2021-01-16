# Limits determined by the Cistercian numeral system
LOWER_LIMIT = 0
UPPER_LIMIT = 9999

def input_is_valid (input_string):
    if (not(input_string.isnumeric())):
        return False
    input_integer = int(input_string)
    if (not(isinstance(input_integer, int))):
        return False
    if (input_integer < LOWER_LIMIT):
        return False
    if (input_integer > UPPER_LIMIT):
        return False
    return True

def getInput():
    print("\nWelcome to Cistercian Numeral Maker")

    input_string = "-1"
    while (not(input_is_valid(input_string))):
        print("Please enter a integer number on the range [0, 9999]")
        input_string = input()

    print("Introduced number is {}".format(input_string))

    return int(input_string)

def main():
    number = getInput()

if __name__ == "__main__":
    main()
