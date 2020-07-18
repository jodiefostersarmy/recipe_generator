#!/usr/sbin/python

import sys
import recipes
import functions
from foodList import ingredients
from functions import select_items
from termcolor import colored, cprint

if "--help" in sys.argv:
    print("""How to use PANTRY:
Each ingredient category will be provided with an accompanying number
""")

functions.greeting()

functions.hasIngredients()

#create goodbye function
# do you want to look for another recipe?
