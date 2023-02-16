from tkinter import *
from tkinter import font

root = Tk()
root.geometry('300x280')

# Create entry boxes

title = Entry(root, width=40,)
title.place(x=25, y=30)

author = Entry(root, width=40,)
author.place(x=25, y=80)

pageCount = Entry(root, width=40,)
pageCount.place(x=25, y=130)

dateFinished = Entry(root, width=40,)
dateFinished.place(x=25, y=180)

# Write user input to csv file
def write_csv():
    print(title.get())
    print(author.get())
    print(pageCount.get())
    print(dateFinished.get())
    title.delete(0, END)
    author.delete(0, END)
    pageCount.delete(0, END)
    dateFinished.delete(0, END)
    create_labels()
    
def temp_title(e):
    title.delete(0, END)
    
def temp_author(e):
    author.delete(0, END)

def temp_page_count(e):
    pageCount.delete(0, END)
    
def temp_date_finished(e):
    dateFinished.delete(0, END)

# Create entry box labels
def create_labels():
    title.insert(1, 'Title')
    title.bind('<FocusIn>', temp_title)

    author.insert(1, 'Author')
    author.bind('<FocusIn>', temp_author)

    pageCount.insert(1, 'Page Count')
    pageCount.bind('<FocusIn>', temp_page_count)

    dateFinished.insert(1, 'Date Finished')
    dateFinished.bind('<FocusIn>', temp_date_finished)
    
create_labels()

# Create submit button
btnFont = font.Font(family='Helvetica', size=11)
submitBtn = Button(root, text='Submit',width=12, height=2, font=btnFont, command=write_csv)
submitBtn.place(x=85, y=215)

root.mainloop()