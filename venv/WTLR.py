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

def load():
    sys.stdout.write("Загрузка")
    for i in range(3):
        time.sleep(.1)
        sys.stdout.write('.')
        #sys.stdout.flush()
        time.sleep(.3)
    sys.stdout.write('\n')

def move(player_name):
    print(f"Ходит: {player_name}!")
    if player_name == player1_name:
        print(field_player1)
    else:
        print(field_player2)

def create_move(player_move, field):
    display_field(field)
    move_p = input("Введите координаты: ")
    if len(move_p) == 2 and move_p[0].isdigit() == False and move_p[1].isdigit() == True:
        print("Есть!")
        if player_move == player1_name:
            current_move = player2_name
            current_field = field_player2
        else:
            current_move = player1_name
            current_field = field_player1

    else:
        print("Никак нет!", "Ошибка. Координаты состоят из двухсимволов пример: b2")
        create_move(player_move, field)

    return move_p

def place_ship():
    print(cm)

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
    global cd
    global cm
    while bs != 0 or ms != 0 or ss != 0:
        print(bs, ms, ss, sep=", ")
        print("Для выбора введите цифру")
        print(f"{player_name}, выберите корабль : \n[1] - Больших кораблей: {bs} (@@@).\n[2] - Средних кораблей: {ms} (@@).\n[3] - Малых кораблей: {ss}. (@)")
        choosen_ship = input()
        if choosen_ship == "1" and bs != 0:
            bs -= 1
            cd = choose_direct(player_name, bs, ms, ss)
            cm = create_move(current_move, current_field)
        elif choosen_ship == "2" and ms != 0:
            ms -= 1
            cd = choose_direct(player_name, bs, ms, ss)
            cm = create_move(current_move, current_field)
        elif choosen_ship == "3" and ss != 0:
            ss -= 1
            cd = choose_direct(player_name, bs, ms, ss)
            cm = create_move(current_move, current_field)
        else:
            print("Ошибка!")



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
    choose_ship(current_move, p1_big_ship, p1_medium_ship, p1_small_ship)
else:
    choose_ship(current_move, p2_big_ship, p2_medium_ship, p2_small_ship)

#
