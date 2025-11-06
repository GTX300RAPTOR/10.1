from typing import Any, Dict, List
from datetime import datetime


def filter_by_state(transactions: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Filters a list of bank transactions by the given state.

    Args:
        transactions: A list of dictionaries representing bank transactions.
        state: The transaction state to filter by (default: 'EXECUTED').

    Returns:
        A new list of dictionaries containing only transactions with the specified state.
    """
    filtered_transactions: List[Dict[str, Any]] = [
        transaction for transaction in transactions if transaction.get('state') == state
    ]
    return filtered_transactions


def sort_by_date(transactions: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Sorts a list of bank transactions by date.

    Args:
        transactions: A list of dictionaries representing bank transactions.
        reverse: Determines the sorting order:
            - True (default): descending (newest first).
            - False: ascending (oldest first).

    Returns:
        A new list of dictionaries sorted by date.
    """
    sorted_transactions: List[Dict[str, Any]] = sorted(
        transactions,
        key=lambda transaction: datetime.fromisoformat(transaction['date']),
        reverse=reverse
    )
    return sorted_transactions
