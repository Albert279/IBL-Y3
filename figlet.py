import sys, random
from pyfiglet import Figlet

Figlet = Figlet()

user = input("Input: ")
fonts = Figlet.getFonts()

try:
    if len(sys.argv) == 1:
        f = random.choice(Figlet.getFonts())
        Figlet.setFont(font = f)
        print(f"Output: {Figlet.renderText(user)}")

    elif sys.argv[1] =='-f' or sys.argv[1] =="--font":
            if sys.argv[1] == "-f" or sys.argv[1] == "--font":
                fig = Figlet.setFont(font=sys.argv[2])
                print(f"Output:{Figlet.renderText(user)}")
    else:
        sys.exit('Invalid usage')
except:
    sys.exit('Invalid usage')