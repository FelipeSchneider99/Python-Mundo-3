RED = '\033[31m'
YELLOW = '\033[93m'
BLUE = '\033[34m'
RESET = '\033[0m'

def read_int(msg):
    while True:
        try:
            num = int(input(msg))
        except ValueError:
            print(f'{RED}ERROR! Enter a valid option.{RESET}')
            continue
        else:
            return num


def line(size = 45):
    return '-' * size


def title(txt):
    print(line())
    print(txt.center(45))
    print(line())


def menu(list):
    title('MAIN MENU')
    c = 1
    for item in list:
        print(f'{YELLOW}{c} -{RESET} {BLUE}{item}{RESET}')
        c += 1
    print(line())
    opc = read_int('Option: ')
    return opc
