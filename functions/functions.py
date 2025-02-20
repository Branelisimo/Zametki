# Импорт библиотеки tkinter
import tkinter as tk
from tkinter import messagebox

# Глобальная переменная для хранения заметок (список или словарь)
notes = []

def add_note():
    """
    Создает окно для добавления новой заметки и сохраняет её в список.

    Открывает новое окно с текстовым полем и кнопкой "Сохранить". При нажатии на кнопку текст заметки
    добавляется в глобальный список `notes` вместе с текущей датой, после чего список обновляется.

    .. note:: Если текст заметки пустой, отображается предупреждение.
    """
    # Создать окно для ввода заметки
    note_window = tk.Toplevel()
    note_window.title("Новая заметка")
    
    # Добавить текстовое поле для ввода
    note_text = tk.Text(note_window, height=10, width=50)
    note_text.pack()
    
    def save_note():
        """
        Сохраняет введённую заметку и обновляет отображение.

        Извлекает текст из текстового поля, проверяет его на пустоту и добавляет в список `notes`.
        После этого обновляет отображение заметок и закрывает окно.
        """
        content = note_text.get("1.0", tk.END).strip()
        if content:
            notes.append({"text": content, "date": "текущая дата"})
            update_notes_display()
            note_window.destroy()
        else:
            messagebox.showwarning("Ошибка", "Заметка не может быть пустой")
    
    # Добавить кнопку "Сохранить"
    save_button = tk.Button(note_window, text="Сохранить", command=save_note)
    save_button.pack()

def update_notes_display():
    """
    Обновляет отображение списка заметок в основном окне.

    Очищает текущий фрейм с заметками и отображает все заметки из списка `notes` в виде кратких
    меток. Каждая метка кликабельна для просмотра полной заметки.

    .. seealso:: :func:`view_note`
    """
    for widget in notes_frame.winfo_children():
        widget.destroy()
    
    for index, note in enumerate(notes):
        note_label = tk.Label(notes_frame, text=note["text"][:50] + "...", anchor="w")
        note_label.pack(fill="x")
        note_label.bind("<Button-1>", lambda e, i=index: view_note(i))

def view_note(index):
    """
    Отображает полное содержание заметки и предоставляет возможность её удаления.

    :param int index: Индекс заметки в списке `notes`.
    :return: None

    Открывает окно с полным текстом заметки в режиме "только чтение" и кнопкой "Удалить".
    При нажатии на кнопку заметка удаляется из списка, а отображение обновляется.
    """
    view_window = tk.Toplevel()
    view_window.title("Просмотр заметки")
    
    note_text = tk.Text(view_window, height=10, width=50)
    note_text.insert("1.0", notes[index]["text"])
    note_text.config(state="disabled")
    note_text.pack()
    
    def delete_note():
        """
        Удаляет заметку из списка и обновляет отображение.

        Удаляет заметку по указанному индексу из списка `notes`, обновляет интерфейс и закрывает окно.
        """
        notes.pop(index)
        update_notes_display()
        view_window.destroy()
    
    delete_button = tk.Button(view_window, text="Удалить", command=delete_note)
    delete_button.pack()

def start_app():
    """
    Инициализирует и запускает основное окно приложения "Zametki".

    Создает главное окно с кнопкой для добавления заметок и фреймом для их отображения.
    Запускает главный цикл приложения.

    :global root: Главное окно приложения.
    :global notes_frame: Фрейм для отображения заметок.
    """
    global root, notes_frame
    root = tk.Tk()
    root.title("Zametki")
    root.geometry("400x500")
    
    add_button = tk.Button(root, text="Добавить заметку", command=add_note)
    add_button.pack(pady=10)
    
    notes_frame = tk.Frame(root)
    notes_frame.pack(fill="both", expand=True)
    
    update_notes_display()
    root.mainloop()

if __name__ == "__main__":
    root.mainloop()