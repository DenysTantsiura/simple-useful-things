import re


def replace_spam_words(text, spam_words):
    for i in spam_words:
        # text = re.sub(i, '*'*len(i), text, re.IGNORECASE, re.IGNORECASE)
        p = re.compile(i, re.IGNORECASE)
        text = p.sub('*'*len(i), text)
    return text


print("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn")
print(replace_spam_words(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn", ['began', 'pythOn']))

