# Разработайте программу, которая выбросит Exception,
# когда пользователь вводит пустую строку.
# Пользователю должно показаться сообщение, что пустые строки вводить нельзя.

def input_text():
    text = input('Введите что-нибудь: ')
    try:
        if len(text) == 0:
            raise Exception
        else:
            print(text)

    except:
        print("Пустые строки вводить нельзя")


input_text()