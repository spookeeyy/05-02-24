algus = int(input("Sisestage esimene arv: "))
lõpp = int(input("Sisestage teine arv: "))
korrutis = 1
for i in range(algus, lõpp, 2):
    print(i)
    korrutis *= 1
print("Korrutis on " +str(korrutis))