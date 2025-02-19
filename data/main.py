import tkinter as tk
from tkinter import messagebox

# Функция обработки нажатия кнопки "Войти"
def login():
<<<<<<< HEAD
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "12345":
        messagebox.showinfo("Успешно", f"Добро пожаловать, {username}!")
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль")
=======
    messagebox.showinfo("Вход", "Вы успешно вошли в систему!")
>>>>>>> functions

# Создание основного окна приложения
root = tk.Tk()
root.title("Приложение 'Заметки'")
<<<<<<< HEAD
root.geometry("300x250")

# Добавление заголовка
label = tk.Label(root, text="Авторизация", font=("Arial", 16))
label.pack(pady=10)

# Поле для ввода логина
username_label = tk.Label(root, text="Логин:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Поле для ввода пароля
password_label = tk.Label(root, text="Пароль:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Кнопка "Войти"
=======
root.geometry("300x200")  # Размеры окна

# Добавление заголовка
label = tk.Label(root, text="Добро пожаловать!", font=("Arial", 16))
label.pack(pady=20)

# Добавление кнопки "Войти"
>>>>>>> functions
login_button = tk.Button(root, text="Войти", command=login, width=10, height=1, font=("Arial", 12))
login_button.pack(pady=20)

# Запуск главного цикла приложения
root.mainloop()