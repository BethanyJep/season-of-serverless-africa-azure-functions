import json


def fetch_meal_data(id: int) -> any:
    '''
    Fetch specific data based on Meals JSON
    '''
    with open("meal.json", "r") as json_file:
            data = json.load(json_file)

    
    mealID = id - 1

    return str(data[mealID])


# fetch multiple data
def fetch_mul_meal_data(valRange: int):
    ids = []
    for i in range(1, valRange + 1):
        id = fetch_meal_data(i)
        ids.append(id)

    return ids 


