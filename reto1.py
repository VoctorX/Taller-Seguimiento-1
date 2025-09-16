import tkinter as tk
from tkinter import messagebox, Toplevel
import random
 
Ruta_del_Logo="adivino.ico"

aleatorio=random.randint(1, 100)

def adivino():
    try:
        num1=int(entry_num1.get())
        if aleatorio==num1:
            resultado=True
            etiqueta_resultado.config(text=f"¡Correcto!\nEl numero es {aleatorio}")
        else:
            etiqueta_resultado.config(text=f"Te equivocaste...\nEl numero era {aleatorio}")
            resultado=False
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese numeros validos")

def nuevo():
    global aleatorio
    aleatorio = random.randint(1, 100)
    etiqueta_resultado.config(text="Nuevo número generado, intenta adivinar de nuevo")

def salir():
    ventana.quit()

def mostrar_ayuda():
    messagebox.showinfo("Ayuda", "Debes ingresar un numero entre 1 y 100.\nSi aciertas, ganaras.")

def acerca_de():
    messagebox.showinfo("Acerca", "Creado por Victor Cordoba\nVerison 1.0\n15/09/2025")


ventana=tk.Tk()
ventana.title("Reto 1")
ventana.geometry("400x200")

try:
    ventana.iconbitmap(Ruta_del_Logo)
except tk.TclError:
    print(f"No se pudo cargar el icono desde la ruta: {Ruta_del_Logo}")

# Barra de menú arriba (como en tu captura)
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

# Menú Archivo
menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Nuevo número", command=nuevo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# Menú Ayuda
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Mostrar ayuda", command=mostrar_ayuda)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

etiqueta_num1=tk.Label(ventana, text="Tu numero: ")
etiqueta_num1.pack()
entry_num1=tk.Entry(ventana)
entry_num1.pack()

frame_botones=tk.Frame(ventana)
frame_botones.pack(pady=10)
 
#Crear y colocar los botones
botton_adivinar=tk.Button(frame_botones, text="Adivinar", command=adivino)
botton_adivinar.pack(side=tk.LEFT, padx=5)

botton_nuevo=tk.Button(frame_botones, text="Nuevo Numero", command=nuevo)
botton_nuevo.pack(side=tk.LEFT, padx=5)

etiqueta_resultado=tk.Label(ventana, text="Esperando tu numero...")
etiqueta_resultado.pack(pady=10)
 
ventana.mainloop()