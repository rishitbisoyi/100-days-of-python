from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(window, text="Hello, Tkinter!")
my_label.pack()
# my_label["text"]="New Text"
# my_label.config(bg="red",fg="white")

# Button
def button_clicked():
#     print("Button clicked!")
    my_label.config(text="Button got clicked")

button = Button(text="Click me",command=button_clicked)
button.pack()

# Entry
input = Entry(width=30)
input.pack()
def input_entered():
    t=input.get()
    my_label.config(text=t)
button1=Button(text="Show input",command=input_entered)
button1.pack()


window.mainloop()

# def add(*args):
#     result = 0
#     for n in args:
#         result += n
#     return result
    
# print(add(1, 2, 3, 4, 5))