# Таблицы DES
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,}|
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

FP = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25]

E = [32, 1, 2, 3, 4, 5, 4, 5,
     6, 7, 8, 9, 8, 9, 10, 11,
     12, 13, 12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21, 20, 21,
     22, 23, 24, 25, 24, 25, 26, 27,
     28, 29, 28, 29, 30, 31, 32, 1]

# S-блоки (не изменены)
S_BOXES = [
    # S1
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
    # S2
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
    # S3
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    # S4
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
    # S5
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
    # S6
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
    # S7
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
    # S8
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]],
]

# Дополнение данных
def pad_data(data):
    pad_len = 8 - (len(data) % 8)
    return data + chr(pad_len) * pad_len

# Функция для удаления дополнения
def unpad_data(data):
    pad_len = ord(data[-1])
    return data[:-pad_len]

# Преобразование строк и битов
def string_to_bits(data):
    bits = []
    # Преобразуем строку в байты с использованием UTF-8
    byte_data = data.encode('utf-8')
    for byte in byte_data:
        # Преобразуем каждый байт в 8 бит
        bits.extend([int(bit) for bit in f"{byte:08b}"])
    return bits

# Преобразование бит в строку с использованием кодировки UTF-8
def bits_to_string(bits):
    byte_data = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        byte_value = int(''.join(map(str, byte)), 2)
        byte_data.append(byte_value)
    # Преобразуем байты обратно в строку с использованием UTF-8
    return bytes(byte_data).decode('utf-8', errors='ignore')

# Функция перестановки
def permute(block, table):
    return [block[i - 1] for i in table]

# Расширение блока
def expand(right_block):
    return permute(right_block, E)

# Реализация функции `s_box_substitution`
def s_box_substitution(block):
    """
    Применяет S-блоки к 48-битному блоку.
    """
    output = []
    for i in range(8):
        chunk = block[i*6:(i+1)*6]
        row = (chunk[0] << 1) | chunk[5]  # Определяем строку (по первому и последнему биту)
        col = (chunk[1] << 3) | (chunk[2] << 2) | (chunk[3] << 1) | chunk[4]  # Определяем столбец
        s_value = S_BOXES[i][row][col]  # Получаем значение из соответствующего S-блока
        output.extend([int(b) for b in f"{s_value:04b}"])  # Преобразуем в 4 бита
    return output

# Функция F
def feistel_function(right, subkey):
    expanded_right = expand(right)
    xored = [er ^ sk for er, sk in zip(expanded_right, subkey)]
    return s_box_substitution(xored)

# Упрощённая генерация подключей
def generate_subkeys(key):
    return [key[:48]] * 16

# DES для одного блока
def des_encrypt_block(block, key):
    block = permute(block, IP)
    left, right = block[:32], block[32:]
    subkeys = generate_subkeys(key)

    for i in range(16):
        temp = right
        right = [(l ^ f) for l, f in zip(left, feistel_function(right, subkeys[i]))]
        left = temp

    return permute(right + left, FP)

# DES дешифрование для одного блока
def des_decrypt_block(block, key):
    block = permute(block, IP)
    left, right = block[:32], block[32:]
    subkeys = generate_subkeys(key)[::-1]  # Инвертируем порядок подключей

    for i in range(16):
        temp = right
        right = [(l ^ f) for l, f in zip(left, feistel_function(right, subkeys[i]))]
        left = temp

    return permute(right + left, FP)

# Основной процесс шифрования и дешифрования
def des_encrypt(data, key):
    blocks = [data[i:i+64] for i in range(0, len(data), 64)]
    encrypted_data = []
    for block in blocks:
        while len(block) < 64:
            block.append(0)
        encrypted_data.extend(des_encrypt_block(block, key))
    return encrypted_data

def des_decrypt(data, key):
    blocks = [data[i:i+64] for i in range(0, len(data), 64)]
    decrypted_data = []
    for block in blocks:
        decrypted_block = des_decrypt_block(block, key)
        decrypted_data.extend(decrypted_block)

    # Преобразуем битовый массив обратно в строку
    decrypted_bits = bits_to_string(decrypted_data)
    
    # Удаляем дополнение
    return unpad_data(decrypted_bits)
    


# Основной код
if __name__ == "__main__":
    print("DES Encryption/Decryption (ECB Mode)")
    plaintext = input("Введите данные для шифрования: ")
    key = input("Введите ключ (8 символов): ")

    if len(key) != 8:
        print("Ошибка: ключ должен быть ровно 8 символов.")
        exit(1)

    # Подготовка данных
    padded_plaintext = pad_data(plaintext)
    print(f"Дополненный текст: {padded_plaintext}")

    data_bits = string_to_bits(padded_plaintext)
    key_bits = string_to_bits(key)

    # Шифрование
    encrypted_bits = des_encrypt(data_bits, key_bits)
    encrypted_text = bits_to_string(encrypted_bits)
    print("Зашифрованные данные:", encrypted_text)

    # Дешифрование
    decrypted_text = des_decrypt(encrypted_bits, key_bits)
    print("Расшифрованные данные:", decrypted_text)