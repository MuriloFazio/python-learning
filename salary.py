salary = float(input('Digite seu salario atual: '))
if salary < 500:
     print ("Seu novo salario eh ", salary*1.15)
elif salary <= 1000:
    print ("Seu novo salario eh ", salary*1.10)
else :
    print ("Seu novo salario eh ", salary*1.05)