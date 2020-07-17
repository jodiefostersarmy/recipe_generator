
ingredients = {    
        1: "vegetables": {
            1: "sweet potato", 
            2: "potatoes - red baby",
            3: "potatoes - gold baby", 
            4: "scallion", 
            5: "tomato - heirloom",
            6: "romaine lettuce", 
            7: "garlic", 
            8: "baby spinach",
            9: "onion - brown", 
            10: "broccoli", 
            11: "carrot", 
            12: "celery", 
            13: "cauliflower",
            14: "onion - red", 
            15: "green peas - frozen", 
            16: "tomato - cherry", 
            17: "arugula" 
            }, 

        "herbs and spices" : { 
        1: "salt - sea", 
        2: "black pepper - cracked", 
        3: "kaffir lime leaf", 
        4: "turmeric - powder",
        5: "sugar",
        6: "pepper flakes - red", 
        7:"paprika powder - smoked", 
        8: "cumin - ground",
        9: "onion powder - dried", 
        10: "garlic powder - dried", 
        11: "basil", 
        12: "coriander/cilantro",
        13: "parsley", 
        14: "pepper - cayenne",
        15: "mustard - powder"
        },

        "sauces and oils" : {
            1: "avocado oil", 
            2: "tamari", 
            3: "maple syrup", 
            4: "mayonnaise", 
            5: "olive oil - extra virgin",
            6: "coconut oil", 
            7: "ghee", 
            8: "thai red curry paste", 
            9: "coconut aminos",
            10 :"soy sauce"
        },

        "fruits" : {
            1: "lemon", 
            2: "lime", 
            3: "avocado", 
            4: "banana", 
            5: "apple", 
            6: "pears", 
            7: "oranges"
        },

        "liquids" : {
            1: "vegetable stock", 
            2: "almond milk", 
            3: "chicken broth", 
            4: "beef bone broth",
            5: "coconut milk", 
            6: "coconut cream", 
            7: "white vingear", 
            8: "balsamic vinegar"
        },

        "animal products" : {
            1: "smoked salmon", 
            2: "egg/s", 
            3: "beef - steak", 
            4: "beef - ground", 
            5: "chicken - ground",
            6: "bacon"
        },

        "dairy" : {
            1: "parmesan cheese", 
            2: "ricotta cheese"
        },

        "nuts and toppings" : {
            1: "nutritional yeast", 
            2: "cashews - raw",
            3: "almonds"
        },

        "asian cooking" : {
            1: "wonton wrappers",
            2: "tempeh"
        }
}

list = []
cont = "yes"

while cont == "yes":

    print("select cat")

    # for key in ingredients:
    #     print(key)
    
    for count,key in enumerate(sorted(ingredients), 1):
        print(f"{count}. {key.title()}")

    cat = input("enter categoty: ")


    for key in ingredients[cat]:
        print(f" {key} - {ingredients[cat][key]}")
        # print(ingredients[cat][key])

    # for key in ingredients[cat]:
    #     print(f" {key} - {ingredients[cat][key]}")
    #     # print(ingredients[cat][key])

    item = int(input("enter item: "))

    list.append(ingredients[cat][item])

    cont = input("would you like to continue?")



print(list)




# ingredients = {    
#         "vegetables": {
#             1: "sweet potato", 
#             2: "potatoes - red baby",
#             3: "potatoes - gold baby", 
#             4: "scallion", 
#             5: "tomato - heirloom",
#             6: "romaine lettuce", 
#             7: "garlic", 
#             8: "baby spinach",
#             9: "onion - brown", 
#             10: "broccoli", 
#             11: "carrot", 
#             12: "celery", 
#             13: "cauliflower",
#             14: "onion - red", 
#             15: "green peas - frozen", 
#             16: "tomato - cherry", 
#             17: "arugula" 
#             }, 

#         "herbs and spices" : { 
#         1: "salt - sea", 
#         2: "black pepper - cracked", 
#         3: "kaffir lime leaf", 
#         4: "turmeric - powder",
#         5: "sugar",
#         6: "pepper flakes - red", 
#         7:"paprika powder - smoked", 
#         8: "cumin - ground",
#         9: "onion powder - dried", 
#         10: "garlic powder - dried", 
#         11: "basil", 
#         12: "coriander/cilantro",
#         13: "parsley", 
#         14: "pepper - cayenne",
#         15: "mustard - powder"
#         },

#         "sauces and oils" : {
#             1: "avocado oil", 
#             2: "tamari", 
#             3: "maple syrup", 
#             4: "mayonnaise", 
#             5: "olive oil - extra virgin",
#             6: "coconut oil", 
#             7: "ghee", 
#             8: "thai red curry paste", 
#             9: "coconut aminos",
#             10 :"soy sauce"
#         },

#         "fruits" : {
#             1: "lemon", 
#             2: "lime", 
#             3: "avocado", 
#             4: "banana", 
#             5: "apple", 
#             6: "pears", 
#             7: "oranges"
#         },

#         "liquids" : {
#             1: "vegetable stock", 
#             2: "almond milk", 
#             3: "chicken broth", 
#             4: "beef bone broth",
#             5: "coconut milk", 
#             6: "coconut cream", 
#             7: "white vingear", 
#             8: "balsamic vinegar"
#         },

#         "animal products" : {
#             1: "smoked salmon", 
#             2: "egg/s", 
#             3: "beef - steak", 
#             4: "beef - ground", 
#             5: "chicken - ground",
#             6: "bacon"
#         },

#         "dairy" : {
#             1: "parmesan cheese", 
#             2: "ricotta cheese"
#         },

#         "nuts and toppings" : {
#             1: "nutritional yeast", 
#             2: "cashews - raw",
#             3: "almonds"
#         },

#         "asian cooking" : {
#             1: "wonton wrappers",
#             2: "tempeh"
#         }
# }

# list = []
# cont = "yes"

# while cont == "yes":

#     print("select cat")

#     # for key in ingredients:
#     #     print(key)
    
#     for count,key in enumerate(sorted(ingredients), 1):
#         print(f"{count}. {key.title()}")

#     cat = input("enter categoty: ")


#     for key in ingredients[cat]:
#         print(f" {key} - {ingredients[cat][key]}")
#         # print(ingredients[cat][key])

#     # for key in ingredients[cat]:
#     #     print(f" {key} - {ingredients[cat][key]}")
#     #     # print(ingredients[cat][key])

#     item = int(input("enter item: "))

#     list.append(ingredients[cat][item])

#     cont = input("would you like to continue?")



# print(list)


