import requests

RED = '\033[31m'
GREEN = '\033[32m'
RESET = '\033[m'

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        print(f'{RED}ERROR! Not able to connect to server.{RESET}')
    except requests.Timeout:
        print(f'{RED}ERROR! Timeout connecting to server.{RESET}')

url = 'https://pudim.com.br'
if check_website(url):
    print(f'{GREEN}Successfully accessed the website "{url}".{RESET}')
else:
    print(f'{RED}The website "{url}" is currently unavailable.{RESET}')