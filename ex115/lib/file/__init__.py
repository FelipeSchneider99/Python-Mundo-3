from ex115.lib.interface import *

def file_exist(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def create_file(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('There was an error creating the file')
    else:
        print(f'File {name} created successfully')

def read_file(name):
    try:
        a = open(name, 'rt')
    except:
        print('Error reading the file.')
    else:
        title('REGISTERED PEOPLE')
        for line in a:
            data = line.split(';')
            if len(data) >= 2:
                data[1] = data[1].replace('\n', '')
                print(f'{data[0]:<30}{data[1]:>3} years')
            else:
                pass
    finally:
        a.close()

def register(fi, name='Unknown', age=0):
    try:
        a = open(fi, 'at')
    except:
        print('There was an ERROR opening the file.')
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            print('There was an ERROR writing the data.')
        else:
            print(f'New record for {name} added successfully.')
            a.close()
