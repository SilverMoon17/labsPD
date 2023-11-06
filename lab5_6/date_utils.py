from datetime import datetime, timedelta

def is_leap_year(year):
    """
    Проверяет, является ли год високосным.

    Параметры:
    year (int): Год, который нужно проверить.

    Возвращает:
    bool: True, если год високосный, иначе False.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_between_dates(date1, date2):
    """
    Рассчитывает разницу в днях между двумя датами.

    Параметры:
    date1 (str): Первая дата в формате 'YYYY-MM-DD'.
    date2 (str): Вторая дата в формате 'YYYY-MM-DD'.

    Возвращает:
    int: Количество дней между датами. Если первая дата идет после второй,
         возвращается отрицательное число.
    """
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    delta = d2 - d1
    return delta.days

def get_current_date(format="%Y-%m-%d"):
    """
    Возвращает текущую дату в заданном формате.

    Параметры:
    format (str): Строка формата, в котором должна быть возвращена текущая дата.

    Возвращает:
    str: Текущая дата в заданном формате.
    """
    return datetime.now().strftime(format)

def add_days_to_date(date_str, days, date_format="%Y-%m-%d"):
    """
    Добавляет заданное количество дней к дате.

    Параметры:
    date_str (str): Дата, к которой нужно добавить дни, в виде строки.
    days (int): Количество дней для добавления.
    date_format (str): Формат даты входной строки.

    Возвращает:
    str: Новая дата после добавления указанного количества дней.
    """
    date = datetime.strptime(date_str, date_format)
    new_date = date + timedelta(days=days)
    return new_date.strftime(date_format)

def has_date_passed(target_date, date_format="%Y-%m-%d"):
    """
    Проверяет, наступила ли уже заданная дата по сравнению с текущей датой.

    Параметры:
    target_date (str): Дата для проверки.
    date_format (str): Формат даты входной строки.

    Возвращает:
    bool: True если заданная дата уже наступила, иначе False.
    """
    current_date = datetime.now()
    check_date = datetime.strptime(target_date, date_format)
    return current_date >= check_date

