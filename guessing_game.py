#! /usr/bin/python3

import random

def guess_loop():
    number_to_guess = random.randint(1 ,100)
    print("I have in mind a number in between 1 and 100, can you find it?")
    while True:
        try:
            guess = int(input())

            if guess > number_to_guess:
                print("The number to guess is lower")
            elif guess < number_to_guess:
                print("The number to guess is higher")
            else:
                nom = input('Donner votre nom: ')
                print("You just found the number, it was indeed", guess,"Bravo",nom)
                return

        except ValueError as err:
            print("Invalid input, please enter an integer")

guess_loop()
