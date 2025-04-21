"""GUI PROGRAM"""

#importamos la librerías
from tkinter import Tk, Frame, Button, Label, Entry,Listbox, PhotoImage,Scrollbar
import sys

from clases import Transform
from functions import button
from functions import input

#creamos el objeto
app = Transform.Transform_word()

#creamos la ventana
window = Tk()

#configuramos la ventana
# Configuración mejorada de la ventana
window.title("Alfabeto fonético NATO")
window.geometry("350x500")
window.minsize(350, 500)
window.config(padx=25, pady=25)
window.config(bg="gray")  # Fondo más suave

# Frame principal con mejor estética
frame_principal = Frame(window)
frame_principal.config(padx=25, pady=25)
frame_principal.pack(fill="both", expand=True)

#ruta proyecto
path = sys.argv[0] #
if path.endswith('.py') or path.endswith('.exe'):
    path = path[:path.rindex('/')]
#rutas de archivos
image_path = path + "./assets/img/nato.png"
csv_path = path + "./assets/data/nato_phonetic_alphabet.csv"

#insertamos la imagen
imagen = PhotoImage(file=image_path)
imagen_label = Label(frame_principal, image=imagen)
imagen_label.pack(side="top", pady=10)

#creamos la caja de texto y establecemos el foco en la entrada de texto al abrir la aplicación
entry = Entry(frame_principal, font=("Arial", 11),justify="center",width=28)
# Añadir placeholder al Entry
entry.insert(0, "Escribe una palabra...")
entry.config(fg="grey", background="#e3e3e3")

# entry functions
entry.bind('<FocusIn>', lambda event: input.on_entry_click(entry))
entry.bind('<FocusOut>', lambda event: input.on_focusout(entry))
entry.bind("<Return>", lambda event: button.button_send(entry, list_word, app, csv_path))
entry.pack(side="top", pady=10)

#creamos el frame para los botones
frame1 = Frame(frame_principal)
frame1.pack(side="top")

#creamos el botón para enviar la palabra
btn_send = Button(frame1, text="Convertir", **button.button_style, bg="#4caf50",
                 command=lambda: button.button_send(entry, list_word, app, csv_path))
btn_send.pack(side="left", padx=5)
# Bind Enter key separately
btn_send.bind("<Return>", lambda event: button.button_send(entry, list_word, app, csv_path))
#creamos el botón para limpiar la lista
btn_clean = Button(frame1, text="Limpiar", **button.button_style,bg="#f44336",
                  command=lambda: button.button_clean(entry, list_word))
btn_clean.pack(side="right", padx=5)

#creamos el frame para la lista
frame2 = Frame(frame_principal)
frame2.pack(side="top", pady=10)

scrollbar = Scrollbar(frame2)
scrollbar.pack(side="right", fill="y" )

#creamos la lista
list_word = Listbox(frame2,width=20, yscrollcommand = scrollbar.set, font=("Arial", 10),exportselection=True,selectmode="extended",
            highlightthickness=0,fg="grey", background="#e3e3e3")
#configuramos la lista
scrollbar.config( command = list_word.yview )
#mostramos la lista
list_word.pack(side="top",fill ="both", pady=10)


window.mainloop()
