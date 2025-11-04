from src.processing import filter_by_state, sort_by_date
import pytest

transactions = [
    {'id': 3, 'state': 'EXECUTED', 'date': '2024-01-01T10:00:00'},
    {'id': 1, 'state': 'EXECUTED', 'date': '2024-01-01T08:00:00'},
    {'id': 2, 'state': 'EXECUTED', 'date': '2024-01-01T09:00:00'}
]


def test_filter_by_state():
    """Тест для проверки фильтрации транзакций по статусу."""
    filtered_transactions = filter_by_state(transactions, state='EXECUTED')
    assert all(transaction['state'] == 'EXECUTED' for transaction in filtered_transactions)


def test_sort_by_date():
    """Тест для проверки сортировки транзакций по дате."""
    sorted_transactions = sort_by_date(transactions)
    assert sorted_transactions[0]['id'] == 3


def test_sort_by_date_different_dates():
    """Тест для проверки сортировки транзакций с разными датами."""
    transactions_with_diff_dates = [
      {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-03T12:00:00'},
      {'id': 2, 'state': 'CANCELED', 'date': '2023-01-01T13:00:00'},
      {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-02T14:00:00'}
    ]
    sorted_transactions = sort_by_date(transactions_with_diff_dates)

    assert sorted_transactions[0]['id'] == 1
