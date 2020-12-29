
# Rock Paper Scissors

import random
from colored import stylize, fg

choices = {1: "ROCK", 2: "PAPER", 3: "SCISSORS"}

def _help():
    print(stylize("""
* ROCK = 1
* PAPER = 2
* SCISSORS = 3
* to view this again type \"help\"
* type \"end\" to quit

""", fg("#ff9d00")))

def check(user, bot):
    if user == "ROCK" and bot == "SCISSORS":
        return True
    elif user == "PAPER" and bot == "ROCK":
        return True
    elif user == "SCISSORS" and bot == "PAPER":
        return True
    elif user == bot:
        return None
    return False

_help()
while True:
    choice = input(stylize("Enter your choice: ", fg('#00fbff')))
    if choice.lower() == "end":
        print(stylize("\nGAME OVER\n", fg('#FF6500')))
        break
    elif choice.lower() == "help":
        _help()
        continue

    try:
        bot_val = random.choice(list(choices.values()))
        user_val = choices[int(choice)]
        match = check(user_val, bot_val)
        print(stylize(f'\nyou chose "{user_val}" and the bot chose "{bot_val}"', fg('#00fbff')))
        if match == True:
            print(stylize("\nCONGRATULATIONS!!!  YOU WON\n", fg('#00ff08')))
        elif match == False:
            print(stylize("\nOOPS!!! YOU LOST TO THE BOT :(\n", fg('#fc5151')))
    except:
        print(stylize("Enter a valid  input", fg('#fc5151')))