from tkinter import *
from tkinter import Button

from PIL import ImageTk, Image


def click():
    entered_text = textentry.get()


window = Tk()
window.title("Gym app")
window.configure(background="black")

photo1 = ImageTk.PhotoImage(file="gym.gif")
Label(window, image=photo1, bg="black").grid(row=0, column=0, sticky=W)

Label(window, text="What day is the excercise?", bg="black", fg="white", font="none 12 bold").grid(row=1, column=0,
                                                                                                   sticky=W)

textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)

Button(window, text="Submit", width=6, command=click).grid(row=3, column=0, sticky=W)


window.resizable(0, 0)
window.mainloop()
