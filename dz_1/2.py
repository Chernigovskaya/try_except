# Реализуйте метод, принимающий в качестве аргументов два целочисленных массива,
# и возвращающий новый массив, каждый элемент которого равен разности элементов двух входящих массивов в
# той же ячейке.
# Если длины массивов не равны, необходимо как-то оповестить пользователя.


def delta_arr(a1, a2):
    array = []

    try:

        for i in range(len(a1)):
            n = a1[i] - a2[i]

        for i in range(len(a2)):
            n = a1[i] - a2[i]

    except IndexError:
        print('Длины массивов должны быть равны')

    else:
        for i in range(len(a2)):
            n = a1[i] - a2[i]
            array.append(n)
        print(array)


print('2 задача: все ок')
arr1 = [5, 10, 1]
arr2 = [2, 12, 15]
delta_arr(arr1, arr2)

print('**************************')
print('2 задача: длины не равны')
arr1 = [5, 10, 1, 2]
arr2 = [2, 12, 15]
delta_arr(arr1, arr2)
