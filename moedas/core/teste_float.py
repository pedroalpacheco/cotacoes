def retponto(valor):
    return valor.replace(",",".")

lista = ['3,2788', '3,2788', '2,350', '3,2892']

listafloat = []

for x in lista:
    svirg = retponto(x)
    numfl = float(svirg)
    listafloat.append(numfl)
print(listafloat)

