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
args = Namespace(country='Two letter country code (Specify ALL for all countries)', phone=Phone number for attack (without +), time=Attack time in seconds, threads=Number of threads, timeout=Request timeout, proxy=Whether to use a proxy for attack (True or False or {"http": "http://your.proxy.com", "https": "http://your.proxy.com"}))
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

# Stopping the attack
attack_threads.join(0)
del attack_threads
time.sleep(5) # Increase the time if the results contain zeros
bomber = bombers[bomber_id]
bomber.stop()
successful, failed = bomber.send_report()
print(f"Successfully sent (Not everyone can get there!): {successful}")
print(f"Failed to send: {failed}")

# Returns the result of the attack after it ends
time.sleep(Attack time in seconds)
time.sleep(5) # Increase the time if the results contain zeros
bomber = bombers[bomber_id]
successful, failed = bomber.send_report()
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
args = Namespace(country='Двухбуквенный код страны (Укажите ALL для всех стран)', phone=Номер телефона для атаки (без +), time=Время атаки в секундах, threads=Количество потоков, timeout=Время ожидания запроса, proxy=Использовать ли прокси для атаки (True или False или {"http": "http://your.proxy.com", "https": "http://your.proxy.com"}))
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

# Остановка атаки
attack_threads.join(0)
del attack_threads
time.sleep(5) # Увеличьте время если в результатах по нулям
bomber = bombers[bomber_id]
bomber.stop()
successful, failed = bomber.send_report()
print(f"Успешно отправлено(Дойти могут не все!): {successful}")
print(f"Не удалось отправить: {failed}")

# Возвращает результат атаки после её окончания
time.sleep(Attack time in seconds)
time.sleep(5) # Увеличьте время если в результатах по нулям
bomber = bombers[bomber_id]
successful, failed = bomber.send_report()
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