import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def mile_to_km():
    result = int(input.get()) * 1.609344
    label_3.config(text=result)

#Label
label_1 = tk.Label(text="is equal to")
label_1.grid(column=0, row=1)

#Create input
input = tk.Entry()
input.grid(column=1, row=0)

#Label 2 
label_2 = tk.Label(text="Miles")
label_2.grid(column=2, row=0)

#Label result
label_3 = tk.Label(text="0")
label_3.grid(column=1, row=1)

#Label 4
label_4 = tk.Label(text="Km")
label_4.grid(column=2, row=1)

#Button
button = tk.Button(text="Calculate", command=mile_to_km)
button.grid(column=1, row=2)

window.mainloop()