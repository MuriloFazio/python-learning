stop_number = int(input('Digite um número para a sequencia Fibonacci: '))

fibonacci_sequence = []
fibonacci = 0
first = 1
second = 0
aux = 0

for index in range(stop_number):
    print(fibonacci)
    fibonacci_sequence.append(fibonacci)
    fibonacci = first + second
    first = second
    second = fibonacci
    

print(fibonacci_sequence)


