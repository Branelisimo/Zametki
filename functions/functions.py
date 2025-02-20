import tkinter as tk
from tkinter import messagebox

# Словарь для хранения заметок (ID: текст заметки)
notes = {}

# Функция для создания новой заметки
def create_note():
    note_id = len(notes) + 1  # Простой ID для заметки
    notes[note_id] = ""  # Создаем пустую заметку
    update_notes_list()  # Обновляем список заметок
    show_note(note_id)  # Открываем созданную заметку для редактирования

# Функция для сохранения заметки
def save_note():
    selected_id = get_selected_note_id()
    if selected_id is not None:
        text = note_text.get("1.0", tk.END).strip()  # Получаем текст из текстового поля
        notes[selected_id] = text  # Сохраняем текст в словаре
        messagebox.showinfo("Сохранено", "Заметка успешно сохранена!")
    else:
        messagebox.showwarning("Ошибка", "Выберите заметку для сохранения")

# Функция для удаления заметки
def delete_note():
    selected_id = get_selected_note_id()
    if selected_id is not None:
        del notes[selected_id]  # Удаляем заметку из словаря
        update_notes_list()  # Обновляем список заметок
        clear_note_view()  # Очищаем поле просмотра заметки
    else:
        messagebox.showwarning("Ошибка", "Выберите заметку для удаления")

# Функция для отображения выбранной заметки
def show_note(note_id):
    note_text.delete("1.0", tk.END)  # Очищаем текстовое поле
    note_text.insert(tk.END, notes.get(note_id, ""))  # Вставляем текст заметки

# Функция для получения ID выбранной заметки
def get_selected_note_id():
    selection = notes_list.curselection()  # Получаем индекс выбранного элемента
    if selection:
        index = selection[0]
        note_ids = list(notes.keys())
        return note_ids[index]  # Возвращаем ID заметки
    return None

# Функция для обновления списка заметок
def update_notes_list():
    notes_list.delete(0, tk.END)  # Очищаем список
    for note_id, note_content in notes.items():
        notes_list.insert(tk.END, f"Заметка {note_id}: {note_content[:20]}...")  # Добавляем краткое описание

# Функция для очистки поля просмотра заметки
def clear_note_view():
    note_text.delete("1.0", tk.END)

# Создание главного окна
root = tk.Tk()
root.title("Приложение 'Заметки'")
root.geometry("600x400")

# Левая панель: список заметок
notes_list = tk.Listbox(root, width=30, selectmode=tk.SINGLE)
notes_list.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

# Кнопки управления
button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, pady=10)

create_button = tk.Button(button_frame, text="Создать", command=create_note)
create_button.pack(side=tk.LEFT, padx=5)

save_button = tk.Button(button_frame, text="Сохранить", command=save_note)
save_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(button_frame, text="Удалить", command=delete_note)
delete_button.pack(side=tk.LEFT, padx=5)

# Правая панель: текстовое поле для редактирования заметки
note_text = tk.Text(root, width=50, height=20)
note_text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Привязка события выбора заметки
notes_list.bind("<<ListboxSelect>>", lambda event: show_note(get_selected_note_id()))

# Запуск приложения
root.mainloop()