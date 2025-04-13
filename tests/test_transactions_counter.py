from src.transaction_counter import count_transactions_by_category


def test_count_transactions_by_category():
    # Пример транзакций
    transactions = [
        {"id": 1, "description": "Оплата за услуги", "amount": 100},
        {"id": 2, "description": "Покупка товара", "amount": 2000},
        {"id": 3, "description": "Оплата за интернет", "amount": 350},
        {"id": 4, "description": "Оплата за услуги", "amount": 150},
    ]

    categories = [
        "Оплата за услуги",
        "Покупка товара",
        "Оплата за интернет",
        "Неправильная категория",
    ]

    expected_result = {
        "Оплата за услуги": 2,
        "Покупка товара": 1,
        "Оплата за интернет": 1,
        "Неправильная категория": 0,
    }

    result = count_transactions_by_category(transactions, categories)

    assert result == expected_result


if __name__ == "__main__":
    test_count_transactions_by_category()
    print("Все тесты пройдены успешно!")