import locale
print(locale.getpreferredencoding(False))

# https://docs.python.org/3/library/codecs.html#standard-encodings

fh = open("D:\\projects\\c_u8.txt")
print(fh)
fh.close()
print(fh)

fh = open("D:\\projects\\c_uc.txt")
print(fh)
fh.close()
print(fh)

fh = open("D:\\projects\\c_ansii.txt")
print(fh)
fh.close()
print(fh)

fh = open("D:\\projects\\c_ucbe.txt")
print(fh)
fh.close()
print(fh)

fh = open("D:\\projects\\c_u8.txt", encoding="utf-8")
print(fh)
fh.close()
print(fh)

fh = open("D:\\projects\\c_ansii.txt", encoding="cp1251")
print(fh)
fh.close()
print(fh)

fh = open("D:\\projects\\c_uc.txt", encoding="utf_7")
print(fh)
fh.close()
print(fh)

fh = open("D:\\projects\\c_ucbe.txt", encoding="utf_16_be")
print(fh)
fh.close()
print(fh)
