from tkinter import *

tasks = []

def add():
    task = str(entry.get())
    if task:
        tasks.append(task)
        update()
        entry.delete(0, END)

def remove():
    number = listbox.curselection()
    if number:
        index = number[0]
        del tasks[index]
        update()

def update():
    listbox.delete(0, END)
    for task in tasks:
        listbox.insert(END, task)

window = Tk()

label = Label(window, text = 'Add a Task:')
entry = Entry(window)

add_button = Button(window, text = "Add Task", command = add)

listbox = Listbox(window)

remove_button = Button(window, text = "Delete Task", command = remove)

label.pack()
entry.pack()
add_button.pack()
listbox.pack()
remove_button.pack()

window.mainloop()