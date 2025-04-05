import unittest
import pandas as pd
from unittest.mock import mock_open, patch

from src.csv_excel import read_financial_operations_csv
from src.csv_excel import read_financial_operations_excel


# Тестовая функция
@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="id;state;date;amount;currency_name;currency_code;from;to;description\n650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации\n3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту\n",
)
def test_read_financial_operations(mock_file):
    file_path = "dummy_path.csv"
    operations = read_financial_operations_csv(file_path)

    expected_operations = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": "29740",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]

    assert operations == expected_operations
    mock_file.assert_called_once_with(file_path, mode="r", encoding="utf-8")


@patch("pandas.read_excel")
def test_read_financial_operations_excel(mock_read_excel):
    # Создаем фейковые данные в виде DataFrame
    mock_data = pd.DataFrame(
        {
            "id": [123, 456],
            "state": ["EXECUTED", "CANCELED"],
            "date": ["2023-01-01", "2023-01-02"],
            "amount": [1000, 2000],
            "currency_name": ["USD", "EUR"],
            "currency_code": ["USD", "EUR"],
            "from": ["Account 1", "Account 2"],
            "to": ["Account 3", "Account 4"],
            "description": ["Test transaction 1", "Test transaction 2"],
        }
    )

    # Настраиваем mock на возврат созданного DataFrame
    mock_read_excel.return_value = mock_data

    # Вызываем тестируемую функцию
    file_path = "dummy_path.xlsx"
    transactions = read_financial_operations_excel(file_path)

    # Ожидаемые результаты
    expected_transactions = [
        {
            "id": 123,
            "state": "EXECUTED",
            "date": "2023-01-01",
            "amount": 1000,
            "currency_name": "USD",
            "currency_code": "USD",
            "from": "Account 1",
            "to": "Account 3",
            "description": "Test transaction 1",
        },
        {
            "id": 456,
            "state": "CANCELED",
            "date": "2023-01-02",
            "amount": 2000,
            "currency_name": "EUR",
            "currency_code": "EUR",
            "from": "Account 2",
            "to": "Account 4",
            "description": "Test transaction 2",
        },
    ]

    # Проверяем, что функция вернула ожидаемые результаты
    assert transactions == expected_transactions

    # Проверяем, что read_excel была вызвана с правильным аргументом
    mock_read_excel.assert_called_once_with(file_path)


if __name__ == "__main__":
    unittest.main()