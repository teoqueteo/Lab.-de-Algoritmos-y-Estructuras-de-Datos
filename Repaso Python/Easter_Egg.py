import random

def cumpleaños_aleatorios(n):
    """Devuelve una lista de n cumpleaños aleatorios (días del 1 al 365)."""
    return [random.randint(1, 365) for _ in range(n)]

def hay_cumpleaños_repetido(cumples):
    """Devuelve True si al menos dos cumpleaños se repiten."""
    return len(cumples) != len(set(cumples))

def simular_paradoja(n, repeticiones=10000):
    """Simula la paradoja del cumpleaños para n personas."""
    coincidencias = 0
    for _ in range(repeticiones):
        cumples = cumpleaños_aleatorios(n)
        if hay_cumpleaños_repetido(cumples):
            coincidencias += 1
    probabilidad = coincidencias / repeticiones
    return probabilidad

print("n\tProbabilidad de al menos un cumpleaños compartido")
for n in range(5, 105, 5):
    prob = simular_paradoja(n)
    print(f"{n}\t{prob:.3f}")
