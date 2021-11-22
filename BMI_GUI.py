"""
BMI Calculator - GUI edition
Author: Nishmithraj, KA, INDIA
version: 0.1
Date published: 21-02-2021
"""
from tkinter import *
import threading
import time

main_root = Tk()
main_root.title("BMI")
data = LabelFrame(main_root, text=None)
data.pack(fill=BOTH)
display = LabelFrame(main_root, text=None)
display.pack(fill=BOTH)
dis2 = LabelFrame(display, text=None)
dis2.grid(row=1, column=0, columnspan=2, sticky=N + E + S + W)
# dis2.pack(fill=BOTH)

# Functions
def start():
    while True:
        try:
            if weight.get() and height.get():
                w = int(weight.get())
                h = int(height.get())
                b = round((w / (h / 100) ** 2), 2)
                w1 = int((18.6 * (h / 100) ** 2))
                w2 = int((24.9 * (h / 100) ** 2))
                if b < 18.5:
                    bmi.config(text=f"{b}", font=("Helvetica", 20, 'bold'), fg="red")
                    l_wt_lmt.config(text=f"{w1}", fg="green", font=10)
                    h_wt_lmt.config(text=f"{w2}", fg="red", font=10)
                    status.config(text="You are Underweight", font=("Helvetica", 12, 'bold'), fg="red")
                elif 18.5 <= b < 25:
                    bmi.config(text=f"{b}", font=("Helvetica", 20, 'bold'), fg="green")
                    l_wt_lmt.config(text=f"{w1}", fg="green", font=10)
                    h_wt_lmt.config(text=f"{w2}", fg="red", font=10)
                    status.config(text="You are Normal. Great!", font=("Helvetica", 12, 'bold'), fg="green")
                elif 25 <= b <= 29.9:
                    bmi.config(text=f"{b}", font=("Helvetica", 20, 'bold'), fg="orange")
                    l_wt_lmt.config(text=f"{w1}", fg="green", font=10)
                    h_wt_lmt.config(text=f"{w2}", fg="red", font=10)
                    status.config(text="You are Overweight!", font=("Helvetica", 12, 'bold'), fg="orange")
                else:
                    bmi.config(text=f"{b}", font=("Helvetica", 20, 'bold'), fg="red")
                    l_wt_lmt.config(text=f"{w1}", fg="green", font=10)
                    h_wt_lmt.config(text=f"{w2}", fg="red", font=10)
                    status.config(text="You are Obese!", font=("Helvetica", 12, 'bold'), fg="red")
        except:
            bmi.config(text="ERROR!", font=("Helvetica", 17, 'bold'), fg="red")
            l_wt_lmt.config(text="!!", fg="green", font=10)
            h_wt_lmt.config(text="!!", fg="red", font=10)
            status.config(text="Please enter appropriate number", font=("Helvetica", 11, 'bold'), fg="red")


# Functions end

# Gui elements
# name_lbl = Label(data, text="Your name :")
# name = Entry(data)
weight_lbl = Label(data, text="Weight in kgs:", font=("Modern", 15, 'bold'))
weight = Entry(data, bd=3, relief="groove")
height_lbl = Label(data, text="Height in cms:", font=("Modern", 15, 'bold'))
height = Entry(data, bd=3, relief="groove")

bmi_lbl = Label(display, text="Your BMI is :", font=("Helvetica", 12, 'bold'))
bmi = Label(display, text=" -- ")

status = Label(dis2, text=" -- ", anchor=CENTER)
l_wt_lmt = Label(dis2, text=" -- ")
optimum_lbl = Label(dis2, text=" < Optimum weight for you < ", font=("Helvetica", 10))
h_wt_lmt = Label(dis2, text=" -- ")

############################################################
# name_lbl.grid(row=0, column=0, sticky=E + W)
# name.grid(row=0, column=1, sticky=E + W)
weight_lbl.grid(row=2, column=0, sticky=E + W, ipady=5)
weight.grid(row=2, column=1, sticky=E + W, ipady=5)
height_lbl.grid(row=1, column=0, sticky=E + W, ipady=5)
height.grid(row=1, column=1, sticky=E + W, ipady=5)

bmi_lbl.grid(row=0, column=0, sticky=E + W)
bmi.grid(row=0, column=1, sticky=E + W)


status.grid(row=0, column=0, columnspan=3, sticky=E + W)
l_wt_lmt.grid(row=1, column=0, sticky=E + W)
optimum_lbl.grid(row=1, column=1, sticky=E + W)
h_wt_lmt.grid(row=1, column=2, sticky=E + W)

# Gui elements end

t1 = threading.Thread(target=start)
t1.daemon = True  # To terminate the thread when program ends
t1.start()

main_root.mainloop()
