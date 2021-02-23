#Pregunta 4.a: La funcion zip
'''def zip(a, b):
    if a and b:
        yield (a[0], b[0])
        for p in zip(a[1:], b[1:]):
            yield p

for p in zip([1, 2, 3], ['a', 'b', 'c']):
    print(p)'''

#Pregunta 4.a.ii: La funcion ZipWith (omg, es la que usamos en haskell :v)
def zipWith(a, b,funcion):
    if a and b:
        yield funcion(a[0], b[0])
        for p in zipWith(a[1:], b[1:],funcion):
            yield p

for p in zipWith([0, 1, 2, 1], [1, 2, 1, 0], lambda x,y: x+y):
    print(p)

#Pregunta 4.b: El misterio
'''def misterio(p):
    yield p
    acum = []
    for p in zipWith([0, *p], [*p, 0], lambda x, y: x + y):
        acum += [p]
    for m in misterio(acum):
        yield m

for m in misterio([0]):
    print(m)'''

#Pregunta 4.b.iii: El suspenso... CHAN CHAN CHAAAN
def suspenso(p):
    for i in p:
        yield i
    acum = []
    for p in zipWith([0, *p], [*p, 0], lambda x, y: x + y):
        acum += [p]
    for m in suspenso(acum):
        yield m

for m in suspenso([1]):
    print(m)