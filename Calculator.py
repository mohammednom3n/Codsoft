from tkinter import *
from tkinter.messagebox import *


font = ('arial baltic', 20, 'bold')


# functions

def buttonclick(event):
    b = event.widget
    text = b['text']

    if text == '=':
        try:
            expression = textField.get()
            answer = eval(expression)
            textField.delete(0, END)
            textField.insert(0,  answer)
        except ZeroDivisionError:
            showerror("You can't divide the number by 0.")
        except Exception:
            showerror('Oops! The expression is invalid.')
        return

    textField.insert(END, text)


def all_clear():
    textField.delete(0, END)


def clear():
    expression = textField.get()
    expression = expression[0:len(expression) - 1]
    textField.delete(0, END)
    textField.insert(0,  expression)


# creating a window

window = Tk()
window.title("Calculator")
window.geometry('450x600')


# heading Label
heading = Label(window, text="Calculator", font=font)
heading.pack(side=TOP, pady=7)

# textfield

textField = Entry(window, font=font, justify=CENTER)
textField.pack(side=TOP, pady=20, fill=X, padx=20)


# buttons
frame = Frame(window)
frame.pack(side=TOP)


# adding buttons now

buttonValue = 1
for i in range(3):
    for j in range(3):
        button = Button(frame, text=buttonValue, font=font, width=5, height=2, relief='sunken', activebackground='blue', activeforeground='white')
        button.grid(row=i, column=j, padx=3, pady=3)
        buttonValue += 1
        button.bind(' <Button-1>', buttonclick)


dot_button = Button(frame, text=".", font=font, width=5, height=2, relief='sunken')
dot_button.grid(row=3, column=0, padx=3, pady=3)

zero_button = Button(frame, text="0", font=font, width=5, height=2, relief='sunken')
zero_button.grid(row=3, column=1, padx=3, pady=3)

equal_button = Button(frame, text="=", font=font, width=5, height=2, relief='sunken')
equal_button.grid(row=3, column=2, padx=3, pady=3)

plus_Button = Button(frame, text="+", font=font, width=5, height=2, relief='sunken')
plus_Button.grid(row=0, column=3, padx=3, pady=3)

minus_Button = Button(frame, text="-", font=font, width=5, height=2, relief='sunken')
minus_Button.grid(row=1, column=3, padx=3, pady=3)

multiply_Button = Button(frame, text="*", font=font, width=5, height=2, relief='sunken')
multiply_Button.grid(row=2, column=3, padx=3, pady=3)

divide_Button = Button(frame, text="/", font=font, width=5, height=2, relief='sunken')
divide_Button.grid(row=3, column=3, padx=3, pady=3)

clear_Button = Button(frame, text="C", font=font, width = 11, height=2, relief='sunken', command=clear)
clear_Button.grid(row= 4, column=0, columnspan=2, padx=3, pady=3)

all_clear_Button = Button(frame, text="AC", font=font, width = 11, height=2, relief='sunken', command=all_clear)
all_clear_Button.grid(row=4, column=2, columnspan=2, padx=3, pady=3)


dot_button.bind(' <Button-1>', buttonclick)
zero_button.bind(' <Button-1>', buttonclick)
equal_button.bind(' <Button-1>', buttonclick)
plus_Button.bind(' <Button-1>', buttonclick)
minus_Button.bind(' <Button-1>', buttonclick)
multiply_Button.bind(' <Button-1>', buttonclick)
divide_Button.bind('<Button-1>', buttonclick)


window.mainloop()

