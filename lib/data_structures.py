spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    #Return a list of the names of each spicy food.
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    #Return a list of foods with heat_level > 5.
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    #Return the dictionary of the food whose cuisine matches the given cuisine.
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    #Print only the foods with heat_level > 5
    #using the same format as print_spicy_foods.
    
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)

def get_average_heat_level(spicy_foods):
    #Return the integer average heat level of all foods.
    total = sum(food["heat_level"] for food in spicy_foods)
    return total // len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    #Add a new spicy food dictionary to the list and return the list.
    #The original list is modified (like list.append).

    spicy_foods.append(spicy_food)
    return spicy_foods
