# Cidade A vs Cidade B 2.0

city_a = int(input("Digite a populacao da Cidade A: "))
city_b = int(input("Digite a populacao da Cidade B: "))

# city_a cresce 3% e a city_b cresce 1,5%
#tempo para igualar ou passar o tamanho da pop
years = 0

while city_a < city_b:    
    city_a = city_a * 1.03
    city_b = city_b * 1.015
    years += 1

print(f"O tempo necessario para cidade a passar cidade b em tamanho sao: {years} anos")
