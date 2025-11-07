from typing import Any, Dict, List
from datetime import datetime


def filter_by_state(transactions: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Фильтрует список банковских транзакций по заданному статусу.

    Аргументы:
        transactions: Список словарей, представляющих банковские транзакции.
        state: Статус транзакции для фильтрации (по умолчанию: 'EXECUTED').

    Возвращает:
        Новый список словарей, содержащий только транзакции с указанным статусом.
    """
    filtered_transactions: List[Dict[str, Any]] = [
        transaction for transaction in transactions if transaction.get('state') == state
    ]
    return filtered_transactions


def sort_by_date(transactions: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список банковских транзакций по дате.

    Аргументы:
        transactions: Список словарей, представляющих банковские транзакции.
        reverse: Определяет порядок сортировки:
            - True (по умолчанию): по убыванию (самые новые в начале).
            - False: по возрастанию (самые старые в начале).

    Возвращает:
        Новый список словарей, отсортированный по дате.
    """
    sorted_transactions: List[Dict[str, Any]] = sorted(
        transactions,
        key=lambda transaction: datetime.fromisoformat(transaction['date']),
        reverse=reverse
    )
    return sorted_transactions
