from tkinter import *

#Simple Calculator
#Declare expresson as global
 expression = ""

def press(num):
    global expression

    expression = expression+str(num)

#Function to evaluate the final expression
def equal_press():
    #Try and except statement is used for handling the error like zero division
    try:
        global expression

        #eval is used for evaluate the expression
        total = str(eval(expression))

        expression = ""

#Function to clear the entry box
def clear():
    global expression
    expression = ""

