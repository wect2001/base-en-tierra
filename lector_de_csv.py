#Se importan todas los modulos de pandas
from pandas import *
#Se importa matplotlib
import matplotlib.pyplot as plt

#Se lee el archivo CSV
datos = read_csv("datos_lanzamiento.csv")

#Enviamos las columnas de interes a listas de python
tiempo = datos['TIEMPO_INSTANTANEO'].tolist()
temperatura = datos['TEMP'].tolist()

#Grafica con matplotlib
plt.plot(tiempo, temperatura)

#Agregamos las etiquetas y añadimos una leyenda.
plt.xlabel('Tiempo (s)')
plt.ylabel('Temperatura (°C)')
#plt.title("Titulo")
plt.legend()
plt.savefig('grafica_temperatura.png')
plt.show()

##########################PRUEBAS##########################
#print(temperatura)