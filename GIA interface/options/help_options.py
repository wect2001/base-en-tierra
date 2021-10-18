import tkinter as tk
from tkinter.constants import LEFT
from PIL import Image, ImageTk

class help:
    def about():
        #nueva ventana
        new_window = tk.Toplevel()
        new_window.iconbitmap('images/LOGO_GIA_transparente.ico')
        new_window.title("About GIA's Base Control System")
        new_window.geometry("600x400")
        new_window.config(bg = '#F2F2F2')
        about_text = 'Version 1.1.1\n15/10/21\nPython 3.8.4\nEscrito por Alvaro Bermudez Marin\nContacto: alvarobermudez04@gmail.com'

        

        #label para la imagen
        gia_logo = ImageTk.PhotoImage(Image.open('images/LOGO GIA transparente v3.png').resize((200, 200)))
        aboutlabellogo = tk.Label(new_window,image=gia_logo)
        #aboutlabellogo.image = gia_logo
        aboutlabellogo.pack()
        
        #texto de about
        aboutlabeltext = tk.Label(new_window,text = about_text,bg = '#F2F2F2',font = ('Arial',10),justify = LEFT)
        aboutlabeltext.pack()
        new_window.mainloop()

if __name__ == '__main__':
    help.about()