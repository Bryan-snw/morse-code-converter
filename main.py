from logo import logoArt

morse_code_dict = {
    "A": "•-",
    "B": "-••",
    "C": "-•-•",
    "D": "-••",
    "E": "•",
    "F": "••-•",
    "G": "--•",
    "H": "••••",
    "I": "••",
    "J": "•---",
    "K": "-•-",
    "L": "•-••",
    "M": "--",
    "N": "-•",
    "O": "---",
    "P": "•--•",
    "Q": "--•-",
    "R": "•-•",
    "S": "•••",
    "T": "-",
    "U": "••-",
    "V": "•••-",
    "W": "•--",
    "X": "-••-",
    "Y": "-•--",
    "Z": "--••",
    "1": "•----",
    "2": "••---",
    "3": "•••--",
    "4": "••••-",
    "5": "•••••",
    "6": "-••••",
    "7": "--•••",
    "8": "---••",
    "9": "----•",
    "0": "-----"
}

print(logoArt)
print("Welcome to Morse Code Converter, we do magic here,\nyou just need to input  your text and we'll do the rest:)\n")

text = input("Enter your desired text:\n").upper()

morse_code = ""
for char in text:
    if char in morse_code_dict:
        morse_code += f"{morse_code_dict[char]} "
    else:
        morse_code += char

print(f"Here is your morse code:\n{morse_code}")
print(f"Thank you, enjoy doing your spying thing😎🕵️")