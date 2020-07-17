import recipes
from foodList import ingredients


def greeting():
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
        yes_or_no = askUser("""Sorry, you will need to enter only numbers beside options.
        
    1. I have ingredients to use.
    2. Let me see the full recipe list!

Selection: """)
    if yes_or_no == 1:
        return select_items()
    if yes_or_no == 2:
        return fullRecipeList()




def select_items():
    userIngredients = []
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
            # print(ingredients[cat][key])


        item = askUser("Selection: ")
        while item > len(ingredients[cat])-1:
            print(f"\n{ingredients[cat]['cat'].title()}")
            for key in ingredients[cat]:
                if key != "cat":
                    print(f"{key} - {ingredients[cat][key].title()}")
            item = askUser("""\nYou will need to enter only numbers beside the options.
Selection: """)

        userIngredients.append(ingredients[cat][item])

        cont = askUser("""Would you like to add more?
1 - YES
2 - NO
Selection: """)
        if cont > 2:
            cont = askUser("""\nSorry, you will need to enter only numbers beside options.
1 - YES
2 - NO
Selection: """)

        userIngredients.sort()
    print("\nThe ingredients in your 'PANTRY' are:\n")
    for count,ingredient in enumerate(userIngredients,1):
        print(f"{count}. {ingredient.title()}")
    return userIngredients


def check():
    print("For ")



def fullRecipeList():
    print("FULL RECIPE LIST")
