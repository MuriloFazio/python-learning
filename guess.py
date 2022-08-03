import random 

def guess (x):
    number = random.randint(1, x)
    guess = 0 
    while guess != number:
        guess = int(input(f"Chute um numero entre 1 e {x} \n"))
        if guess < number:
            print("ERROUUU, chuta mais alto!!")
        elif guess > number:
            print("ERROUUU, chuta mais baixo!!")

    print("Acertou miseravel")
guess(20)
