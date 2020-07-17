import recipes
import functions
from foodList import ingredients
from functions import select_items


print("""Welcome to...

'########:::::'###::::'##::: ##:'########:'########::'##:::'##:
 ##.... ##:::'## ##::: ###:: ##:... ##..:: ##.... ##:. ##:'##::
 ##:::: ##::'##:. ##:: ####: ##:::: ##:::: ##:::: ##::. ####:::
 ########::'##:::. ##: ## ## ##:::: ##:::: ########::::. ##::::
 ##.....::: #########: ##. ####:::: ##:::: ##.. ##:::::: ##::::
 ##:::::::: ##.... ##: ##:. ###:::: ##:::: ##::. ##::::: ##::::
 ##:::::::: ##:::: ##: ##::. ##:::: ##:::: ##:::. ##:::: ##::::
..:::::::::..:::::..::..::::..:::::..:::::..:::::..:::::..:::::


This application will provide you with suggested recipes for diets 
that follow the Whole30, vegetarian or plant-based diets based on the
ingredients that you have in your fridge and pantry.

We aim to match the recipes closest to the ingredients that you already 
have on hand, and provide you with a quick and easy way to prepare a 
healthy and tasty meal.

We begin by asking you everything that you have in your pantry that you 
would like to use, then once we have all the ingredients, we will provide 
you with a selection of recipes across the diets mentioned above.
You will be able to select the best fitting option based on taste, cook time
and diet.

We recommend that you provide the application with at least 3 ingredients to 
maximise its benefit.

If you need any help, or more instructions, call the help flag with --help
""")
print("\n\n")
print("""To find the best recipes for your dietary preference, we will need to add a few ingredients you have on hand.
Or, alternatively you can also browse the full list of recipes we have in the database.
""")

# begin = functions.askUser("""1. I have some ingredients to use.
# 2. Let me see the full list!
# """)

# if begin == 1:
#     print("\nGreat, please select the right category of food group below using the numbers to add items to your 'PANTRY' list.\n")
# else:
#     print(recipes.recipes.sort())



select_items()



# how_many_ingredients = functions.askUser("\nPlease input the number beside the category you would like to use\n")

# while how_many_ingredients < 3:
#     print("You must have at least 3 or more ingredients for this guide to be beneficial.\n")
#     how_many_ingredients = functions.askUser("How many ingredients in your pantry would you like to use?\n")


# functions.get_ingredients(how_many_ingredients)
# functions.user_ingredients.sort()

# print(f"\nOkay, so your ingredients list contains:\n")
# for ingredient in functions.user_ingredients:
#     print(ingredient.title())

# step2 = input("""\nIs this correct?
# 1. YES
# 2. NO
# """)


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
        



