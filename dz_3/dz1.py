# Создать статический метод который принимает на вход три параметра: login, password и confirmPassword.
# Login должен содержать только латинские буквы, цифры и знак подчеркивания.
# Длина login должна быть меньше 20 символов. Если login не соответствует этим требованиям,
# необходимо выбросить WrongLoginException.
# Password должен содержать только латинские буквы, цифры и знак подчеркивания.
# Длина password должна быть меньше 20 символов. Также password и confirmPassword должны быть равны.
# Если password не соответствует этим требованиям, необходимо выбросить WrongPasswordException.
import re


class WrongLoginException(Exception):
    def __init__(self, text):
        self.text = text


class WrongPasswordException(Exception):
    def __init__(self, text):
        self.text = text


class User:

    def __init__(self):
        self.login = None
        self.password = None

    def create_login(self):
        while True:
            login = input('Введите логин: ')

            if len(login) < 20 and '_' in login and all(re.search(p, login) for p in ('\d', '[a-z]')):
                self.login = login
                print('Успешно')
                # break
            else:
                raise WrongLoginException('Login должен содержать латинские буквы, цифры и знак подчеркивания и'
                                          ' быть меньше 20 символов')


    def create_password(self):
        while True:
            password = input('Введите пароль: ')

            if not (len(password) < 20 and '_' in password and all(re.search(p, password) for p in ('\d', '[a-z]'))):
                raise WrongLoginException('password должен содержать только латинские буквы, цифры '
                      'и знак подчеркивания и быть меньше 20 символов')
            else:
                self.password = password
                print('Успешно')
                break

        confirmPassword = input('Повторите пароль: ')

        if password != confirmPassword:
            raise WrongPasswordException('Пароли не соответствуют. Повторите попытку')
        else:
            print('вы успешно зарегистрировались')


u = User()

try:
    u.create_login()
    u.create_password()

except (WrongLoginException, WrongPasswordException) as we:
    print(we)
