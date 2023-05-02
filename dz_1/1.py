# Реализуйте 3 метода, чтобы в каждом из них получить разные исключения

# 1 Файл не существует
def open_file():
    file = 'text.txt'
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

    except (FileNotFoundError, EOFError) as e:
        print(f'файл не существует: {e}')
    else:
        print(content)
        f.close()


print('1 метод:')
open_file()


#2 несуществующий индекс
def print_num_index(arr, i):
    try:
        print(arr[i])
    except (IndexError) as e:
        print(f'ошибка: {e}')
    finally:
        print(arr)

print('**************************')
print('2 метод:')
array = [1, 2, 3, 4]
print_num_index(array, 10)


def find_day():
    d = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }

    try:
        i = int(input('Номер дня недели: '))
    except (ValueError) as e:
        print('Вы ввели не число!')
    else:
        print(d.get(i, 'Такого дня нет!'))


print('**************************')
print('3 метод:')
find_day()

