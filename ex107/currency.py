def currency(price = 0, currency = 'R$'):
    return f'{currency}{price:.2f}'.replace('.', ',')


def half(price = 0, format = False):
    hf = price / 2
    return currency(hf) if format else hf


def double(price = 0, format = False):
    doub = price * 2
    return currency(doub) if format else doub


def increase(price = 0, much = 0, format = False):
    inc = price + (price * much / 100)
    return currency(inc) if format else inc


def decrease(price = 0, much = 0, format = False):
    dec = price - (price * much / 100)
    return currency(dec) if format else dec
