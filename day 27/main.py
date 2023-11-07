import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label component
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 16, "bold"))
my_label.grid(column=0, row=0)

def button_clicked():
    my_label.config(text=input.get())
    

#Button Component
button = tkinter.Button(text="Button", command=button_clicked)
button.grid(column=1, row=1)

#New Button
new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry Component
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()