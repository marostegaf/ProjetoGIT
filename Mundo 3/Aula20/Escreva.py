def escreva(msg):
    tot = len(msg) + 4
    print(f"=" * tot)
    print(f"{msg:^{tot}}")
    #OU print(f"  {msg}")
    print(f"=" * tot)


resp = input("O que deseja escrever: ")
escreva(resp)
