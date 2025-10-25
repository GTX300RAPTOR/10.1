from datetime import datetime


def get_date(date_string: str) -> str:
    """
    Преобразует строку даты из формата "ГГГГ-ММ-ДДTHH:MM:SS.ffffff" в формат "ДД.ММ.ГГГГ".

    Аргументы:
        date_string: Строка, представляющая дату в формате "ГГГГ-ММ-ДДTHH:MM:SS.ffffff".

    Возвращает:
        Строка, представляющая дату в формате "ДД.ММ.ГГГГ".

    Примеры:
        >>> get_date("2024-03-11T02:26:18.671407")
        '11.03.2024'
    """
    date_object = datetime.fromisoformat(date_string.replace("Z", "+00:00"))
    return date_object.strftime("%d.%m.%Y")


if __name__ == "__main__":
    print(get_date("2025-10-20T02:26:18.671407"))
