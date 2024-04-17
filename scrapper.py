from bs4 import BeautifulSoup, Tag
from abc import ABC, abstractmethod
import requests
import threading

class JsonBuilderAbstracto(ABC):
    @abstractmethod
    def GetIngredientes(self, doc, dic_item):
        pass

    @abstractmethod
    def GetInstruccionesConservacion(self, doc, dic_item):
        pass

    @abstractmethod
    def GetInfoNutricional(self, doc, dic_item):
        pass

class Json_Builder(JsonBuilderAbstracto):
    def __init__(self, url):
        self.resultado = {}
        self.GetDatos(url)


    def GetDatos(self, url):
        datos = requests.get(url)
        doc = BeautifulSoup(datos.text, "html.parser")
        lis_items = doc.find_all(class_="col col-xs-12 col-sm-12 col-md-12 col-lg-12 product-item big-item")
        self.resultado = {}

        for i in range(len(lis_items)):
            dat_item = lis_items[i]
            item = {} # Diccionario local donde guardare titulo, precio, precio por kg si tiene, img, estrellas

            # Título de alimento
            item["titulo"] = dat_item.select("h2[class='product-title'] a")[0].text.strip()

            # Precio en euros
            item["precio"] = dat_item.select("span[class='price-offer-now']")[0].text.strip() + "€" # Concateno con signo de €

            # Precio por kilo si tiene en caso contrario nulo:
            lis_prec_pes = dat_item.select("p[class='quantity-price']")
            if len(lis_prec_pes) > 0: # Si tiene peso por kilo
                str1 = lis_prec_pes[0].select_one(".quantity-product")
                str2 = lis_prec_pes[0].select_one(".price-product")
                if isinstance(str1, Tag) and isinstance(str2, Tag): # Si los dos son Bs4.tags y no datos None
                    item["precio_peso"] = str1.text.strip() + " " + str2.text.strip().replace("\xa0", "")
                else:
                    item["precio_peso"] = None
            else:
                item["precio_peso"] = None

            # Guardo url img
            item["img"] = dat_item.find("img", class_="product-img")["src"]

            # Estrellas
            item["estrellas"] = dat_item.find("div", class_='product-col-50 starbar-container').find("div").text.strip().replace("\xa0", "") # Cojo el texto del div hijo de product-col-50 starbar-container y filtro los &nbsp

            # Guardo a self.resultado
            self.resultado[i] = item

            # Ahora saco información detallada con otra solicitud al alimento/item:
            url_item = "https://supermercado.eroski.es" + dat_item.find("h2", class_="product-title").find("a")["href"]
            threading.Thread(target=self.SacarDetallesItem, args=(url_item, item)).start()

        return self.resultado

    def SacarDetallesItem(self, url_item: str, dic_item: dict):
        datos = requests.get(url_item)
        doc = BeautifulSoup(datos.text, "html.parser")
        self.GetIngredientes(doc, dic_item)
        self.GetInstruccionesConservacion(doc, dic_item)
        self.GetInfoNutricional(doc, dic_item)

    def GetIngredientes(self, doc, dic_item):
        ingred = doc.select_one("div[class='col col-lg-12 col-md-12 col-sm-12 col-xs-12 border-0 feature feature-text feature-text-ingredients']")
        dic_item["ingredientes"] = ingred.select_one(".text").text.strip() if isinstance(ingred, Tag) else None

    def GetInstruccionesConservacion(self, doc, dic_item):
        ins_conserv = doc.select_one("div[class='col col-lg-12 col-md-12 col-sm-12 col-xs-12 border-0 feature feature-text feature-text-preservation']")
        dic_item["ins_conservación"] = ins_conserv.select_one(".text").text.strip() if isinstance(ins_conserv, Tag) else None

    def GetInfoNutricional(self, doc, dic_item):
        elem_ul = doc.find("ul", class_="list")
        nutr = {}
        if elem_ul:
            for li_element in elem_ul.find_all('li'):
                key = li_element.contents[0].strip()
                valor = li_element.span.get_text(strip=True)
                nutr[key] = valor
        dic_item["nutrientes"] = None


json_builder = Json_Builder("https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059746-carnes-y-aves/")

hilos = threading.enumerate()
num_hilos = len(hilos)

for i in range(num_hilos):
    hilo_actual = hilos[i]
    if hilo_actual != threading.current_thread():
        hilo_actual.join()

#print(json_builder.resultado)

    



