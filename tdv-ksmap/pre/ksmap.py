import os

r = open('ks_list.txt')

for i in r:
    ##print(i)
    kspoint=str(i)
    kspoint=kspoint.rstrip()#kspoint=kspoint.rstrip([chars])
    kspoint=kspoint.replace(' ', '+')
    #print(kspoint)
    os.system('start  https://www.google.com/maps/search/'+kspoint)
    #os.system('start https://www.google.com/search?q='+i)
##    if len(i) > 4:
##        break

##    if i == 'end':
##        break
##
##    if 'https://' in i:
##        os.system('start '+i)
##        print('if')
##
##    elif 'www.' in i:
##        sayt = 'https://'+i
##        os.system('start '+i)
##        print('elif')
##
##    else:
##        sayt = 'https://www.'+i
##        os.system('start '+i)
##        print('else') 





