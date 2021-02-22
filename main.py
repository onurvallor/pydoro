import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedStyle

window_width = 500
window_height = 700

window_width_calc = window_width / 3

class HelloWorld(ttk.Frame):
    def __init__(self, parent):
        super(HelloWorld, self).__init__(parent)

        timer_var = tk.IntVar()
        timer_var.set(30)

        #H = hour, M = Minute, S = Second
        hour = IntVar()
        minute = IntVar()
        second = IntVar()

        hour.set("00")
        minute.set("30")
        second.set("00")

        def start_timer():
            pass

        def set_timer():
            #self.label['text'] = str(int(self.time_slider.get())) + ":00"
            print(hour_entry.get())
            hour.set(hour_entry.get())
            print(hour.get())
            minute.set(minute_entry.get())
            second.set(second_entry.get())
            pass

        
        #self.label = Label(self, textvariable=m, width=3, font=("Arial Bold", 50))
        #self.label.pack(padx=25,pady=10)
  

        hour_entry = Entry(self, width=3, font=("Arial", 16, ""), textvariable=hour)
        hour_entry.grid(column=0, row=0, padx=(5,5))
        minute_entry = Entry(self, width=3, font=("Arial", 16, ""), textvariable=minute)
        minute_entry.grid(column=1, row=0, padx=(5,5))
        second_entry = Entry(self, width=3, font=("Arial", 16, ""), textvariable=second)
        second_entry.grid(column=2, row=0, padx=(5,5))

        self.set_btn = Button(self, text='set', width = 5, command=set_timer).grid(row=1, column=0, columnspan=3, sticky=E+W+N+S)
        self.start_btn = Button(self, text='start', width = 5).grid(row=2, column=0, columnspan=3, sticky=E+W+N+S)
        

        # self.start_btn.pack(padx=2, pady=2)

        #self.time_slider = Scale(self, from_=0, to=60, variable=timer_var,orient=HORIZONTAL)
        #self.time_slider.pack()

        # self.time_slider_btn = Button(self, text='Set', command=set_timer)
        # self.time_slider_btn.pack()

        


        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pomodoro Timer")
    #root.geometry(str(window_width) + "x" + str(window_height))

    style = ThemedStyle(root)
    style.set_theme("yaru")


    main = HelloWorld(root)

    # main.grid(sticky="nsew")
    # root.grid_rowconfigure(0, weight=1)
    # root.grid_columnconfigure(0, weight=1)

    main.pack(fill="both", expand=True)
    root.mainloop()