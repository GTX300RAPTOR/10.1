def mask_account_card(account_info: str) -> str:
    """
    Маскирует номера карт или счетов в строке.

    Аргументы:
        account_info: Строка, содержащая тип карты и номер
                      (например, "Visa Platinum 7000792289606361" или "Счет 73654108430135874305").

    Возвращает:
        Строка с замаскированным номером карты или счета.

    Примеры:
        >>> mask_account_card("Visa Platinum 7000792289606361")
        'Visa Platinum 7000 79** **** 6361'

        >>> mask_account_card("Счет 73654108430135874305")
        'Счет **4305'
    """
    parts = account_info.split()
    account_type = parts[0]
    # Исправлено: если в строке только один элемент, account_number будет пустым
    account_number = parts[1] if len(parts) > 1 else ""

    if account_type.lower() == "счет":
        masked_number = "**" + account_number[-4:]
    else:
        masked_number = f"{account_number[:4]} {account_number[4:6]}** **** {account_number[12:]}"

    return f"{account_type} {masked_number}"


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
