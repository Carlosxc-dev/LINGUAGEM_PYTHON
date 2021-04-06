import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('o site pudim nao esta acessivel no momento')
else:
    print('consegui aceesar o site pudim com sucesso ')
    print(site.read()) # ver script do site 
