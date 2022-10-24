
# Користувач вводить повідомлення з клавіатури, потрібно закоувати повідомлення
morze_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

# Шось типу такого? ) :

user_message = input("Enter secret!: ")
user_message = user_message.upper()

result = ""
for symbol in user_message:
    if code := morze_dict.get(symbol):
        result += code + " "
print(result)


result = " ".join(
    [code for symbol in user_message if (code := morze_dict.get(symbol))])
print(result)

# simpl...
print(" ".join([code for symbol in input("Enter secret!: ").upper() if (code := morze_dict.get(symbol))]))


# alter by Anton Holovin
m_text = [morze_dict.get(x) for x in input("Введіть текст: ").upper() if x.isdigit() or x.isalpha()]
print(" ".join(m_text))
