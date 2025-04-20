"""CLASE CONVERTIR DATOS ALFABETO FONETICO"""
#Importar librerias
import pandas as pd

#declarar clase
class Transform_word:
    """Convierte una palabra en su equivalente en el alfabeto fonético de la OTAN
    
    param: palabra: palabra a convertir
    param: diccionario: diccionario con las letras y sus equivalentes en el alfabeto fonético de la OTAN
    param: salida: lista con las letras convertidas
    """
    def __init__(self):
        """Inicializa la clase"""
        self.word = ""
        self.dict = ""
        self.output = []

    def read_data(self, path):
        """Obtiene los datos del archivo csv y los guarda en un diccionario"""
        self.dict = pd.read_csv(path)
        self.dict = {row.letter:row.code for (index,row) in self.dict.iterrows()}
        return self.dict

    def transform_word_dict(self, word, phonetic_dict):
        """Convierte una palabra en su equivalente en el alfabeto fonético de la OTAN"""
        self.word = word
        self.dict = phonetic_dict
        self.output = [f"{i+1}. {self.dict[letra]}" for i, letra in enumerate(self.word)]
        return self.output 

# app = Convertir()
# print(app.convertir_palabra_dict("HELLO", app.leer_datos("assets/data/nato_phonetic_alphabet.csv")))





