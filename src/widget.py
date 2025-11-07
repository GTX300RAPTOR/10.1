from datetime import datetime


def get_date(date_string: str) -> str:
    """
    Преобразует строку даты из формата "YYYY-MM-DDTHH:MM:SS.ffffff" в формат "DD.MM.YYYY".

    Аргументы:
        date_string: Строка, представляющая дату в формате "YYYY-MM-DDTHH:MM:SS.ffffff".

    Возвращает:
        Строка, представляющая дату в формате "DD.MM.YYYY".

    Примеры:
        >>> get_date("2024-03-11T02:26:18.671407")
        '11.03.2024'
    """
    date_object = datetime.fromisoformat(
        date_string.replace("Z", "+00:00"))
    return date_object.strftime("%d.%m.%Y")
