from tkinter import *

#Raiz
raiz = Tk()

#Frame
miFrame = Frame(raiz, width = 1200, height = 600)
miFrame.pack()

#Label
nombreLabel = Label(miFrame, text= "Nombre:")
###ombreLabel.place( x=120, y=100 )
nombreLabel.grid(row = 0 , column = 0)

#CuadroTexto
cuadroTexto = Entry(miFrame)  #en qué cuerpo aparece
###cuadroTexto.place( x = 100, y =200) #lugar donde irá
cuadroTexto.grid(row = 0, column = 1)


raiz.mainloop()