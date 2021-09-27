from tkinter import *

# Globally declare the expressoin variable
expression = ""


# Function to update expression in the entry box
def press(num):
    global expression
    expression = expression + str(num)

#Function to evaluate the final expression
def equal_press():

    try:
        global expression
        #eval is used for evaluate the expression
        total=str(eval(expression))


        expression = ""

    except:

        expression = ""

#Function to clear the entry box
def clear():
    global expression
    expression = ""



window=Tk()


window.mainloop()