import random

def isprime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Генерация кандидата на простое число
def generate_prime_candidate(length):
    p = random.getrandbits(length)
    print(p)
    # Убедитесь, что число нечетное
    p |= (1 << length - 1) | 1
    return p

# Генерация простого числа
def generate_prime_number(length):
    p = 4
    while not isprime(p):
        p = generate_prime_candidate(length)
    return p

# Наибольший общий делитель
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Обратный элемент по модулю
# Расширенный алгоритм Евклида
def mod_inverse(e, phi):
    m0, x0, x1 = phi, 0, 1

    # тк 1 % 1 = 0 
    if phi == 1:
        return 0
    
    while e > 1:
        # Здесь мы вычисляем целую часть от деления e на ф
        # Это значение q (квотент)
        q = e // phi
        phi, e = e % phi, phi
        # Это обновление коэффициентов происходит в соответствии с выражением a⋅x+b⋅y=gcd(a,b)
        x0, x1 = x1 - q * x0, x0

    # После завершения цикла x1 может оказаться отрицательным
    if x1 < 0:
        x1 += m0

    return x1

# Генерация пары ключей RSA
def rsa_keypair(bits):
    # p = generate_prime_number(bits)
    # q = generate_prime_number(bits)
    p = int(input("Введите значение p: "))
    q = int(input("Введите значение q: "))
    
    r = p * q
    # Вычисление функции Эйлера ϕ(n)=(p−1)×(q−1)
    phi = (p - 1) * (q - 1)
    
    # Выбор открытой экспоненты
    # Ko = 65537  # (или 2^16+1) используются много где (например OpenSSL)
    Ko = int(input("Введите значение K_o: "))

    if gcd(Ko, phi) == 1:
        print(f"Значение K_o = {Ko} взаимно просто с φ(n) = {phi}, и его можно использовать как открытый ключ.")
    else:
        print("Нужно выбрать другое значение для K_o.")
        exit(0)
    
    # Вычисление закрытой экспоненты
    Kc = mod_inverse(Ko, phi)

    print("p:\t", p)
    print("q:\t", q)
    print("r:\t", r)
    print("ф:\t", phi)
    print("Ko:\t", Ko)
    print("Kc:\t", Kc)
    
    return ((Ko, r), (Kc, r))  # Открытый и закрытый ключи

# Шифрование сообщения
def rsa_encrypt(public_key, plaintext):
    Ko, r = public_key  # Распаковка открытого ключа
    encrypted_numbers = []

    # Преобразование каждого символа в число и шифрование
    for char in plaintext:
        # Преобразуем символ в его ASCII-код
        m = char_to_int(char)
        # Шифруем с помощью формулы: c = m(i)^Ko mod r
        c = pow(m, Ko, r)
        encrypted_numbers.append(c)

    return encrypted_numbers

def rsa_decrypt(private_key, cipher_text):
    Kc, r = private_key  # Распаковка закрытого ключа
    decrypted_chars = []

    # Расшифровка каждого зашифрованного числа
    for c in cipher_text:
        # Расшифровываем с помощью формулы: m = c(i)^Kc mod r
        m = pow(c, Kc, r)
        # Преобразуем число обратно в символ
        decrypted_chars.append(int_to_char(m))

    return ''.join(decrypted_chars)

def char_to_int(char):
    return ord(char) - ord('А') + 2

def int_to_char(int):
    return chr(int + ord('А') - 2)

def text_to_int(text):
    return [char_to_int(char) for char in text]

bits = 10 # Длина ключа, можно увеличить для большей безопасности
public_key, private_key = rsa_keypair(bits)

message = input("Введите сообщение для шифрования (только заглавные буквы): ")

print("Сообщение в числовом представлении:", text_to_int(message))
print("Оригинальное сообщение:", message)

encrypted_message = rsa_encrypt(public_key, message)
print("Зашифрованное сообщение:", encrypted_message)

decrypted_message = rsa_decrypt(private_key, encrypted_message)
print("Расшифрованное сообщение:", decrypted_message)
