from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New text "
my_label.config(text="New text nnn")

def btn_clicked():

    my_label.config(text=entry.get())
    


entry = Entry(width=30)
entry.pack()

button = Button(text="Click me", command=btn_clicked)
button.pack()

window.mainloop()
