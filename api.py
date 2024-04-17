from fastapi import FastAPI, Path, Query
import json


app = FastAPI()

with open("carnes.json", "r") as file:
    resultado_url1 = json.load(file)

with open("azucares.json", "r") as file:
    resultado_url2 = json.load(file)

with open("cereales.json", "r") as file:
    resultado_url3 = json.load(file)

@app.get("/")
def home():
    return {"Datos": "Hola mundo"}

@app.get("/inventario/{archivo_json}/{id_item}")
def inventario_info(archivo_json: str, id_item: str = Path(description="El identificador único del item")):
    if archivo_json == "carnes":
        resultado = resultado_url1
    elif archivo_json == "azucares":
        resultado = resultado_url2
    elif archivo_json == "cereales":
        resultado = resultado_url3
    else:
        return {"Error": "Archivo JSON no encontrado"}

    if id_item in resultado:
        print(resultado[str(id_item)])
        return {resultado[str(id_item)]}
    return {"Datos": "Item no encontrado"}

@app.get("/inventario/{archivo_json}/{id_item}/{parametro}")
def inventario_param(archivo_json: str, id_item: str = Path(description="El identificador único del item"), parametro: str = Path(description="El parámetro que queremos obtener del item")):
    if archivo_json == "carnes":
        resultado = resultado_url1
    elif archivo_json == "azucares":
        resultado = resultado_url2
    elif archivo_json == "cereales":
        resultado = resultado_url3
    else:
        return {"Error": "Archivo JSON no encontrado"}

    if id_item in resultado:
        if parametro in resultado[id_item]:
            return {parametro: resultado[id_item][parametro]}
    return {"Datos": "Item no encontrado"}
