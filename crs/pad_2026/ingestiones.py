import json



class Ingestiones():
    def __init__(self):
        self.ruta_static = "C:/Proyecto_repositorio/ubert_toro/crs/pad_2026/static/"
    def leer_json(self,nombre):
        # r read w write
        ruta_json = f"{self.ruta_static}json/datos_personas.json"
        with open(ruta_json, "r",encoding="utf-8") as f:
            datos = json.load(f)
        return datos
        
    def leer_txt(self):
        # r read w write

        ruta_txt = f"{self.ruta_static}txt/info.txt"
        with open(ruta_txt, "r",encoding="utf-8") as f:
            datos = f.read()
        return datos

    def leer_varios_txt(self,nombre):
        # r read w write
        ruta_txt = f"{self.ruta_static}txt/{nombre}"
        with open(ruta_txt, "r",encoding="utf-8") as f:
            datos = f.read()
        return datos 
    
    def  leer_cualquier_ecxel(self,nombre=""):
        pass

    def  leer_cualquier_csv(self,nombre=""):
        pass

    def  leer_html(self,url=""):
        pass

    def  leer_bd(self,nombre_bd="",servidor="",puerto=0):
        pass

    def  leer_api(self,url=""):
        pass

    def escribir_txt(self,nombre,datos):
        # r read w write
        
        ruta_txt = f"{self.ruta_static}txt/{nombre}"
        with open(ruta_txt, "w",encoding="utf-8") as f:
            f.write(datos)
        return datos
    



              
inges = Ingestiones()
datos_json = inges.leer_json("datos_personas.json")
print(datos_json)
print("************************************************************************************************************")
print("************************************************************************************************************")
datos_txt = inges.leer_txt()
print(datos_txt)
print("************************************************************************************************************")
print("************************************************************************************************************")
nombre_archivo= "info copy.txt"
datos_txt = inges.leer_varios_txt(nombre_archivo)
print(datos_txt)


