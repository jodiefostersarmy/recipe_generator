import recipes
import functions
import foodList
from foodList import ingredients

new = []
for i in range(len(ingredients)):
    new += sorted(ingredients[i].keys())

new_s = sorted(new)

for count, item in enumerate(new_s, 1):
  print(f"{count}. {item.title()}")

# def listToString(ingredients):  
    
#     # initialize an empty string 
#     str1 = " " 
    
#     # return string   
#     return (str1.join(ingredients)) 
        
# # Driver code     
# print(listToString(ingredients)) 

# print(ingredients.keys())

# def display_inventory(inventory):
#     s_lst = sorted(inventory)
#     print('{:<25}'.format('Vegetables') + '{:<25}'.format('Prices:') + '{:<10}'.format('Nuts'))
#     for ingredient in s_lst:
#         print('{:<25}'.format(ingredient) + '{:<25}'.format(herbs_and_spices) + '{:<10}'.format('Dairy'))

# display_inventory(foodList.vegetables)

# num = [1, 2, 3] 
# color = ['red', 'while', 'black'] 
# value = [255, 256] 
  
# # iterates over 3 lists and excutes  
# # 2 times as len(value)= 2 which is the 
# # minimum among all the three  
# for (a, b, c) in zip(num, color, value): 
#      print (a, b, c) 
# for inventory in vegetables:
#     print(inventory)

# for (i1, i2, i3) in zip(vegetables, herbs_and_spices, sauces_oils):
#     print('{:<25}'.format(i1) + '{:<25}'.format(i2) + '{:<10}'.format(i3))
