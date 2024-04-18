from api import API

if __name__ == "__main__":
    lista_de_jsons =["azucares.json", "carnes.json", "cereales.json"]
    obj_api = API("Supermercado Eroski", lista_de_jsons)
    obj_api.ejecutar_api()