#--------------------------------
# Github : https://github.com/UN56/PythonMathGame
#--------------------------------
text = "MATH GAME!"
import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import time
import colorama
from colorama import Fore, Style
from random import randrange

def wrong():
    print(f"{Fore.RED}Wrong!")
    time.sleep(0.3)

def quit():
    print(f"{Fore.RED}\nPROGRAM WILL CLOSED AFTER 1 SECOND")
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

# p = ["+", "-", "*"]

# ---------------Source: https://stackoverflow.com/questions/9632995/how-to-easily-print-ascii-art-text
myfont = ImageFont.truetype("verdanab.ttf", 12)
size = myfont.getsize(text)
img = Image.new("1", size, "black")
draw = ImageDraw.Draw(img)
draw.text((0, 0), text, "white", font=myfont)
pixels = np.array(img, dtype=np.uint8)
chars = np.array([' ', '#'], dtype="U1")[pixels]
strings = chars.view('U' + str(chars.shape[1])).flatten()
print("\n".join(strings))
# -------------------------------------------------------------------------
print("\n")
print(f"{Fore.YELLOW}INPUT 'q' FOR QUIT THE GAME!!")
print("\n\n\n")
j = input("multiplication: [x], addition: [+]: ")

while True:
    n = randrange(1, 10)
    m = randrange(1, 10)
    start = time.time()
    if j == "+":
        v = n + m
        jawaban = input(str(n) + " + " + str(m) + " = ")
        # start = time.time()
        if jawaban == "q":
            quit()
            break
        if representsInt(jawaban):
            if int(jawaban) == v:
                end = time.time()
                tm = end - start
                print(f"{Fore.GREEN}Correct! [" + "%.2f" % tm + "]")
                time.sleep(0.3)
            else:
                wrong()
        else:
            wrong()
    # elif j == "/":
    #     v = n / m
    #     jawaban = int(input(str(n) + " ÷ " + str(m) + " = "))
    #     # start = time.time()
    #     if jawaban == v:
    #         end = time.time()
    #         tm = end - start
    #         print(f"{Fore.GREEN}Correct! [" + str(tm) + "]")
    #     else:
    #         print(f"{Fore.RED}Wrong!")
    elif j == "x":
        v = n * m
        jawaban = input(str(n) + " x " + str(m) + " = ")
        # start = time.time()
        if jawaban == "q":
            quit()
            break
        if representsInt(jawaban):
            if int(jawaban) == v:
                end = time.time()
                tm = end - start
                # "%.2f" % 12.34567
                print(f"{Fore.GREEN}Correct! [" + "%.2f" % tm + " sec]")
                time.sleep(0.3)
            else:
                wrong()
        else:
            wrong()
    else:
        print(f"{Fore.MAGENTA}ape nii?: " + j)
        print(f"{Fore.RED}\nPROGRAM WILL CLOSED AFTER 2 SECOND")
        time.sleep(2)
        break
