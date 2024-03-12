import json
from scrapper import Json_Builder

def ProcesarGuardar(url, output_filename):
    json_builder = Json_Builder(url)
    result = json_builder.GetDatos(url)
    existing_data = {}
    try:
        with open(output_filename, 'r') as infile:
            existing_data = json.load(infile)
    except FileNotFoundError:
        pass
    existing_data.update(result)
    with open(output_filename, 'w') as outfile:
        json.dump(existing_data, outfile, indent=4)

if __name__ == "__main__":
    urls = [
        "https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059746-carnes-y-aves/",
        "https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060182-azucar-y-edulcorante",
        "https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/5000189-cereales-y-barritas"
    ]
    output_filenames = [
        "carnes.json",
        "azucares.json",
        "cereales.json"
    ]

    for url, output_filename in zip(urls, output_filenames):
        ProcesarGuardar(url, output_filename)
