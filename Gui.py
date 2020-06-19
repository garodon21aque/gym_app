from tkinter import *
from tkinter import Button

from PIL import ImageTk, Image



#main page def and config
window = Tk()
window.title("Gym app")
window.configure(background="black")
#Main bg Image from main library
photo1 = ImageTk.PhotoImage(file="gym.gif")
Label(window, image=photo1, bg="black").grid(row=0, column=0, sticky=W)
#def section

def mb_day1():
    return

def mb_day2():
    return
def mb_day3():
    return
def mb_day4():
    return
def mb_day5():
    return
def mb_day6():
    return
def mb_day7():
    return

#main window text
Label(window, text="What day is the excercise?", bg="black", fg="white", font="none 12 bold").grid(row=1, column=0,
                                                                                                   sticky=W)
my_button_day1 = Button(window, text="Monday", bg="black", pidx=30, command=mb_day1)
my_button_day2 = Button(window, text="Tuesday", bg="black", pidx=30, command=mb_day2) 
my_button_day3 = Button(window, text="Wednesday", bg="black", pidx=30, command=mb_day3)   
my_button_day4 = Button(window, text="Thursday", bg="black", pidx=30, command=mb_day4)
my_button_day5 = Button(window, text="Friday", bg="black", pidx=30, command=mb_day5)
my_button_day6 = Button(window, text="Saturday", bg="black", pidx=30, command=mb_day6)
my_button_day7 = Button(window, text="Sunday", bg="black", pidx=30, command=mb_day7)
#refference for positions with .grid

my_button_day1.grid(row=3,column=1, sticky=W)
my_button_day2.grid(row=3,column=2, sticky=W)
my_button_day3.grid(row=3,column=3, sticky=W)
my_button_day4.grid(row=3,column=4, sticky=W)
my_button_day5.grid(row=3,column=5, sticky=W)
my_button_day6.grid(row=3,column=6, sticky=W)
my_button_day7.grid(row=3,column=7, sticky=W)

                      




window.resizable(0, 0)
window.mainloop()
