
from tkinter import *
w1 = Tk()
w1.title("Calculator")
#w1.geometry('400x500')

BUTTON_WIDTH = 5
BUTTON_HEIGHT = 3


entry = Text(width= 20, height= 1, pady=5)
entry.grid(row=0, column=0, columnspan=4)

button1 = Button(w1, text='7', fg='black', bg='gray', height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
button1.grid(row=1, column=0)

button2 = Button(w1, text=' 8 ', fg='black', bg='gray', height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
button2.grid(row=1, column=1)

button3 = Button(w1, text=' 9 ', fg='black', bg='gray', height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
button3.grid(row=1, column=2)

button3 = Button(w1, text=' x ', fg='black', bg='gray', height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
button3.grid(row=1, column=3)

button3 = Button(w1, text=' 4 ', fg='black', bg='gray', height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
button3.grid(row=2, column=0)

button3 = Button(w1, text=' 5 ', fg='black', bg='gray', height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
button3.grid(row=2, column=1)

button3 = Button(w1, text=' 6 ', fg='black', bg='gray', height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
button3.grid(row=2, column=2)

button3 = Button(w1, text=' - ', fg='black', bg='gray', height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
button3.grid(row=2, column=3)

button3 = Button(w1, text=' 1 ', fg='black', bg='gray', height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
button3.grid(row=3, column=0)

button3 = Button(w1, text=' 2 ', fg='black', bg='gray', height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
button3.grid(row=3, column=1)

button3 = Button(w1, text=' 3 ', fg='black', bg='gray', height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
button3.grid(row=3, column=2)

button3 = Button(w1, text=' + ', fg='black', bg='gray', height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
button3.grid(row=3, column=3)

button3 = Button(w1, text=' = ', fg='black', bg='gray', height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
button3.grid(row=4, column=0)

button3 = Button(w1, text=' 0 ', fg='black', bg='gray', height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
button3.grid(row=4, column=1)

button3 = Button(w1, text=' . ', fg='black', bg='gray', height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
button3.grid(row=4, column=2)

button3 = Button(w1, text=' / ', fg='black', bg='gray', height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
button3.grid(row=4, column=3)


w1.mainloop()