import random


def generate_key(len):
    generated_key = ""
    for i in range(len):
        generated_key += generate_rand_char()
    return generated_key


def generate_rand_char():
    random_eng_or_rus_decimal = random.choice([random.randint(65, 122), random.randint(1040, 1103)])
    rand_char = chr(random_eng_or_rus_decimal)
    return rand_char


def vernam_encrypt(plain_text, key):
    if len(plain_text) != len(key):
        raise ValueError("Длина ключа должна быть равна длине текста")

    encrypted_text = ""
    for i in range(len(plain_text)):
        encrypted_char = chr(ord(plain_text[i]) ^ ord(key[i]))
        encrypted_text += encrypted_char

    return encrypted_text


def vernam_decrypt(encrypted_text, key):
    if len(encrypted_text) != len(key):
        raise ValueError("Длина ключа должна быть равна длине зашифрованного текста")

    decrypted_text = ""
    for i in range(len(encrypted_text)):
        decrypted_char = chr(ord(encrypted_text[i]) ^ ord(key[i]))
        decrypted_text += decrypted_char

    return decrypted_text


plain_text = input("Введите текст для шифрования: ").upper()
key = generate_key(len(plain_text)).upper()

try:
    encrypted_text = vernam_encrypt(plain_text, key)
    print("Зашифрованный текст:", encrypted_text)

    decrypted_text = vernam_decrypt(encrypted_text, key)
    print("Расшифрованный текст:", decrypted_text)
except ValueError as e:
    print("Ошибка:", e)
