
from constants import *
from tkinter import Button, Canvas, Label, PhotoImage, Tk
import math

# Repetitions
reps = 0
timer = None


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00 : 00')
    title_label.config(text='Timer')
    check_marks.config(text="")

# Countdown


def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min} : {count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += '✓'
        check_marks.config(text=marks)


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text='Break', fg=PINK)
    else:
        countdown(work_sec)
        title_label.config(text='Work', fg=GREEN)


# UI Setup
window = Tk()
window.title('Pomodoro Timer Tkinter')
window.config(padx=100, pady=50, bg='white')


title_label = Label(text='Timer', fg=GREEN, font=(
    FONT_NAME, 60, 'normal'), bg='white')
title_label.grid(column=1, row=0)

canvas = Canvas(width=500, height=500, bg='white', highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(240, 250, image=image)

timer_text = canvas.create_text(
    250, 300, text='00 : 00', fill='white', font=(FONT_NAME, 35, 'bold'))

canvas.grid(column=1, row=1)

start_button = Button(command=start_timer, text='Start',
                      highlightthickness=0, width=19, font=('Roboto', 19))
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', highlightthickness=0,
                      width=19, font=('Roboto', 19), command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text="", fg=GREEN, bg='white', font=('Roboto', 60))
check_marks.grid(column=1, row=2)

window.mainloop()
