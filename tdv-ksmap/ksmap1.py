import sys, os

def fun_try_open_file(var_file):
    try:
        return open(var_file)
    except OSError as err:
        print('File is missing?',err)
        return 0

r = fun_try_open_file('ks_list.txt')# open file of address list
if r != 0:
    for i in r: #cilce(loop) in each line (each address)
        kspoint=str(i) #from read line to string
        kspoint=kspoint.rstrip()#remove EndLine?                #kspoint=kspoint.rstrip([chars])
        kspoint=kspoint.replace(' ', '+')#change " " to "+" in address string
        os.system('start  https://www.google.com/maps/search/'+kspoint) #open map address in new bookmark
    r.close()





