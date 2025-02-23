from typing import Union


def get_mask_card_number(card_num: Union[str, int]) -> Union[str]:
    """Скрывает часть введенного номера карты"""
    if len(card_num) != 16:
        return "Не верно введен номер карты"
    else:
        return f"{card_num[:4]} {card_num[4:6]}** **** {card_num[-4:]}"


# print(get_mask_card_number(input("Введите номер карты")))


def get_mask_account(account_num: Union[str, int]) -> Union[str]:
    """Оставляет последние 4 цифры номера счета"""
    if len(account_num) != 20:
        return "Не верно введен номер счета"
    else:
        return f"**{account_num[-4:]}"


# print(get_mask_account(input("Введите номер счета")))
