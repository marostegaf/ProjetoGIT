#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ang = float(input("Digite o ângulo: "))
seno = math.sin(math.radians(ang))
print(f"O seno do ângulo {ang} é {seno:.2f}")
cos = math.cos(math.radians(ang))
print(f"O cosseno do ângulo {ang} é {cos:.2f}")
tan = math.tan(math.radians(ang))
print(f"A tangente do ângulo {ang} é {tan:.2f}")