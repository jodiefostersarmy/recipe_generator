import recipes
from foodList import ingredients
from termcolor import colored, cprint

def greeting():
    cprint("""
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
""", 'white')

    cprint("""This application will provide you with suggested recipes for diets 
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
""", 'white')


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
    # userIngredients = []
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
            # Dont print if they key is "cat"
            # Cat is not an ingredient, it is the name of the category
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
    
    # if cont == 2:


    print("\nThe ingredients in your 'PANTRY' are:\n")
    for count,ingredient in enumerate(userIngredients,1):
        print(f"{count}. {ingredient.title()}")
    
    return check()


def check():
    checking = askUser("""\nIs this correct?
1 - YES
2 - NO
Selection: """)
    if checking == 1:
        diet = askUser("""\nAre you following any of the diets listed below?
1 - Whole 30
2 - Vegetarian
3 - Plant-based
Selection: """)
    else:
        add_or_remove = askUser("""\nPlease select the best option below:
1 - ADD INGREDIENT
2 - REMOVE INGREDIENT
Selection: """)
        if add_or_remove == 1:
            return select_items()
        elif add_or_remove == 2:
            for count,ingredient in enumerate(userIngredients,1):
                print(f"{count} - {ingredient.title()}")
            remove = askUser(f"""\nWhich ingredient do you want to remove from your list?
Type the corresponding number below:

Selection: """)
            del userIngredients[remove-1]

            cprint('{:*^40}'.format(f"Your 'PANTRY' list"), 'blue', 'on_white')

            if len(userIngredients) > 0:
                for count,ingredient in enumerate(userIngredients,1):
                    print(f"{count} - {ingredient.title()}")
            else:
                cprint("You have no items in your PANTRY\n", 'white', 'on_red')



def fullRecipeList():
    print("FULL RECIPE LIST")
