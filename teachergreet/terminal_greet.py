import time
import os
from colorama import Fore, Style, init

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_terminal_greeting(message="🎓 Happy Teachers' Day 🎓", cycles=10, delay=0.3):
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    for i in range(cycles):
        clear()
        color = colors[i % len(colors)]
        print("\n" * 5)
        print(" " * 10 + color + Style.BRIGHT + message)
        time.sleep(delay)
    print("\n" * 5)
    print(" " * 10 + Fore.GREEN + Style.BRIGHT + "🙏 Thank You Gurujis!")
