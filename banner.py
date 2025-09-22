
PINK = "\033[95m"  # ridan
BLUE = "\033[94m"  # XD
CYAN = "\033[94m"  # colored_text
RESET = "\033[0m"
LIME = "\033[93m"
GREEN = "\033[96m"
RED = "\033[92m"

lines = ["--------------------------------------------------------------------------"]

colored_lines = ["============================================================="]


colored_text = [ "@ridanxd.git"]

art_lines = [
"   *              *        *    *  __      __  ____                ",
" *   *  *     *        *           \\ \\    / / |    \\              ",
"  _____  _*     __ * ____      *    \\ \\  / /  |     \\             ",
" | ____|| | *  |  | |__  | * ___     \\ \\/ /   |  |\\  \\           ",
" | |    | |  __|  |  __| |  / _ \\    / /\\ \\   |  |/  /           ",
" | |    | | | __  | | __ | | | | |  / /  \\ \\  |     /            ",
" |_|    |_| |_____| |____| |_| |_| /_/    \\_\\ |____/             ",
""
""
]
def print_banner():
	print(RED + colored_lines[0] + RESET)


	for line in art_lines:
	    pink_part = line[:70] 
	    print(PINK + pink_part + RESET)
	print(RED + colored_lines[0] + RESET)

	print(" ")
	print(lines[0])

	print(LIME + "Disclaimer, my project is free to use, you can use it for anything" + RESET)
	print(GREEN + "Follow me on instagram: "+ RESET + CYAN + colored_text[0] + RESET + GREEN + "\nGitHub: " + RESET + "@ridanXD")

	print(lines[0])

print_banner()
