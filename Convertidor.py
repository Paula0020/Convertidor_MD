import os
import tkinter as tk
from tkinter import *
from obspy import read

root=tk.Tk()
root.title("Convertidor de archivos")
root.geometry("450x230")
root.resizable(0, 0)
color="honeydew3"
root.configure(bg=color)

path_guardar=" "
archivo=" "
f_path=" "

Show= Label(root,text="Archivos reftek130 a mseed \n Guatemala 2021",font= "Times 8",bg=color, fg="RoyalBlue4")
Show.grid(row=0, column=0,sticky="W")
k= Label(root,text="Convertidor de archivos",font= "Cambria 20",bg=color, fg="white")
k.grid(row=3, column=0,columnspan=2)
espace= Label(root,text=" ",font= "times 12",bg=color)
espace.grid(row=4, column=0)

def extraer():
    global archivo
    global f_path
    file_path = tk.filedialog.askdirectory()
    f_path=file_path
    archivo = os.listdir(file_path)

Show= Label(root,text="Seleccione una carpeta para la extracción: ",font= "Times 12",bg=color, fg="RoyalBlue4")
Show.grid(row=5, column=0)
Get_Button = Button(root,bd=1,font="cambria 9 ", background="white", text="Selección",relief="sunken",command= extraer)
Get_Button.grid(row=5, column=1)

def getpath():
    global path_guardar
    pp = tk.filedialog.askdirectory()
    path_guardar=pp
    
def guardar():
    try:
        for i in archivo:
            a= read(f_path+"/"+i)
            a.write(path_guardar+"/"+i+".mseed",format="MSEED")
        tk.messagebox.showinfo(message= "Conversión completada")
    except:
        tk.messagebox.showerror(title=None, message="El tipo de archivo no coincide con los esperado. Conversión no realizada.")

Show2= Label(root,text="Seleccione una carpeta para guardar los archivos mseed: ",font= "Times 12",bg=color, fg="RoyalBlue4")
Show2.grid(row=7, column=0)
Get_Button2 = Button(root,bd=1,font="cambria 9", background="white", text="Selección",relief="sunken",command= getpath)
Get_Button2.grid(row=7, column=1)
space= Label(root,text="",font= "Times 12",bg=color, fg="RoyalBlue4")
space.grid(row=8, column=0)
Aceptar = Button(root,bd=1,font="cambria 11", background="tomato2",fg="white", text="Aceptar",relief="flat",command= guardar)
Aceptar.grid(row=9, column=0,columnspan=2)
root.mainloop()

