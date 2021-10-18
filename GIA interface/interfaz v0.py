#librerias
import tkinter as tk
from tkinter.constants import ANCHOR
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from PIL import ImageTk, Image
import pandas as pd


#configuracion de la ventana
window = tk.Tk()
#icono y titulo de ventana
window.iconbitmap('LOGO_GIA_transparente.ico')
window.title("GIA's Base Control System")

#tamaño y fondo 
window.geometry("940x450")
window['background']=['#1B2631']

#LECTURA DE LOS DATOS CSV
datos = pd.read_csv("datos_lanzamiento.csv")

#tener cuidado para graficar, los csv si estan con decimales con comas pasarlos a puntos
datos['GPS_LONGITUD'] = datos['GPS_LONGITUD'].str.replace(',', '.').astype(float)
datos['GPS_ALTITUD'] = datos['GPS_ALTITUD'].str.replace(',', '.').astype(float)
datos['GPS_LATITUD'] = datos['GPS_LATITUD'].str.replace(',', '.').astype(float)



#print(datos.head(3))
#print(datos['ALTITUD'])



#funciones de prueba
def B0f():
    x = datos['TIEMPO_INSTANTANEO']
    y = datos['ALTITUD']
    
    
    clearFrame()
    figure = plt.Figure(figsize=(5,6), dpi=100)
    figure.patch.set_facecolor('#BB8FCE')
    
    ax = figure.add_subplot(111)
    ax.patch.set_facecolor('#F7DC6F')

    line = FigureCanvasTkAgg(figure, right_frame)
    line.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)


    ax.plot(x,y), ax.grid(True)
    ax.set_xlabel('$x$'),ax.set_ylabel('$y(x)$')
    ax.set_title('TIEMPO CONTRA ALTITUD')
    line.draw()

    #color de los botones
    B0['bg']='#239B56'
    B1['bg']='#FDFEFE'
    B2['bg']='#FDFEFE'
    B3['bg']='#FDFEFE'
    B4['bg']='#FDFEFE'

def B1f():
    #vectores
    x = datos['GPS_LATITUD']
    y = datos['GPS_LONGITUD']
    z = datos['GPS_ALTITUD']
    #limpia el grafico anterior limpiando la figura
    clearFrame()
    figure = plt.Figure(figsize=(5,6), dpi=100)
    
    line = FigureCanvasTkAgg(figure, right_frame)
    line.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)


    ax = figure.add_subplot(111,projection = '3d')
    ax.plot(x,y,z), ax.grid(True)



    #titulo, label y dibujo de la linea
    ax.set_xlabel('$x$'),ax.set_ylabel('$y(x)$')
    ax.set_title('POSICION GPS')

    #color de los botones
    B0['bg']='#FDFEFE'
    B1['bg']='#239B56'
    B2['bg']='#FDFEFE'
    B3['bg']='#FDFEFE'
    B4['bg']='#FDFEFE'
    
def B2f():
    x = np.linspace(0,2*np.pi,100)
    y = np.exp(-0.5*x)*np.sin(4*x)
    #limpia el grafico anterior
    clearFrame()
    figure = plt.Figure(figsize=(5,6), dpi=100)
    ax = figure.add_subplot(111)
    line = FigureCanvasTkAgg(figure, right_frame)
    line.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)


    ax.plot(x,y), ax.grid(True)



    #titulo, label y dibujo de la linea
    ax.set_xlabel('$x$'),ax.set_ylabel('$y(x)$')
    ax.set_title('$y(x)=e^{-0.5x}sin(4x)$')
    line.draw()

    #color de los botones
    B0['bg']='#FDFEFE'
    B1['bg']='#FDFEFE'
    B2['bg']='#239B56'
    B3['bg']='#FDFEFE'
    B4['bg']='#FDFEFE'

def B3f():
    #vectores
    x = np.linspace(0,10,100)
    y = np.exp(x)
    #limpia el grafico anterior
    clearFrame()
    figure = plt.Figure(figsize=(5,6), dpi=100)
    ax = figure.add_subplot(111)
    line = FigureCanvasTkAgg(figure, right_frame)
    line.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)


    ax.plot(x,y), ax.grid(True)


    #titulo, label y dibujo de la linea
    ax.set_xlabel('$x$'),ax.set_ylabel('y(x)')
    ax.set_title('$y(x) = e^{x}$')
    line.draw()

    #color de los botones
    B0['bg']='#FDFEFE'
    B1['bg']='#FDFEFE'
    B2['bg']='#FDFEFE'
    B3['bg']='#239B56'
    B4['bg']='#FDFEFE'
    
def B4f():
    #vectores
    def gaussian(x, mu, sig):
        return 1./(np.sqrt(2.*np.pi)*sig)*np.exp(-np.power((x - mu)/sig, 2.)/2)
    x = np.linspace(0,10,100)
    y = gaussian(x,5,1.3)


    #limpia el grafico anterior
    clearFrame()
    figure = plt.Figure(figsize=(5,6), dpi=100)
    ax = figure.add_subplot(111)
    line = FigureCanvasTkAgg(figure, right_frame)
    line.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)



    ax.plot(x,y), ax.grid(True)



    #titulo, label y dibujo de la linea
    ax.set_xlabel('$x$'),ax.set_ylabel('y(x)')
    ax.set_title('$y(x) = Gaussian(x,5,1.3)$')
    line.draw()
    
    #color de los botones
    B0['bg']='#FDFEFE'
    B1['bg']='#FDFEFE'
    B2['bg']='#FDFEFE'
    B3['bg']='#FDFEFE'
    B4['bg']='#239B56'


#frames para poner los botones y otro para el grafico
left_frame = tk.Frame(window)
left_frame.place(relx=0.03, rely=0.05, relwidth=0.25, relheight=0.9)
left_frame['background']='#A04000'

right_frame = tk.Frame(window, bg='#C0C0C0', bd=1.5)
right_frame.place(relx=0.3, rely=0.05, relwidth=0.65, relheight=0.9)
right_frame['background']='#A04000'

#botones
RH = 0.1
B0 = tk.Button(left_frame,text="ALTURA-TIEMPO",command = B0f)
B0.place(relheight=RH, relwidth=1)

B1 = tk.Button(left_frame,text="COS(4x)",command = B1f)
B1.place(rely=(0.1 + RH*0.54) ,relheight=RH, relwidth=1)

B2 = tk.Button(left_frame,text="EXP(-0.5x)SIN(x)",command = B2f)
B2.place(rely= 2*(0.1 + RH*0.54) ,relheight=RH, relwidth=1)

B3 = tk.Button(left_frame,text="EXP(x)",command = B3f)
B3.place(rely= 3*(0.1 + RH*0.54) ,relheight=RH, relwidth=1)

B4 = tk.Button(left_frame,text="Gaussian(x)",command = B4f)
B4.place(rely= 4*(0.1 + RH*0.54) ,relheight=RH, relwidth=1)

#funcion para eliminar los widgets en un frame
def clearFrame():
    # destroy all widgets from frame
    for widget in right_frame.winfo_children():
        widget.destroy()
        
    # this will clear frame and frame will be empty
    # if you want to hide the empty panel then


window.mainloop()
