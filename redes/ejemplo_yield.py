"""
Ejemplo de uso de yield en Python.

yield se puede traducir como "ceda el paso".  (ahora le llaman "uno por uno")
"""

def fibonacci_lista(n: int) -> list:
    """Devuelve cada valor de fibonacci antes de n. n > 2.
    1 1 2 3 5 8 13 ...
    """
    if n < 2:
        return [1]
    else:
        lista = [1,1]
        for i in range(n-2):
            lista.append(lista[-1]+lista[-2])
        return lista

def fibonacci_generador(n: int) -> int:
    a = 1
    b = 1
    if n > 0:
        yield a
    if n > 1:
        yield b
    for i in range(n-2):
        a, b = b, a+b
        yield b

for i in fibonacci_generador(10):
    pass
print(i)
