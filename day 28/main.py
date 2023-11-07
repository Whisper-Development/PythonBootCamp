import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 25
LONG_BREAK_MIN = 20
reps = 0
timers = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timers)
    timer.config(text="Timer", bg=YELLOW)
    background.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
    background.config(bg=YELLOW)
    window.config(bg=YELLOW)
    tick.config(bg=YELLOW)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_br_sec = SHORT_BREAK_MIN*60
    long_br_sec = LONG_BREAK_MIN*60
    
    if reps % 8 == 0:
        count_down(long_br_sec)
        timer.config(text="Break", bg=GREEN)
        background.config(bg=GREEN)
        window.config(bg=GREEN)
        tick.config(bg=GREEN)
    elif reps % 2 == 0:
        count_down(short_br_sec)
        timer.config(text="Break", bg=PINK)
        background.config(bg=PINK)
        window.config(bg=PINK)
        tick.config(bg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work", bg=RED)
        background.config(bg=RED)
        window.config(bg=RED)
        tick.config(bg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    background.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timers
        timers = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✓"
        tick.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

background = tk.Canvas(width=220, height=230, bg=YELLOW, highlightthickness=0)
tomato_pic =tk.PhotoImage(file="day 28/tomato.png")
background.create_image(110, 118, image=tomato_pic)
timer_text = background.create_text(110, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
background.grid(column=1, row=1)


#Label timer
timer = tk.Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)

#Button start
start = tk.Button(text="Start", command=start_timer)
start.grid(column=0, row=2)

#Button reset
reset = tk.Button(text="Reset", command=reset_timer)
reset.grid(column=2, row=2)

#Label tick
tick = tk.Label(fg=GREEN, font=18, bg=YELLOW)
tick.grid(column=1, row=2)

window.mainloop()