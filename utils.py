import time
import sys
from termcolor import colored


def line(length, color):
    print(colored("="*length, color))


def loading(teks):
    color = "white"
    for i in range(101):
        time.sleep(0.1)

        if (i > 25):
            color = "blue"

        if (i > 50):
            color = "magenta"

        if (i > 75):
            color = "green"

            color = "blue"
        sys.stdout.write(
            colored(f"\r {teks} %d%%" % i, color))
        sys.stdout.flush()
