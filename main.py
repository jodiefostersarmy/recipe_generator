#!/usr/sbin/python

import sys
import recipes
import functions
from foodList import ingredients
from functions import select_items
from termcolor import colored, cprint

if "--help" in sys.argv:
    print("""HOW TO NAVIGATE PANTRY:

1,2,3,etc           Each ingredient category will be provided
                    with an accompanying number beside it.
                    Please enter the integer beside your desired 
                    option and hit ENTER/RETURN to proceed.
                    You will be prompted with messages thereafter
                    to assist in the recipe selection.

ctrl + c            This will stop the program at any point.
""")

else:
    functions.greeting()
    functions.hasIngredients()
    functions.endFunction()

