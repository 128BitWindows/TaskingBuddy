import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox
top = tk.Tk()

top.geometry("640x480")
top.title("Tasking Buddy")


top.timer_label = tk.Label(top, text="15:00", font=("Helvetica", 24))
top.timer_label.pack(pady=20)

def beginTimer():
    end_time = time.time() + 15 * 60
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        mins, secs = divmod(remaining_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        top.timer_label.config(text = timer)
        top.update()
        time.sleep(1)


start_button = Button(top, text = 'Start', command = beginTimer)


start_button.pack()
top.mainloop()