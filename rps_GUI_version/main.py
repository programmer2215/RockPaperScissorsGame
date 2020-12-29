from tkinter import *
import random

root = Tk()
root.config(bg="#23C4ED")
root.geometry("540x300")

choices = ['ROCK', 'PAPER', 'SCISSORS']


lab1 = Label(root, text='You:', bg="#23C4ED", font= ('Helvetica', 16, 'bold')).grid(row=1, column=0, columnspan=2, pady=30)
var = StringVar()
user_lab = Label(root, textvariable=var, bg="#23C4ED", font= ('Helvetica', 16, 'bold'))
user_lab.grid(row=2, column=0, columnspan=2, sticky=S)

lab2 = Label(root, text='Bot:', bg="#23C4ED", font= ('Helvetica', 16, 'bold')).grid(row=1, column=1, columnspan=2, pady=30)
var2 = StringVar()
bot_lab = Label(root, textvariable=var2, bg="#23C4ED", font= ('Helvetica', 16, 'bold'))
bot_lab.grid(row=2, column=1, columnspan=2, sticky=S)

str_var3 = StringVar(root, value='Status: ')
status_lab = Label(root, textvariable=str_var3, bg="#23C4ED", font= ('Helvetica', 16, 'bold'))
status_lab.grid(row=3, column=0, columnspan=3, pady=30)
def check(user, bot):
    if user == choices[0] and bot == choices[2]:
        return True
    elif user == choices[1] and bot == choices[0]:
        return True
    elif user == choices[2] and bot == choices[1]:
        return True
    elif user == bot:
        return None
    return False

def but_func(user_choice):
    var.set(user_choice)
    bot_choice = random.choice(choices)
    var2.set(bot_choice)
    has_won = check(user_choice, bot_choice)
    if has_won:
        str_var3.set("Status: YOU WON")
    elif has_won == False:
        str_var3.set("Status: BOT WON")
    else:
        str_var3.set("Status: TIE")


rock = Button(root, text='ROCK', font= ('Helvetica', 16, 'bold'), command=lambda: but_func(choices[0])).grid(row=0, column=0, ipadx=40, ipady=20)
paper = Button(root, text='PAPER', font= ('Helvetica', 16, 'bold'), command=lambda: but_func(choices[1])).grid(row=0, column=1, ipadx=40, ipady=20)
scissors = Button(root, text='SCISSORS', font=('Helvetica', 16, 'bold'), command=lambda: but_func(choices[2])).grid(row=0, column=2, ipadx=40, ipady=20)

root.mainloop()
