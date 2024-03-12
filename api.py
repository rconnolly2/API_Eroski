from typing import Annotated
from fastapi import FastAPI, Path, Query
import json


app = FastAPI()

with open("carnes.json", "r") as file:
    result_url1 = json.load(file)

with open("azucares.json", "r") as file:
    result_url2 = json.load(file)

with open("cereales.json", "r") as file:
    result_url3 = json.load(file)

@app.get("/")
def home():
    return {"Datos": "Hola mundo"}

@app.get("/recetas")
def home():
    return {"receta": "Melon"}

@app.get("/inventario/{json_file}/{id_item}/{parametro}")
def inventario_param(json_file: str, id_item: str = Path(description="El identificador único del item"), parametro: str = Path(description="El parámetro que queremos obtener del item")):
    if json_file == "carnes":
        result = result_url1
    elif json_file == "azucares":
        result = result_url2
    elif json_file == "cereales":
        result = result_url3
    else:
        return {"Error": "Archivo JSON no encontrado"}

    if id_item in result:
        if parametro in result[id_item]:
            return {parametro: result[id_item][parametro]}
    return {"Datos": "Item no encontrado"}
