# Universidad del Valle de Guatemala
# Cifrado de Información
# Laboratorio 3
#
# Andrei Portales 19825
# Jose Javier Hurtarte 19707
# Christian Pérez 19710

import numpy as np
import random
import re
import matplotlib.pyplot as plt
from PIL import Image
from skimage.data import camera 
from functools import reduce

# Hansel Rata 🐀

# 
def linearGenerator(m, a, c, n):
    # a: multiplicador
    # m: modulo
    # c: corrimiento
    # n: cantidad de numeros a generar

    seed = round(random.random() * 100) % m
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

#Suponiendo que se alimenta el primero
def lfsr(seed,n,step = 1,positions = []):
    def nextStep(chain):
        step = chain[1:]
        return str(reduce(lambda i, j: int(i)^int(j), [chain[n] for n in positions])) + step
    result = ''
    current = '{0:b}'.format(seed)
    for x in range(n*step):
        current = nextStep(current)[-1]
        if (x%step) ==0:
            result += current
        
    return result


def img2bits(I):
    m, n = I.shape
    s = ''
    for i in range(0, m):
        for j in range(0, n):
            s = s + '{0:08b}'.format(I[i,j])
    return s

def bits2img(x, shape):
    m, n = shape
    I = np.zeros(m*n).astype(np.uint8)
    bts = re.findall('........', x)
    for i in range(0, len(bts)):
        I[i] = int(bts[i], 2)
    I = I.reshape(m,n)
    return I

# I = camera()
# J = Image.fromarray(I)
# J = J.resize((J.size[0]//2, J.size[1]//2), Image.LANCZOS)
# I = np.array(J)

# plt.figure()
# plt.imshow(I, cmap='gray')
# plt.show()