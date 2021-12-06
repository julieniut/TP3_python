import random

x=random.randint(0,100)
nombre=0
essaye=int(input("deviner le chiffre qui est compris entre 0 à 100"))

while(x!=essaye):
    nombre +=1
    essaye = int(input("deviner le chiffre qui est compris entre 0 à 100 "))
    if(x<essaye):
        print("inférieur")

    else:print("supérieur")


if (x==essaye):
    print("vous avez trouvez ",x)
    print("en", nombre,"essaye")


