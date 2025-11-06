def mask_account_card(account_info: str) -> str:
    """
    Masks card or account numbers in a string.

    Args:
        account_info: A string containing the card type and number
                      (e.g., "Visa Platinum 7000792289606361" or "Счет 73654108430135874305").

    Returns:
        A string with the masked card or account number.  Returns the original
        string if the input format is invalid.

    Examples:
        >>> mask_account_card("Visa Platinum 7000792289606361")
        'Visa Platinum 7000 79** **** 6361'

        >>> mask_account_card("Счет 73654108430135874305")
        'Счет **4305'
    """
    try:
        parts = account_info.split()
        if len(parts) < 2:
            return account_info  # Return original if invalid format

        account_type = parts[0].lower()
        account_number = parts[1]

        if account_type == "счет" or account_type == "счёт":
            masked_number = "**" + account_number[-4:]  # Mask account number
        else:
            masked_number = f"{account_number[:4]} {account_number[4:6]}** **** {account_number[12:]}"

        return f"{parts[0]} {masked_number}"

    except (IndexError, ValueError):
        return account_info  # Return original if an error occurs
