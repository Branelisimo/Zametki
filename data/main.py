import tkinter as tk
from tkinter import messagebox

# Функция обработки входа
def authenticate():
    user = user_input.get()
    pwd = pwd_input.get()
    if user == "root" and pwd == "password":
        show_message("Успешная авторизация", f"Привет, {user}!")
    else:
        show_message("Ошибка", "Неверный пользователь или пароль")

# Вспомогательная функция для вывода сообщений
def show_message(title, message):
    messagebox.showinfo(title, message)

# Создание основного окна
window = tk.Tk()
window.title("Авторизация")
window.geometry("350x250")
window.resizable(False, False)

# Создание фрейма для элементов
frame = tk.Frame(window, padx=20, pady=20)
frame.grid(row=0, column=0)

# Добавление заголовка
header = tk.Label(frame, text="Пожалуйста, войдите", font=("Arial", 14))
header.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Поле для ввода пользователя
user_label = tk.Label(frame, text="Имя пользователя:", font=("Arial", 10))
user_label.grid(row=1, column=0, sticky="w", pady=5)
user_input = tk.Entry(frame, width=30)
user_input.grid(row=1, column=1, pady=5)

# Поле для ввода пароля
pwd_label = tk.Label(frame, text="Пароль:", font=("Arial", 10))
pwd_label.grid(row=2, column=0, sticky="w", pady=5)
pwd_input = tk.Entry(frame, show="*", width=30)
pwd_input.grid(row=2, column=1, pady=5)

# Кнопка входа
login_button = tk.Button(frame, text="Войти", command=authenticate, font=("Arial", 12), bg="#4caf50", fg="white")
login_button.grid(row=3, column=0, columnspan=2, pady=20)

# Запуск главного цикла
window.mainloop()