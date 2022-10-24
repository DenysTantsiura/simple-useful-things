message = input("введіть повідолмення: ")
offset = int(input("Введіть зсув: "))
encoded_message = ""
for ch in message:
    if "a" <= ch <= "z":
        pos = ord(ch) - ord("a")
        pos = (pos + offset) % 26
        new_char = chr(pos + ord("a"))
        encoded_message = encoded_message + new_char
    if "A" <= ch <= "Z":
        pos = ord(ch) - ord("A")
        pos = (pos + offset) % 26
        new_char = chr(pos + ord("A"))
        encoded_message = encoded_message + new_char
    else:
        encoded_message = encoded_message + ch
print(encoded_message)

# Hello my little friends!

