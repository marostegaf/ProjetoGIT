import time

print("\033[36mContagem regressiva para os fogos!\033[m")
for i in range(10, 0, -1):
    print(i)
    time.sleep(0.5)
print("\033[35mBOOOOM!!!\033[m")
