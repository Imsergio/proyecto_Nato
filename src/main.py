"""GUI PROGRAM"""

#importamos la librerías
from tkinter import Tk, Button, Label, Entry,Listbox, PhotoImage

window = Tk()
window.title("Alfabeto fonético Nato")
window.geometry("300x420")
window.minsize(300, 300)
window.config(padx=20, pady=50)

#insertamos la imagen
imagen = PhotoImage(file="assets/img/nato.png")
imagen_label = Label(window, image=imagen)
imagen_label.pack(side="top", pady=10)
#creamos la etiqueta
word = Label(window, text="", font=("Arial",10, "italic"))
word.pack(side="top", pady=10)
#creamos la caja de texto
entry = Entry(window, font=("Arial", 10, "italic"),width=40)
entry.pack(side="top", pady=10)
#creamos el botón
button = Button(window, text="Convertir", font=("Arial", 10))
button.pack(side="top", pady=10)
#creamos la lista
list_word = Listbox(window, font=("Arial", 10))
list_word.pack(side="top", pady=10)

window.mainloop()


