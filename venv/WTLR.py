import time, sys, os

field_player1 = [

    ["#", "#","#","#","#","#"],
    ["#", "#","#","#","#","#"],
    ["#", "#","#","#","#","#"],
    ["#", "#","#","#","#","#"],
    ["#", "#","#","#","#","#"],
    ["#", "#","#","#","#","#"]

]
p1_big_ship = 1
p1_medium_ship = 2
p1_small_ship = 3


field_player2 = [

    ["#", "#","#","#","#","#"],
    ["#", "#","#","#","#","#"],
    ["#", "#","#","#","#","#"],
    ["#", "#","#","#","#","#"],
    ["#", "#","#","#","#","#"],
    ["#", "#","#","#","#","#"]
]
p2_big_ship = 1
p2_medium_ship = 2
p2_small_ship = 3

coordinates = ["a","b","c","d","e","f"]

player1_name = str(input("Введите имя первого игрока: "));
player2_name = str(input("Введите имя второго игрока: "));

current_move = player1_name
current_field = field_player1

def get_cords():
    cord = []
    while cord != None:
        try:
            cord = [str(input("Введите координату (Буква слева): ")), int(input("Введите координату (Цифра слева): "))]
            if cord[0] not in coordinates or (cord[1]<0 or cord[1]>6) :
                print("Ошибка")
            else:
                print("Координаты записаны!")
                break
        except ValueError:
            print("Ошибка")
    return cord

def load():
    sys.stdout.write("Загрузка")
    for i in range(3):
        time.sleep(.05)
        sys.stdout.write('.')
        #sys.stdout.flush()
        time.sleep(.25)
    sys.stdout.write('\n')

def move(player_name):
    print(f"Ходит: {player_name}!")
    if player_name == player1_name:
        print(field_player1)
    else:
        print(field_player2)

def create_move(player_move, field, cs, direct):
    display_field(field)
    if cs == "1":
        print("Корабль: Большой @@@")
        ship_size = 3
    elif cs == "2":
        print("Корабль: Средний @@")
        ship_size = 2
    else:
        print("Корабль: Малый @")
        ship_size = 1
    cord = get_cords()
    if direct == "1":
        x = coordinates.index(cord[0])
        y = cord[1] - 1
        cm = place_ship_horizonatal(y, x, ship_size, current_field)
    else:
        x = coordinates.index(cord[0])
        y = cord[1] - 1
        cm = place_ship_vertical(y, x, ship_size, current_field)
    return cm


def place_ship_horizonatal(y, x, ship_size, field):
    flag = False
    break_flag = False
    for i in range(x-1, x+2):
        if break_flag:
            break
        if i < 0 or i >= 6:
            continue
        for j in range(y-1, ship_size+y+1):
            if j < 0 or j >= 6:
                continue
            if field[i][j] == "#":
                flag = True
            else:
                flag = False
                break_flag = True
                print("Рядом стоимт корабль!")
                break
    if flag:
        if 6 - y >= ship_size:
            for k in range(y, ship_size + y):
                field[x][k] = "B"
            print("Корабль на воде!")
        elif 6 - y < ship_size:
            print("Не хватает места для корабля такого размера!")
    display_field(field)
    return flag
def place_ship_vertical(y, x, ship_size, field):
    flag = False
    break_flag = False
    for j in range(y-1, ship_size+y+1):
        if break_flag:
            break
        if j < 0 or j >= 6:
            continue
        for i in range(x-1, 3):
            if i < 0 or i >= 6:
                continue
            if field[i][j] == "#":
                flag = True
            else:
                flag = False
                break_flag = True
                print("Рядом стоимт корабль!")
                break
    if flag:
        if 6 - x >= ship_size:
            for k in range(x, ship_size + x):
                field[k][y] = "B"
        elif 6 - x < ship_size:
            print("Не хватает места для корабля такого размера!")
    display_field(field)
    return flag
def display_field(field):
    row = 0
    colums = 0
    for k in range(6):
        row+= 1
        print('   ',f"{row}",end='')
    print()

    for i in field:
        print(coordinates[colums], end='   ')
        colums += 1
        for j in i:
            print(j, end='    ')
        print()

def choose_ship(player_name, bs, ms, ss):
    while bs != 0 or ms != 0 or ss != 0:
        print(f"Большие: {bs}. Средние: {ms}. Малые: {ss}.")
        print("Для выбора введите цифру")
        print(f"{player_name}, выберите корабль : \n[1] - Больших кораблей: {bs} (@@@).\n[2] - Средних кораблей: {ms} (@@).\n[3] - Малых кораблей: {ss}. (@)")
        choosen_ship = input()
        if choosen_ship == "1" and bs != 0:

            cd = choose_direct(player_name, bs, ms, ss)
            cm = create_move(current_move, current_field, choosen_ship, cd)
            if cm:
                bs -= 1
        elif choosen_ship == "2" and ms != 0:

            cd = choose_direct(player_name, bs, ms, ss)
            cm = create_move(current_move, current_field, choosen_ship, cd)
            if cm:
                ms -= 1
        elif choosen_ship == "3" and ss != 0:

            cd = choose_direct(player_name, bs, ms, ss)
            cm = create_move(current_move, current_field, choosen_ship, cd)
            if cm:
                ss -= 1
        else:
            print("Такие корабли у вас кончились!!!")



def choose_direct(player_name, bs, ms, ss):
    print("Для выбора введите цифру")
    print(f"{player_name}, выберите направление: \n[1] - Горизонатльно\n[2] - Вертикально")
    choosen_direct = (input())
    if len(choosen_direct) != 1 and (choosen_direct != "1" or choosen_direct != "2"):
        print("Ошибка!")
        choose_direct(player_name, bs, ms, ss)
    else:
        return choosen_direct

def clearConsol():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

load()
clearConsol()
print("Расстановка кораблей!")
if current_move == player1_name:
    current_field = field_player1
    choose_ship(current_move, p1_big_ship, p1_medium_ship, p1_small_ship)
else:
    current_field = field_player2
    choose_ship(current_move, p2_big_ship, p2_medium_ship, p2_small_ship)

#
