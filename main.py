import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedStyle
from tkinter import messagebox

import time
from datetime import date
import pandas as pd


# df = pd.read_csv("examples.csv",)

class PyDoro(ttk.Frame):
    def __init__(self, parent):
        super(PyDoro, self).__init__(parent)

        timer_var = tk.IntVar()
        timer_var.set(30)

        #H = hour, M = Minute, S = Second
        hour = IntVar()
        minute = IntVar()
        second = IntVar()

        hour.set("00")
        minute.set("30")
        second.set("00")

        # https://www.geeksforgeeks.org/create-countdown-timer-using-python-tkinter/
        def start_timer():
            try:
                temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
                print(temp)
            except:
                print("Enter in correct values.")

            while temp > -1:
                m, s = divmod(temp, 60)

                h = 0
                if m > 60:
                    h, m = divmod(m, 60)

                hour.set("{0:2d}".format(h))
                minute.set("{0:2d}".format(m))
                second.set("{0:2d}".format(s))

                root.update()
                time.sleep(1)

                if temp == 0:
                    root.bell()
                    messagebox.showinfo("PyDoro", "Time is up!")
                
                temp -= 1

        # def test():
        #     d1 = date.today().strftime("%m-%d-%Y")
        #     year = d1 - date.timedelta(days=1*365)
        #     print(d1)
        #     print(year)
  
        hour_entry = Entry(self, width=3, font=("Arial", 16, ""), textvariable=hour)
        hour_entry.grid(column=0, row=0, padx=(5,5))
        minute_entry = Entry(self, width=3, font=("Arial", 16, ""), textvariable=minute)
        minute_entry.grid(column=1, row=0, padx=(5,5))
        second_entry = Entry(self, width=3, font=("Arial", 16, ""), textvariable=second)
        second_entry.grid(column=2, row=0, padx=(5,5))

        self.start_btn = Button(self, text='start', width = 5, command=start_timer).grid(row=2, column=0, columnspan=3, sticky=E+W+N+S)

        # self.test_btn = Button(self, text='test', width = 5, command=test).grid(row=3, column=0, columnspan=3, sticky=E+W+N+S)
        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pomodoro Timer")
    #root.geometry(str(window_width) + "x" + str(window_height))

    style = ThemedStyle(root)
    style.set_theme("yaru")


    main = PyDoro(root)

    main.pack(fill="both", expand=True)
    root.mainloop()