from banner import print_banner
import pyfiglet
import os

def main():
    print_banner()

    PINK = "\033[95m"
    RESET = "\033[0m"
    
    banner_text = pyfiglet.figlet_format("ASCII Text Generator", font="slant")
    print(f"{PINK}{banner_text}{RESET}")

    print("===========================================================================")

    WHITE = "\033[97m"
    text = input("Input Text: ")

    ascii_art = pyfiglet.figlet_format(text, font="slant")
    ascii_art_3d = ascii_art.replace("/", "|").replace("\\", "|").replace("_", "_").replace("|", "/")


    print(f"{WHITE}{ascii_art_3d}{RESET}")


    if not os.path.exists("out"):
        os.makedirs("out")


    file_path = os.path.join("out", f"{text.replace(' ', '_')}.py")
    with open(file_path, "w") as f:
        f.write(f"print('''{ascii_art_3d}''')")

    print(f"ASCII art saved in {file_path}")

main()
