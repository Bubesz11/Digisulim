szamok=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

parosszamok = []
for i in szamok:
    if i % 2==0:
        print(i)
        parosszamok.append(i)
possz=len(parosszamok)
print(possz,"ennyi páros szám van")