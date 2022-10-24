'''
Завдання: Пошук email
- алфавіт, який використовується для назви email, - англійська
- префікс (все, що знаходиться до символу @) починається з латинської літери і може містити будь-яке число або літеру,
включаючи нижнє підкреслення та символ крапки, складається щонайменше з двох символів
- суфікс почти (все, що знаходиться після символу @) складається тільки з букв англійського алфавіту, складається
з двох частин, розділених точкою, і доменне ім'я верхнього рівня не може бути менше двох символів (все, що після крапки)
'''

import re
text = "Ima_Fool@YTna.org Ima.Fool@iana.o Fool1@iana.org first_last@iana.org first.middle.last@iana.or a@test.com " \
       "abc111@test.com.ua 12Fool1@iana.org aqua.erk@debt.by aqua2.erk@debt.b aqua3.erk@debt.bib aqua4.erk@debt.b.c" \
       " ase.ert@qwert..as ase.ert@qwert..as.com ase.ert@qwert..as.by"

# result = re.findall(r'[A-Za-z]{1}[\w\.]+@[A-Za-z]+\.[A-Za-z]{2,3}', text)
# result = re.findall(r"\b[a-zA-Z]\w+\.?\w*\.?\w*@\w*\.\w{2,}", text)
# result = re.findall(r"\b[A-Za-z][\w+.]+@\w+[.][a-z]{2,3}", text)
# result = re.findall(r'[a-zA-Z]{1,}[a-zA-Z0-9._]{1,}[@][a-zA-Z]{1,}[.][a-zA-Z]{2,}', text)
result = re.findall(r"\b[a-zA-z][\w_.]+@[a-zA-z]+\.[a-zA-z]{2,}", text) # ? .com.ua
print(result)
result = re.findall(r"\b[a-zA-z][\w_.]+@[a-zA-z]+\.[a-zA-z]+\.?[a-zA-z]+", text)
print(result)
result = re.findall(r"\b[a-zA-z][\w_.]+@[a-zA-z]+\.[a-zA-z]*[a-zA-z\.]?[a-zA-z]{2,}", text)
print(result)

print()

result1 = re.findall(r"\b[a-zA-z][\w_.]+@[a-zA-z]+\.[a-zA-z]{2,}[ ]", text)
result1 = [i.strip() for i in result1]
result2 = re.findall(r"\b[a-zA-z][\w_.]+@[a-zA-z]+\.[a-zA-z]+\.[a-zA-z]{2,}", text)
print(list(set(result1+result2)))
