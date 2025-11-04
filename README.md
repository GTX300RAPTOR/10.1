# Bank Transactions Processor

This project provides functions for filtering and sorting bank transaction data.

## Installation

No specific installation is required.  Just clone the repository.

## Usage
python
from src.processing import filter_by_state, sort_by_date


transactions = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01T12:00:00'},
    {'id': 2, 'state': 'CANCELED', 'date': '2023-01-02T13:00:00'}
]


filtered_transactions = filter_by_state(transactions, 'EXECUTED')
sorted_transactions = sort_by_date(transactions)


print(filtered_transactions)
print(sorted_transactions)


## Author

GTX300Raptor