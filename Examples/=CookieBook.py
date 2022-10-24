#...!
import os, sys, pickle, json

class CookieBook:
    def __init__(self):
        self.cookies = {}
        self.last_cookies_id = 0
    
    def add_c(self, cookie):
        self.cookies[self.last_cookies_id] = cookie 
        self.last_cookies_id += 1

    def delete_c(self, cookie_id: int):
        try:
            cookie_number = int(cookie_id)
            self.cookies.pop(cookie_number)
        except TypeError:
            raise Incorrectinput(f"Cookie ID {cookie_id} is not int")
        except KeyError:
            raise Incorrectinput(f"Cookie {cookie_id} not found")

    def update_c(self, cookie_id, field_idx, value):
        cookie = self.cookies[cookie_id]
        cookie.update(field_idx, value)

    def clear_c(self):
        self.cookies.clear()
        self.last_cookies_id = 0

    def __str__(self, idx):### time q 
        return f"{idx}:{self.cookies[idx]}"### time q 

def main():
    cb1 = CookieBook()
    cb1.add_c("cookie1")
    cb1.add_c("cookie2")
    print(cb1.last_cookies_id)
    print(cb1.cookies)
    cb2 = CookieBook()
    cb2.add_c("cookie3")
    cb2.add_c("cookie4")
    cb3 = CookieBook()
    cb3.add_c("cookie5")
    cb3.add_c("cookie6")

    clist = [cb1,cb2,cb3]# obj no in jsn
    print(f"list of obj: {clist}")
    print(f"element of obj-1-1: {clist[1].cookies[1]}")
    print(f"elements of obj-1: {clist[1].cookies}")
    #
    clist2 = [{'ct':'a','w':1},{'ct':'b','w':2},{'ct':'c','w':3}]
    jsn = json.dumps(clist2)
    print(f"List from json-dump: {jsn}")
    #
    with open('PBKP.txt', "ab") as varWordsFile:
        pickle.dump(clist, varWordsFile)
    f = open('PBKP.txt', 'rb')
    clist_read = pickle.load(f) # загружаем объект из файла
    print(f"Read of dumpPickle: {clist_read}")
    print(f"Read of dumpPickle-elements-lastID: {clist_read[0].last_cookies_id}")
    print(f"Read of dumpPickle-cookies: {clist_read[0].cookies}")
    clist_read[0].add_c("cookie7")
    print(f"Read of dumpPickle-cookies: {clist_read[0].cookies}")
    #
    clist_read_json = json.loads(jsn)
    print(f"Type of json read: {type(clist_read_json)}")
    print(f"Json read: {clist_read_json}")


if __name__ == "__main__":
    main()
