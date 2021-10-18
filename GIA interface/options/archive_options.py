#librerias
import tkinter as tk
from tkinter.constants import LEFT
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class file:
    def new(window):
        #colores usados en el GIU
        figure_bg = '#ffcc5c' #amarillo crema
        graphic_bg = '#ffeead' #amarillo fuerte
        #font para texto
        text_font = ('Arial',13)
        #LECTURA DE LOS DATOS CSV
        datos = pd.read_csv("data/datos_lanzamiento.csv")

        #tener cuidado para graficar, los csv si estan con decimales con comas pasarlos a puntos
        datos['GPS_LONGITUD'] = datos['GPS_LONGITUD'].str.replace(',', '.').astype(float)
        datos['GPS_ALTITUD'] = datos['GPS_ALTITUD'].str.replace(',', '.').astype(float)
        datos['GPS_LATITUD'] = datos['GPS_LATITUD'].str.replace(',', '.').astype(float)
        datos['PRESION'] = datos['PRESION'].str.replace(',', '.').astype(float)
        datos['TENSION_ELECTRICA_BATERIA'] = datos['TENSION_ELECTRICA_BATERIA'].str.replace(',', '.').astype(float)
        datos['ALTITUD'] = datos['ALTITUD'].str.replace(',', '.').astype(float)

        #frames para colocar graficos
        left_frame = tk.Frame(window, bg=figure_bg, bd=4)
        left_frame.place(relx=0.03, rely=0.05, relwidth=0.65, relheight=0.65)

        right_frame = tk.Frame(window)
        right_frame.place(relx=0.7, rely=0.05, relwidth=0.27, relheight=0.9)

        #bottom frame para poner datos actuales de vuelo
        bottom_frame = tk.Frame(window,bg = figure_bg)
        bottom_frame.place(relx=0.03, rely=0.73, relwidth=0.65, relheight=0.22)
        

        #grafico3d de la izquierda
        #figura
        figure3d = plt.Figure(figsize=(5,6), dpi=100)
        figure3d.patch.set_facecolor(graphic_bg)
        line3d = FigureCanvasTkAgg(figure3d, left_frame)
        line3d.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)

        #variables para grafico 3d
        gps_latitud=datos['GPS_LATITUD']
        gps_longitud=datos['GPS_LONGITUD']
        gps_altitud=datos['GPS_ALTITUD']
        #grafico
        ax3d = figure3d.add_subplot(111,projection = '3d')
        ax3d.plot(gps_latitud,gps_longitud,gps_altitud)
        #titulo, label y dibujo de la linea
        ax3d.grid(True)
        ax3d.set_facecolor(graphic_bg)
        ax3d.set_xlabel('Latitud')
        ax3d.set_ylabel('Longitud')
        ax3d.set_zlabel('Altitud (m)')
        ax3d.set_title('Posicion GPS en el tiempo')

        #graficos de la derecha
        
        #figura
        figure = plt.Figure(figsize=(5,6), dpi=100, constrained_layout = True)
        figure.patch.set_facecolor(figure_bg)
        line = FigureCanvasTkAgg(figure, right_frame)
        line.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
        line.draw()

        #variables para graficos 2d
        tiempo = datos['TIEMPO_INSTANTANEO']
        presion = datos['PRESION']
        temperatura = datos['TEMP']
        tension = datos['TENSION_ELECTRICA_BATERIA']
        #grafico 1
        a1 = figure.add_subplot(311)
        a1.plot(tiempo,presion)
        #personalizacion del grafico
        a1.patch.set_facecolor(graphic_bg)
        a1.set_xlabel('Tiempo (s)',fontsize=9)
        a1.set_ylabel('Presion (Pa)',fontsize=9)
        a1.set_title('Tiempo contra presion',fontsize=10)
        a1.grid(True)

        #grafico 2
        a2 = figure.add_subplot(312)
        a2.plot(tiempo,temperatura)
        #personalizacion del grafico
        a2.patch.set_facecolor(graphic_bg)
        a2.set_xlabel('Tiempo (s)',fontsize=9)
        a2.set_ylabel('Temperatura (\u2103)',fontsize=9)
        a2.set_title('Tiempo contra temperatura',fontsize=10)
        a2.grid(True)

        #grafico 3
        a3 = figure.add_subplot(313)
        a3.plot(tiempo,tension)
        #personalizacion del grafico
        a3.patch.set_facecolor(graphic_bg)
        a3.set_xlabel('Tiempo (s)',fontsize=9)
        a3.set_ylabel('Tension (V)',fontsize=9)
        a3.set_title('Tiempo contra tension',fontsize=10)
        a3.grid(True)

        

        #dato actual (ultima fila en el data frame)
        tiempo_gps = 'Tiempo actual: ' + str(datos['TIEMPO_GPS'].iloc[-1]) + '\n'
        paquetes = 'Paquetes recibidos: ' + str(datos['CONTEO_PAQUETE'].iloc[-1]) +'\n'
        etapa = 'Etapa actual: ' + str(datos['ETAPA'].iloc[-1]) +'\n'
        satelites = 'Satelites captados: ' + str(datos['GPS_SATS'].iloc[-1]) +'\n'
        iteraciones = 'Iteraciones realizadas: ' + str(datos['NUMERO_DE_ITERACION'].iloc[-1]) + '\n'

        #labels para poner texto
        label1 = tk.Label(bottom_frame, 
        text = tiempo_gps + paquetes + etapa + satelites + iteraciones, 
        bg = figure_bg,
        font = text_font,
        justify = LEFT
        )
        label1.pack()
        label1.place(x=20,y=10)

        #Datos interesantes/importantes
        altura_max = 'Altura maxima: ' + str(datos['ALTITUD'].max()) + ' (m)\n'
        presion_max = 'Presion maxima: ' + str(round(datos['PRESION'].max(),2)) + ' (Pa)\n'
        temperatura_max = 'Temperatura maxima: ' + str(datos['TEMP'].max()) + ' (C'u'\N{DEGREE SIGN}'')\n'

        #label 2
        label2 = tk.Label(bottom_frame, 
        text = altura_max + presion_max + temperatura_max, 
        bg = figure_bg,
        font = text_font,
        justify = LEFT
        )
        label2.pack()
        label2.place(x=300,y=10)

    def close(window):
        list = window.place_slaves()
        for l in list:
            l.place_forget()


if __name__ == '__main__':
    file.new()
