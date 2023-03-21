import tkinter as tk
import time
import os
from tkinter import *
from tkinter import messagebox

class TaskingBuddy(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("400x450")
        self.title("Tasking Buddy")
        self.font = "System"

        self.current_script_path = os.path.abspath(__file__)
        self.project_directory = os.path.dirname(self.current_script_path)
        self.work_gif_path = "Assets/work_gif.gif"
        self.break_gif_path = "Assets/work_gif.gif"
        self.gif_path = self.work_gif_path
        self.full_path = os.path.join(self.project_directory, self.gif_path)
        self.gif = tk.PhotoImage(file = self.full_path)

        self.curr_gif = self.gif
        self.work_time = 1 * 10
        self.break_time = 1 * 5
        self.remaining_time = self.work_time
        self.running = False
        self.timer_mode = "Work"

        self.init_buttons()

        

    def init_buttons(self):
        self.timer_label = tk.Label(self, text="Timer Not Started", font=(self.font, 24))
        self.timer_label.pack(pady=20)

        self.gif = tk.Label(self, image=self.curr_gif)
        self.gif.pack(pady=20)
        #self.animate_gif(0)

        self.start_button = tk.Button(self, text = 'Start', font=(self.font, 12), command = self.beginTimer)
        self.start_button.pack(side = "left", padx=40)

        self.reset_button = tk.Button(self, text = 'Reset', font=(self.font, 12), command = self.reset)
        self.reset_button.pack(side = "right", padx=40)

    def beginTimer(self):
        self.running = not self.running
        if not self.running: self.last_time = time.perf_counter()
        self.start_button.config(text="Pause" if self.running else "Start")
        if self.running:
            self.updateTimer()
            
    def updateTimer(self):
        mins, secs = divmod(self.remaining_time, 60)
        timer_text = '{mode} Time!\n'.format(mode = self.timer_mode) + '{:02d}:{:02d}'.format(mins, secs)
        
        if self.running:
            self.timer_label.config(text = timer_text)
            self.remaining_time -= 1
            if self.remaining_time < 0: 
                self.remaining_time = 0
                self.finishedTimer()
            self.after(1000, self.updateTimer)
    
    def finishedTimer(self):
        if self.timer_mode == "Work":
            self.timer_mode = "Break"
            self.remaining_time = self.break_time
        else:
            self.timer_mode = "Work"
            self.remaining_time = self.work_time
    
    def reset(self):
        self.running = False
        self.timer_mode = "Work"
        self.remaining_time = self.work_time
        self.start_button.config(text="Start")
        self.timer_label.config(text = "Timer Not Started")


if __name__ == "__main__":
    app = TaskingBuddy()
    app.mainloop()