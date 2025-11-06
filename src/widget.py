from datetime import datetime


def get_date(date_string: str) -> str:
    """
    Converts a date string from the format "YYYY-MM-DDTHH:MM:SS.ffffff"
    to the format "DD.MM.YYYY".

    Args:
        date_string: A string representing the date in the format
                     "YYYY-MM-DDTHH:MM:SS.ffffff".

    Returns:
        A string representing the date in the format "DD.MM.YYYY".

    Examples:
        >>> get_date("2024-03-11T02:26:18.671407")
        '11.03.2024'
    """
    date_object = datetime.fromisoformat(
        date_string.replace("Z", "+00:00"))
    return date_object.strftime("%d.%m.%Y")
