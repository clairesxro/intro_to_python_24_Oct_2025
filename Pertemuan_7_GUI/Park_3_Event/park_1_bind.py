import tkinter as tk
from tkinter import ttk


def getSapa(event):
    print(f"Hello World!!!!!")

layar1 = tk.Tk()  
layar1.title("Using command")  

label = ttk.Label(layar1,text= "Arahkan mouse ke sini !")
label.bind("<Enter>",getSapa)
label.pack(padx=10,pady=10)

layar1.mainloop()  # jalankan code