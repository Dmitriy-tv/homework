import logging
import os.path
from typing import Union

logger = logging.getLogger("masks")
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "../logs", "masks.log"), mode="w"
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
logger.setLevel(logging.ERROR)


def get_mask_card_number(card_num: Union[str, int]) -> Union[str]:
    """Скрывает часть введенного номера карты"""
    if not card_num:
        logger.error("Номер карты пустой")
        return "0"
    elif len(card_num) != 16:
        logger.error("Не верно введен номер карты")
        return "Не верно введен номер карты"
    else:
        logger.info("Выполняется маскировка номера карты")
        return f"{card_num[:4]} {card_num[4:6]}** **** {card_num[-4:]}"


print(get_mask_card_number(input("Введите номер карты")))


def get_mask_account(account_num: Union[str, int]) -> Union[str]:
    """Оставляет последние 4 цифры номера счета"""
    if not account_num:
        logger.error("Номер счета пустой")
        return "0"
    elif len(account_num) != 20:
        logger.error("Не верно введен номер счета")
        return "Не верно введен номер счета"
    else:
        logger.info("Выполняется маскировка номера счета")
        return f"**{account_num[-4:]}"


print(get_mask_account(input("Введите номер счета")))
