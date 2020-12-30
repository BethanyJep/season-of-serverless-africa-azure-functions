import logging
import json

import azure.functions as func
def fetch_meal_data(id: int) -> any:
    '''
    Fetch specific data based on Meals JSON
    '''
    with open("meal.json", "r") as json_file:
            data = json.load(json_file)

    # with open("meal.json") as json_file:
    #     dt = json.load(json_file)
    #     data = json.dumps(dt, indent=4, sort_keys=True)
    mealID = id - 1

    return str(data[mealID])

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        # data = str(json.load(open("meal.json")))
        # loading data directly from json file
        # with open("meal.json", "r") as json_file:
        #     data = str(json.load(json_file))
        # return func.HttpResponse(data[:15])

        # with open("meal.json", "r") as json_file:
        #     data = json.load(json_file)
        # return func.HttpResponse(str(data[0]))

        #Using fetch_meal_data function to fetch data
        return func.HttpResponse(fetch_meal_data(1))