from typing import Union


def get_mask_card_number(card_num: Union[str]) -> Union[str]:
    """Скрывает часть введенного номера карты"""

    return f"{card_num[:4]} {card_num[4:6]}** **** {card_num[-4:]}"


# print(get_mask_card_number(input("Введите номер карты")))


def get_mask_account(account_num: Union[str]) -> Union[str]:
    """Оставляет последние 4 цифры номера счета"""

    return f"**{account_num[-4:]}"


# print(get_mask_account(input("Введите номер счета")))
