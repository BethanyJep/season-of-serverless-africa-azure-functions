import logging
import json

import azure.functions as func

from .fetchData import fetch_meal_data

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
        user = req.params.get('id')
        if user == None:
            return func.HttpResponse("no ID provided. use http://localhost:7071/api/HttpTrial/?id=1")

        return func.HttpResponse(json.dumps(fetch_meal_data(int(user))))