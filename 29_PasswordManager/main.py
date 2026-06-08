from tkinter import *
from tkinter import messagebox
import pyperclip
import PasswordGenerator

WHITE="#F5F5F5"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_setup():
    dialog = Toplevel(window)
    dialog.title("Password Generator")
    dialog.config(padx=20, pady=20, bg=WHITE)

    alpha_label = Label(dialog, text="Number of alphabets:", bg=WHITE)
    alpha_label.grid(column=0, row=0)
    alpha_entry = Entry(dialog, bg=WHITE)
    alpha_entry.insert(0, "2")
    alpha_entry.grid(column=1, row=0)

    upper_label = Label(dialog, text="Number of uppercase letters:", bg=WHITE)
    upper_label.grid(column=0, row=1)
    upper_entry = Entry(dialog, bg=WHITE)
    upper_entry.insert(0, "2")
    upper_entry.grid(column=1, row=1)

    digit_label = Label(dialog, text="Number of digits:", bg=WHITE)
    digit_label.grid(column=0, row=2)
    digit_entry = Entry(dialog, bg=WHITE)
    digit_entry.insert(0, "2")
    digit_entry.grid(column=1, row=2)

    char_label = Label(dialog, text="Number of special characters:", bg=WHITE)
    char_label.grid(column=0, row=3)
    char_entry = Entry(dialog, bg=WHITE)
    char_entry.insert(0, "2")
    char_entry.grid(column=1, row=3)

    def generate():
        alpha = int(alpha_entry.get())
        upper = int(upper_entry.get())
        digit = int(digit_entry.get())
        char = int(char_entry.get())

        password = PasswordGenerator.generate_password(alpha, upper, digit, char)

        password_entry.delete(0, END)
        password_entry.insert(0, password)

        pyperclip.copy(password)

        is_ok = messagebox.askokcancel(
        title="Password Generated",
        message="Password has been copied to clipboard.\n\nPress OK to continue or Cancel to modify the password settings.")
        if is_ok:
            dialog.destroy()

    generate_button = Button(dialog,text="Generate Password",bg=WHITE,command=generate)
    generate_button.grid(column=0, row=4, columnspan=2)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    
    is_empty=website=="" or email=="" or password==""
    if is_empty:
        messagebox.showerror(title="Error",message="Please don't leave any fields empty!")
        return

    is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

    if is_ok:
        with open("29_PasswordManager/data.txt","a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0,END)
        password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=35,pady=35,bg=WHITE)

logo_img=PhotoImage(file="29_PasswordManager/logo.png")

canvas=Canvas(width=200,height=200,bg=WHITE,highlightthickness=0)
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0,columnspan=2,sticky="EW")

website_label=Label(text="Website:",bg=WHITE)
website_label.grid(column=0,row=1)
email_label=Label(text="Email/Username:",bg=WHITE)
email_label.grid(column=0,row=2)
password_label=Label(text="Password:",bg=WHITE)
password_label.grid(column=0,row=3)

website_entry=Entry(width=35,bg=WHITE)
website_entry.focus()
website_entry.grid(column=1,row=1,columnspan=2,sticky="EW")
email_entry=Entry(width=35,bg=WHITE)
email_entry.insert(0,"example@example.com")
email_entry.grid(column=1,row=2,columnspan=2,sticky="EW")
password_entry=Entry(width=21,bg=WHITE)
password_entry.grid(column=1,row=3,sticky="EW")

add_button=Button(text="Add",width=37,bg=WHITE,command=save_password)
add_button.grid(column=1,row=4,columnspan=2)
generate_button=Button(text="Generate Password",bg=WHITE,highlightthickness=0,command=password_setup)
generate_button.grid(column=2,row=3)

window.mainloop()
