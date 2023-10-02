from tkinter import *
from tkinter import messagebox

window = Tk()

photoList = ['dog.gif', 'cat.gif', 'rabbit.gif']

def myFunc():
    selected_value = chk.get()
    if selected_value ==  1:
        photo = PhotoImage(file = photoList[0])
    elif selected_value ==  2:
        photo = PhotoImage(file = photoList[1])
    elif selected_value ==  3:
        photo = PhotoImage(file = photoList[2])
    else:
        messagebox.showinfo("오류", "항목을 선택하세요.")

    pLabel.configure(image = photo)
    pLabel.image = photo

label = Label(text = "좋아하는 동물 투표", font = ("궁서체", 20), fg = 'blue')

chk = IntVar()
rb1 = Radiobutton(window, text = "강아지", variable = chk, value = 1)
rb2 = Radiobutton(window, text = "고양이", variable = chk, value = 2)
rb3 = Radiobutton(window, text = "토끼", variable = chk, value = 3)

button = Button(window, text = "사진 보기", command = myFunc)

pLabel = Label(window)
pLabel.image = None

label.pack()
rb1.pack()
rb2.pack()
rb3.pack()
button.pack()
pLabel.pack()

window.mainloop()