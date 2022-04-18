from tkinter import *
import time
import threading
import random


class TypeSpeedGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Typing Speed Test")
        self.window.geometry("800x600")

        self.text = open("text.txt").read().split("\n")

        self.frame = Frame(self.window, width=100, highlightbackground="black", highlightthickness=1)

        self.sample_label = Label(self.frame, text=random.choice(self.text), font=("Arial", 16))
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

        self.input_entry = Entry(self.frame, width=40, font=("Arial", 22))
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyRelease>", self.start)

        self.speed_label = Label(self.frame, text="Speed: \n0.00 WPM", font=("Arial", 16))
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.reset_button = Button(self.frame, text="Reset", command=self.reset, font=("Helvetica", 24))
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        self.milisec_counter = 0
        self.time_is_running = False

        self.window.mainloop()

    def reset(self):
        self.sample_label.config(text=random.choice(self.text))
        self.milisec_counter = 0
        self.time_is_running = False
        self.speed_label.config(text="Speed: \n0.00 WPM")
        self.input_entry.delete(0, END)

    def start(self, event):
        if not self.time_is_running:
            if not event.keycode in [16, 17, 18]:
                self.time_is_running = True
                t1 = threading.Thread(target=self.time_thread)
                t1.start()
        if not self.sample_label.cget("text").startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")
        if self.input_entry.get() == self.sample_label.cget("text"):
            self.time_is_running = False
            self.input_entry.config(fg="green")

    def time_thread(self):
        while self.time_is_running:
            time.sleep(0.1)
            self.milisec_counter += 1
            wps = len(self.input_entry.get().split(" ")) / self.milisec_counter
            wpm = wps * 60
            self.speed_label.config(text=f"Speed: {wpm:.2f} WPM.")


type_speed_gui = TypeSpeedGUI()