import tkinter as tk


def cast_on_button(y):
    print("pressed! the name is", y)


window = tk.Tk()

ert1_logo = tk.PhotoImage(file="source/ert1.png")
x = "mitsos"
button = tk.Button(master=window, image=ert1_logo, command=lambda: cast_on_button(x))
button.grid(row=0, column=0, sticky="nsew")
# button.pack()
window.mainloop()


