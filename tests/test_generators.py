import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.mark.parametrize("transactions, currency", [
    ([
         {
             "id": 939719570,
             "state": "EXECUTED",
             "date": "2018-06-30T02:08:58.425572",
             "operationAmount": {
                 "amount": "9824.07",
                 "currency": {
                     "name": "USD",
                     "code": "USD"
                 }
             },
             "description": "Перевод организации",
             "from": "Счет 75106830613657916952",
             "to": "Счет 11776614605963066702"
         },
         {
             "id": 142264268,
             "state": "EXECUTED",
             "date": "2019-04-04T23:20:05.206878",
             "operationAmount": {
                 "amount": "79114.93",
                 "currency": {
                     "name": "USD",
                     "code": "USD"
                 }
             },
             "description": "Перевод со счета на счет",
             "from": "Счет 19708645243227258542",
             "to": "Счет 75651667383060284188"
         }
     ], "USD")
])
def test_filter_by_currency(transactions, currency):
    """Тест работы функции filter_by_currency"""

    filtered_transactions = filter_by_currency(transactions, currency)
    assert next(filtered_transactions)["id"] == 939719570


@pytest.mark.parametrize("transaction, expected", [
    ({"description": "Перевод организации"}, "Перевод организации"),
    ({"description": "Перевод со счёта на счёт"}, "Перевод со счёта на счёт"),
    ({"description": "Перевод с карты на карту"}, "Перевод с карты на карту"),
])
def test_transaction_descriptions(transaction: [dict], expected: [str]):
    """Тест работы функции transaction_descriptions"""

    descriptions = transaction_descriptions([transaction])
    assert list(descriptions) == [expected]


def test_card_number_generator():
    """Тест работы функции card_number_generator"""

    generator = card_number_generator(1, 3)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
