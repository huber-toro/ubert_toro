
# Evidencia de aprendizaje Clases, Objetos y archivos de datos en Python
# Ubert Toro - IUDIGITAL

import requests
import json
import os

class Ingestiones():
    def __init__(self):
        self.ruta_static = "SRC/pad_2026/Static/"
        
    def leer_api(self, url="http://api.citybik.es/v2/networks"):
        response = requests.get(url)
        return response.json()

    def escribir_json(self, nombre, datos):
        ruta_json = "{}/Json/{}".format(self.ruta_static, nombre)
        os.makedirs(os.path.dirname(ruta_json), exist_ok=True)
        with open(ruta_json, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

# Uso
inges = Ingestiones()
datos_api = inges.leer_api()
print(datos_api["networks"][:5])  # muestra solo los primeros 5 sistemas

inges.escribir_json("Actividad_1.json", datos_api)








