# Evidencia de aprendizaje Clases, Objetos y archivos de datos en Python
# Ubert Toro - IUDIGITAL

import sys
import io
import requests
import json
import os

# Forzar salida en UTF-8 para evitar errores en Windows/GitHub Actions
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

class Ingestiones:
    def __init__(self):
        # Carpeta base donde se guardarán los archivos
        self.ruta_static = "src/pad_2026/static/"
        
    def leer_api(self, url="http://api.citybik.es/v2/networks"):
        """Lee datos desde la API de CityBikes"""
        response = requests.get(url)
        return response.json()

    def escribir_json(self, nombre, datos):
        """Escribe los datos en un archivo JSON dentro de la carpeta static/Json"""
        ruta_json = os.path.join(self.ruta_static, "Json", nombre)
        os.makedirs(os.path.dirname(ruta_json), exist_ok=True)
        with open(ruta_json, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

# Uso de la clase
if __name__ == "__main__":
    inges = Ingestiones()
    datos_api = inges.leer_api()
    
    # Mostrar solo los primeros 5 sistemas de la API
    print(datos_api["networks"][:5])
    
    # Guardar todo el JSON en un archivo
    inges.escribir_json("Actividad_1.json", datos_api)
