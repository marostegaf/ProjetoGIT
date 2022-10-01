num = []

while len(num) < 5:
    n = int(input("Digite um número: "))
    if len(num) == 0 or n > num[-1]:
        num.append(n)
    else:
        for i in range(5):
            if n <= num[i]:
                num.insert(i,n)
                break

print("\n\033[36mValores\033[m: ",end="")
for i in range(5):
    print(num[i],end=" ")