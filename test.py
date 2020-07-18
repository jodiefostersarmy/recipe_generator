recipes = [
    {
        "name": "roasted rainbow potatoes",
        "diet": ["Whole 30", "plant-based"],
        "ingredients": ["1 medium sweet potato", "4 red baby potatoes",
"4 gold baby potatoes", "2 tablespoons avocado oil",
"1 teaspoon sea salt", "½ teaspoon black pepper", "1 whole scallion, minced",
"2 tablespoons fresh parsley, minced", "½ fresh lime, thinly slices",
"Juice and zest from ½ fresh lime"]
    }, 
     {
        "name": "smoked tempeh BLT",
        "diet": ["plant-based", "vegetarian"],
        "ingredients": ["1 1/2 tablespoons reduced-sodium tamari",
"1 tablespoon pure maple syrup", "2 teaspoons smoked paprika",
"1 1/2 teaspoons black pepper, divided", "1 (8-oz.) pkg. tempeh, cut into 16 slices",
"1/2 cup wild black cherry wood chips", "8 (1-oz.) whole-wheat bread slices",
"5 teaspoons canola mayonnaise", "1 heirloom tomato (about 6 oz.), cut into 8 slices",
"8 romaine lettuce leaves, cut in half horizontally"]
    }
]

test = ["potato","salt"]
elevenPM = [name for name in recipes[0]["ingredients"] if str(test) in name]
print(elevenPM)
