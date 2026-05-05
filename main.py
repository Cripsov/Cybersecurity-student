import bytesize
import base64

data =b"label"

for key in range(256):
    result = bytes([key ^ b for b in data]) # Ключ для байта а байты берём из даты
    if all(32 <= b <= 126 for b in result): # Если все числа больше 32 и меньше 12 то байты пишутся в результат
        print(f'Ключ: {key}, шифр {result}')