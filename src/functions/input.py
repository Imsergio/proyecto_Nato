"""Funciones para entradas de texto"""

def on_entry_click(entry):
    """Borrar el texto de la entrada de texto cuando se hace clic en ella"""
    if entry.get() == "Escribe una palabra...":
        entry.delete(0, "end")
        entry.config(fg="black")

def on_focusout(entry):
    """Restablecer el texto de la entrada de texto cuando se pierde el foco"""
    if entry.get() == "":
        entry.insert(0, "Escribe una palabra...")
        entry.config(fg="grey")