"""
BMI Calculator - Windows Console edition
Author: Nishmithraj, KA, INDIA
version: 0.3
Date published: 22-07-2020
"""

import time
import os
import pyautogui


def bmi(name, height, weight):
    b = (weight / (height / 100) ** 2)
    w1 = int((18.6 * (height / 100) ** 2))
    w2 = int((24.9 * (height / 100) ** 2))
    print('-' * 100)
    print('Your BMI is,', b)
    if b < 18.5:
        print(name + ', you are Underweight')
        print('-' * 100)
        print("You should have the weight between", w1, "and", w2, "to have a normal BMI")
    elif 18.5 <= b < 25:
        print(name + ', you are Normal. Great!')
        print('-' * 100)
        print("You should have the weight between", w1, "and", w2, "to maintain this normal BMI")
    elif 25 <= b <= 29.9:
        print(name + ', you are Overweight!')
        print('-' * 100)
        print("You should have the weight between", w1, "and", w2, "to have a normal BMI")
    else:
        print(name + ', you are Obese!')
        print('-' * 100)
        print("You should have the weight between", w1, "and", w2, "to have a normal BMI")


def fun():
    a = input('\nPress Q to exit...\n')
    if a == 'Q':
        exit()


def normalBMI():
    print("As per W.H.O,\n  ")
    print("  BMI < 18.5          => Underweight")
    print("  18.5 < BMI < 24.9   => Normal")
    print("  25 < BMI < 29.9     => Overweight")
    print("  BMI > 30            => Obese\n")


if __name__ == '__main__':
    pyautogui.hotkey('win', 'up')
    time.sleep(0.5)
    print('*' * 100)
    print("Hello! Welcome to BMI calculator by NPR.\n[NOTE] : The results it provides is W.H.O. approved.\n")
    print('*' * 100)
    normalBMI()
    ppl = int(input('Number of people whom you want to calculate BMI for: '))
    for i in list(range(0, ppl)):
        print('*' * 100)
        bmi(name=input('Name: '), height=int(input('Height(in cms): ')), weight=int(input('Weight(in Kgs): ')))
        i += 1

    time.sleep(1)
    print('*' * 43, 'Thank you!!!', "*" * 43)
    print('')
    input('Press Enter..')
    os.system('cls')
    normalBMI()
    time.sleep(1)
    fun()
