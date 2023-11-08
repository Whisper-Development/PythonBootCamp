from tkinter import *
import pandas as pd
import random

#Constants
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv('day 31\data\words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('day 31\data\words_in_french.csv')
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    french_word = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    canvas.itemconfig(card_background, image=flash_card)
    flip_timer = window.after(4000, func=flip_card)

    
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)

def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pd.DataFrame(to_learn)  
    data.to_csv("day 31/data/words_to_learn.csv", index=False) 
    next_card()


#User Interface
window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(4000, func=flip_card)

#Flashcard
canvas = Canvas(width=800, height=526)
flash_card = PhotoImage(file="day 31\images\card_front.png")
card_back = PhotoImage(file="day 31\images\card_back.png")
card_background = canvas.create_image(400, 263, image=flash_card)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

#Buttons
cross_image = PhotoImage(file="day 31\images\wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="day 31\images\check.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)




next_card()

window.mainloop()

