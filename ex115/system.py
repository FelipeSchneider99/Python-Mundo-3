from ex115.lib.interface import *
from ex115.lib.file import *
from time import sleep


fi = 'records.txt'

if not file_exist(fi):
    create_file(fi)

while True:
    try:
        answer = menu(['View Registered People', 'Register New Person', 'Exit System'])
        if answer == 1:
            # Option to list file contents.
            read_file(fi)
        elif answer == 2:
            # Option to register a person.
            title('NEW REGISTRATION')
            name = str(input('NAME: ')).title().strip()
            age = int(input('AGE: '))
            register(fi, name, age)
        elif answer == 3:
            # Option to exit the system.
            title('Exiting the System...')
            break
        else:
            print('\033[31mERROR! Enter a valid option.\033[m')
        sleep(1.5)
    except KeyboardInterrupt:
        print(f'{RED}The user chose not to enter the option.{RESET}')
        break