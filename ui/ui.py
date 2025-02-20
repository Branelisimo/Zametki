import tkinter as tk
from tkinter import messagebox
import time

# Создание главного окна
root = tk.Tk()
root.title("Демонстрация UI-действий")
root.geometry("400x300")

# Глобальная переменная для отслеживания состояния
counter = 0

# Функция для обновления текста метки
def update_label():
    global counter
    counter += 1
    label.config(text=f"Текущее значение: {counter}")  # Обновление текста метки
    if counter < 10:
        root.after(1000, update_label)  # Вызов самой себя через 1 секунду

# Функция для изменения цвета кнопки
def change_button_color():
    current_color = button.cget("bg")  # Получение текущего цвета кнопки
    new_color = "red" if current_color == "blue" else "blue"
    button.config(bg=new_color)  # Изменение цвета кнопки

# Функция для вывода диалогового окна
def show_message():
    response = messagebox.askyesno("Подтверждение", "Вы хотите продолжить?")
    if response:
        label.config(text="Продолжаем...")
    else:
        label.config(text="Операция отменена.")

# Функция для управления ползунком
def update_slider(value):
    progress_label.config(text=f"Прогресс: {int(value)}%")  # Обновление текста метки прогресса

# Создание метки для отображения счетчика
label = tk.Label(root, text="Текущее значение: 0", font=("Arial", 14))
label.pack(pady=10)

# Создание кнопки для изменения цвета
button = tk.Button(root, text="Изменить цвет", command=change_button_color, bg="blue", fg="white")
button.pack(pady=10)

# Создание кнопки для вывода диалогового окна
message_button = tk.Button(root, text="Показать сообщение", command=show_message)
message_button.pack(pady=10)

# Создание ползунка для отображения прогресса
slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, length=200, command=update_slider)
slider.pack(pady=10)

# Метка для отображения прогресса ползунка
progress_label = tk.Label(root, text="Прогресс: 0%", font=("Arial", 12))
progress_label.pack(pady=10)

# Запуск обновления метки каждую секунду
update_label()

# Запуск главного цикла приложения
root.mainloop()