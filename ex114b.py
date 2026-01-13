import urllib.error
import urllib.request

try:
    url = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('The Pudim website is currently unavailable.')
else:
    print('Successfully accessed the Pudim website.')