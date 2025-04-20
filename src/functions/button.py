"""Módulo para el botón"""
import clases.Transform

def button_send(entry, list_word, app):
    """Convertir palabra a alfabeto fonético"""
    word = entry.get().upper()
    list_word.delete(0, "end")
    if word.isalpha():
        ouput = app.transform_word_dict(word, app.read_data())
        for index, element in enumerate(ouput):
            list_word.insert(index, element)
    else:
        list_word.insert(1,"Escribe solo letras")

def button_clean(entry, list_word):
    """Eliminar contenido de la caja de texto"""
    entry.delete(0, "end")
    list_word.delete(0, "end")