from tkinter import *
import random

root = Tk()
root.config(bg='#515b66') #515b66
root.geometry("540x300")
root.resizable(width=False, height=False)

choices = ['ROCK', 'PAPER', 'SCISSORS']


lab1 = Label(root, text='You:', bg='#515b66', fg="#699cfa",font= ('Helvetica', 16, 'bold')).grid(row=1, column=0, columnspan=2, pady=30)
var = StringVar()
user_lab = Label(root, textvariable=var, bg='#515b66', fg='#c7ccd1',font= ('Helvetica', 16, 'bold'))
user_lab.grid(row=2, column=0, columnspan=2, sticky=S)

lab2 = Label(root, text='Bot:', bg='#515b66', fg="#fa7369",font= ('Helvetica', 16, 'bold')).grid(row=1, column=1, columnspan=2, pady=30)
var2 = StringVar()
bot_lab = Label(root, textvariable=var2, bg='#515b66', fg='#c7ccd1',font= ('Helvetica', 16, 'bold'))
bot_lab.grid(row=2, column=1, columnspan=2, sticky=S)

str_var3 = StringVar(root, value='Status: ')
status_lab = Label(root, textvariable=str_var3, bg='#515b66', font= ('Helvetica', 16, 'bold'))
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

user_score_val = 0
bot_score_val = 0
def but_func(user_choice):
    global user_score_val, bot_score_val
    var.set(user_choice)
    bot_choice = random.choice(choices)
    var2.set(bot_choice)
    has_won = check(user_choice, bot_choice)
    if has_won:
        status_lab.config(fg="#699cfa")
        str_var3.set("Status: YOU WON!!")
        user_score_val += 1
        user_score_var.set(f'Your \nScore: {user_score_val}')
    elif has_won == False:
        status_lab.config(fg="#fa7369")
        str_var3.set("Status: BOT WON :(")
        bot_score_val += 1
        bot_score_var.set(f'Bot\'s \nScore: {bot_score_val}')
    else:
        status_lab.config(fg="#c7ccd1")
        str_var3.set("Status: TIE ¯\_(ツ)_/¯")


rock = Button(root, text='ROCK', bg='#9fa8b3', font= ('Helvetica', 16, 'bold'), command=lambda: but_func(choices[0])).grid(row=0, column=0, ipadx=40, ipady=20)
paper = Button(root, text='PAPER', bg='#9fa8b3',font= ('Helvetica', 16, 'bold'), command=lambda: but_func(choices[1])).grid(row=0, column=1, ipadx=40, ipady=20)
scissors = Button(root, text='SCISSORS', bg='#9fa8b3', font=('Helvetica', 16, 'bold'), command=lambda: but_func(choices[2])).grid(row=0, column=2, ipadx=40, ipady=20)

user_score_var = StringVar(root, value='Your \nScore: ')
user_score = Label(root, textvariable=user_score_var, bg='#515b66', fg="#699cfa", font= ('Helvetica', 16, 'bold'))
user_score.grid(row=3, column=0, padx=20)

bot_score_var = StringVar(root, value='Bot\'s \nScore: ')
bot_score = Label(root, textvariable=bot_score_var, bg='#515b66', fg="#fa7369", font= ('Helvetica', 16, 'bold'))
bot_score.grid(row=3, column=2)

root.mainloop()
