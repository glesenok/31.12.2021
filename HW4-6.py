from itertools import count, cycle

print('Программа генерирует числа, начиная с указанногою Для генерации числа нажмите ентер, для выхода нажмите q')
for i in count(int(input('Введите стартовове число:'))):
    print(i, end='')
    quit = input()
    if quet =='q':
        break

print('Программа повтряет элементы из списка Для генерации числа нажмите ентер, для выхода нажмите q')
u_list = input('Введите список, разделяя элементы пробелами').split()
iter_=cycle(u_list)
quit = None

while quit !='q':
    print(next(iter_), end='')
    quit = input
