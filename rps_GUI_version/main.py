from tkinter import *
import random

FONT_TXT = ('Helvetica', 16, 'bold')
# COLOUR CONSTANTS
GREY = '#515b66'
GREY_LGHT = '#c7ccd1'
GREY_BTN = '#9fa8b3'
BLUE = '#699cfa'
RED = '#fa7369'


root = Tk()
root.config(bg=GREY) #515b66
root.geometry("580x300")
root.resizable(width=False, height=False)

# The three valid choices
choices = ['ROCK', 'PAPER', 'SCISSORS']


lab1 = Label(root, text='You:', bg = GREY, fg=BLUE,font=FONT_TXT).grid(row=1, column=0, columnspan=2, pady=30)
var = StringVar()
user_lab = Label(root, textvariable=var, bg=GREY, fg=GREY_LGHT,font= FONT_TXT)
user_lab.grid(row=2, column=0, columnspan=2, sticky=S)

lab2 = Label(root, text='Bot:', bg=GREY, fg=RED,font= FONT_TXT).grid(row=1, column=1, columnspan=2, pady=30)
var2 = StringVar()
bot_lab = Label(root, textvariable=var2, bg=GREY, fg=GREY_LGHT,font= FONT_TXT)
bot_lab.grid(row=2, column=1, columnspan=2, sticky=S)

str_var3 = StringVar(root, value='Status: ')
status_lab = Label(root, textvariable=str_var3, bg=GREY, font= FONT_TXT)
status_lab.grid(row=3, column=0, columnspan=3, pady=30)

# function to check for win
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
        status_lab.config(fg=BLUE)
        str_var3.set("Status: YOU WON!!")
        user_score_val += 1
        user_score_var.set(f'Your \nScore: {user_score_val}')
    elif has_won == False:
        status_lab.config(fg=RED)
        str_var3.set("Status: BOT WON :(")
        bot_score_val += 1
        bot_score_var.set(f'Bot\'s \nScore: {bot_score_val}')
    else:
        status_lab.config(fg=GREY_LGHT)
        str_var3.set("Status: TIE ¯\_(ツ)_/¯")


rock = Button(root, text='ROCK', bg=GREY_BTN, font= FONT_TXT, command=lambda: but_func(choices[0])).grid(row=0, column=0, ipadx=40, ipady=20)
paper = Button(root, text='PAPER', bg=GREY_BTN,font= FONT_TXT, command=lambda: but_func(choices[1])).grid(row=0, column=1, ipadx=40, ipady=20)
scissors = Button(root, text='SCISSORS', bg=GREY_BTN, font=FONT_TXT, command=lambda: but_func(choices[2])).grid(row=0, column=2, ipadx=40, ipady=20)

user_score_var = StringVar(root, value='Your \nScore: ')
user_score = Label(root, textvariable=user_score_var, bg=GREY, fg=BLUE, font= FONT_TXT)
user_score.grid(row=3, column=0, padx=20)

bot_score_var = StringVar(root, value='Bot\'s \nScore: ')
bot_score = Label(root, textvariable=bot_score_var, bg=GREY, fg=RED, font= FONT_TXT)
bot_score.grid(row=3, column=2)

root.mainloop()
