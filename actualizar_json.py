import json
from scrapper import Json_Builder

def ProcesarGuardar(url, ruta_salida):
    json_builder = Json_Builder(url)
    resultado = json_builder.GetDatos(url)
    datos_existentes = {}
    try:
        with open(ruta_salida, 'r') as arch_input:
            datos_existentes = json.load(arch_input)
    except FileNotFoundError:
        pass
    datos_existentes.update(resultado)
    with open(ruta_salida, 'w') as arch_input:
        json.dump(datos_existentes, arch_input, indent=4)

if __name__ == "__main__":
    urls = [
        "https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059746-carnes-y-aves/",
        "https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060182-azucar-y-edulcorante",
        "https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/5000189-cereales-y-barritas"
    ]
    archivos_json = [
        "carnes.json",
        "azucares.json",
        "cereales.json"
    ]

    for i in range(len(urls)):
        ProcesarGuardar(urls[i], archivos_json[i])
