import json
import os.path
from typing import List
from venv import logger

from src.external_api import currency_conversion


def data_transactions(way: str) -> List[dict]:
    """
    Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях.
    """
    try:
        logger.info("Открытие JSON-файла")
        with open(way, "r", encoding="utf-8") as date_json:
            try:
                logger.info("Получение списка данными о финансовых транзакциях")
                list_data_transactions = json.load(date_json)
                return list_data_transactions
            except json.decoder.JSONDecodeError:
                logger.error("Ошибка обработки файла")
                print("Ошибка обработки файла")
                return []
    except FileNotFoundError:
        logger.error("JSON-файла не найден")
        return []  # instead of return False


current_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_dir, "../data", "operations.json")
list_transactions = data_transactions(json_file_path)


def transaction_amount(txn: dict) -> float:
    """Функция, которая выводит сумму транзакции"""

    if not txn:
        logger.info("Транзакция не найдена")
        return 0.0

    if "operationAmount" in txn:
        currency = txn["operationAmount"]["currency"]["code"]
        if currency == "RUB":
            logger.info(f"Вывод суммы транзакции, если код валюты {currency}")
            return txn["operationAmount"]["amount"]
        elif currency != "RUB":
            logger.info(f"Вывод суммы транзакции, если код валюты {currency}")
            return currency_conversion(currency, txn["operationAmount"]["amount"])
    logger.info("Нет ключа 'operationAmount' в транзакции")
    return 0.0
