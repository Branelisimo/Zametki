import tkinter as tk
from tkinter import messagebox


def login():
    """
    Функция обработки нажатия кнопки "Войти".

    Проверяет введенные пользователем логин и пароль.
    Если данные верны, отображает сообщение об успешной авторизации.
    Если данные неверны, показывает ошибку.

    Returns:
        None
    """
    username = username_entry.get()  # Получение значения из поля логина
    password = password_entry.get()  # Получение значения из поля пароля

    if username == "admin" and password == "12345":
        # Отображение успешного входа
        messagebox.showinfo("Успешно", f"Добро пожаловать, {username}!")
    else:
        # Отображение ошибки при неверных данных
        messagebox.showerror("Ошибка", "Неверный логин или пароль")


# Создание основного окна приложения
root = tk.Tk()
"""
Создание главного окна приложения с использованием библиотеки Tkinter.

Attributes:
    root (Tk): Основное окно приложения.
"""

root.title("Приложение 'Заметки'")  # Установка заголовка окна
root.geometry("300x250")  # Установка размеров окна

# Добавление заголовка
label = tk.Label(root, text="Авторизация", font=("Arial", 16))
"""
Создание метки (Label) для заголовка авторизации.

Attributes:
    label (Label): Метка с текстом "Авторизация".
"""
label.pack(pady=10)  # Размещение метки на экране

# Поле для ввода логина
username_label = tk.Label(root, text="Логин:")
"""
Создание метки для поля ввода логина.

Attributes:
    username_label (Label): Метка с текстом "Логин:".
"""
username_label.pack()  # Размещение метки на экране

username_entry = tk.Entry(root)
"""
Создание поля ввода для логина.

Attributes:
    username_entry (Entry): Поле ввода для логина.
"""
username_entry.pack(pady=5)  # Размещение поля ввода на экране

# Поле для ввода пароля
password_label = tk.Label(root, text="Пароль:")
"""
Создание метки для поля ввода пароля.

Attributes:
    password_label (Label): Метка с текстом "Пароль:".
"""
password_label.pack()  # Размещение метки на экране

password_entry = tk.Entry(root, show="*")
"""
Создание поля ввода для пароля с маскировкой символов.

Attributes:
    password_entry (Entry): Поле ввода для пароля.
"""
password_entry.pack(pady=5)  # Размещение поля ввода на экране

# Кнопка "Войти"
login_button = tk.Button(root, text="Войти", command=login, width=10, height=1, font=("Arial", 12))
"""
Создание кнопки "Войти" с привязкой функции `login`.

Attributes:
    login_button (Button): Кнопка для выполнения авторизации.
"""
login_button.pack(pady=20)  # Размещение кнопки на экране

# Запуск главного цикла приложения
if __name__ == "__main__":
    root.mainloop()
"""
Запуск главного цикла обработки событий Tkinter.
"""