# Universidad del Valle de Guatemala
# Cifrado de Información
# Laboratorio 3
#
# Andrei Portales 19825
# Jose Javier Hurtarte 19707
# Christian Pérez 19710

import numpy
import random


# Hansel Rata 🐀


def linearGenerator(m, a, c, n):
    # a: multiplicador
    # m: modulo
    # c: corrimiento
    # n: cantidad de numeros a generar

    seed = round(random.random() * 100)
    randomNums = [0] * n
    randomNums[0] = seed

    for i in range(1, n):
        randomNums[i] = ((randomNums[i - 1] * a) + c) % m

    bits = ''.join(list(map(lambda x: '{0:08b}'.format(x), randomNums)))
    return bits


def wichmanGenerator(a, b, n):
    s1 = round(random.random() * 10000)
    s2 = round(random.random() * 10000)
    s3 = round(random.random() * 10000)
    m1 = 30269
    m2 = 30307
    m3 = 30323

    randomNums = []

    for i in range(1, n + 1):
        s1 = (171 * s1) % m1
        s2 = (172 * s2) % m2
        s3 = (170 * s3) % m3
        v = (s1 / m1 + s2 / m2 + s3 / m3) % 1
        randomNums.append(v)

    bits = ''.join(list(map(lambda x: '{0:08b}'.format(int(x * 100)), randomNums)))

    return bits
