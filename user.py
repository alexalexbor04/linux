import socket

def get_users_input(value):
    user_input = input(f'Введите значение, по умолчанию им является {value}: ')
    if not user_input:
        return value
    return user_input