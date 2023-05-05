#######################################################################################################
# Assignment        : Guess the Number Game  (Automation Included)                                    #
# Group Members     : Srishti, Kumar Satyajit, Vinay Sharma                                           #
# Submission Date   : 05-May-2023                                                                     #
# DSBA02                                                                                              #
#######################################################################################################

'''
This code runs in Manual mode or Auto mode. Please follow onscreen instruction.
This will create scoreboard.txt file, so you should have permissions to create the file in the current
working directory
'''

import random
import time
from datetime import datetime

#Function to generate the fun message
def gen_msg():
    message = ['Come on you can do it!', 'Alas! This is not correct', 'Do you need coffee?',
               'O Boy, Come on, you are very close', 'Don''t Lose hope, you can try more', 'Chat GPT can''t beat me','Let me know if you are sleepy!']
    idx = random.randint(0, len(message)-1)
    adv_msg = message[idx]
    return adv_msg

def score_board(attempts,usr):
    now = datetime.now()
    current_time = now.strftime('%d-%m-%y %H:%M:%S')
    file1 = open('scoreboard.txt', 'a')
    file1.writelines(f"{current_time} :          {usr}                : {attempts}\n")

#Function to print the score board after each win!
def print_score():
    file12 = open('scoreboard.txt', 'r')
    content = file12.read()
    print("+------------------------------------------------------------+")
    print("|                   HALL OF FAME                             |")
    print("|------------------------------------------------------------|")
    print("|Date Time        :            USER               : Attempts |")
    print("+------------------------------------------------------------+")
    print(content)

#If User wants to play again or not, this function will return the Flag accordingly
def play_again():
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != 'y':
        Flag = False
    else:
        Flag = True
    return Flag

#Function to generate the guessing number
def guess_the_number():
    secret_number = random.randint(1, 20)
    attempts = 6

    print("Welcome to Guess the Number Game!")
    user = input("Enter your name :")
    print("I have chosen a number between 1 and 20.")
    print("You have 6 attempts to guess the number.")
    auto_mode = input("Do you want to play It in auto mode?[y/n] :")

    while attempts > 0 :
        print("\nAttempts left:", attempts)
        if auto_mode.lower() == 'y':
            guess = random.randint(1, 20)
            guess_mode = "Auto"
            user = "Computer"
            print("Computer's guess :", guess)
        else:
            guess = int(input("Enter your number :"))
            guess_mode = "Your"


        if guess < secret_number:
            print(f"The secret number is higher than the {guess_mode} guess.")
            print(gen_msg())
        elif guess > secret_number:
            print(f"The secret number is lower than the {guess_mode} guess.")
            print(gen_msg())
        else:
            print(f"Congratulations! {guess_mode} guessed number is correct!")
            score_board(7-attempts,user)
            time.sleep(1)
            print_score()
            break



        attempts -= 1
        # This is to ensure that the game exits once all attempts are exhausted and prints relevant message
        if attempts == 0:
            print("\nGame over! The computer ran out of attempts.")
            print("The secret number was:", secret_number)
            break

        time.sleep(1)

Flag = True

#This is the main loop where the game starts according to the Flag
while Flag:
    guess_the_number()
    Flag = play_again()
