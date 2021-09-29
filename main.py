import winsound
from tkinter import Button, Label, Tk, DISABLED, NORMAL

turn = 1
x = []
o = []

def retry_game():
    global turn, x, o

    turn = 1
    x = []
    o = []

    turn_lbl.configure(text="X Turn!")

    p1["state"] = p2["state"] = p3["state"] = p4["state"] = p5["state"] = p6["state"] = p7["state"] = p8["state"] = p9["state"] = NORMAL

    p1.configure(text='   ')
    p2.configure(text='   ')
    p3.configure(text='   ')
    p4.configure(text='   ')
    p5.configure(text='   ')
    p6.configure(text='   ')
    p7.configure(text='   ')
    p8.configure(text='   ')
    p9.configure(text='   ')


def btn_press(arg):

    global turn, x, o
    winsound.Beep(400, 75)
    


    if turn % 2 == 1:
        turn_lbl.configure(text="O Turn!")
    else:
        turn_lbl.configure(text="X Turn!")

    if arg == 1:
        if turn % 2 == 1:
            p1.configure(text='X', fg='RED', font=("Comic Sans MS", 22, "bold"),  height=1, width=3)
        else:
            p1.configure(text='O', fg='BLUE', font=("Comic Sans MS", 22, "bold"),  height=1, width=3)
        p1["state"] = DISABLED

    if arg == 2:
        if turn % 2 == 1:
            p2.configure(text='X', fg='RED', font=("Comic Sans MS", 22, "bold"),  height=1, width=3)
        else:
            p2.configure(text='O', fg='BLUE', font=("Comic Sans MS", 22, "bold"),  height=1, width=3)
        p2["state"] = DISABLED

    if arg == 3:
        if turn % 2 == 1:
            p3.configure(text='X', fg='RED', font=("Comic Sans MS", 22, "bold"),  height=1, width=3)
        else:
            p3.configure(text='O', fg='BLUE', font=("Comic Sans MS", 22, "bold"),  height=1, width=3)
        p3["state"] = DISABLED

    if arg == 4:
        if turn % 2 == 1:
            p4.configure(text='X', fg='RED', font=("Comic Sans MS", 22, "bold"),  height=1, width=3)
        else:
            p4.configure(text='O', fg='BLUE', font=("Comic Sans MS", 22, "bold"),  height=1, width=3)
        p4["state"] = DISABLED

    if arg == 5:
        if turn % 2 == 1:
            p5.configure(text='X', fg='RED', font=("Comic Sans MS", 22, "bold"),  height=1, width=3)
        else:
            p5.configure(text='O', fg='BLUE', font=("Comic Sans MS", 22, "bold"),  height=1, width=3)
        p5["state"] = DISABLED

    if arg == 6:
        if turn % 2 == 1:
            p6.configure(text='X', fg='RED', font=("Comic Sans MS", 22, "bold"),  height=1, width=3)
        else:
            p6.configure(text='O', fg='BLUE', font=("Comic Sans MS", 22, "bold"),  height=1, width=3)
        p6["state"] = DISABLED

    if arg == 7:
        if turn % 2 == 1:
            p7.configure(text='X', fg='RED', font=("Comic Sans MS", 22, "bold"),  height=1, width=3)
        else:
            p7.configure(text='O', fg='BLUE', font=("Comic Sans MS", 22, "bold"),  height=1, width=3)
        p7["state"] = DISABLED

    if arg == 8:
        if turn % 2 == 1:
            p8.configure(text='X', fg='RED', font=("Comic Sans MS", 22, "bold"),  height=1, width=3)
        else:
            p8.configure(text='O', fg='BLUE', font=("Comic Sans MS", 22, "bold"),  height=1, width=3)
        p8["state"] = DISABLED

    if arg == 9:
        if turn % 2 == 1:
            p9.configure(text='X', fg='RED', font=("Comic Sans MS", 22, "bold"),  height=1, width=3)
        else:
            p9.configure(text='O', fg='BLUE', font=("Comic Sans MS", 22, "bold"),  height=1, width=3)
        p9["state"] = DISABLED

    if turn % 2 == 1:
        x.append(arg)
        x.sort()
        check1 = x
    else:
        o.append(arg)
        o.sort()
        check2 = o

    check1 = ''.join(map(str, x))
    check2 = ''.join(map(str, o))

    if ("123" in check1) or ("456" in check1) or ("789" in check1) or ("1" in check1 and "4" in check1 and "7" in check1) or ("2" in check1 and "5" in check1 and "8" in check1) or ("3" in check1 and "6" in check1 and "9" in check1) or ("1" in check1 and "5" in check1 and "9" in check1) or ("3" in check1 and "5" in check1 and "7" in check1):
        turn_lbl.configure(text="X WIN!")
        p1["state"] = p2["state"] = p3["state"] = p4["state"] = p5["state"] = p6["state"] = p7["state"] = p8["state"] = p9["state"] = DISABLED
        retry_btn["state"] = NORMAL
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS) 

    elif ("123" in check2) or ("456" in check2) or ("789" in check2) or ("1" in check2 and "4" in check2 and "7" in check2) or ("2" in check2 and "5" in check2 and "8" in check2) or ("3" in check2 and "6" in check2 and "9" in check2) or ("1" in check2 and "5" in check2 and "9" in check2) or ("3" in check2 and "5" in check2 and "7" in check2):
        turn_lbl.configure(text="O WIN!")
        p1["state"] = p2["state"] = p3["state"] = p4["state"] = p5["state"] = p6["state"] = p7["state"] = p8["state"] = p9["state"] = DISABLED
        retry_btn["state"] = NORMAL
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS) 

    elif turn == 9:
        turn_lbl.configure(text="DRAW!")
        retry_btn["state"] = NORMAL
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS) 

    turn = turn + 1


