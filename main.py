from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}


def next_card():
    global random_word, timer
    window.after_cancel(timer)
    random_word = random.choice(data)
    french_word = random_word["French"]
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    timer=window.after(3000, func=flip_card)


def flip_card():
    english_word = random_word["English"]
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_word, fill="white")


# Create window
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer=window.after(3000, func=flip_card)


# Create canvas and initialize text
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# Buttons
unknown_button_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_button_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)
known_button_image = PhotoImage(file="images/right.png")
known_button = Button(image=known_button_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

df = pandas.read_csv("data/french_words.csv")
data = df.to_dict(orient="records")

next_card()

window.mainloop()
