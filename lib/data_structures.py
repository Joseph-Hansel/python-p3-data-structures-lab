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
    food_list = []
    for f in spicy_foods:
        new = f.get("name")
        food_list.append(new)
    return food_list    

def get_spiciest_foods(spicy_foods):
    food_list = []
    for f in spicy_foods:
        if f.get("heat_level") > 5:
            food_list.append(f)
    return food_list

def print_spicy_foods(spicy_foods):
    for f in spicy_foods:
        name = f.get("name")
        cuisine = f.get("cuisine")
        heat_level = f.get("heat_level")
        graphic_heat_level = heat_level * "🌶"
        print(f"{name} ({cuisine}) | Heat Level: {graphic_heat_level}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for f in spicy_foods:
        if f.get("cuisine") == cuisine:
            return f

def print_spiciest_foods(spicy_foods):
    food_list = []
    for f in spicy_foods:
        if f.get("heat_level") > 5:
            food_list.append(f)
    for f in food_list:
        name = f.get("name")
        cuisine = f.get("cuisine")
        heat_level = f.get("heat_level")
        graphic_heat_level = heat_level * "🌶"
        print(f"{name} ({cuisine}) | Heat Level: {graphic_heat_level}")


def get_average_heat_level(spicy_foods):
    sum = 0
    for f in spicy_foods:
        heat_level = f.get("heat_level")
        sum += heat_level
    quantity = len(spicy_foods)
    mean = sum / quantity
    return int(mean)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
