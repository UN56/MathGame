#--------------------------------
# Github : https://github.com/UN56/MathGame
#--------------------------------
text = "MATH GAME!"
import time
import colorama
from colorama import Fore
from random import randrange
import pyfiglet

def correct():
    print(f"{Fore.GREEN}Correct! [" + "%.2f" % tm + "]")
    time.sleep(0.3)

def wrong():
    print(f"{Fore.RED}Wrong!")
    time.sleep(0.3)

def quit():
    print(f"{Fore.MAGENTA}\nPROGRAM WILL CLOSE AFTER 1 SECOND")
    time.sleep(1)

def representsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

colorama.init(autoreset=True)

print('\033[31m')
print('\033[39m')  # and reset to default color
print()

# ---------------Create Banner
bannerText = pyfiglet.figlet_format("Math Game", font = "banner3-D" )
print(bannerText)
# ----------------------------
print("\n")
print(f"{Fore.YELLOW}INPUT 'q' FOR QUIT THE GAME!!")
print("\n\n\n")
j = input("multiplication: [x], addition: [+], subtraction: [-]: ")

while True:
    n = randrange(1, 10)
    m = randrange(1, 10)
    start = time.time()
    if j == "+" or j == "addition":
        v = n + m
        answer = input(f"{n} + {m} = ")
        # start = time.time()
        if answer == "q":
            quit()
            break
        if representsInt(answer):
            if int(answer) == v:
                end = time.time()
                tm = end - start
                correct()
            else:
                wrong()
        else:
            wrong()

    elif j == "-" or j == "subtraction":
        numlist = [n,m]
        numlist.sort(reverse=True)
        v = numlist[0] - numlist[1]
        answer = input(f"{numlist[0]} - {numlist[1]} = ")
        # start = time.time()
        if answer == "q":
            quit()
            break
        if representsInt(answer):
            if int(answer) == v:
                end = time.time()
                tm = end - start
                correct()
            else:
                wrong()
        else:
            wrong()
    elif j == "x" or j == "multiplication":
        v = n * m
        answer = input(f"{n} x {m} = ")
        # start = time.time()
        if answer == "q":
            quit()
            break
        if representsInt(answer):
            if int(answer) == v:
                end = time.time()
                tm = end - start
                correct()
            else:
                wrong()
        else:
            wrong()
    else:
        print(f"{Fore.RED}ERROR!: " + j)
        print(f"{Fore.MAGENTA}\nPROGRAM WILL CLOSE AFTER 2 SECOND")
        time.sleep(2)
        break