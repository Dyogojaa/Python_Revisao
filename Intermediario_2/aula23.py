import importlib

import aula22

print(aula22.variavel)

for i in range(10):
    importlib.reload(aula22)
    print(i)

print('Fim')