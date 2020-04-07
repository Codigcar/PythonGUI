from tkinter import *

#ventana
raiz = Tk()


#Frame
miFrame = Frame() #Crea Frame
miFrame.pack()  #Inserta a la ventana Raiz
miFrame.config(bg="red") 
miFrame.config(width = "650", height ="350")
miFrame.config(relief = "sunken",bd=35) #Bordes y tamaño
miFrame.config(cursor = "pirate")

#Bucle
raiz.mainloop()


