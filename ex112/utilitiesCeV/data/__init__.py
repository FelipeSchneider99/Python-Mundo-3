def read_money(msg):
    while True:
        inp = input(msg).replace(',','.').strip()
        try:
            return float(inp)
        except ValueError:
            print(f'\033[0;31mERROR: \"{inp}\" is not a valid price\033[m')