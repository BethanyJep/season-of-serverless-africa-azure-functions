import json


def fetch_meal_data(id: int) -> any:
    '''
    Fetch specific data based on Meals JSON
    '''
    with open("meal.json", "r") as json_file:
            data = json.load(json_file)

    
    mealID = id - 1

    return str(data[mealID])





