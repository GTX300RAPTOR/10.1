from src.processing import filter_by_state, sort_by_date


transactions = [
    {'id': 3, 'state': 'EXECUTED', 'date': '2024-01-01T10:00:00'},
    {'id': 1, 'state': 'EXECUTED', 'date': '2024-01-01T08:00:00'},
    {'id': 2, 'state': 'EXECUTED', 'date': '2024-01-01T09:00:00'}
]


def test_filter_by_state() -> None:
    """Тест для проверки фильтрации транзакций по статусу."""
    filtered_transactions = filter_by_state(transactions, state='EXECUTED')
    assert all(transaction['state'] == 'EXECUTED' for transaction in filtered_transactions)


def test_sort_by_date() -> None:
    """Тест для проверки сортировки транзакций по дате."""
    sorted_transactions = sort_by_date(transactions)
    # проверяем, что список отсортирован в обратном порядке по дате
    assert sorted_transactions[0]['date'] == '2024-01-01T10:00:00'
    assert sorted_transactions[1]['date'] == '2024-01-01T09:00:00'
    assert sorted_transactions[2]['date'] == '2024-01-01T08:00:00'


def test_sort_by_date_different_dates() -> None:
    """Тест для проверки сортировки транзакций с разными датами."""
    transactions_with_diff_dates = [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-03T12:00:00'},
        {'id': 2, 'state': 'CANCELED', 'date': '2023-01-01T13:00:00'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-02T14:00:00'}
    ]
    sorted_transactions = sort_by_date(transactions_with_diff_dates)

    # проверяем, что список отсортирован в обратном порядке по дате
    assert sorted_transactions[0]['date'] == '2023-01-03T12:00:00'
    assert sorted_transactions[1]['date'] == '2023-01-02T14:00:00'
    assert sorted_transactions[2]['date'] == '2023-01-01T13:00:00'


def test_sort_by_date_ascending() -> None:
    """Тест для проверки сортировки транзакций по дате в возрастающем порядке."""
    transactions_with_diff_dates = [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-03T12:00:00'},
        {'id': 2, 'state': 'CANCELED', 'date': '2023-01-01T13:00:00'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-02T14:00:00'}
    ]
    sorted_transactions = sort_by_date(transactions_with_diff_dates, reverse=False)

    # Проверяем, что список отсортирован в возрастающем порядке по дате
    assert sorted_transactions[0]['date'] == '2023-01-01T13:00:00'
    assert sorted_transactions[1]['date'] == '2023-01-02T14:00:00'
    assert sorted_transactions[2]['date'] == '2023-01-03T12:00:00'
