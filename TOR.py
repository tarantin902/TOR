import os
import tkinter as tk
from tkinter import filedialog, Scrollbar, Listbox

# Функция для получения списка файлов и папок, отсортированных по дате создания
def get_recent_files_and_folders(folder_path):
    items = os.listdir(folder_path)
    items = [os.path.join(folder_path, item) for item in items]
    items.sort(key=os.path.getctime, reverse=True)
    return items

# Функция для выбора папки
def choose_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry.delete(0, tk.END)
        entry.insert(0, folder_path)
        update_listbox()

# Функция для открытия выбранного файла или папки
def open_selected_item():
    selected_item = listbox.get(listbox.curselection())
    os.startfile(selected_item)

# Функция для обновления списка в окне Tkinter
def update_listbox():
    folder_path = entry.get()
    if os.path.isdir(folder_path):
        items = get_recent_files_and_folders(folder_path)
        listbox.delete(0, tk.END)  # Очистить текущий список
        for item in items:
            listbox.insert(tk.END, item)

# Создание главного окна Tkinter
root = tk.Tk()
root.title("TOR Самые свежие файлы и папки")
root.geometry("400x400")
root.resizable(0, 0) 

# Установка цветов
root.configure(bg="#aaffaa")  # Светло-зеленый фон

# Виджет для ввода пути к папке
label = tk.Label(root, text="Выберите папку:")
label.pack()

entry = tk.Entry(root)
entry.pack()

# Кнопка для выбора папки (красная)
choose_button = tk.Button(root, text="Выбрать папку", command=choose_folder, bg="red", fg="white")
choose_button.pack()

# Кнопка для обновления списка (серая)
update_button = tk.Button(root, text="Обновить список", command=update_listbox, bg="gray")
update_button.pack()

# Кнопка для открытия выбранного элемента (оранжевая)
open_button = tk.Button(root, text="Открыть выбранный элемент", command=open_selected_item, bg="orange")
open_button.pack()

# Список для вывода результатов
scrollbar = Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = Listbox(root, yscrollcommand=scrollbar.set, height=20)  # Здесь можно установить желаемую высоту

listbox.pack(fill=tk.BOTH)
scrollbar.config(command=listbox.yview)

# Запустить главный цикл Tkinter
root.mainloop()
