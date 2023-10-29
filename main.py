import tkinter

window = tkinter.Tk()
window.minsize(width=200, height=150)
window.title("Miles to Km Convertor")
window.config(padx=30, pady=30)


def calculate():
    miles = float(input.get())
    km = round(miles * 1.6)
    print(km)
    result.config(text=f'{km}')
    return km


input = tkinter.Entry(width=12)
input.focus()
input.grid(column=1, row=0)

miles_label = tkinter.Label(text='Miles')
miles_label.grid(column=2, row=0)

is_equal_to_label = tkinter.Label(text='is equal to')
is_equal_to_label.grid(column=0, row=1)

result = tkinter.Label(width=12, text='0')
result.grid(column=1, row=1)

km_label = tkinter.Label(text='Km')
km_label.grid(column=2, row=1)

button = tkinter.Button(text='Calculate', command=calculate)
button.grid(column=1, row=2)

window.mainloop()
