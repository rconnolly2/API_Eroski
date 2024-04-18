from fastapi import FastAPI, Path, Query
import json
import uvicorn


class API():
    app = FastAPI()
    def __init__(self, nombre_api: str, lista_json: list):
        self.nombre_api = nombre_api
        self.resultado_url1 = None
        self.resultado_url2 = None
        self.resultado_url3 = None

        #Cargo los json creados a la variable
        self.cargar_datos(lista_json[0], lista_json[1], lista_json[2])

    def cargar_datos(self, archivo1, archivo2, archivo3):
        '''
        Esta función carga los archivos json 
        que se sitúan en la misma dirección 
        que este script: necesita 3 strings que son el nombre del json
        '''
        try:
            arch1 = open(archivo1, "r")
            self.resultado_url1 = json.load(arch1)
            arch2 = open(archivo2, "r")
            self.resultado_url2 = json.load(arch2)
            arch3 = open(archivo3, "r")
            self.resultado_url3 = json.load(arch3)
        except:
            print("Ha habido un error al cargar los jsons")
        finally:
            arch1.close()
            arch2.close()
            arch3.close()



    def ejecutar_api(self):
        '''
        Esta función ejecuta la API pero 
        previamente hay que tener los json cargados
        '''
        uvicorn.run("api:app", host="0.0.0.0", port=80, reload=True)
    
    @app.get("/")
    def home():
        return {"Datos": "Hola mundo"}

    @app.get("/inventario/{archivo_json}/{id_item}")
    def inventario_info(self, archivo_json: str, id_item: str = Path(description="El identificador único del item")):
        if archivo_json == "carnes":
            resultado = self.resultado_url1
        elif archivo_json == "azucares":
            resultado = self.resultado_url2
        elif archivo_json == "cereales":
            resultado = self.resultado_url3
        else:
            return {"Error": "Archivo JSON no encontrado"}

        if id_item in resultado:
            print(resultado[str(id_item)])
            return {resultado[str(id_item)]}
        return {"Datos": "Item no encontrado"}

    @app.get("/inventario/{archivo_json}/{id_item}/{parametro}")
    def inventario_param(self, archivo_json: str, id_item: str = Path(description="El identificador único del item"), parametro: str = Path(description="El parámetro que queremos obtener del item")):
        if archivo_json == "carnes":
            resultado = self.resultado_url1
        elif archivo_json == "azucares":
            resultado = self.resultado_url2
        elif archivo_json == "cereales":
            resultado = self.resultado_url3
        else:
            return {"Error": "Archivo JSON no encontrado"}

        if id_item in resultado:
            if parametro in resultado[id_item]:
                return {parametro: resultado[id_item][parametro]}
        return {"Datos": "Item no encontrado"}






# app = FastAPI()

# with open("carnes.json", "r") as file:
#     resultado_url1 = json.load(file)

# with open("azucares.json", "r") as file:
#     resultado_url2 = json.load(file)

# with open("cereales.json", "r") as file:
#     resultado_url3 = json.load(file)

# @app.get("/")
# def home():
#     return {"Datos": "Hola mundo"}

# @app.get("/inventario/{archivo_json}/{id_item}")
# def inventario_info(archivo_json: str, id_item: str = Path(description="El identificador único del item")):
#     if archivo_json == "carnes":
#         resultado = resultado_url1
#     elif archivo_json == "azucares":
#         resultado = resultado_url2
#     elif archivo_json == "cereales":
#         resultado = resultado_url3
#     else:
#         return {"Error": "Archivo JSON no encontrado"}

#     if id_item in resultado:
#         print(resultado[str(id_item)])
#         return {resultado[str(id_item)]}
#     return {"Datos": "Item no encontrado"}

# @app.get("/inventario/{archivo_json}/{id_item}/{parametro}")
# def inventario_param(archivo_json: str, id_item: str = Path(description="El identificador único del item"), parametro: str = Path(description="El parámetro que queremos obtener del item")):
#     if archivo_json == "carnes":
#         resultado = resultado_url1
#     elif archivo_json == "azucares":
#         resultado = resultado_url2
#     elif archivo_json == "cereales":
#         resultado = resultado_url3
#     else:
#         return {"Error": "Archivo JSON no encontrado"}

#     if id_item in resultado:
#         if parametro in resultado[id_item]:
#             return {parametro: resultado[id_item][parametro]}
#     return {"Datos": "Item no encontrado"}
