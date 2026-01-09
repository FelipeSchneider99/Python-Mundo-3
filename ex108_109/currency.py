def currency(price = 0, currency_symb = 'R$'):
    '''
        Formats a numeric value into a currency string with comma separation.
    :param price:The monetary value to format. Defaults to 0.
    :param currency_symb:The currency symbol to prepend. Defaults to 'R$'.
    :return:The formatted currency string (e.g., 'R$10,50')
    '''
    return f'{currency_symb}{price:.2f}'.replace('.', ',')


def half(price = 0, form = False):
    '''
        Calculates half of the given price.
    :param price:The base price. Defaults to 0.
    :param form:If True, returns the result formatted as a currency string.
                If False, returns the raw float value. Defaults to False.
    :return:Half of the price, either as a float or a formatted string.
    '''
    hf = price / 2
    return currency(hf) if form else hf


def double(price = 0, form = False):
    '''
        Calculates double of the given price.
    :param price: The base price. Defaults to 0.
    :param form:If True, returns the result formatted as a currency string.
                If False, returns the raw float value. Defaults to False.
    :return:Double of the price, either as a float or a formatted string.
    '''
    db = price * 2
    return currency(db) if form else db


def increase(price = 0, much = 0, form = False):
    '''
    Increases the price by a given percentage.
    :param price: The base price. Defaults to 0.
    :param much: The percentage to increase by (e.g., 10 for 10%). Defaults to 0.
    :param form:If True, returns the result formatted as a currency string.
                If False, returns the raw float value. Defaults to False.
    :return: The increased price, either as a float or a formatted string.
    '''
    inc = price + (price * much / 100)
    return currency(inc) if form else inc


def decrease(price = 0, much = 0, form = False):
    '''
    Decreases the price by a given percentage.
    :param price:The base price. Defaults to 0.
    :param much:The percentage to decrease by (e.g., 10 for 10%). Defaults to 0.
    :param form:If True, returns the result formatted as a currency string.
                If False, returns the raw float value. Defaults to False.
    :return: The decreased price, either as a float or a formatted string.
    '''
    dec = price - (price * much / 100)
    return currency(dec) if form else dec
