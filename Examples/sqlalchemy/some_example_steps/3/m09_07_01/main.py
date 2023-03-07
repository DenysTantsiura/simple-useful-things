import argparse
import sys
from sqlalchemy.exc import SQLAlchemyError
from database.repository import get_user, get_all_todos, create_todo, update_todo, remove_todo

parser = argparse.ArgumentParser(description='Todo APP')  # параметри в консолі не в 'одинарних', а в подвійних "лапках"
parser.add_argument('--action', help='Command: create, update, list, remove')
parser.add_argument('--id')
parser.add_argument('--title')
parser.add_argument('--desc')
parser.add_argument('--login')

arguments = parser.parse_args()
# print(arguments)
my_arg = vars(arguments)
# print(my_arg)

action = my_arg.get('action')  # action
title = my_arg.get('title')
description = my_arg.get('desc')
_id = my_arg.get('id')
login = my_arg.get('login')


def main(user):
    match action:  # match з версії 3.10 Пайтона!
        case 'create':
            create_todo(title=title, description=description, user=user)
        case 'list':
            todos = get_all_todos(user)
            for t in todos:
                print(t.id, t.title, t.description, t.user.login)
        case 'update':
            t = update_todo(_id=_id, title=title, description=description, user=user)
            if t:
                print(t.id, t.title, t.description, t.user.login)
            else:
                print('Not found')
        case 'remove':
            r = remove_todo(_id=_id, user=user)
            print(f'Remove: {r}')
        case _:  # Якщо немає співпадінь з match - default value
            print('Nothing')


if __name__ == '__main__':
    user = get_user(login)
    password = input('Password: ')
    if password == user.password:
        main(user)
    else:
        print('Password wrong!')
