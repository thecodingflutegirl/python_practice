from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = ''.join(password_list)
    # print(f"Your password is: {password}")

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if website and email and password:
        is_ok = messagebox.askokcancel(
            title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open('data.txt', 'a') as data:
                data.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                email_input.delete(0, END)
                password_input.delete(0, END)
    else:
        messagebox.showinfo(
            title='WARNING', message="Don't leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)  # bg='white')

canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

password_input = Entry(width=20)
password_input.grid(column=1, row=3)

make_password = Button(text='Make Password', command=generate_password)
make_password.grid(column=2, row=3)

add_btn = Button(text="Add", width=35, command=save_data)
add_btn.grid(column=1, row=4, columnspan=2)


window.mainloop()
# I would like to edit this for some of the colors but its not a high priority
