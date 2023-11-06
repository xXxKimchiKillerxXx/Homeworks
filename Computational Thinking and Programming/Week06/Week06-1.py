import sqlite3
con = sqlite3.connect("C:/Users/jsbjs/Desktop/pytest/naverDB")
row = None
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS md202310631(id char(4), userName char(15), email char(15), birthyear int)")
cur.execute("SELECT * FROM md202310631")

from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("700x250")
window.title("GUI 데이터 입력")

head1 = ["사용자ID", "--------------------"]
head2 = ["사용자이름", "--------------------"]
head3 = ["이메일", "--------------------"]
head4 = ["출생연도", "--------------------"]

entry1 = Entry(window)
entry2 = Entry(window)
entry3 = Entry(window)
entry4 = Entry(window)
listbox1 = Listbox(window)
listbox2 = Listbox(window)
listbox3 = Listbox(window)
listbox4 = Listbox(window)

from re import *

def update():
    # Re-query the database to fetch the latest data
    cur.execute("SELECT * FROM md202310631")
    global rows
    rows = cur.fetchall()

def add():
    data1 = entry1.get()
    data2 = entry2.get()
    data3 = entry3.get()
    data4 = entry4.get()
    p = compile(r'[1-9]\d{3}')
    r = match(p, data4)

    if entry1.get() == '' or entry2.get() == '' or entry3.get() == '' or entry4.get() == '' or r == None:
        messagebox.showerror("오류", "데이터 입력 오류가 발생함")
    else:
        values = (data1, data2, data3, data4)
        sql = "INSERT INTO md202310631 (id, userName, email, birthyear) VALUES (?, ?, ?, ?)"
        cur.execute(sql, values)
        con.commit()

        head1.append(data1)
        head2.append(data2)
        head3.append(data3)
        head4.append(data4)

        reset()
        messagebox.showinfo("성공", "데이터 입력 성공")

def reset():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)

def refresh():
    reset()
    update()

    if rows == None:
        messagebox.showerror("오류", "데이터가 없습니다")
    else:
        for head in list(head1):
            listbox1.insert(END, head)
            head1.remove(head)
        for head in list(head2):
            listbox2.insert(END, head)
            head2.remove(head)
        for head in list(head3):
            listbox3.insert(END, head)
            head3.remove(head)
        for head in list(head4):
            listbox4.insert(END, head)
            head4.remove(head)

        for row in rows:
            listbox1.insert(END, row[0])
            listbox2.insert(END, row[1])
            listbox3.insert(END, row[2])
            listbox4.insert(END, row[3])
        print(rows)

btn_input = Button(window, text = "입력", command = add)
btn_view = Button(window, text = "조회", command = refresh)

btn_input.grid(row = 0, column = 4)
btn_view.grid(row = 0, column = 5)

entry1.grid(row = 0, column = 0)
entry2.grid(row = 0, column = 1)
entry3.grid(row = 0, column = 2)
entry4.grid(row = 0, column = 3)
listbox1.grid(row = 1, column = 0)
listbox2.grid(row = 1, column = 1)
listbox3.grid(row = 1, column = 2)
listbox4.grid(row = 1, column = 3)

window.mainloop()
con.close()