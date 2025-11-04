from typing import Any, Dict, List


def filter_by_state(transactions: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Фильтрует список банковских транзакций по заданному статусу.

    Args:
        transactions: Список словарей, представляющих банковские транзакции.
        state: Статус транзакции для фильтрации (по умолчанию 'EXECUTED').

    Returns:
        Новый список словарей, содержащий только транзакции с указанным статусом.
    """
    filtered_transactions: List[Dict[str, Any]] = [
        transaction for transaction in transactions if transaction.get('state') == state
    ]
    return filtered_transactions


def sort_by_date(transactions: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список банковских транзакций по дате.

    Args:
        transactions: Список словарей, представляющих банковские транзакции.
        descending: Определяет порядок сортировки:
            - True (по умолчанию): по убыванию (сначала самые новые).
            - False: по возрастанию (сначала самые старые).

    Returns:
        Новый список словарей, отсортированный по дате.
    """
    sorted_transactions: List[Dict[str, Any]] = sorted(
        transactions,
        key=lambda transaction: transaction['date'],
        reverse=descending
    )
    return sorted_transactions


if __name__ == '__main__':
    # Пример использования функций
    transactions_data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

    # Пример использования filter_by_state
    executed_transactions = filter_by_state(transactions_data)
    print("Транзакции со статусом EXECUTED:")
    for transaction in executed_transactions:
        print(transaction)

    canceled_transactions = filter_by_state(transactions_data, state='CANCELED')
    print("\nТранзакции со статусом CANCELED:")
    for transaction in canceled_transactions:
        print(transaction)

    # Пример использования sort_by_date
    sorted_transactions_desc = sort_by_date(transactions_data)
    print("\nТранзакции, отсортированные по дате (убыванию):")
    for transaction in sorted_transactions_desc:
        print(transaction)

    sorted_transactions_asc = sort_by_date(transactions_data, descending=False)
    print("\nТранзакции, отсортированные по дате (возрастанию):")
    for transaction in sorted_transactions_asc:
        print(transaction)
