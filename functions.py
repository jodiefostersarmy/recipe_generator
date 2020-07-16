import recipes

def askUser(prompt):
    while True:
        try:
            num = int(input(prompt))
            break
        except ValueError:
            print("Please input an integer value\n")
    return num


user_ingredients = []


def get_ingredients(num):
    start = 0
    print("Please type in each ingredient on a new line.")
    while start < int(num):
        ingredients = input(f"Ingredient: ")
        user_ingredients.append(ingredients.lower())
        start += 1

chosen_recipes = []


#two lists, check if these words are in the other list
