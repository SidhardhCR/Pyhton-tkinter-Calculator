from tkinter import *

# Globally declare the expressoin variable
expression = ""


# Function to update expression in the entry box
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

#Function to evaluate the final expression
def equal_press():

    try:
        global expression
        #eval is used for evaluate the expression
        total=str(eval(expression))
        equation.set(total)
        expression = ""

    except:

        equation.set("error")
        expression = ""

#Function to clear the entry box
def clear():
    global expression
    expression = ""


#Create GUI window

window=Tk()
#Set background colour

window.configure(background="gray")
#Set title

window.title('Simple Calculator')
window.geometry('370x250')
#StringVar is the variable class

equation = StringVar()

#Create the entry box

input_field =Entry(window, textvariable=equation)
input_field.grid(columnspan=8, ipadx=120)

window.mainloop()