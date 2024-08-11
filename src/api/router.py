import requests
from typing import Dict
from fastapi import FastAPI
from pydantic import BaseModel
from retriver.parser.parser import get_page_features
from retriver.url.url_adapter import adapt_url_to_be_valid


class Item(BaseModel):
    url: str


app = FastAPI()


@app.post("/get_endpoints/")
def get_endpoints(item: Item) -> Dict:
    url = adapt_url_to_be_valid(item.url)

    try:
        response = requests.get(url)

    except requests.exceptions.MissingSchema:
        return {"error": "The provided url is not a valid url"}

    except requests.exceptions.ConnectionError:
        return {"error": "Unable to connect to the requested url"}

    else:
        return {"webmap": get_page_features(response.content, url)}
