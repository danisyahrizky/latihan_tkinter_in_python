import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.configure(bg="white")
window.wm_geometry("300x200")
window.wm_resizable(False,False)
window.wm_title("Input Nama")

namaDepan = tk.StringVar()
namaBelakang = tk.StringVar()

# frame input
input_frame = ttk.Frame(window)

# penempatan grid, pack, place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen-komponen
# 1. label nama depan
namaDepanLabel = ttk.Label(input_frame,text="Nama Depan")
namaDepanLabel.pack(padx=10,fill="x",expand=True)

# 2. entry nama depan
namaDepanEntry = ttk.Entry(input_frame, textvariable = namaDepan)
namaDepanEntry.pack(padx=10,pady=10,fill="x",expand=True)

# 3. label nama belakang
namabelakangLabel = ttk.Label(input_frame,text="Nama Belakang")
namabelakangLabel.pack(padx=10,fill="x",expand=True)

# 4. entry nama belakang
namabelakangEntry = ttk.Entry(input_frame, textvariable = namaBelakang)
namabelakangEntry.pack(padx=10,pady=10,fill="x",expand=True)

# 5. tombol
def tombol_click():
    pesan = f"Berhasil Input {namaDepan.get()} {namaBelakang.get()}"
    messagebox.showinfo(title="Input Nama", message=pesan)

tombolSapa = ttk.Button(input_frame, text = "Input", command=tombol_click)
tombolSapa.pack(fill="x", expand=True,padx=10, pady=10)

window.mainloop()