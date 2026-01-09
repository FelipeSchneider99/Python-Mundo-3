from ex108_109 import currency

p = float(input('Enter the price: R$'))
print(f'The half of {currency.currency(p)} is {currency.half(p, True)}')
print(f'The double of {currency.currency(p)} is {currency.double(p, True)}')
print(f'Increasing 10%, we got {(currency.increase(p, 10, True))}')
print(f'Decreasing 13%, we got {(currency.decrease(p, 13, True))}')