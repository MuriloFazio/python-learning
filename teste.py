# TODO 
#contabilizar lista (pares e impares)
#printar numero de pares e impares

numbers = []
for i in range (10):
    number = int(input("Digite um numero "))
    numbers.append(number)
    i += 1 

def odds_even(numbers):
    odds = 0
    even = 0 
    for number in numbers:
        if number % 2 == 0:
            odds += 1
        else:
            even += 1
    print(f"O numero de pares e {odds}, a quantidade de impare e {even}")

odds_even(numbers)



