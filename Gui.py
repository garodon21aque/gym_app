from tkinter import *
from tkinter import Button
from PIL import ImageTk, Image
import sqlite3

# main page def and config
window = Tk()
window.title("Gym app")
window.configure(background="white")
window.geometry("1980x1040")


# Main bg Image from main library


# def section
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


def submit1():
    # creating a database for the app
    conn = sqlite3.connect('training_info.db')

    # create cursor
    c1 = conn.cursor()

    # create table
    c1.execute("INSERT INTO training VALUES (:training_name, :laps_amount, :training_amount)",
               {
                   'training_name': training_name.get(),
                   'laps_amount': laps_amount.get(),
                   'training_amount': training_amount.get()
               }
    )

    # commit connection
    conn.commit()

    # close conn
    conn.close()

    # clear text boxes
    training_amount.delete(0, END)
    laps_amount.delete(0, END)
    training_name.delete(0, END)

def query():
    # creating a database for the app
    conn = sqlite3.connect('training_info.db')

    # create cursor
    c1 = conn.cursor()

    # create query
    c1.execute("SELECT *, oid FROM training")
    records = c1.fetchall()
    print(records)
    #loop thru query
    print_records = ' '
    for record in records():
        print_records += str(record) + "\n"

    query_label = Label(window, text=print_records)
    query_label.grid(row=12, column=9, sticky=W)


    # commit connection
    conn.commit()

    # close conn
    conn.close()


# Lists
days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]
# inside funcions
clicked = StringVar()
clicked.set(days[0])
# main window text
Label(window, text="What day is the excercise?", bg="black", fg="white", font="none 12 bold").grid(row=1, column=0,
                                                                                                   sticky=W)

my_button_day1 = Button(window, text="Monday", bg="black", fg="white", padx=30, command=mb_day1)
my_button_day2 = Button(window, text="Tuesday", bg="black", fg="white", padx=30, command=mb_day2)
my_button_day3 = Button(window, text="Wednesday", bg="black", fg="white", padx=30, command=mb_day3)
my_button_day4 = Button(window, text="Thursday", bg="black", fg="white", padx=30, command=mb_day4)
my_button_day5 = Button(window, text="Friday", bg="black", fg="white", padx=30, command=mb_day5)
my_button_day6 = Button(window, text="Saturday", bg="black", fg="white", padx=30, command=mb_day6)
my_button_day7 = Button(window, text="Sunday", bg="black", fg="white", padx=30, command=mb_day7)

drop_down = OptionMenu(window, clicked, *days)

# refference for positions with .grid

my_button_day1.grid(row=3, column=1, sticky=W)
my_button_day2.grid(row=3, column=2, sticky=W)
my_button_day3.grid(row=3, column=3, sticky=W)
my_button_day4.grid(row=3, column=4, sticky=W)
my_button_day5.grid(row=3, column=5, sticky=W)
my_button_day6.grid(row=3, column=6, sticky=W)
my_button_day7.grid(row=3, column=7, sticky=W)
drop_down.grid(row=6, column=7, sticky=W)

button_quit = Button(window, text="Exit app", command=window.quit)
button_quit.grid(row=4, column=3, sticky=W)

# creating a database for the app
conn = sqlite3.connect('training_info.db')

# create cursor
c1 = conn.cursor()

# create table
'''' c1.execute("""CREATE TABLE training (
        training_name text,
        laps_amount integer,
        training_amount integer
)
""")
'''

# commit connection
conn.commit()

# close conn
conn.close()
# entry fields for exercises
training_name = Entry(window, width=30)
laps_amount = Entry(window, width=30)
training_amount = Entry(window, width=30)
# grids for exercises
training_name.grid(row=7, column=9, sticky=W)
laps_amount.grid(row=8, column=9, sticky=W)
training_amount.grid(row=9, column=9, sticky=W)
# label for entry
training_name_label = Label(window, text="Training Name")
laps_amount_label = Label(window, text="Laps amount")
training_amount_label = Label(window, text="Training amount")

# label for entry positions
training_name_label.grid(row=7, column=8, sticky=W)
laps_amount_label.grid(row=8, column=8, sticky=W)
training_amount_label.grid(row=9, column=8, sticky=W)

# submit button for datab
submit_btn = Button(window, text="Add the exercise", command=submit1)
submit_btn.grid(row=10, column=9, sticky=W)
#query button
query_button = Button(window, text="Query button", command=query)
query_button.grid(row=11, column=9, sticky=W)

window.mainloop()
