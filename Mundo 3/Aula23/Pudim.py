import urllib
import urllib.request

try:
    user = input("Digite o link do site: ")
    site = urllib.request.urlopen(user)
except urllib.error.URLError:
    print("\033[31mO site não está acessível no momento!\033[m")
else:
    print("\033[32mO site está acessível\033[m")
