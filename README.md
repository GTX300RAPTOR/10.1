# Виджет банковских операций клиента

Этот проект представляет собой виджет для обработки и отображения информации о банковских операциях клиента с целью, например, визуализации статистики расходов, формирования отчетов или интеграции в другие финансовые инструменты. Он включает в себя функции для фильтрации операций по статусу и сортировки по дате. Разработка ведётся по GitFlow с использованием линтеров и статического анализа кода для обеспечения высокого качества и поддерживаемости.

## Зависимости

Для работы проекта необходимы:

*   Python 3.10+
*   pip
*   Git

Необходимые Python-пакеты:

*   `pytest` (для тестирования)
*   `mypy` (для статической проверки типов)
*   `flake8` (для линтинга кода)

## Установка

1.  **Клонирование репозитория:**

    ```bash
    git clone <https://github.com/GTX300RAPTOR/10.1.git>
    cd PythonProject1
    ```

2.  **Создание и активация виртуального окружения (рекомендуется):**

    ```bash
    python -m venv .venv
    # Windows:
    .venv\Scripts\activate
    # macOS и Linux:
    source .venv/bin/activate
    ```

3.  **Установка зависимостей:**

    ```bash
    pip install pytest mypy flake8
    ```

## Использование

### Модуль `processing`

Модуль `src/processing.py` содержит функции для обработки данных о банковских операциях.

*   **`filter_by_state(transactions: list[dict], state: str = 'EXECUTED') -> list[dict]`**

    Фильтрует список транзакций по указанному статусу (`state`).  Возвращает новый список, содержащий только транзакции с совпадающим статусом.  По умолчанию фильтрует по статусу `'EXECUTED'`.

    **Пример:**

    ```python
    from src.processing import filter_by_state

    transactions = [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-10-26'},
        {'id': 2, 'state': 'PENDING', 'date': '2023-10-27'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-10-28'}
    ]

    executed_transactions = filter_by_state(transactions)
    print(executed_transactions)

    # Output: [{'id': 1, 'state': 'EXECUTED', 'date': '2023-10-26'}, {'id': 3, 'state': 'EXECUTED', 'date': '2023-10-28'}]

    canceled_transactions = filter_by_state(transactions, state='PENDING')
    print (canceled_transactions)
    # Output: [{'id': 2, 'state': 'PENDING', 'date': '2023-10-27'}]
    ```

*   **`sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]`**

    Сортирует список транзакций по дате. Возвращает новый список, отсортированный по дате в указанном порядке.  По умолчанию сортирует в обратном порядке (от новых к старым).

    **Пример:**

    ```python
    from src.processing import sort_by_date

    transactions = [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-10-28'},
        {'id': 2, 'state': 'PENDING', 'date': '2023-10-26'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-10-27'}
    ]

    sorted_transactions = sort_by_date(transactions)
    print( sorted_transactions )
    # Output: [{'id': 1, 'state': 'EXECUTED', 'date': '2023-10-28'}, {'id': 3, 'state': 'EXECUTED', 'date': '2023-10-27'}, {'id': 2, 'state': 'PENDING', 'date': '2023-10-26'}]

    ascending_transactions = sort_by_date(transactions, reverse=False)
    print(ascending_transactions)
    # Output: [{'id': 2, 'state': 'PENDING', 'date': '2023-10-26'}, {'id': 3, 'state': 'EXECUTED', 'date': '2023-10-27'}, {'id': 1, 'state': 'EXECUTED', 'date': '2023-10-28'}]
    ```

## Запуск тестов

bash
pytest tests/


## Линтинг и проверка типов

bash
flake8 src/ tests/
mypy src/ tests/


## Структура веток GitFlow

*   `main`: Основная ветка с релизным кодом.
*   `develop`: Ветка разработки, в которую интегрируются все новые фичи.
*   `feature/*`: Ветки для разработки отдельных фич (например, `feature/homework_10_1`).  Ветки `feature` сливаются в `develop`.
*   `release/*`: Ветки для подготовки релизов.  Используются для стабилизации кода перед выпуском.
*   `hotfix/*`: Ветки для срочного исправления ошибок в production-коде.

## Лицензия

------------?.

## Автор

*   GTX300Raptor