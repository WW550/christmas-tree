import time
import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Function to generate a firework explosion
def generate_firework():
    colors = [
        Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN
    ]
    explosion = [
        "        *", 
        "       ***", 
        "      *****", 
        "     *******", 
        "      *****", 
        "       ***", 
        "        *"
    ]
    colored_explosion = [random.choice(colors) + line for line in explosion]
    return "\n".join(colored_explosion)

# Function to display fireworks and text
def display_fireworks():
    try:
        while True:
            # Clear the screen
            print("\033c", end="")

            # Display fireworks
            for _ in range(3):
                print(generate_firework())
                time.sleep(0.5)

            # Display "Happy 2025"
            print("\n" * 5)
            print(Fore.YELLOW + Style.BRIGHT + "    H A P P Y")
            print(Fore.CYAN + Style.BRIGHT + "        2 0 2 5")
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nWishing you a wonderful 2025!")

if __name__ == "__main__":
    display_fireworks()
