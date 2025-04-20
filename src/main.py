"""GUI PROGRAM"""

#importamos la librerías
from tkinter import Tk, Frame, Button, Label, Entry,Listbox, PhotoImage
from clases import Transform
from functions import button

#creamos el objeto
app = Transform.Transform_word()

#creamos la ventana
window = Tk()

#configuramos la ventana
window.title("Alfabeto fonético Nato")
window.geometry("300x420")
window.minsize(300, 300)
window.config(padx=20, pady=50)

#insertamos la imagen
imagen = PhotoImage(file="assets/img/nato.png")
imagen_label = Label(window, image=imagen)
imagen_label.pack(side="top", pady=10)

#creamos la caja de texto
entry = Entry(window, font=("Arial", 10, "italic"),width=30)
entry.pack(side="top", pady=10)

# Asociar la función a la tecla Enter
entry.bind("<Return>", lambda event: button.button_send(entry, list_word, app))

#creamos el frame
frame = Frame(window)
frame.pack(side="top", pady=10)

#creamos el botón para enviar la palabra
btn_send = Button(frame, text="Convertir", font=("Arial", 10),
            command=lambda: button.button_send(entry, list_word, app))
btn_send.pack(side="left", pady=10, padx=10)
#creamos el botón para limpiar la caja de texto
btn_clean = Button(frame, text="Limpiar", font=("Arial", 10),
            command=lambda: button.button_clean(entry, list_word))
btn_clean.pack(side="right", pady=10)

#creamos la lista
list_word = Listbox(window, font=("Arial", 10))
list_word.pack(side="top", pady=10)

window.mainloop()
