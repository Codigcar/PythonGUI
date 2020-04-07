from tkinter import *

#raiz
raiz = Tk()

#Frame
miFrame= Frame(raiz, width = 500, height = 400)
miFrame.pack()

#Label
miLabel = Label(miFrame,text="es un label", fg = "red", font= (18))
miLabel.place( x = 100, y = 200)

raiz.mainloop()


