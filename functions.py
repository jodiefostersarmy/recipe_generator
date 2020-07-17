import recipes
from foodList2 import ingredients

def askUser(prompt):
    while True:
        try:
            num = int(input(prompt))
            break
        except ValueError:
            print("Please input an integer value\n")
    return num


def select_items():
    userIngredients = []
    cont = 1

    while cont == 1:

        print("select cat")
        
        for key in ingredients:
                print(f"{key} - {ingredients[key]['cat'].title()}")
        

        cat = int(input("enter category: "))

        print(ingredients[cat]["cat"].title())
        
        for key in ingredients[cat]:
            # Dont print if they key is "cat"
            # Cat is not an ingredient, it is the name of the category
            if key != "cat":
                print(f" {key} - {ingredients[cat][key].title()}")  
            # print(ingredients[cat][key])


        item = int(input("enter item: "))

        userIngredients.append(ingredients[cat][item])

        cont = int(input("""Would you like to add more?
1 - YES
2 - NO
"""))

    print("Your list contains:\n")
    print(userIngredients)
    return userIngredients


#two lists, check if these words are in the other list
