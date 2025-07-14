from tkinter import *
window = Tk()

lbl1 = Label(window, text="이것은 레이블입니다.")
lbl2 = Label(window, text="문자를",font=("궁서체",20,"bold"))
lbl3 = Label(window, text="출력하는",bg="yellow")
lbl4 = Label(window,text="위젯입니다.",width=20,height=3,bg="skyblue",anchor="se")

lbl1.pack()
lbl2.pack()
lbl3.pack()
lbl4.pack()

window.mainloop()