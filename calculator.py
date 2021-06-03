import random
from random import choice
import time
from time import sleep
import sys

num1 = int(input("Enter the first number: "))
op = input("Enter operator: ")
num2 = int(input("Enter the second number: "))

try:
    if op == "+":
        time.sleep(0.5)
        print("The result is: ", num1+num2)
    elif op == "-":
        time.sleep(0.5)
        print("The result is: ", num1-num2)
    elif op == "x":
        time.sleep(0.5)
        print("The result is: ", num1*num2)
    elif op == ":": 
        time.sleep(0.5)
        print("The result is: ", num1/num2)
    else:
        time.sleep(0.5)
        print('This is not a valid operation! Sorry :(')
except:
    time.sleep(30)
    pass