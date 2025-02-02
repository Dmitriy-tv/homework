# Банковские операции клиента

Проект скрывает номера счетов и карт клиента,
а также сортирует список операций по дате и по типу
выполненная или отмененная.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Dmitriy-tv/homework
   ```
2. Перейдите в директорию проекта:
   ```bash
   cd src
   ```
3. Установите необходимые зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Использование

Примеры использования функций:

```python
from src.processing import filter_by_state, sort_by_date

# Пример использования filter_by_state
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]
executed_transactions = filter_by_state(transactions)

# Пример использования sort_by_date
sorted_transactions = sort_by_date(transactions)
```

## Тестирование
Проект покрыт тестами. Для запуска тестов выполните команду:
```poetry run pytest --cov```

Тесты выполняют проверку работоспособности кода и сокращают количество ошибок.

## Вклад

Если вы хотите внести свой вклад, пожалуйста, создайте форк репозитория и отправьте пул-реквест.
Проект распространяется под [лицензией MIT](LICENSE).