import tkinter as tk
from tkinter import ttk, messagebox

# Функции для шифра Виженера
def vigenere_encrypt(text, key):
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    encrypted_text = []
    key = key.upper()
    key_length = len(key)

    for i, char in enumerate(text.upper()):
        if char in alphabet:
            shift = alphabet.index(key[i % key_length])
            encrypted_text.append(alphabet[(alphabet.index(char) + shift) % len(alphabet)])
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text)

def vigenere_decrypt(encrypted_text, key):
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    decrypted_text = []
    key = key.upper()
    key_length = len(key)

    for i, char in enumerate(encrypted_text.upper()):
        if char in alphabet:
            shift = alphabet.index(key[i % key_length])
            decrypted_text.append(alphabet[(alphabet.index(char) - shift) % len(alphabet)])
        else:
            decrypted_text.append(char)

    return ''.join(decrypted_text)

# Функция для шифрования текста из интерфейса
def encrypt_text():
    text = text_entry.get()
    key = key_entry.get()
    method = method_var.get()

    if not text or not key:
        messagebox.showwarning("Внимание", "Введите текст и ключ!")
        return

    if method == "Виженера":
        encrypted_text = vigenere_encrypt(text, key)

    result_label.config(text="Зашифрованный текст: " + encrypted_text)
    encrypted_text_entry.delete(0, tk.END)
    encrypted_text_entry.insert(0, encrypted_text)

# Функция для дешифрования текста из интерфейса
def decrypt_text():
    encrypted_text = encrypted_text_entry.get()
    key = key_entry.get()
    method = method_var.get()

    if not encrypted_text or not key:
        messagebox.showwarning("Внимание", "Введите зашифрованный текст и ключ!")
        return

    if method == "Виженера":
        decrypted_text = vigenere_decrypt(encrypted_text, key)

    result_label.config(text="Расшифрованный текст: " + decrypted_text)

# Создание окна
root = tk.Tk()
root.title("Шифрование")

# Поле ввода исходного текста
tk.Label(root, text="Введите текст:").grid(row=0, column=0, padx=10, pady=5)
text_entry = tk.Entry(root, width=50)
text_entry.grid(row=0, column=1, padx=10, pady=5)

# Поле ввода ключа
tk.Label(root, text="Введите ключ:").grid(row=1, column=0, padx=10, pady=5)
key_entry = tk.Entry(root, width=50)
key_entry.grid(row=1, column=1, padx=10, pady=5)

# Выпадающий список для выбора метода шифрования
tk.Label(root, text="Метод шифрования:").grid(row=2, column=0, padx=10, pady=5)
method_var = tk.StringVar(value="Виженера")
method_combobox = ttk.Combobox(root, textvariable=method_var, values=["Виженера"], state="readonly")
method_combobox.grid(row=2, column=1, padx=10, pady=5)

# Кнопка для шифрования текста
encrypt_button = tk.Button(root, text="Зашифровать", command=encrypt_text)
encrypt_button.grid(row=3, column=0, padx=10, pady=10)

# Поле для отображения зашифрованного текста
tk.Label(root, text="Зашифрованный текст:").grid(row=4, column=0, padx=10, pady=5)
encrypted_text_entry = tk.Entry(root, width=50)
encrypted_text_entry.grid(row=4, column=1, padx=10, pady=5)

# Кнопка для дешифрования текста
decrypt_button = tk.Button(root, text="Дешифровать", command=decrypt_text)
decrypt_button.grid(row=5, column=0, columnspan=2, pady=10)

# Метка для отображения результата
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
