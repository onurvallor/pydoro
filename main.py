import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedStyle


class HelloWorld(ttk.Frame):
    def __init__(self, parent):
        super(HelloWorld, self).__init__(parent)

        timer_var = tk.IntVar()
        timer_var.set(30)

        def start_timer():
            pass

        def set_timer():
            self.label['text'] = str(int(self.time_slider.get())) + ":00"

        
        self.label = Label(self, text="30:00", font=("Arial Bold", 50))
        self.label.pack(padx=25,pady=10)

        self.start_btn = Button(self, text='start')
        self.start_btn.pack(padx=2, pady=2)

        self.time_slider = Scale(self, from_=0, to=60, variable=timer_var,orient=HORIZONTAL)
        self.time_slider.pack()
        

        self.time_slider_btn = Button(self, text='Set', command=set_timer)
        self.time_slider_btn.pack()

        


        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pomodoro Timer")
    root.geometry("500x700")

    style = ThemedStyle(root)
    style.set_theme("yaru")


    main = HelloWorld(root)
    main.pack(fill="both", expand=True)
    root.mainloop()