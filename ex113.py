RED = '\033[31m'
RESET = '\033[m'

def read_int(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print(f'{RED}ERROR! Enter a valid integer.{RESET}')
            continue
        except KeyboardInterrupt:
            print(f'{RED}The user chose not to enter this number.{RESET}')
            return 0
        else:
            return num

def read_float(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print(f'{RED}ERROR! Enter a valid decimal number.{RESET}')
            continue
        except KeyboardInterrupt:
            print(f'{RED}The user chose not to enter this number.{RESET}')
            return 0
        else:
            return num

integer_input = read_int('Enter an integer number: ')
float_input = read_float('Enter a decimal number: ')

print(f'The integer entered was {integer_input} and the decimal number was {float_input}')