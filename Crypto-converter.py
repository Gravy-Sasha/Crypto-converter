import requests
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


# Основная функция конвертации валют
def exchange():
    a_code = a_combobox.get() #Получаем выбранный код криптовалюты
    b_code = b_combobox.get() #Получаем выбранный код валюты
    c_code = c_combobox.get() #Получаем выбранный код второй валюты
    if a_code and b_code or c_code: #Проверяем наличие выбора валюты
        try:
            # Запрашиваем информацию API CoinGecko по первой валюте
            response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={a_code}&vs_currencies={b_code}')
            response.raise_for_status() # Проверка на ошибки
            data1 = response.json()

            # Запрашиваем информацию API CoinGecko по второй валюте
            response2 = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={a_code}&vs_currencies={c_code}')
            response2.raise_for_status()  # Проверка на ошибки
            data2 = response2.json()

            #Проверяем наличие ответа, выводим по ключу
            if a_code in data1 and data1[a_code]:
                exchange_rate1 = data1[a_code][b_code]
                a_name = crypto_cur[a_code]
                b_name = cur[b_code]
                result_label1.config(text=f'Курс: {exchange_rate1:.1f} {a_name} за 1 {b_name}', font='Arial 10', bg='salmon')
                exchange_rate2 = data2[a_code][c_code]
                a_name = crypto_cur[a_code]
                c_name = cur[c_code]
                result_label2.config(text=f'Курс: {exchange_rate2:.1f} {a_name} за 1 {c_name}', font='Arial 10', bg='green')
            else:
                mb.showerror('Ошибка!', f'Валюта {a_code} не найдена!')
        except Exception as e:
            mb.showerror('Ошибка!', f'Произошла ошибка: {e}.')

    else:
        mb.showwarning('Внимание!', 'Введите код валюты!')


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
    'rub': 'Российский рубль',
    'eur':'Евро',
    'gbr':'Британский фунт стерлингов',
    'jpy':'Японская йена',
    'cny':'Китайский юань',
    'kzt':'Казахский тенге',
    'uzs':'Узбекский сум',
    'chf':'Швейцарский франк',
    'aed':'Дирхан ОАЭ',
    'cad':'Канадский доллар',
    'usd':'Американский доллар'
}


# Создание основного окна приложения
window = Tk()
window.title('Курс обмена криптовалют')
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w2 = w//2-180
h2 = h//2-200
window.geometry(f'360x400+{w2}+{h2}')


# Виджеты для работы с приложением
# Метка выбора криптовалюты, комбо-бокс к ней и метка вывода
Label(text='Выберите криптовалюту:', font='Arial 12').pack( padx=10, pady=10)
a_combobox = ttk.Combobox(values=list(crypto_cur.keys()))
a_combobox.pack()
a_combobox.bind('<<ComboboxSelected>>', update_a_label)

a_label = ttk.Label(text='Тестовая строка')
a_label.pack()

#Метка выбора валюты, комбо-бокс к ней и метка вывода
Label(text='Выберите валюту:', font='Arial 12').pack(pady=10, padx=10)
b_combobox = ttk.Combobox(values=list(cur.keys()))
b_combobox.pack()
b_combobox.bind('<<ComboboxSelected>>', update_b_label)

b_label = ttk.Label(text='Тестовая строка')
b_label.pack()

#Метка выбора второй валюты, комбо-бокс к ней и метка вывода
Label(text='Выберите вторую валюту:', font='Arial 12').pack(pady=10, padx=10)
c_combobox = ttk.Combobox(values=list(cur.keys()))
c_combobox.pack()
c_combobox.bind('<<ComboboxSelected>>', update_c_label)

c_label = ttk.Label(text='Тестовая строка')
c_label.pack()

#Метки вывода результата и кнопка загрузки
result_label1 = Label()
result_label1.pack(padx=10,pady=10)

result_label2 = Label()
result_label2.pack(padx=10, pady=10)

Button(text='Получить курс обмена', font='Arial 12', padx=40, command=exchange).pack()

window.mainloop()
