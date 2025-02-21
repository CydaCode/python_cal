#CALCULATOR APP

#IMPORT LIBRARY
from tkinter import *

#FUNCTION THAT EXECUTES THE BUTTON CLICK
def on_button_clicked(value):
    #Get the current state of the entry
    current = entry_var.get()

    #Update the currrent state
    entry_var.set(current + value)

    #Logic
    if value == "C" or value == "c":
        entry_var.set("")

    elif value == "⌫":
        entry_var.set(current[:-1])

    elif value == "=":
        try:
            result = eval(current)
            entry_var.set(result)

        except Exception as e:
            print("Syntax Error")

    else:
        entry_var.set(current + str(value))


#INITIALIZING THE WINDOW
root=Tk()
root.title("The optimum calculator")
root.geometry("450x400")
root.configure(bg="gray")
root.resizable(False, False)

font_style=("Arial", 14, "bold")

entry_var = StringVar()

cal_entry = Entry(root, textvariable=entry_var, font=("Arial", 28, "bold"), bg="#442510", fg='#eab676', justify="right", bd=5)
cal_entry.grid(row=0, column=0, padx=8, pady=8, sticky="w", columnspan=4)

#buttons for (C, del, (, ), )
cancel_btn = Button(root, text="C", font=font_style, width=5, height=1, command=lambda: on_button_clicked("C"))
cancel_btn.grid(row=2, column=0, ipady=4, ipadx=4)

del_btn = Button(root, text="⌫", font=font_style, width=5, height=1, command=lambda: on_button_clicked("⌫"))
del_btn.grid(row=2, column=1,  ipady=4, ipadx=4)

bracket_open = Button(root, text="(", font=font_style, width=5, height=1, command=lambda: on_button_clicked("("))
bracket_open.grid(row=2, column=2, ipady=4, ipadx=4)

bracket_close = Button(root, text=")", font=font_style, width=5, height=1, command=lambda: on_button_clicked(")"))
bracket_close.grid(row=2, column=3, ipady=4, ipadx=4)

#buttons for (7, 8, 9, /, )
nine_btn = Button(root, text="9", font=font_style, width=5, height=1, command=lambda: on_button_clicked("9"))
nine_btn.grid(row=3, column=0, ipady=4, ipadx=4, pady=7 )

eight_btn = Button(root, text="8", font=font_style, width=5, height=1, command=lambda: on_button_clicked("8"))
eight_btn.grid(row=3, column=1,  ipady=4, ipadx=4, pady=7)

seven_btn = Button(root, text="7", font=font_style, width=5, height=1, command=lambda: on_button_clicked("7"))
seven_btn.grid(row=3, column=2, ipady=4, ipadx=4, pady=7)

division = Button(root, text="/", font=font_style, width=5, height=1, command=lambda: on_button_clicked("/"))
division.grid(row=3, column=3, ipady=4, ipadx=4, pady=7)


#buttons for (4, 5, 6, +, )
six_btn = Button(root, text="6", font=font_style, width=5, height=1, command=lambda: on_button_clicked("6"))
six_btn.grid(row=4, column=0, ipady=4, ipadx=4, pady=7 )

five_btn = Button(root, text="5", font=font_style, width=5, height=1, command=lambda: on_button_clicked("5"))
five_btn.grid(row=4, column=1,  ipady=4, ipadx=4, pady=7)

four_btn = Button(root, text="4", font=font_style, width=5, height=1, command=lambda: on_button_clicked("4"))
four_btn.grid(row=4, column=2, ipady=4, ipadx=4, pady=7)

addition = Button(root, text="+", font=font_style, width=5, height=1, command=lambda: on_button_clicked("+"))
addition.grid(row=4, column=3, ipady=4, ipadx=4, pady=7)

#buttons for (1, 2, 3, (-), )
three_btn = Button(root, text="3", font=font_style, width=5, height=1, command=lambda: on_button_clicked("3"))
three_btn.grid(row=5, column=0, ipady=4, ipadx=4, pady=7 )

two_btn = Button(root, text="2", font=font_style, width=5, height=1, command=lambda: on_button_clicked("2"))
two_btn.grid(row=5, column=1,  ipady=4, ipadx=4, pady=7)

one_btn = Button(root, text="1", font=font_style, width=5, height=1, command=lambda: on_button_clicked("1"))
one_btn.grid(row=5, column=2, ipady=4, ipadx=4, pady=7)

subtraction = Button(root, text="-", font=font_style, width=5, height=1, command=lambda: on_button_clicked("-"))
subtraction.grid(row=5, column=3, ipady=4, ipadx=4, pady=7)

#buttons for (0, ., =, (*), )
zero_btn = Button(root, text="0", font=font_style, width=5, height=1, command=lambda: on_button_clicked("0"))
zero_btn.grid(row=6, column=0, ipady=4, ipadx=4, pady=7 )

amp_btn = Button(root, text=".", font=font_style, width=5, height=1, command=lambda: on_button_clicked("."))
amp_btn.grid(row=6, column=1,  ipady=4, ipadx=4, pady=7)

equal_btn = Button(root, text="=", font=font_style, width=5, height=1, command=lambda: on_button_clicked("="))
equal_btn.grid(row=6, column=2, ipady=4, ipadx=4, pady=7)

multiplication = Button(root, text="*", font=font_style, width=5, height=1, command=lambda: on_button_clicked("*"))
multiplication.grid(row=6, column=3, ipady=4, ipadx=4, pady=7)




root.mainloop()
