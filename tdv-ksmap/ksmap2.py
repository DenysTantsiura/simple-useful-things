import sys
import os
import locale
from typing import Any
import time
'''
task: open many browser tabs with a map of each address listed in the file
'''


def fun_try_open_file(var_file):  # try to open the file without error
    try:
        return open(var_file)  # to open for reading
    except OSError as err:
        print('File is missing?', err)
        return 0
    except Exception as erro:
        print('Unknown error opening file', erro)
        return 0


# !!!? txt ANSI or UTF-8 or ... ??? now at ANSI in system, but what in file?
def open_multiple_tabs_with_address_maps(address_list='ks_list.txt'):
    with open(address_list, "r", encoding=locale.getpreferredencoding(do_setlocale=False)) as file_h:  # open file of address list
        #file_h = fun_try_open_file('ks_list.txt')
        if file_h != 0:
            for i in file_h:  # cilce(loop) in each line (each address)
                kspoint = str(i)  # from read line to string
                # remove EndLine:                #kspoint=kspoint.rstrip([chars])
                kspoint = kspoint.rstrip()
                # change " " to "+" in address string
                kspoint = kspoint.replace(' ', '+')
                # kspoint = kspoint.replace('/', '//')
                # open map address in new bookmark
                if len(kspoint) > 3:  # Not an empty line
                    os.system(
                        'start  https://www.google.com/maps/search/' + kspoint)
                    time.sleep(1/2)  # pause
                # pass
        # the program closes before the system call is executed
        # this is system call is not executed: why?
        # os.system('start  https://www.google.com/maps/search/Київ+вул.+Ак.+Глушкова,+13б,+ТРЦ+Магелан')
    # file_h.close()


def open_multiple_tabs_with_address_maps_alter(address_list='ks_list.txt'):
    with open(address_list, "r", encoding=locale.getpreferredencoding(do_setlocale=False)) as file_h:  # open file of address list
        address_list = file_h.readlines()
        if address_list != []:
            for i in address_list:
                kspoint = str(i)
                kspoint = kspoint.rstrip()
                kspoint = kspoint.replace(' ', '+')
                # kspoint = kspoint.replace('/', '//')
                if len(kspoint) > 3:  # Not an empty line
                    os.system(
                        'start  https://www.google.com/maps/search/' + kspoint)
                    time.sleep(1/2)
                    # print('start  https://www.google.com/maps/search/' + kspoint)
    # the program closes before the system call is executed
    # this is system call is not executed: why?
    # os.system('start  https://www.google.com/maps/search/' + kspoint)
    # os.system('dir')


def main():
    open_multiple_tabs_with_address_maps()
    # open_multiple_tabs_with_address_maps_alter()
    # pass


if __name__ == "__main__":
    main()
