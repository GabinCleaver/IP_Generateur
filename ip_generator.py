import random
from colorama import Fore, init

init()

how_many = int(input(Fore.CYAN + "Entrez le nombre d'ip a générer: "))

r = open("ip.txt", "a+", encoding='utf-8')

for ip in range (0, how_many):
    first_ip_part = random.randint(1,250)
    second_ip_part = random.randint(1,250)
    third_ip_part = random.randint(1,250)
    last_ip_part = random.randint(1,250)

    r.write(str(first_ip_part) + "." + str(second_ip_part) + "." + str(third_ip_part) + "." + str(last_ip_part) + "\n")
    print(Fore.GREEN + str(first_ip_part) + "." + str(second_ip_part) + "." + str(third_ip_part) + "." + str(last_ip_part))