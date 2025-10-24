nimi=input("mis su nimi on ")
N=int(input("mitu korda soovid tervitust saada? "))
for i in range(1, N+1):
    print(f"Tere {nimi}! See on sinu {i}. tervitus.")

i=1
while True:
    print(f"Tere {nimi}! See on sinu {i}. tervitus.")
    i+=1
    if i>N: break

i=1
while i<=N:
    print(f"Tere {nimi}! See on sinu {i}. tervitus.")
    i+=1









from random import*
tehe=input(" kas tahad trenni teha")
if tehe == "jah":
    print("tuleb trenn!")
    mitu- int(input("mitu ulessannet"))
    for i in range(mitu):
        print("teeme ulessande", i + 1)
        print("trenn tehtud!")
        arv1=randint(1,100)
        arv2=randint(1,100)
        print(f"{arv1} + {arv2}")

        vastus=float(input("="))
        if vastus == arv1 + arv2:
            print("oige vastus")
            
else:
    print("ei tule trenni")
    




    import random
numbrid = ""
for i in range(5):
    number = random.randint(0, 9)
    numbrid += str(number)
print(numbrid)





for i in range(1, 11):
    print(i)

print("\nKorrutustabel:")

for i in range(1, 11):
    for j in range(1, 11):
        tulemus = i * j
        print(f"{i} x {j} = {tulemus}")
    print()





    summa=0
korda=0

while True:
    try:
        print(summa)
        arv=float(input("sisesta arv: "))
        if arv=="":
            break

        summa+=arv
        korda+=1

        if korda>=10:
            break
    except:
        print("Palun sisesta kehtiv arv")
        if arv=="":
            break






        nimesid = []
arv = int(input())

for i in range(arv):
    nimi = input()
    nimesid.append(nimi)

koige_pikem = max(nimesid, key=len)
koige_luhim = min(nimesid, key=len)

print(koige_pikem)
print(koige_luhim)








katsete_arv = 0
while True:
    print("Osta elevant ära!")
    vastus = input()
    katsete_arv += 1
    if vastus.lower() == "elevant":
        break
print(f"Küsimus esitati {katsete_arv} korda.")