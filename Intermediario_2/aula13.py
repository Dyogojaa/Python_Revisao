# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n #pausa a execução da função
        n += 1

        if n >= maximum:
            return # encera a função


gen = generator(maximum=1000)
for n in gen:
    print(n)