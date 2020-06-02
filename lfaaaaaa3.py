from collections import defaultdict
import string

f = open("in.txt", "r")
productii = dict()
for i in f.readline().split():
    productii.update({i: []})
for i in f.readlines():
    i = i.split()
    for j in range(1, len(i)):
        productii.setdefault(i[0], []).append(i[j])

# ----- PASUL 1 i)
for i in productii.keys():
    aux = productii.get(i)
    if aux == ['lambda']:
        productii.update({i: []})
        for j in productii.keys():
            p = 0
            for k in productii[j]:
                if i in k and len(k) == 1:
                    productii[j][p] = 'lambda'
                elif i in k:
                    productii[j][p] = k.replace(i, "")
                p += 1
productii = {k: v for k, v in productii.items() if v}

# ------- PASUL 1 ii)
for i in productii.keys():
    aux = productii.get(i)
    if 'lambda' in aux:
        p = 0
        for z in range(len(aux)):
            if aux[z] == 'lambda':
                productii[i][p] = aux[z].replace('lambda', "")
                p -= 1
            p += 1
        for q in productii.values():
            if '' in q:
                q.remove('')
        for j in productii.keys():
            for k in range(len(productii[j])):
                if i in productii[j][k] and len(productii[j][k]) != 1:
                    if productii[j][k].replace(i, i) not in productii[j]:
                        productii[j].append(productii[j][k].replace(i, i))
                    productii[j].append(productii[j][k].replace(i, ''))
to_remove = []

# -------- PASUL 2
for i in reversed(productii.keys()):
    aux = productii.get(i)
    for j in reversed(productii.keys()):
        if i in productii[j]:
            for k in range(len(aux)):
                productii[j].append(productii[i][k])
            for m in range(len(productii[j])):
                if i == productii[j][m]:
                    productii[j][m] = i.replace(i, '')
            ok = 0
            for y in productii.values():
                for q in range(len(y)):
                    if i in y[q] and len(y[q]) != 1:
                        ok = 1
            if ok == 0:
                to_remove.append(i)
            for q in productii.values():
                if '' in q:
                    q.remove('')
for i in to_remove:
    productii.pop(i)

productie1 = list(productii.keys())

# --------- PASUL 3
p = 0
for i in productie1:
    for j in range(len(productii[i])):
        if productii[i][j].isupper() == False and len(productii[i][j]) > 1:
            for k in productii[i][j]:
                if k.islower() == True:
                    productii.update({chr(51 + p): []})
                    productii[chr(51 + p)].append(k)
                    productii[i][j] = productii[i][j].replace(k, chr(51 + p))
                    p += 1

# --------- PASUL 4
p = 0
productie1 = []
while productie1 != list(productii.keys()):
    productie1 = list(productii.keys())
    for i in productie1:
        for j in range(len(productii[i])):
            if len(productii[i][j]) > 2:
                productii[i].append(productii[i][j][0] + chr(33 + p))
                productii.update({chr(33 + p): [productii[i][j][1:]]})
                productii[i][j] = productii[i][j].replace(productii[i][j], '')
                p += 1
            for q in productii.values():
                if '' in q:
                    q.remove('')

print(productii)


def cykFun(substr, productii, cyk, x):
    rez = set()
    for z in range(x - 1):
        var1 = cyk[substr[:z + 1]]
        var2 = cyk[substr[z + 1:]]
        for var in [x + y for x in var1 for y in var2]:
            for key in productii:
                if var in productii[key]:
                    rez.add(key)
    cyk[substr] = rez
    return cyk


cyk = defaultdict(set)
string = input("Introduceti cuvantul: ")

for x in range(1, len(string) + 1):
    for y in range(len(string) + 1 - x):
        substr = (string[y:y + x])
        if x == 1:
            for key in productii.keys():
                if substr in productii[key]:
                    cyk[substr].add(key)
        else:
            cyk = cykFun(substr, productii, cyk, x)

print("Apartine" if cyk[string] else "NU Apartine")
