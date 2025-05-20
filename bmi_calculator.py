from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=300,height=400)

label = Label(text="Enter your weight (kg)")
label.config(fg="black")
label.config(padx=60,pady=60)
label.pack()

label_2 = Label(text="Enter your height (cm)")
label_2.config(fg="black")
label_2.config(padx=80,pady=80)
label_2.pack()

entry = Entry(width=20)
entry.place(x=90,y=90)

entry_2 = Entry(width=20)
entry_2.place(x=90,y=250)


result_label = Label(text="", fg="blue")
result_label.pack( pady=10)

def button_clicked():

    try:
        weight = float(entry.get())
        height = float(entry_2.get()) / 100
        bmi = weight / (height**2)

        if bmi < 18.5:
            result = "Underweight"
        elif 18.5 <= bmi <= 24.9:
            result = "Normal weight"
        elif 25.0 <= bmi <= 29.9:
            result = "Overweight"
        else:
            result = "Obese"
        result_label.config(text=result)


    except ValueError:
        result_label.config(text="Please enter a valid number")

button = Button(text="Calculate",command=button_clicked)
button.config(padx=20,pady=10)
button.pack()


window.mainloop()