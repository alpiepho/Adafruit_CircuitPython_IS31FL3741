# SPDX-FileCopyrightText: 
# SPDX-License-Identifier: MIT

# NOTE: mash up between is31fl3741_rgbswirl.py with 
# https://github.com/adafruit/Adafruit_IS31FL3741/blob/main/examples/qtmatrix-text-buffered/qtmatrix-text-buffered.ino

import board
from rainbowio import colorwheel
import time

from adafruit_is31fl3741.adafruit_rgbmatrixqt import Adafruit_RGBMatrixQT
import adafruit_is31fl3741

# TODO these should be in adafruit_rgbmatrixqt
def matrix_fill(matrix, value):
    for y in range(height):
        for x in range(width):
            matrix.pixel(x, y, value)

def matrix_setRotation(matrix, degrees):
    # TBD
    pass

def matrix_setTextWrap(matrix, bvalue):
    # TBD
    pass

# TODO find parameters, guessing
def matrix_getTextBounds(matrix, text, x, y):
    # TBD
    return false, false, 0, 0

def matrix_setCursor(matrix, text_x, text_y):
    pass
        

matrix = Adafruit_RGBMatrixQT(board.I2C(), allocate=adafruit_is31fl3741.PREFER_BUFFER)
matrix.set_led_scaling(0xFF)
matrix.global_current = 0xFF
# print("Global current is: ", is31.global_current)
matrix.enable = True
# print("Enabled? ", is31.enable)
matrix_setRotation(0)
matrix_setTextWrap(false)

text = "ADAFRUIT!"     # A message to scroll
text_x = matrix.width; # Initial text position = off right edge
text_y = 1
text_min = 0           # Pos. where text resets (calc'd later)

# Get text dimensions to determine X coord where scrolling resets
w = 0
h = 0
### matrix.getTextBounds(text, 0, 0, &ignore, &ignore, &w, &h);
_, _, w, h = matrix_getTextBounds(matrix, text, 0, 0)
text_min = -w; # Off left edge this many pixels


while True:
    matrix_fill(matrix, 0) # Fill screen to erase old text
    matrix_setCursor(matrix, text_x, text_y)
    ### for (int i = 0; i < (int)strlen(text); i++) {
    ###     // set the color thru the rainbow
    ###     uint32_t color888 = matrix.ColorHSV(65536 * i / strlen(text));
    ###     uint16_t color565 = matrix.color565(color888);
    ###     matrix.setTextColor(color565); // No background color needed
    ###     matrix.print(text[i]); // write the letter
    ### }

    matrix.show(); # Buffered matrix MUST use show() to update!

    text_x = text_x -1
    if text_x < text_min:
        text_x = matrix.width

    time.sleep(0.025)
