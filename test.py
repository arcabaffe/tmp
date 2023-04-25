def concat(L,t):
    for i in range(t//2):
        L[i] = L[i*2] + L[i*2+1]
    if t % 2 == 1:
        L[t//2] = L[t-1]
        return (L,t//2+1)
    return (L,t//2)

def concat_opti(L):
    t = len(L)
    while t != 1:
        (L,t) = concat(L,t)
    return L[0]

from time import *
deb3 = time()
oui = "um ah human huffman is fun i am a fan ha ha ha ha ha ha je suis alexandre aazpi"
oui2 = ""

#test concat opti

for i in range(100000):
    oui2 += oui
print(time()-deb3)
print("opti")
print("")

deb2 = time()
L = []
for i in range(100000):
    L.append(oui)
deb = time()
test = concat_opti(L)
print("time opti")
print(time()-deb)
print("time with append")
print(time()-deb2)
