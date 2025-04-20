# Relative import option
from clases.Transform import Transform_word

def button_clicked(entry, list_word, app):
    """Convertir palabra a alfabeto fonético"""
    word = entry.get().upper()
    list_word.delete(0, "end")
    if word.isalpha():
        ouput = app.transform_word_dict(word, app.read_data())
        for index, element in enumerate(ouput):
            list_word.insert(index, element)
    else:
        list_word.insert(1,"Escribe solo letras")