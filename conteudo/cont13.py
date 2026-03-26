#importando funcionalidades específicas
from math import sqrt, floor, ceil
num = int(input('Digite um número: ' ))
raiz = sqrt(num)
print('a raiz de {} é igual a {}'.format(num, ceil(raiz))) #arredonda pra cima
print('a raiz de {} é igual a {}'.format(num, floor(raiz)))