if __name__ == "__main__":

    board = Tk()
    board.title("Tic Tac Toe")
    board.geometry("198x260")
    board.minsize(198, 260)
    board.maxsize(198, 260)

    p1 = Button(board, text='   ',
                command=lambda: btn_press(1), height=4, width=8, relief="solid", borderwidth=3)
    p1.grid(row=0, column=0)

    p2 = Button(board, text='   ',
                command=lambda: btn_press(2), height=4, width=8, relief="solid", borderwidth=3)
    p2.grid(row=0, column=1)

    p3 = Button(board, text='   ',
                command=lambda: btn_press(3), height=4, width=8, relief="solid", borderwidth=3)
    p3.grid(row=0, column=2)

    p4 = Button(board, text='   ',
                command=lambda: btn_press(4), height=4, width=8, relief="solid", borderwidth=3)
    p4.grid(row=1, column=0)

    p5 = Button(board, text='   ',
                command=lambda: btn_press(5), height=4, width=8, relief="solid", borderwidth=3)
    p5.grid(row=1, column=1)

    p6 = Button(board, text='   ',
                command=lambda: btn_press(6), height=4, width=8, relief="solid", borderwidth=3)
    p6.grid(row=1, column=2)

    p7 = Button(board, text='   ',
                command=lambda: btn_press(7), height=4, width=8, relief="solid", borderwidth=3)
    p7.grid(row=2, column=0)

    p8 = Button(board, text='   ',
                command=lambda: btn_press(8), height=4, width=8, relief="solid", borderwidth=3)
    p8.grid(row=2, column=1)

    p9 = Button(board, text='   ',
                command=lambda: btn_press(9), height=4, width=8, relief="solid", borderwidth=3)
    p9.grid(row=2, column=2)

    turn_lbl = Label(board, text="X Turn!", font=("Comic Sans MS", 20, "bold"))
    turn_lbl.place(x=5, y=219)

    retry_btn = Button(board, text="Retry", command=retry_game, relief="solid", borderwidth=2, font=("Comic Sans MS", 9, "bold"), padx=4)
    retry_btn.place(x=140, y=227)
    retry_btn["state"] = DISABLED

    board.mainloop()