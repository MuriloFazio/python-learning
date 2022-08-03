
number = int(input("Digite o numero que deseja a tabuada: "))
multiplo = 0 
print(f"TABUADA DE {number}")
for i in range(1,11): 
    multiplo += 1 
    print(f"{number} x {multiplo} = {number * i}")