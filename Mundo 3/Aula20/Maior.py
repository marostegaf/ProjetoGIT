from time import sleep

def maior(*num):
    print("=" * 45)
    print(f"Números analisados: ",end="")
    for valor in num:
        print(valor,end=" ",flush=True)
        sleep(0.4)
    print(f"\nValores ao todo: {len(num)}")
    print(f"O maior valor informado foi: {max(num)}")



maior(4, 7, 0)
maior(1,3,5,89)