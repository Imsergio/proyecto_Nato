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
# Configuración mejorada de la ventana
window.title("Alfabeto fonético NATO")
window.geometry("350x500")
window.minsize(350, 500)
window.config(bg="#f0f0f0")  # Fondo más suave

# Frame principal con mejor estética
frame_principal = Frame(window, bg="#f0f0f0")
frame_principal.config(padx=25, pady=25)
frame_principal.pack(fill="both", expand=True)

# Estilo consistente para los botones
button_style = {
    "font": ("Arial", 10, "bold"),
    "fg": "white",
    "activebackground": "#45a049",
    "borderwidth": 2,
    "relief": "raised",
    "padx": 10,
    "pady": 5
}
#ruta proyecto
path = sys.argv[0] #
if path.endswith('.py') or path.endswith('.exe'):
    path = path[:path.rindex('/')]
#rutas de archivos
image_path = path + "./assets/img/nato.png"
csv_path = path + "./assets/data/nato_phonetic_alphabet.csv"

#frame principal
frame_principal = Frame(window)
frame_principal.config(padx=20, pady=30)
frame_principal.pack(side="top", pady=10)

#insertamos la imagen
imagen = PhotoImage(file=image_path)
imagen_label = Label(frame_principal, image=imagen)
imagen_label.pack(side="top", pady=10)

#creamos la caja de texto y establecemos el foco en la entrada de texto al abrir la aplicación
entry = Entry(frame_principal, font=("Arial", 11),justify="center",width=28,
        highlightthickness=1,highlightcolor="blue",bg="white")
entry.focus() 
entry.pack(side="top", pady=10)

# Añadir placeholder al Entry
entry.insert(0, "Escribe una palabra...")
entry.config(fg="grey")

def on_entry_click(event):
    if entry.get() == "Escribe una palabra...":
        entry.delete(0, "end")
        entry.config(fg="black")

def on_focusout(event):
    if entry.get() == "":
        entry.insert(0, "Escribe una palabra...")
        entry.config(fg="grey")

entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)

#creamos el frame para los botones
frame1 = Frame(frame_principal)
frame1.pack(side="top")

#creamos el botón para enviar la palabra
btn_send = Button(frame1, text="Convertir", **button_style,bg="#4caf50",
                 command=lambda: button.button_send(entry, list_word, app, csv_path))
btn_send.pack(side="left", padx=5)
#creamos el botón para limpiar la lista
btn_clean = Button(frame1, text="Limpiar", **button_style,bg="#f44336",
                  command=lambda: button.button_clean(entry, list_word))
btn_clean.pack(side="right", padx=5)

#creamos el frame para la lista
frame2 = Frame(frame_principal)
frame2.pack(side="top", pady=10)

scrollbar = Scrollbar(frame2)
scrollbar.pack(side="right", fill="y" )

#creamos la lista
list_word = Listbox(frame2,width=20, yscrollcommand = scrollbar.set, font=("Arial", 10),exportselection=True,selectmode="extended",
            bd=1,highlightthickness=1,highlightcolor="blue")
#configuramos la lista
scrollbar.config( command = list_word.yview )
#mostramos la lista
list_word.pack(side="top",fill ="both", pady=10)


window.mainloop()
