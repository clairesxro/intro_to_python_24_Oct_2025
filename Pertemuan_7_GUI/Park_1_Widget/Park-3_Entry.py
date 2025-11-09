import tkinter as tk
from tkinter import ttk

def cetak_pesan():
    data_inputan = input_nama.get()
    print(f"Teks yang di inputkan {data_inputan}")

layar1 = tk.Tk()  
layar1.title("Contoh dari entry")  

input_nama = ttk.Entry(layar1,width=30)
input_nama.pack(padx=20,pady=20)

tombol_cetak = ttk.Button(layar1,text="Kirim!",command=cetak_pesan)
tombol_cetak.pack()

layar1.mainloop()  # jalankan code