"""GUI PROGRAM"""

#importamos la librerías
from tkinter import Tk, Frame, Button, Label, Entry,Listbox, PhotoImage,Scrollbar
import sys

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

#ruta proyecto
path = sys.argv[0] #
if path.endswith('.py') or path.endswith('.exe'):
    path = path[:path.rindex('/')]
#rutas de archivos
image_path = path + "./assets/img/nato.png"
csv_path = path + "./assets/data/nato_phonetic_alphabet.csv"

#insertamos la imagen
imagen = PhotoImage(file=image_path)
imagen_label = Label(window, image=imagen)
imagen_label.pack(side="top", pady=10)

#creamos la caja de texto y establecemos el foco en la entrada de texto al abrir la aplicación
entry = Entry(window, font=("Arial", 10, "italic"),justify="center",width=30)
entry.focus() 
entry.pack(side="top", pady=10)

# Asociar la función a la tecla Enter
entry.bind("<Return>", lambda event: button.button_send(entry, list_word, app, csv_path))

#creamos el frame para los botones
frame1 = Frame(window)
frame1.pack(side="top", pady=10)

#creamos el botón para enviar la palabra
btn_send = Button(frame1, text="Convertir", font=("Arial", 10),
            command=lambda: button.button_send(entry, list_word, app, csv_path))
btn_send.pack(side="left", pady=10, padx=10)
#creamos el botón para limpiar la caja de texto
btn_clean = Button(frame1, text="Limpiar", font=("Arial", 10),
            command=lambda: button.button_clean(entry, list_word))
btn_clean.pack(side="right", pady=10)

#creamos el frame para la lista
frame2 = Frame(window)
frame2.pack(side="top", pady=10)

scrollbar = Scrollbar(frame2)
scrollbar.pack(side="right", fill="y" )

#creamos la lista
list_word = Listbox(frame2, yscrollcommand = scrollbar.set, font=("Arial", 10),exportselection=True,selectmode="extended",bd=1)
#configuramos la lista
scrollbar.config( command = list_word.yview )
#mostramos la lista
list_word.pack(side="top",fill ="both", pady=10)


window.mainloop()
