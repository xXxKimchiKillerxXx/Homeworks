from tkinter import *

fnameList = []
num = 0

def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    update_label()

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    update_label()

def update_label():
    label.configure(text = "jeju" + str(num + 1) + ".png")

window = Tk()

btnPrev = Button(window, text = "<< 이전", command = clickPrev)
btnNext = Button(window, text = "다음 >>", command = clickNext)

label = Label(window, font = ("궁서체", 20), fg = "blue")
btnPrev.pack(side = LEFT); label.pack(side = LEFT); btnNext.pack(side = LEFT)


label.configure(text = "jeju1.png")
window.mainloop()