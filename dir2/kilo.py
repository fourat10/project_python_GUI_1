from tkinter import *

window = Tk()
window.title("MILES to KILOMETRE")
window.minsize(width=290, height=150)
window.config(padx=50,pady=50)

entry = Entry(width=10)
entry.grid(column=1,row=0)


label_miles=Label(text="MILES")
label_miles.grid(column=2,row=0)

label_equal=Label(text=" is equal to ")
label_equal.grid(column=0,row=1)

label_miles=Label(text=" 0 ")
label_miles.grid(column=1,row=1)

label_KM=Label(text=" KM ")
label_KM.grid(column=2,row=1)


def btn_clicked():
    miles = float(entry.get())
    km=miles*1.609
    label_miles.config(text=f"{km}")


button = Button(text=" Calculate", command=btn_clicked)
button.grid(column=1,row=2)

window.mainloop()