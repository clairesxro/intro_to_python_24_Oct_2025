import tkinter as tk
from tkinter import ttk

windows = tk.Tk()  # buat bikin jendela
windows.title("Contoh dari label")  # buat memberikan label jendela

label_sambutan = ttk.Label(
    windows,  # lokasi jendela
    text="Selamat datang di GUI Pertama",  # pesan nya
    font=("Helvetica",10)  # tipe font nya
)

label_sambutan.pack(pady=20,padx=20)  # style nya
windows.mainloop()  # jalankan code