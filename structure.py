recipes = [
    {
        "name": "pepperoni pizza",
        "diet": "whole 30",
        "ingredients": ("pepperoni", "flour", "cheese")
    },
    {
        "name": "quesadilla",
        "diet": "",
        "ingredients": ("cheese", "tortilla", "chicken")
    },
    {
        "name": "taco",
        "diet": "whole 30",
        "ingredients": ("cheese", "tortilla", "beef")
    }
]

ingredient = "pepperoni"
chosen_recipes = []

for recipe in recipes:
    if recipe["diet"] == "whole 30":
        if ingredient in recipe["ingredients"]:
            chosen_recipes.append(recipe["name"])

print(chosen_recipes)

