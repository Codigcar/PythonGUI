from tkinter import *

#Raiz
raiz = Tk()

#Frame
miFrame = Frame(raiz)
miFrame.pack()

#Label
miLabel = Label(miFrame, text = "Nombre")
miLabel.grid(row = 0 , column = 0 , padx = 10,pady = 10)

#Texto
miTexto = Entry(miFrame)
miTexto.grid(row = 0 , column = 1, padx = 10,pady = 10)


raiz.mainloop()