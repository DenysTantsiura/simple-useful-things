# try find max bit? )
a = 3402826692093846346337460743176821455
b = int(a/1844674407709551615)
for i in range(0, 2**64):
    print(a*(b**i))
