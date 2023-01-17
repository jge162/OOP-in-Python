#  simply degree conversion calculator
#  in python, using formatting in print function.
#  Author: Jeremy Escobar 1/13/2023
#  learned during google crash course on Python

def convert_to_celsius(degree):  # function declarations done here 
    return (degree - 32) * 5 / 9  # math to convert to celsius


for degree in range(-10, 101, 10):
    print("{:>6} F | {:>7.2f} C".format(degree, convert_to_celsius(degree)))
#  print out range from (-10, to 100 in increments of 10) USING FOR LOOP
#  Use floating point .2f to display two decimal points.
#  thanks
#  {:>6 means align to the left 3 spaces
#  {:>7 means align to the right 6 spaces
#  Thanks again and please lmk if u have input. 


# Output below
"""
   -10 F |  -23.33 C
     0 F |  -17.78 C
    10 F |  -12.22 C
    20 F |   -6.67 C
    30 F |   -1.11 C
    40 F |    4.44 C
    50 F |   10.00 C
    60 F |   15.56 C
    70 F |   21.11 C
    80 F |   26.67 C
    90 F |   32.22 C
   100 F |   37.78 C
"""
