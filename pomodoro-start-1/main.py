from tkinter import*
import math
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timmer  = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timmer)
    timer_label.config(text='Timer',fg=GREEN)
    canvas.itemconfig(time_txt,text='00:00')
    tik_label.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def timeer(count):
    global timmer
    min = math.floor(count/60)
    sec = math.ceil(count % 60)
    if sec < 10:
        sec = f"0{sec}"
    if min < 10:
        min = f"0{min}"
    canvas.itemconfig(time_txt, text=f"{min}:{sec}")
    if count > 0:
       timmer =  window.after(1000, timeer, count-1)
    else:
        start_timer()
        tick = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            tick += '✔'
        tik_label.config(text=tick)


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    SHORT_BREAK_sec = SHORT_BREAK_MIN * 60
    LONG_BREAK_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timeer(LONG_BREAK_sec)
        timer_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        timeer(SHORT_BREAK_sec)
        timer_label.config(text='Break', fg=PINK)
    else:
        timeer(work_sec)
        timer_label.config(text='Work', fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# timer Label
timer_label = Label(text='Timer', font=(
    FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)


# Background Picture
tomato_img = PhotoImage(file='pomodoro-start-1/tomato.png')
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
time_txt = canvas.create_text(100, 130, text='00:00', fill='white',
                              font=('Arial', 24, 'bold'))
canvas.grid(column=1, row=1)


# start Button
start_btn = Button(text='Start', command=start_timer)
start_btn.grid(column=0, row=2)

#  tik label
tik_label = Label(fg=GREEN, font=('Arial', 20), bg=YELLOW)
tik_label.grid(column=1, row=3)

# reset Button
reset_btn = Button(text='Reset', highlightthickness=0,command=reset_timer)
reset_btn.grid(column=2, row=2)


window.mainloop()
