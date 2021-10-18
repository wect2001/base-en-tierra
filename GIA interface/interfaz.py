#librerias
import tkinter as tk

#import otros archivos python
from options import help_options as ho
from options import archive_options as ao

#configuracion de la ventana
window = tk.Tk()
#icono, titulo de ventana, tamaño y fondo 
window.iconbitmap('images/LOGO_GIA_transparente.ico')
window.title("GIA's Base Control System")
window.geometry("940x650") 
window.config(bg = '#96ceb4') #verde suave

#barras de menu de la ventanta
menubar = tk.Menu(window)
window.config(menu=menubar)

def new():
    ao.file.new(window)

def close():
    ao.file.close(window)

#menu de archivo
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Nueva misión", command=new)
filemenu.add_command(label="Abrir misión")
filemenu.add_command(label="Guardar misión")
filemenu.add_command(label="Cerrar misión", command=close)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=window.quit)

#menu de edicion
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")

#menu de ayuda
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de..." ,command = ho.help.about)

#labels de los menus
menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

window.mainloop()