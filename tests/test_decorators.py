import pytest

from src.decorators import log


def test_log_captured(capsys) -> None:
    @log()
    def my_function(x: int, y: int) -> int:
        """Функция суммирует два числа и возвращает результат"""
        return x + y
    my_function(1, 2)
    captured = capsys.readouterr()
    assert 'my_function ok' in captured.out


# Тестирование ошибки
def test_my_function_error(capsys):
    @log()
    def faulty_function(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        faulty_function(1, 0)
    captured = capsys.readouterr()
    assert "faulty_function error" in captured.out
