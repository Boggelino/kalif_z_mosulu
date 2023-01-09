def kalif(poc_ludu, n):
    hraci = []
    for i in range(poc_ludu):
        hraci.append(i+1)
    while len(hraci) > 1:
        hraci = hraci[n-1:] + hraci[:n-1]
        hraci.pop(0)
    return hraci[0]

poc_ludu = int(input("Počet ľudu na smrteľnú hru: "))
n = int(input("Každého ktorého človeka mám streliť: "))

prezil = kalif(poc_ludu, n)
print("Prežil človek s číslom:", prezil)