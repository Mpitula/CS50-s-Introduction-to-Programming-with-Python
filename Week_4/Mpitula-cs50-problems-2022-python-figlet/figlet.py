import sys
import random
import pyfiglet

# Create a Figlet instance to work with fonts
figlet = pyfiglet.Figlet()

# Get all available fonts
fonts = figlet.getFonts()

# Handle arguments
if len(sys.argv) == 1:
    # No args — pick a random font
    font = random.choice(fonts)

elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")

    if sys.argv[2] not in fonts:
        sys.exit("Invalid font name")

    font = sys.argv[2]

else:
    sys.exit("Invalid usage")

# Set the font
figlet.setFont(font=font)

# Prompt for text
text = input("Input: ")

# Print in chosen font
print(figlet.renderText(text))
