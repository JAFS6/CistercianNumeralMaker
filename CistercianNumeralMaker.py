import os
import sys
from PIL import Image
from PIL import ImageOps

# Limits determined by the Cistercian numeral system
LOWER_LIMIT = 0
UPPER_LIMIT = 9999


def input_is_valid(input_string):
    """Checks if the input is valid for the program.
    Returns True if it is, False otherwise.
    """
    if not (input_string.isnumeric()):
        return False
    input_integer = int(input_string)
    if not (isinstance(input_integer, int)):
        return False
    if input_integer < LOWER_LIMIT:
        return False
    if input_integer > UPPER_LIMIT:
        return False
    return True


def get_input():
    """Gets user input through prompt.
    Returns a list with a single string object.
    """
    print("\nWelcome to Cistercian Numeral Maker")

    input_string = "-1"
    while not (input_is_valid(input_string)):
        phrase = "Please enter a integer number on the range [{}, {}]"
        print(phrase.format(LOWER_LIMIT, UPPER_LIMIT))
        input_string = input()

    print("Introduced number is {}".format(input_string))

    return [input_string]


def get_number_decomposition(number_string):
    """Decomposes the number in its digits.
    Returns a list of strings [units, tens, hundreds, thousands].
    """
    number = int(number_string)

    decomposition = [number_string[len(number_string) - 1]]

    for i in range(1, 4):
        if number >= pow(10, i):
            decomposition.append(number_string[len(number_string) - (i + 1)])
    return decomposition


def number_string_2_integers(_list):
    """Gets a list of strings and returns a list of the correspondant integers.
    Returns the translated list.
    """
    integer_list = []
    for _int_str in _list:
        integer_list.append(int(_int_str))
    return integer_list


def composer_numeral_image(decomposition):
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
    units_images = []

    for i in range(1, 10):
        filename = "img/digit{}.png".format(i)
        units_images.append(Image.open(filename).convert('RGBA'))

    position = 0
    for element in decomposition:
        if element > 0:
            digit_image = units_images[(decomposition[position]) - 1]
            if position == 1:
                digit_image = ImageOps.mirror(digit_image)
            elif position == 2:
                digit_image = ImageOps.flip(digit_image)
            elif position == 3:
                digit_image = ImageOps.mirror(ImageOps.flip(digit_image))
            out = Image.alpha_composite(out, digit_image)
        position += 1
    return out


def save_image(image, name):
    """Saves the image to the output folder.
    """
    output_folder_name = "output"
    if not os.path.exists(output_folder_name):
        os.mkdir(output_folder_name)
    image.save("{}/{}.png".format(output_folder_name, name))


def main():
    """Entry point of the program.
    """
    got_parameters = False

    if len(sys.argv) > 1:
        got_parameters = True
        input_strings = sys.argv[1:len(sys.argv)]  # 1 to exclude program's name
    else:
        input_strings = get_input()

    for element in input_strings:
        if input_is_valid(element):
            decomposition = get_number_decomposition(element)
            result = composer_numeral_image(number_string_2_integers(decomposition))
            if not got_parameters:
                result.show()
            save_image(result, element)


if __name__ == "__main__":
    main()
