# --------- Dev: Ali Jafarbeglou - Password Manager GUI - tkinter ---------
# Password Manager GUI App - will generate strong password and save data into txt

from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

BG_COLOR = "white"
FG_COLOR = "black"
WHITE = "white"
FONT = "calibri"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    # from random we imported random randint, shuffle, etc .. that allows us to code simpler like below:
    # also, instead of making 3 variables. I did it in only one variable!!!
    [password_list.append(choice(letters)) for _ in range(randint(8, 10))]
    [password_list.append(choice(symbols)) for _ in range(randint(2, 4))]
    [password_list.append(choice(numbers)) for _ in range(randint(2, 4))]

    # This will shuffle the List
    shuffle(password_list)
    password = "".join(password_list)
    password_ent.insert(0, password)

    # to save in clipboard (copy method) easy to paste!
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web = website_ent.get()
    email = email_ent.get()
    password = password_ent.get()

    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Oops, You shouldn't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {email} \nPassword: {password}\nIS it ok to save?")

        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{web} | {email} | {password}\n")
                website_ent.delete(0, END)
                password_ent.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
# window.minsize(height=400, width=400)
# window.maxsize(width=400 ,height=400)
window.config(pady=70, padx=70, bg=BG_COLOR)

# -- CANVAS - Logo
canvas = Canvas(width=200, height=200, bg=BG_COLOR, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)


# ------- Labels::::
website_lbl = Label(text="Website:", fg=FG_COLOR, bg=BG_COLOR, font=(FONT, 16))
website_lbl.grid(row=1, column=0)

email_lbl = Label(text="Email/Username:", fg=FG_COLOR, bg=BG_COLOR, font=(FONT, 16))
email_lbl.grid(row=2, column=0)

password_lbl = Label(text="Password:", fg=FG_COLOR, bg=BG_COLOR, font=(FONT, 16))
password_lbl.grid(row=3, column=0)

# ------- Entry::::
website_ent = Entry(width=35, highlightthickness=0)
website_ent.grid(row=1, column=1, columnspan=2)
website_ent.focus()  # cursor automatically here at lunch

email_ent = Entry(width=35, highlightthickness=0)
email_ent.grid(row=2, column=1, columnspan=2)
email_ent.insert(0, "youremail@email.com")
# 0, put text at the very email ---  END, will put at the end.

password_ent = Entry(width=19, highlightthickness=0)
password_ent.grid(row=3, column=1)

# ------- Buttons::::
password_btn = Button(text="Generate Password", highlightbackground=BG_COLOR, command=generate_password)
password_btn.config(width=12)
password_btn.grid(row=3, column=2)

add_btn = Button(text="Add", highlightbackground=BG_COLOR, command=save)
add_btn.config(width=33)
add_btn.grid(row=4, column=1, columnspan=2)

# < _______________________________END_____________________________ >
window.mainloop()