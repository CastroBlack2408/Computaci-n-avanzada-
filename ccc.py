import tkinter as tk
from tkinter import *
 
ventana = tk.Tk()

ventana.title("Tu Chocolatito del Sabor")
ventana.geometry("600x480+211+25")
ventana.configure(bg="#AC3949")
imagen = tk.PhotoImage(file = "principal ventana.png")
imagen1 = tk.PhotoImage(file = "1.png")
imagen2 = tk.PhotoImage(file = "2.png")


etiqueta_imagen1=tk.Label(ventana,height=420,width=420, image= imagen)

etiqueta_imagen1.pack()

def catalogo(ventana):
    ventana1 = tk.Tk()
    ventana1.title("Catalogo")
    ventana1.geometry("600x480+211+25")
    ventana1.configure(bg="blue")

   
    etiqueta_imagen1=tk.Label(ventana1,height=110,width=210, image= imagen1)
    etiqueta_imagen1.pack()



    entrada = Entry(ventana1,font=13)
    entrada.pack()

    
    ventana1.mainloop()




boton = tk.Button(ventana,height=4,width=12, text ="Ver Catalogo",command=lambda:catalogo(ventana))
boton.place(x=250,y=275)



label=tk.Label(ventana,text="Bienvenidos a tu Tienda del Sabor")
label.place(x=200,y=346)









ventana.mainloop()