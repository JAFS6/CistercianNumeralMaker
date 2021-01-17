import os
import sys
from PIL import Image
from PIL import ImageOps

# Limits determined by the Cistercian numeral system
LOWER_LIMIT = 0
UPPER_LIMIT = 9999

def inputIsValid (inputString):
    """Checks if the input is valid for the program.
    Returns True if it is, False otherwise.
    """
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
    """Gets user input through prompt.
    Returns a list with a single string object.
    """
    print("\nWelcome to Cistercian Numeral Maker")

    inputString = "-1"
    while (not(inputIsValid(inputString))):
        phrase = "Please enter a integer number on the range [{}, {}]"
        print(phrase.format(LOWER_LIMIT, UPPER_LIMIT))
        inputString = input()

    print("Introduced number is {}".format(inputString))

    return [inputString]

def getNumberDecomposition(numberString):
    """Decomposes the number in its digits.
    Returns a list of strings [units, tens, hundreds, thousands].
    """
    number = int(numberString)

    decomposition = [numberString[len(numberString) - 1]]

    for i in range(1, 4):
        if (number >= pow(10, i)):
            decomposition.append(numberString[len(numberString) - (i + 1)])
    return decomposition

def numberString2Integers(list):
    """Gets a list of strings and returns a list of the correspondant integers.
    Returns the translated list.
    """
    integerList = []
    for element in list:
        integerList.append(int(element))
    return integerList

def composeNumeralImage(decomposition):
    """Creates the image through alpha composition.
    First it set the base image common to all numerals.
    After that, it checks each position (units, tens, hundreds, thousands) to
    add it correspondant image.
    'Units' images are the base ones.
    'Tens' images are a mirror over the 'units'.
    'Hundreds' images are a flip over the 'units'.
    'Thousands' images are a mirror of a flip over the 'units'.
    Returns an Image object.
    """
    # Convert images on load to RGBA to make sure all image modes are the same
    out = Image.open('img/digit0.png').convert('RGBA')
    unitsImages = []

    for i in range(1,10):
        filename = "img/digit{}.png".format(i)
        unitsImages.append(Image.open(filename).convert('RGBA'))

    position = 0
    for element in decomposition:
        if (element > 0):
            digitImage = unitsImages[(decomposition[position])-1]
            if (position == 1):
                digitImage = ImageOps.mirror(digitImage)
            elif (position == 2):
                digitImage = ImageOps.flip(digitImage)
            elif (position == 3):
                digitImage = ImageOps.mirror(ImageOps.flip(digitImage))
            out = Image.alpha_composite(out, digitImage)
        position += 1
    return out

def saveImage(image, name):
    """Saves the image to the output folder.
    """
    outputFolderName = "output"
    if not os.path.exists(outputFolderName):
        os.mkdir(outputFolderName)
    image.save("{}/{}.png".format(outputFolderName, name))

def main():
    """Entry point of the program.
    """
    gotParameters = False
    inputStrings = []

    if (len(sys.argv) > 1):
        gotParameters = True
        inputStrings = sys.argv[1:len(sys.argv)] # 1 to exclude program's name
    else:
        inputStrings = getInput()

    for element in inputStrings:
        if (inputIsValid(element)):
            decomposition = getNumberDecomposition(element)
            result = composeNumeralImage(numberString2Integers(decomposition))
            if (not gotParameters):
                result.show()
            saveImage(result, element)

if __name__ == "__main__":
    main()
