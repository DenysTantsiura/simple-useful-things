import os

r = open('ks_list.txt')# open file of address list

for i in r: #cilce(loop) in each line (each address)
    kspoint=str(i) #from read line to string
    kspoint=kspoint.rstrip()#remove EndLine?                #kspoint=kspoint.rstrip([chars])
    kspoint=kspoint.replace(' ', '+')#change " " to "+" in address string
    os.system('start  https://www.google.com/maps/search/'+kspoint) #open map address in new bookmark






