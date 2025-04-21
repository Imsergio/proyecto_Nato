"""Módulo para el botón"""
import clases.Transform

# Estilo consistente para los botones
button_style = {
    "font": ("Arial", 10, "bold"),
    "fg": "white",
    "activebackground": "#45a049",
    "borderwidth": 0,
    "highlightthickness": 0,
    "relief": "solid",
    "padx": 10,
    "pady": 5
}

def button_send(entry, list_word, app, file_path):
    """Convertir palabra a alfabeto fonético"""
    word = entry.get().upper()
    list_word.delete(0, "end")
    if word.isalpha():
        ouput = app.transform_word_dict(word, app.read_data(file_path))
        for index, element in enumerate(ouput):
            list_word.insert(index, element)
        list_word.focus()
        list_word.selection_set(0)
    else:
        list_word.insert(0,"Entrada no valida")
def button_clean(entry, list_word):
    """Eliminar contenido de la caja de texto"""
    entry.delete(0, "end")
    list_word.delete(0, "end")
    entry.config(fg="black")
    entry.focus() 