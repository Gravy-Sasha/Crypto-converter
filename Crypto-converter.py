import requests
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


# Функции для данных из комбо-боксов
def update_a_label(event):
    code = a_combobox.get()
    name = crypto_cur[code]
    a_label.config(text=name)


def update_b_label(event):
    code = b_combobox.get()
    name = cur[code]
    b_label.config(text=name)


def update_c_label(event):
    code = c_combobox.get()
    name = cur[code]
    c_label.config(text=name)


#Словарь с названиями криптовалют
crypto_cur = {
    'bitcoin': 'Биткоин (BTC)',
    'ethereum': 'Эфириум (ETH)',
    'cardano': 'Кардано (ADA)',
    'tether': 'Тезер (USDT)',
    'solana': 'Солана (SOL)',
    'stacks': 'Стакс (STX)',
    'dogecoin': 'Догикоин (DOGE)',
}


# Словарь с названиями валют
cur = {
    'RUB': 'Российский рубль',
    'EUR':'Евро',
    'GBP':'Британский фунт стерлингов',
    'JPY':'Японская йена',
    'CNY':'Китайский юань',
    'KZT':'Казахский тенге',
    'UZS':'Узбекский сум',
    'CHF':'Швейцарский франк',
    'AED':'Дирхан ОАЭ',
    'CAD':'Канадский доллар',
    'USD':'Американский доллар'
}


# Создание основного окна приложения
window = Tk()
window.title('Курс обмена криптовалют')
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w2 = w//2-300
h2 = h//2-200
window.geometry(f'600x400+{w2}+{h2}')


# Виджеты для работы с приложением
# Метка выбора криптовалюты, комбо-бокс к ней и метка вывода
Label(text='Выберите криптовалюту:', font='Arial 12').grid(row=0,column=1, padx=10, pady=10)
a_combobox = ttk.Combobox(values=list(crypto_cur.keys()))
a_combobox.grid(row=1, column=1,padx=10, pady=10)
a_combobox.bind('<<ComboboxSelected>>', update_a_label)

a_label = ttk.Label(text='Тестовая строка')
a_label.grid(row=2, column=1,padx=10, pady=10)

#Метка выбора валюты, комбо-бокс к ней и метка вывода
Label(text='Выберите валюту:', font='Arial 12').grid(row=3,column=0, padx=10)
b_combobox = ttk.Combobox(values=list(cur.keys()))
b_combobox.grid(row=4, column=0,padx=20, pady=10)
b_combobox.bind('<<ComboboxSelected>>', update_b_label)

b_label = ttk.Label(text='Тестовая строка')
b_label.grid(row=5, column=0, padx=20, pady=10)

#Метка выбора второй валюты, комбо-бокс к ней и метка вывода
Label(text='Выберите вторую валюту:', font='Arial 12').grid(row=3,column=3)
c_combobox = ttk.Combobox(values=list(cur.keys()))
c_combobox.grid(row=4, column=3,padx=10, pady=10)
c_combobox.bind('<<ComboboxSelected>>', update_c_label)

c_label = ttk.Label(text='Тестовая строка')
c_label.grid(row=5, column=3, padx=20, pady=10)

#Метки вывода результата и кнопка загрузки
result_label1 = Label(text='Тестовая строка')
result_label1.grid(row=6, column=0, padx=20, pady=30)

result_label2 = Label(text='Тестовая строка')
result_label2.grid(row=7, column=0, padx=20, pady=5)

Button(text='Получить курс обмена', font='Arial 12').grid(row=8, column=1)

window.mainloop()
