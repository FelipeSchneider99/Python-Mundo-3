from ex112.utilitiesCeV import currency, data
p = data.read_money('Enter the price: R$')
currency.summary(p, 35, 22)