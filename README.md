# Cistercian Numeral Maker
Program to create a representation of any number on the interval [0, 9999] following the Cistercian numeral system.

A description of this numeral system can be found on [this link to wikipedia](https://en.wikipedia.org/wiki/Cistercian_numerals).

This system consist in represent a number by composition of its digits bearing in mind the position they occupy as units, tens, hundreds and thousands. The symbols for each digit on each position can be seen on the following image:

![Cistercian digits](img/Cistercian_digits.png)

Some examples:

![Cistercian examples](img/Cistercian_examples.png)

# Usage

## Without arguments:

```python CistercianNumeralMaker.py```

You will be asked for the number to create and forced to input a valid integer on the valid range [0, 9999]. Your favourite image viewer program will be launched to show you the created image. After closing the image viewer, the created image will be saved on the 'output' folder; the name of the image correspond to the number being represented.

## With arguments:

```python CistercianNumeralMaker.py <arg1> <arg2> ... <argn>```

The program will generate and save all asked numbers on the 'output' folder; the name of the image correspond to the number being represented. All invalid arguments will be skipped.

e.g. ```python CistercianNumeralMaker.py 1265 1357 2568 3546 4684 5846```

# License
This script is licensed under the [MIT License](https://github.com/JAFS6/CistercianNumeralMaker/blob/main/LICENSE).

# Author
[Juan Antonio Fajardo Serrano](https://www.linkedin.com/in/jafs6)
