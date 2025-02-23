import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "value, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456"),
        ("0987654321123456", "0987 65** **** 3456"),
        ("6543210987431678", "6543 21** **** 1678"),
        ("9120384756152749", "9120 38** **** 2749")
    ]
)
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize(
    "input_error, result",
    [
        ("", "Не верно введен номер карты"),
        ("654321098743167865431678", "Не верно введен номер карты"),
        ("0987654321", "Не верно введен номер карты"),
        ("Visa", "Не верно введен номер карты"),
        ("Visa Classic", "Не верно введен номер карты")
    ]
)
def test_get_mask_card_number_invalid(input_error, result):
    assert get_mask_card_number(input_error) == result


@pytest.mark.parametrize(
    "input_user, conclusion",
    [
        ("70007922896063610153", "**0153"),
        ("12345678901298143456", "**3456"),
        ("09876543212683123456", "**3456"),
        ("65432101038987431678", "**1678"),
        ("91203847184656152749", "**2749")
    ]
)
def test_get_mask_account(input_user, conclusion):
    assert get_mask_account(input_user) == conclusion


@pytest.mark.parametrize(
    "input_user_error, conclusion_error",
    [
        ("", "Не верно введен номер счета"),
        ("654321098743167865431678", "Не верно введен номер счета"),
        ("0987654321", "Не верно введен номер счета"),
        ("Visa", "Не верно введен номер счета"),
        ("Visa Classic", "Не верно введен номер счета")
    ]
)
def test_get_mask_account_invalid(input_user_error, conclusion_error):
    assert get_mask_account(input_user_error) == conclusion_error
