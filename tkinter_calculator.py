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
    equation.set("")

#Create GUI window

window=Tk()
#Set background colour

window.configure(background="light gray")
#Set title

window.title('Simple Calculator')
window.geometry('370x220')
#StringVar is the variable class

equation = StringVar()

#Create the entry box

input_field =Entry(window, textvariable=equation)
input_field.grid(columnspan=8, ipadx=120)

#Create Buttons

button7 = Button(window, text='7', fg='black', bg='white', command=lambda: press(7), height=2, width=7,)
button7.grid(row=1, column=0)
button8 = Button(window, text='8', fg='black', bg='white', command=lambda: press(8), height=2, width=7)
button8.grid(row=1, column=1)
button9 = Button(window, text='9', fg='black', bg='white', command=lambda: press(9), height=2, width=7)
button9.grid(row=1, column=2)
buttondiv = Button(window, text='/', fg='black', bg='white', command=lambda: press("/"), height=2, width=7)
buttondiv.grid(row=1, column=3)

button4 = Button(window, text='4', fg='black', bg='white', command=lambda: press(4), height=2, width=7,)
button4.grid(row=2, column=0)
button5 = Button(window, text='5', fg='black', bg='white', command=lambda: press(5), height=2, width=7)
button5.grid(row=2, column=1)
button6 = Button(window, text='6', fg='black', bg='white', command=lambda: press(6), height=2, width=7)
button6.grid(row=2, column=2)
buttonmul = Button(window, text='x', fg='black', bg='white', command=lambda: press("*"), height=2, width=7)
buttonmul.grid(row=2, column=3)

button1 = Button(window, text='1', fg='black', bg='white', command=lambda: press(1), height=2, width=7,)
button1.grid(row=3, column=0)
button2 = Button(window, text='2', fg='black', bg='white', command=lambda: press(2), height=2, width=7)
button2.grid(row=3, column=1)
button3 = Button(window, text='3', fg='black', bg='white', command=lambda: press(3), height=2, width=7)
button3.grid(row=3, column=2)
buttonmin = Button(window, text='-', fg='black', bg='white', command=lambda: press("-"), height=2, width=7)
buttonmin.grid(row=3, column=3)

buttondot = Button(window, text='.', fg='black', bg='white', command=lambda: press("+"), height=2, width=7,)
buttondot.grid(row=4, column=0)
buttonzero = Button(window, text='0', fg='black', bg='white', command=lambda: press(0), height=2, width=7)
buttonzero.grid(row=4, column=1)
buttonplus = Button(window, text='+', fg='black', bg='white', command=lambda: press("+"), height=2, width=7)
buttonplus.grid(row=4, column=2)
buttonequal = Button(window, text='=', fg='black', bg='white', command=lambda: equal_press(), height=2, width=7)
buttonequal.grid(row=4, column=3)
buttonclear = Button(window, text='Clear', fg='black', bg='white', command=lambda: clear(), height=2, width=7)
buttonclear.grid(row=4, column=4)

# Start
window.mainloop()