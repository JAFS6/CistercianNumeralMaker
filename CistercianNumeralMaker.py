# Limits determined by the Cistercian numeral system
LOWER_LIMIT = 0
UPPER_LIMIT = 9999

def inputIsValid (inputString):
    if (not(inputString.isnumeric())):
        return False
    inputInteger = int(inputString)
    if (not(isinstance(inputInteger, int))):
        return False
    if (inputInteger < LOWER_LIMIT):
        return False
    if (inputInteger > UPPER_LIMIT):
        return False
    return True

def getInput():
    print("\nWelcome to Cistercian Numeral Maker")

    inputString = "-1"
    while (not(inputIsValid(inputString))):
        phrase = "Please enter a integer number on the range [{}, {}]"
        print(phrase.format(LOWER_LIMIT, UPPER_LIMIT))
        inputString = input()

    print("Introduced number is {}".format(inputString))

    return inputString

def main():
    numberString = getInput()
    number = int(numberString)

    # Decompose the number in its units, tens, hundreds and thousands
    decomposition = [numberString[len(numberString) - 1]]

    if (number >= 10):
        decomposition.append(numberString[len(numberString) - 2])

    if (number >= 100):
        decomposition.append(numberString[len(numberString) - 3])

    if (number >= 1000):
        decomposition.append(numberString[len(numberString) - 4])

    print(decomposition)

if __name__ == "__main__":
    main()
