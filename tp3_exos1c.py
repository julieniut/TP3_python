vs10=0
vi=0
vs15=0
for i in range(10):
    n=int(input("une valeur en 0 entre 20"))
    while n<0 or n>20:
        n = int(input("une valeur incorrete, entrez une valeur en 0 et 20"))
    if n<10:
         vi=vi+1
    elif n>10 or n<15:
         vs10=vs10+1
    else:
         vs15=vs15+1

print(vi,"valeurs inférieur strictement à 10",vs10,"valeurs inférieur strictement à 10",vs15,"valeurs inférieur strictement à 10")