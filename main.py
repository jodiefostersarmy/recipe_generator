import recipes
import functions
from foodList import ingredients
from functions import select_items



functions.greeting()

functions.hasIngredients()








# #FIRST ROUND: Correct Ingredients

# ##I can possibly turn correct ingredients into a function as I will need this later on
# ##when they have fixed their ingredients list

# if str(step2) == "1":
#     print("Great, just a couple more questions.\n")
#     dietChoice = input("""Which diet guideline would you like to cook with?
# 1. Whole 30
# 2. Vegetarian
# 3. Plant-based
# """)
#     if int(dietChoice) == 1:
#         for recipe in recipes.recipes:
#             if "Whole 30" in recipe["diet"]:
                
#             # if recipe["diet"] == "Whole 30":
#                 # print(f"{functions.user_ingredients} === {recipe['ingredients']}")
#                 # if functions.user_ingredients in recipe["ingredients"]:

#                 if set(functions.user_ingredients).issubset(set(recipe["ingredients"])):
#                     print("------------")
#                     functions.chosen_recipes.append(recipe["name"])
#         print(functions.chosen_recipes)

#     # elif int(dietChoice) == 2:
    
#     # elif int(dietChoice) == 3:









# #FIRST ROUND: ADD Ingredients
# if str(step2) == "2":
#     add_or_remove = input("""\nDo you need to add an ingredient, or remove an ingredient?
# 1. ADD
# 2. REMOVE
# """)
#     if add_or_remove == "1":
#         i = 0
#         how_many_more = functions.askUser("How many more? ")
#         while i < how_many_more:
#             more_ingredients = input(f"Ingredient: ")
#             functions.user_ingredients.append(more_ingredients)
#             i += 1
#         print(f"\nYour updated ingredients list contains:\n")
#         functions.user_ingredients.sort()
#         for ingredient in functions.user_ingredients:
#             print(ingredient.title())
#         continue_with_these = input("""Would you like to continue with these ingredients?
# 1. YES
# 2. NO
# """)


# #FIRST ROUND: REMOVE Ingredients
#     elif add_or_remove == "2":
#         remove = input("Which ingredient would you like to remove?\n")
#         functions.user_ingredients.remove(remove.lower())
#         print(f"\nYour updated ingredients list contains:\n {functions.user_ingredients}\n")
    

# # else:
# #     while step2 != 1 or step2 != 2:
        



