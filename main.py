#!/usr/sbin/python

import sys
import recipes
import functions
from foodList import ingredients
from functions import select_items
from termcolor import colored, cprint

if "--help" in sys.argv:
    print("""HOW TO NAVIGATE PANTRY:

Each ingredient category will be provided with an accompanying number beside it.
Please enter the integer beside your desired option and hit ENTER/RETURN to proceed.

You will be prompted with messages thereafter to assist in the recipe selection.
""")

else:
    functions.greeting()
    functions.hasIngredients()
    functions.endFunction()



#create goodbye function
# do you want to look for another recipe?
