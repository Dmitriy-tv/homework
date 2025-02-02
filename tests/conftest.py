import pytest

from src.processing import sort_by_date


@pytest.fixture
def fixture_filter_by_state():
    return 'EXECUTED'


@pytest.fixture
def fixture_sort_by_date():
    return sort_by_date

