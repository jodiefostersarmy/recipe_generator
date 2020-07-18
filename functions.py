import recipes
from foodList import ingredients
from termcolor import colored, cprint




def greeting():
    print("""
                                 d8P                     
                              d888888P                   
?88,.d88b, d888b8b    88bd88b   ?88'    88bd88b?88   d8P 
`?88'  ?88d8P' ?88    88P' ?8b  88P     88P'  `d88   88  
  88b  d8P88b  ,88b  d88   88P  88b    d88     ?8(  d88  
  888888P'`?88P'`88bd88'   88b  `?8b  d88'     `?88P'?8b 
  88P'                                                )88
 d88                                                 ,d8P
 ?8P                                              `?888P' 
 ========================================================
""")

    print("""This application will provide you with suggested recipes for diets 
that follow the Whole30, vegetarian or plant-based diets based on the
ingredients that you have in your fridge and pantry.

We aim to match the recipes closest to the ingredients that you already 
have on hand, and provide you with ideas for healthy and tasty meal.

We begin by asking you everything that you have in your pantry that you 
would like to use, then once we have all the ingredients, we will provide 
you with a selection of recipes across the diets mentioned above.

If you need any help, or more instructions, call the help flag with --help
""")





def askUser(prompt):
    while True:
        try:
            num = int(input(prompt))
            break
        except ValueError:
            print("Please input an integer value\n")
    return num







def hasIngredients():
    print("""To find the best recipes for your dietary preference, we will need to add a few ingredients you have on hand.

Or, alternatively you can also browse the full list of recipes we have in the database.""")
    yes_or_no = askUser("""\nPlease select what you would like to do:

    1. I have ingredients to use.
    2. Let me see the full recipe list!

Selection: """)
    while yes_or_no > 2:
        yes_or_no = askUser("""You will need to enter either 1 or 2.
        
    1. I have ingredients to use.
    2. Let me see the full recipe list!

Selection: """)
    if yes_or_no == 1:
        return select_items()
    if yes_or_no == 2:
        return fullRecipeList()







userIngredients = []


def select_items():
    cont = 1

    while cont == 1:
        print("")
        print('{:*^40}'.format('Select food category'))
        print("")
        for key in ingredients:
            print('{:>14}'.format(f"{key} -  ") + '{:<0}'.format(ingredients[key]['cat'].title()))
        

        cat = int(askUser("\nEnter category number: "))

        print(ingredients[cat]["cat"].title())
        
        for key in ingredients[cat]:
            if key != "cat":
                print(f" {key} - {ingredients[cat][key].title()}")  
            


        item = askUser("Selection: ")
        while item > len(ingredients[cat])-1:
            print(f"\n{ingredients[cat]['cat'].title()}")
            for key in ingredients[cat]:
                if key != "cat":
                    print(f"{key} - {ingredients[cat][key].title()}")
            item = askUser(f"""\nYou will need to enter numbers between 1 - {len(ingredients[cat])-1}
Selection: """)

        userIngredients.append(ingredients[cat][item])
        cprint('{:*^40}'.format(f'You just added {ingredients[cat][item].title()}.'), 'blue', 'on_white')
        cont = askUser(f"""\nWould you like to add something else?
1 - YES
2 - NO
Selection: """)
        if cont > 2:
            cont = askUser("""\nSorry, you will need select 1 or 2.
1 - YES
2 - NO
Selection: """)

        userIngredients.sort()
    

    cprint("\nThe ingredients in your 'PANTRY' are:\n", 'blue','on_white')

    for count,ingredient in enumerate(userIngredients,1):
        print(f"{count}. {ingredient.title()}")
    
    return check()







def check():
    checking = askUser("""\nAre you happy with these ingredients?
1 - YES
2 - NO
Selection: """)
    if checking == 1:
        diet = askUser("""\nAre you following any of the diets listed below?
1 - Whole 30
2 - Vegetarian
3 - Plant-based
4 - None
Selection: """)

        selectedRecipes = []
        for recipe in recipes.recipes:
            if diet in recipe["diet"] or diet == 4:
                for ingredient in userIngredients:
                    if ingredient in recipe["ingredients"]:
                        selectedRecipes.append(recipe["name"])
                        break
        
        
        if len(selectedRecipes) == 0:
                cprint(f"\nSorry, there are no recipes with those ingredients for the {recipes.diets[diet].title()} diet.\n", 'white', 'on_red')
                return check()
        else:
            cprint('{:*^40}'.format('YOUR RECIPES'), 'blue', 'on_white')
            print("")
            for recipe in selectedRecipes:
                cprint(recipe.title(), 'white', 'on_red')
                print("")

    else:
        print("""\nPlease select the best option below:

1 - ADD INGREDIENT
2 - REMOVE INGREDIENT""")
        add_or_remove = askUser("Selection: ")
        if add_or_remove == 1:
            return select_items()
        elif add_or_remove == 2:
            print(f"""\nWhich ingredient do you want to remove from your list?
Type the corresponding number below:\n""")
            for count,ingredient in enumerate(userIngredients,1):
                print(f"{count} - {ingredient.title()}")
            remove = askUser("Selection: ")
            del userIngredients[remove-1]

            cprint('{:*^40}'.format(f"Your 'PANTRY' list"), 'blue', 'on_white')

            if len(userIngredients) > 0:
                for count,ingredient in enumerate(userIngredients,1):
                    print(f"{count} -  {ingredient.title()}")
                return check()
            
            else:
                cprint("You have no items in your PANTRY\n", 'white', 'on_red')
                return check()







def fullRecipeList():
    print("")
    cprint('{:*^40}'.format(f'PANTRY Full Recipe List'), 'blue', 'on_white')
    print("")
    for count,recipe in enumerate(recipes.recipes, 1):
        print(f"{count} - {recipe['name'].title()}")
    print("")





def endFunction():
    cprint('{:*^40}'.format('Thanks for using PANTRY!'), 'white', 'on_blue')
    endFunc = askUser("""1 - I want to see what else I can make!
2 - I'm done with this.

Selection: """)
    if endFunc == 1:
        return hasIngredients()
    else:
        print("See ya!")    
