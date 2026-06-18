def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise Exception('Inverse does not exist')
    else:
        return x % phi

def prime_factors(n):
    factors = []
    # Находим простые множители
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

def main():
    # Ввод открытых ключей
    e = int(input("Введите открытый ключ e: "))
    n = int(input("Введите модуль n: "))

    # Находим p и q как простые множители n
    factors = prime_factors(n)
    if len(factors) < 2:
        raise Exception("Не удалось найти два простых множителя для n.")

    p = factors[0]
    q = factors[1]

    # Вычисляем phi(n)
    phi = (p - 1) * (q - 1)

    # Находим закрытый ключ d
    d = mod_inverse(e, phi)

    print(f"Закрытый ключ K_c: {d}")
    print(f"Простые множители n: p = {p}, q = {q}")
    print(f"phi(n) = {phi}")

    # Хэш-значение сообщения
    m = 7
    print(f"Значение хэш-образа m: {m}")

    # Проверка заданных пар <m, s>
    pairs = [(193, 90), (62, 163), (95, 57)]
    for m_i, s_i in pairs:
        m_prime = pow(s_i, e, n)  # Проверка подписи: m' ≡ s^e (mod n)
        print(f"Проверка подписи для <{m_i}, {s_i}>: m' = {m_prime}")
        if m_prime == m_i:
            print(f"Подпись для <{m_i}, {s_i}> действительна.")
        else:
            print(f"Подпись для <{m_i}, {s_i}> недействительна.")

    # Проверка подписи для хэш-образа m = 7
    # Для проверки создаем подпись для h = 7
    s_for_m = pow(m, d, n)  # Создание подписи для 7
    print(f"Созданная подпись для хэш-образа m = {m}: s = {s_for_m}")

    # Проверка подписи
    m_prime_check = pow(s_for_m, e, n)  # Проверка подписи: m' ≡ s^e (mod n)
    print(f"Проверка подписи для хэш-образа m = 7: m' = {m_prime_check}")
    if m_prime_check == m:
       print("Подпись для хэш-образа m = 7 действительна.")
    else:
        print("Подпись для хэш-образа m = 7 недействительна.")

if __name__ == "__main__":
    main()

