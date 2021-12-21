from tkinter import *
import pandas 
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
## ---------------------- GET DICT DATA ------------ ###
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    current_card['French']
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_background, image=front_card_image)
    flip_timer = window.after(3000, func=flip_card)

# ----------------- FLIP CARD --------------- ##
def flip_card():
    global current_card
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=back_card_image)
    

## ------------------ KNOWN CARD ---------##
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


## ------------------------ UI SETUP ---------------- ###
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
right = PhotoImage(file='images/right.png')
wrong = PhotoImage(file='images/wrong.png')
front_card_image = PhotoImage(file='images/card_front.png')
back_card_image = PhotoImage(file='images/card_back.png')

canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
card_background = canvas.create_image(400, 263, image=front_card_image)
card_title = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'), fill='black')
card_word = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'), fill='black')
canvas.grid(column=0, row=0, columnspan=2)


right_btn = Button(image=right, highlightthickness=0, bd=0, highlightbackground=BACKGROUND_COLOR, command=is_known)
right_btn.grid(column=0, row=1)
wrong_btn = Button(image=wrong, highlightthickness=0, bd=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_btn.grid(column=1, row=1)


next_card()


window.mainloop()

