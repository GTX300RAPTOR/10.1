def mask_account_card(account_info: str) -> str:
    """
    Маскирует номера карт или счетов в строке.

    Аргументы:
        account_info: Строка, содержащая тип карты и номер
                      (напр., "Visa Platinum 7000792289606361" или "Счет 73654108430135874305").

    Возвращает:
        Строка с замаскированным номером карты или счета.  Возвращает исходную
        строку, если формат ввода некорректен.

    Примеры:
        >>> mask_account_card("Visa Platinum 7000792289606361")
        'Visa Platinum 7000 79** **** 6361'

        >>> mask_account_card("Счет 73654108430135874305")
        'Счет **4305'
    """
    try:
        parts = account_info.split()
        if len(parts) < 2:
            return account_info  # Возвращаем оригинал, если некорректный формат

        account_type = parts[0].lower()
        account_number = parts[1]

        if account_type == "счет" or account_type == "счёт":
            masked_number = "**" + account_number[-4:]  # Маскируем номер счета
        else:
            masked_number = f"{account_number[:4]} {account_number[4:6]}** **** {account_number[12:]}"

        return f"{parts[0]} {masked_number}"

    except (IndexError, ValueError):
        return account_info  # Возвращаем оригинал при возникновении ошибки
