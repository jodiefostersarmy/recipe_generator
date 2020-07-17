#!/usr/sbin/python

import recipes
import functions
import foodList
from foodList import ingredients

# new = []
# for i in range(len(ingredients)):
#     new += sorted(ingredients[i].keys())

# new_s = sorted(new)

# for count, item in enumerate(new_s, 1):
#   print(f"{count}. {item.title()}")


# for (i1, i2, i3) in zip(vegetables, herbs_and_spices, sauces_oils):
#     print('{:<25}'.format(i1) + '{:<25}'.format(i2) + '{:<10}'.format(i3))


# new = []
# for i in ingredients["vegetables"]:
#     new += sorted(ingredients[i].values())

# new_v = sorted(new)


for count, item in enumerate(sorted(ingredients[0]["vegetables"]), 1):
  print(f"{count}. {item.title()}")
