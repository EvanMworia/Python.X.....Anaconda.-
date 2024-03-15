from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
#get a list of all available fonts
figletFonts = figlet.getFonts()
#capture users input
allowedFlags = ["-f", "--font"]
#if no command line arguments were passed
#format the text provided by a random font
if len(sys.argv) < 2:
    text = input("Enter text to be formatted to ASCII art! ")
    randomFont = figletFonts[random.randint(0, 200)]
    figlet.setFont(font=randomFont)

    print(figlet.renderText(text))
#if the user has supplied commandline arguments
elif len(sys.argv) > 2  :
    #checking if the first flag is in our allowed list of flags
    if sys.argv[1] not in allowedFlags :
        sys.exit(f"{sys.argv[1]} is an unsupported flag, Expected: -f or --font")
    #check if figlet fonts has the font specified by the user
    elif figletFonts.__contains__(sys.argv[2]):
        text = input("Enter text to be formatted to ASCII art! ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(text))
    else:
        sys.exit("sorry the specified font doesn't exist, chec spelling or change font name")

else:
    sys.exit("Improper usage, expected only two command line arguments OR none at all")



