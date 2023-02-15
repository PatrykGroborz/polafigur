from tkinter import *
import tkinter as tk

window = Tk()
window.title("Pola figur")
window.geometry("500x500")

frame = Frame(window)
frame.pack(side=TOP, expand=True, fill="both")

label = tk.Label(frame, font=("Comic Sans", 35), text = "Menu")
label.pack(side = tk.TOP)
def clearFrame():
    for widget in frame.winfo_children():
        widget.destroy()
    frame.pack_forget()
def kwadrat():
    clearFrame()
    canvas = Canvas(window, height=400, width=500)
    canvas.pack()
    kwadrat1 = canvas.create_rectangle(150, 150, 350, 350)
    text = canvas.create_text(110, 250, text="a = ?")
    value = tk.IntVar()
    label = tk.Label(window, text="Podaj bok a: ")
    label.pack(side = tk.TOP)
    spinbox = tk.Spinbox(window, from_=0, to=99999999999999999999999, textvariable=value)
    spinbox.pack(side = tk.TOP)
    def oblicz():

    button = tk.Button(window, text="Oblicz pole", pady=15)
    button.pack(pady=20)
button = tk.Button(frame, text="Kwadrat", command=kwadrat)
button.pack()
window.mainloop()