'''
Crie um código em Python que teste se o site da Castleform está acessível a partir do seu computador.
'''

import urllib.request

URL = 'https://castelform.pt/'

try:
    tenta = urllib.request.urlopen(URL) # 200

except Exception as e:
    print(repr(e))

else:
    print(repr(tenta))
