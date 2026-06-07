from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer
    reps = 0
    if timer:
        window.after_cancel(timer)
    canvas.itemconfig(canvas_timer, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(canvas_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        marks = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

check_marks = Label(text="",fg=GREEN,bg=YELLOW,font=("Arial", 40))
check_marks.grid(column=1, row=3)

start_button = Button(text="Start",highlightbackground=YELLOW,command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",highlightbackground=YELLOW,command=reset_timer)
reset_button.grid(column=2, row=2)

tom = PhotoImage(file="28_Pomodoro/tomato.png")
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightbackground=YELLOW)
canvas.create_image(101, 112, image=tom)
canvas_timer = canvas.create_text(101,130,text="00:00",fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()