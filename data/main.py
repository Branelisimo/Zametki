import tkinter as tk
from tkinter import messagebox

# Функция обработки нажатия кнопки "Войти"
def login():
    messagebox.showinfo("Вход", "Вы успешно вошли в систему!")

# Создание основного окна приложения
#
root = tk.Tk()
root.title("Приложение 'Заметки'")
root.geometry("300x200")  # Размеры окна

# Добавление заголовка
label = tk.Label(root, text="Добро пожаловать!", font=("Arial", 16))
label.pack(pady=20)

# Добавление кнопки "Войти"
login_button = tk.Button(root, text="Войти", command=login, width=10, height=1, font=("Arial", 12))
login_button.pack(pady=20)

# Запуск главного цикла приложения
root.mainloop()