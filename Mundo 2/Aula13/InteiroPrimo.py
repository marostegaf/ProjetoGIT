num = int(input("Digite um número: "))
total = 0
for i in range(1 , num + 1):
    if num % i == 0:
        print("\033[32m", end="")
        total += 1
    else:
        print("\033[31m", end="")
    print(i, end=" ")

print(f"\033[m\nO número {num} foi divisível {total} vezes")
if total == 2:
    print(f"O número {num} é \033[32mPRIMO!\033[m")
else:
    print(f"O número {num} não é \033[32mPRIMO!z033[m")
