from tkinter import *

root = Tk()
root.geometry('500x500')

# Write user input to csv file
def write_csv():
    print(entry.get())
    
# Create entry boxes

title = Entry(root, width=40,)
title.place(x=200, y=100)

author = Entry(root, width=40,)
author.place(x=200, y=150)

pageCount = Entry(root, width=40,)
pageCount.place(x=200, y=200)

dateFinished = Entry(root, width=40,)
dateFinished.place(x=200, y=250)

# Create submit button

submitBtn = Button(root, text='Submit', command=write_csv)
submitBtn.place(x=100, y=150)

root.mainloop()