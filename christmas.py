import time
import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Function to generate a Christmas tree with lights
def generate_tree():
    tree = []
    tree.append("          *")
    tree.append("         ***")
    tree.append("        *****")
    tree.append("       *******")
    tree.append("      *********")
    tree.append("     ***********")
    tree.append("    *************")
    tree.append("   ***************")
    tree.append("  *****************")
    tree.append(" *******************")
    tree.append("         |||")
    return tree

# Function to add lights with random colors
def add_lights(tree):
    colors = [
        Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN
    ]
    lit_tree = []
    for row in tree:
        new_row = ""
        for char in row:
            if char == "*":
                new_row += random.choice(colors) + "*"
            else:
                new_row += char
        lit_tree.append(new_row)
    return lit_tree

# Main function to display the Christmas tree with changing lights
def display_tree():
    tree = generate_tree()
    try:
        while True:
            lit_tree = add_lights(tree)
            print("\n".join(lit_tree))
            time.sleep(0.5)
            print("\033c", end="")  # Clear the screen
    except KeyboardInterrupt:
        print("\nMerry Christmas!")

if __name__ == "__main__":
    display_tree()
