import base64

text = "POFNLEP ALECZW DWZE ACZDAPC"

for shift in range(26):
    result = ''
    for char in text:
        if char.isalpha():
            result += chr((ord(char) - 65 - shift ) % 26 + 65)
        else:
            result += char
    print(f'сдвиг {shift}: {result}')