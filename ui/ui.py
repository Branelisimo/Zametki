import tkinter as tk
from tkinter import messagebox
import time

# Создание главного окна
root = tk.Tk()
"""
Создание главного окна приложения "Демонстрация UI-действий".

Attributes:
    root (Tk): Главное окно приложения.
"""
root.title("Демонстрация UI-действий")  # Установка заголовка окна
root.geometry("400x300")  # Установка размеров окна

# Глобальная переменная для отслеживания состояния
counter = 0
"""
Глобальная переменная для отслеживания счетчика.

Attributes:
    counter (int): Текущее значение счетчика.
"""


def update_label():
    """
    Обновляет текст метки каждую секунду, пока счетчик меньше 10.

    Глобальная переменная `counter` увеличивается на 1, и текст метки обновляется.
    Если счетчик достигает значения 10, функция прекращает вызывать себя.

    Returns:
        None
    """
    global counter
    counter += 1
    label.config(text=f"Текущее значение: {counter}")  # Обновление текста метки
    if counter < 10:
        root.after(1000, update_label)  # Вызов самой себя через 1 секунду


def change_button_color():
    """
    Изменяет цвет кнопки между красным и синим.

    Получает текущий цвет кнопки, меняет его на противоположный (красный → синий или синий → красный)
    и применяет новый цвет к кнопке.

    Returns:
        None
    """
    current_color = button.cget("bg")  # Получение текущего цвета кнопки
    new_color = "red" if current_color == "blue" else "blue"
    button.config(bg=new_color)  # Изменение цвета кнопки


def show_message():
    """
    Показывает диалоговое окно с запросом подтверждения.

    Выводит диалоговое окно с вопросом "Вы хотите продолжить?".
    В зависимости от ответа пользователя обновляет текст метки.

    Returns:
        None
    """
    response = messagebox.askyesno("Подтверждение", "Вы хотите продолжить?")
    if response:
        label.config(text="Продолжаем...")
    else:
        label.config(text="Операция отменена.")


def update_slider(value):
    """
    Обновляет текст метки прогресса в зависимости от положения ползунка.

    Args:
        value (str): Текущее значение ползунка (передается как строка).

    Returns:
        None
    """
    progress_label.config(text=f"Прогресс: {int(value)}%")  # Обновление текста метки прогресса


# Создание метки для отображения счетчика
label = tk.Label(root, text="Текущее значение: 0", font=("Arial", 14))
"""
Метка для отображения текущего значения счетчика.

Attributes:
    label (Label): Метка с текстом счетчика.
"""
label.pack(pady=10)

# Создание кнопки для изменения цвета
button = tk.Button(root, text="Изменить цвет", command=change_button_color, bg="blue", fg="white")
"""
Кнопка для изменения цвета фона.

Attributes:
    button (Button): Кнопка с начальным цветом фона "синий".
"""
button.pack(pady=10)

# Создание кнопки для вывода диалогового окна
message_button = tk.Button(root, text="Показать сообщение", command=show_message)
"""
Кнопка для показа диалогового окна подтверждения.

Attributes:
    message_button (Button): Кнопка для вызова диалогового окна.
"""
message_button.pack(pady=10)

# Создание ползунка для отображения прогресса
slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, length=200, command=update_slider)
"""
Ползунок для отображения прогресса.

Attributes:
    slider (Scale): Ползунок с диапазоном от 0 до 100.
"""
slider.pack(pady=10)

# Метка для отображения прогресса ползунка
progress_label = tk.Label(root, text="Прогресс: 0%", font=("Arial", 12))
"""
Метка для отображения прогресса ползунка.

Attributes:
    progress_label (Label): Метка с текстом прогресса.
"""
progress_label.pack(pady=10)

# Запуск обновления метки каждую секунду
update_label()

# Запуск главного цикла приложения
if __name__ == "__main__":
    root.mainloop()
"""
Запуск главного цикла обработки событий Tkinter.
"""