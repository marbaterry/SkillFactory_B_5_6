ERROR = '[\033[31mERROR\033[0m]'
space = [['-'] * 3 for _ in range(3)]


def show_space(f):
    print("\033[34m"'    0 1 2 B'"\033[0m")
    for i in range(len(space)):
        print("\033[34m", str(i), "\033[0m", *space[i])
    print("\033[34m"' A'"\033[0m")


def user_side(f, user):
    while True:
        if user == '\033[33mx\033[0m':
            coordinates = input('Ход играка x. Введите координаты поля  A и B через пробел:\n').split()
        else:
            coordinates = input('Ход играка o. Введите координаты поля  A и B через пробел:\n').split()
        if len(coordinates) != 2:
            print(ERROR + ' Введите два значения:\n')
            continue
        if not (coordinates[0].isdigit() and coordinates[1].isdigit()):
            print(ERROR + ' Введите числа:\n')
            continue
        a, b = map(int, coordinates)
        if not (a >= 0 and a <= 2 and b >= 0 and b <= 2):
            print(ERROR + ' Указано несуществующее поле:\n')
            continue
        if f[a][b] != '-':
            print(ERROR + ' Поле занято:\n')
            continue
        break
    return a, b


def check_winner(f, user):
    win_combo = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),\
                 ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),\
                 ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2)))
    for combo in win_combo:
        symbols=[]
        for c in combo:
            symbols.append(f[c[0]][c[1]])
            if symbols == [user, user, user]:
                return True
    return False


def run():
    count = 0
    while True:
        if count == 9:
            print('Ничья')
            show_space(space)
            break
        if count % 2 == 0:
            user = '\033[33mx\033[0m'
        else:
            user = '\033[33mo\033[0m'
        show_space(space)
        a, b = user_side(space, user)
        space[a][b] = user
        if check_winner(space, user):
            print('\033[5mПобеда за игроком ' + user)
            show_space(space)
            break
        count += 1


run()