import logging

# from time import time
from timeit import default_timer


logging.basicConfig(level=logging.DEBUG, format="%(threadName)12s %(message)90s")


def duration(fun):
    def inner(*args, **kwargs):
        start = default_timer()
        rez = fun(*args, **kwargs)
        logging.info(f"Args:{args}, {default_timer()-start=} sec")

        return rez

    return inner


@duration
def email_aligner1(email: str) -> str:
    email_aligner_base = {
        "main.net": "maindex.net",
        "googlemail.com": "gmail.com",
    }

    email = email.lower()
    # if email[-6:] == '@ha.ua':
    #     return f'{email[:-6]}@hawin.ua'
    # return email
    name, domain = email.split("@")
    align_domain = email_aligner_base.get(domain, None)
    return f"{name}@{align_domain}" if align_domain else email


def main():
    email_test_group = {
        "qwe@main.net": "qwe@maindex.net",
        "aswe@Maindex.nEt": "aswe@maindex.net",
        "asd@MaiN.Net": "asd@maindex.net",
        "zSer@gMaiL.com": "zser@gmail.com",
        "yandexser@Maindex-Team.neT": "yandexser@maindex-team.net",
        "z1Ser@gOOgleMaiL.com": "z1ser@gmail.com",
    }
    print(default_timer())
    for element in email_test_group:
        assert email_aligner1(element) == email_test_group[element]


if __name__ == "__main__":
    main()
