from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- DATA ------------------------------- #
try:
    data = pd.read_csv("31_FlashCardApp/data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("31_FlashCardApp/data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}
current_card_index = 0

# ---------------------------- LEARNED ------------------------------- #
def learned():
    global current_card, to_learn
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("31_FlashCardApp/data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- NEXT CARD ------------------------------- #
def next_card():
    global current_card, flip_timer, to_learn
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(language_title, text="French", fill="black")
    canvas.itemconfig(word_title, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    global current_card
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(language_title, text="English", fill="white")
    canvas.itemconfig(word_title, text=current_card["English"], fill="white")

# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="31_FlashCardApp/images/card_front.png")
card_back_img = PhotoImage(file="31_FlashCardApp/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

flip_timer = window.after(3000, func=flip_card)

language_title = canvas.create_text(400, 150, text="Language", font=("Courier", 40, "italic"))
word_title = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

right_button_img = PhotoImage(file="31_FlashCardApp/images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0,command=next_card)
right_button.grid(row=1, column=1)
left_button_img = PhotoImage(file="31_FlashCardApp/images/wrong.png")
left_button = Button(image=left_button_img, highlightthickness=0,command=learned)
left_button.grid(row=1, column=0)

next_card()

window.mainloop()