from typing import Any, Dict, Generator, Iterable, Iterator


def filter_by_currency(transactions: list[Dict[str, Any]], currency: str = "USD"
                       ) -> Generator[dict[str, Any], None, None]:
    """
    Поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD).
    """
    if not transactions:
        raise ValueError("Не верно введены данные")
    else:
        for transaction in transactions:
            if transaction['operationAmount']['currency']['name'] == currency:
                yield transaction

# Пример использования функции
# usd_transactions = filter_by_currency(transactions, "USD")
# for _ in range(3):
    # print(next(usd_transactions))


def transaction_descriptions(transactions: Iterable[Dict[str, Any]]) -> Iterator[str]:

    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""

    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")

# Пример использования функции
# descriptions = transaction_descriptions(transactions)
# for _ in range(5):
    # print(next(descriptions))


def card_number_generator(start: int, stop: int) -> Generator[str, Any, None]:
    """
Выдает номера банковских карт в формате
XXXX XXXX XXXX XXXX, где X — цифра номера карты. Генератор может сгенерировать
номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999
    """
    for card_list in range(start, stop + 1):
        card_numbers = '0000000000000000'
        if start <= stop or start >= 1 or stop <= 9999999999999999:
            card_num = (card_numbers[:-len(str(card_list))] + str(card_list))
            format_card_num = " ".join([card_num[i:i + 4] for i in range(0, 16, 4)])
            yield format_card_num
        else:
            yield "Ошибка"

# Пример работы генератора
# for card_number in card_number_generator(1, 5):
    # print(card_number)
