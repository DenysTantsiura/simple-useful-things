'''модуль 8, завдання на самостійну практику:
1) скільки днів до якоїсь певної дати, введенної користувачем
2) створити список дейтам-обєктів з випадковою датою
    3) Десімал - затик )
5) створити іменований кортеж з 5-6 полями, і створення та оброблення і виведення з нього(них)
6) кількість символа у великій строці за допомогою колектіонс-модуля, вибрати найпопулярніших символів (рандомної кількості з 1-6)
7) створити словник з слів які поч на певні букви
8) створити список обмежений макс кількістю довжини, 3 елементи
'''
from datetime import datetime
import random
import collections


def test_self_task_6(var_input="qdadfghtki;ofyyhrsgstkuilksrgwTG4365689-864235 THGM,I;UBDTHRSYAERTGRDGRDGdyherssfdhtyikjsydfgh547564352wf2"):

    rez = collections.Counter(var_input)
    print(rez)
    c = collections.Counter(a=4, b=2, c=0, d=-2)
    d = collections.Counter(a=1, b=2, c=3, d=4)
    c.subtract(d)
    print(c)

    words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
    grouped_words = collections.defaultdict(list)
    for word in words:
        char = word[0]
        grouped_words[char].append(word)

    d = collections.deque(maxlen=3)
    d.append('last')
    d.appendleft('first')
    d.insert(1, 'middle')
    d.append('lastest')
    print(d)            # deque(['middle', 'last', 'lastest'], maxlen=3)
    print(d.pop())      # 'lastest'
    print(d.popleft())  # 'middle'
    print(d)            # deque(['last'], maxlen=3)

    return rez.most_common(3)


def test_named_tupple():
    named_tupple_1 = collections.namedtuple('great_day', ["date", "importance", "cathegory", "description"])
    date1 = named_tupple_1(random_date(), 1, "relative", "birthday")
    date2 = named_tupple_1(random_date(), 0.5, "celebrate", "First Day celebrating ...")
    print(date1.description)
    print(date2.cathegory)
    print(date1.date)
    print(date2.date)
    print(date2.description)
    date2 = named_tupple_1(date2.date, 12, date2.cathegory, date2.description)
    print(date2.importance)
    print(date2)


def inputing_users_date():
    return datetime.strptime(input("Enter date(YYYY-MM-DD): "), '%Y-%m-%d')


def random_date(max_year=2072):

    if max_year < 2022:
        max_year = 2022
    Year = random.randint(2022, max_year)   # 2022, 2072
    month = random.randint(1, 12)  # 1, 12
    day = random.randint(1, 31)  # 30/29/28  1, 31
    while True:
        try:
            datetime(year=Year, month=month, day=day)
            break
        except ValueError:
            day = random.randint(1, 31)

    return datetime(year=Year, month=month, day=day)


def list_of_random_date(size_of_list=1):

    if size_of_list > 0:
        return [random_date() for i in range(size_of_list)]
    return None


def duration_up_to(date_point: datetime):
    return (date_point - datetime.now()).days


def main():

    # print(duration_up_to(inputing_users_date()))
    # print(duration_up_to(random_date()))
    # print(list_of_random_date(5))
    # test_named_tupple()
    print(test_self_task_6())
    print(test_self_task_6([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6,
          5, 4, 3, 2, 1, 1, 4, 5, 5, 4, 2, 1, 1, 2, 3, 4, 3, 2, 1, 0]))


if __name__ == "__main__":
    exit(main())
