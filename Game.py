from tkinter import *
from tkinter import messagebox
import random as playerfind


def button(window):
    b = Button(window, padx=1, bg="#856ff8", width=3, text="   ", font=('times new roman', 60, 'bold'))
    return b

def change_a():
    global turn
    for i in ['O', 'X']:
        if not (i == turn):
            turn = i
            break


def reset():
    global turn
    for i in range(3):
        for j in range(3):
            box_played[i][j]["text"] = " "
            box_played[i][j]["state"] = NORMAL
    turn = playerfind.choice(['O', 'X'])


def check():
    for i in range(3):
        if box_played[i][0]["text"] == box_played[i][1]["text"] == box_played[i][2]["text"] == turn:
            messagebox.showinfo("Congrats!!", "'" + turn + "' has won")
            reset()
        elif box_played[0][i]["text"] == box_played[1][i]["text"] == box_played[2][i]["text"] == turn:
            messagebox.showinfo("Congrats!!", "'" + turn + "' has won")
            reset()
    if box_played[0][0]["text"] == box_played[1][1]["text"] == box_played[2][2]["text"] == turn:
        messagebox.showinfo("Congrats!!", "'" + turn + "' has won")
        reset()
    elif box_played[0][2]["text"] == box_played[1][1]["text"] == box_played[2][0]["text"] == turn:
        messagebox.showinfo("Congrats!!", "'" + turn + "' has won")
        reset()
    elif box_played[0][0]["state"] == box_played[0][1]["state"] == box_played[0][2]["state"] == box_played[1][0]["state"] == box_played[1][1]["state"] == box_played[1][2][
        "state"] == box_played[2][0]["state"] == box_played[2][1]["state"] == box_played[2][2]["state"] == DISABLED:
        messagebox.showinfo("Tied!!", "The match ended in a draw")
        reset()


def click(row, col):
    box_played[row][col].config(text=turn, state=DISABLED, disabledforeground=colour[turn])
    check()
    change_a()
    label.config(text=turn + "'s Chance")


parent = Tk()
parent.title("Tic Tac Toe With GUI")
turn = playerfind.choice(['O', 'X'])
colour = {'O': "deep sky blue", 'X': "Red"}
box_played = [[], [], []]
for i in range(3):
    for j in range(3):
        box_played[i].append(button(parent))
        box_played[i][j].config(command=lambda row=i, col=j: click(row, col))
        box_played[i][j].grid(row=i, column=j)
label = Label(text=turn + "'s Chance", font=('sans', 25, 'bold'))
label.grid(row=3, column=0, columnspan=3)
parent.mainloop()
