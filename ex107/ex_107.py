import currency

p = float(input('Enter the price: R$'))
print(f'The half of {p} is R${currency.half(p)}')
print(f'The double of {p} is R${currency.double(p)}')
print(f'Increasing 10%, we got R${currency.increase(p, 10)}')
print(f'Decreasing 13%, we got R${currency.decrease(p, 13)}')