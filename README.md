Descripción:
Crear una API utilizando FastAPI que recupere datos de alimentos de archivos JSON a través de web scraping utilizando la biblioteca BeautifulSoup 4. Los datos de los alimentos se clasificarán según su categoría y se almacenarán para permitir múltiples solicitudes simultáneas sin esperar el tiempo de respuesta de cada solicitud individual. Se implementará threading para ejecutar el programa con hilos y mejorar la eficiencia de procesamiento.

Requisitos:

- La API deberá estar desarrollada utilizando FastAPI para gestionar las solicitudes HTTP.
- Se utilizará BeautifulSoup 4 para realizar el web scraping y extraer los datos de los alimentos.
- Los datos de los alimentos se almacenarán en archivos JSON y se clasificarán por categoría.
- Se implementarán hilos para permitir la ejecución concurrente de múltiples solicitudes.
- Se establecerán mecanismos de manejo de errores utilizando bloques try-catch para garantizar la robustez del programa.
- Se realizarán pruebas unitarias utilizando pytest para asegurar el correcto funcionamiento del código y la integridad de sus componentes.
