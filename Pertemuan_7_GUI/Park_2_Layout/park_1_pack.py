import tkinter as tk
from tkinter import ttk

layar1 = tk.Tk()  
layar1.title("Contoh dari entry")  

ttk.Label(layar1,text="Label 1").pack()
ttk.Button(layar1,text="Button 1").pack()
ttk.Label(layar1,text="Label ke 3").pack(padx=50,pady=50)



layar1.mainloop()  # jalankan code