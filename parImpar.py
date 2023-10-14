# Sistema para informar se o número digitado é par ou impar

num = int(input("Informe um número: "))

if ((num % 2) == 0):
    print(f"O número {num} é par!")
else:
    print(f"O número {num} é impar!")

