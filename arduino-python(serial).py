import serial
arduino_port = "COM8" #serial port of Arduino
baud = 9600 #arduino uno runs at 9600 baud
fileName="prueba2.csv" #name of the CSV file generated
ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port:" + arduino_port)
file = open(fileName, "a")
print("Created file")
#display the data to the terminal
getData = str(ser.readline().decode())
data=getData[0:][:-2]
print(data)

#add the data to the file
file = open(fileName, "a") #append the data to the file
file.write(data + "\n") #write data with a newline

#close out the file
file.close()

print_labels = False
line = 0 #start at 0 because our header is 0 (not real data)
while True:
    getData = str(ser.readline().decode())
    data=getData[0:][:-2]
    print(data)
    file = open(fileName, "a")
    file.write(data + "\n") #write data with a newline
    
    
print("Data collection complete!")
file.close()


ser.close()
