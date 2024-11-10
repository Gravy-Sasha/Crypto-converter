import requests
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


window = Tk()
window.title('Курс обмена криптовалют')
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w2 = w//2-180
h2 = h//2-225
window.geometry(f'360x450+{w2}+{h2}')

window.mainloop()