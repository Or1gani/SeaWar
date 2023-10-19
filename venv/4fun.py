import time, sys, os


class Player():
    player_name = ""

    big_ship = 1
    medium_ship = 2
    small_ship = 3
    alive_ships = 6

class Field():
    field_name = f"{Player.player_name}_field"

    field = [
        ["#", "#", "#", "#", "#", "#"],
        ["#", "#", "#", "#", "#", "#"],
        ["#", "#", "#", "#", "#", "#"],
        ["#", "#", "#", "#", "#", "#"],
        ["#", "#", "#", "#", "#", "#"],
        ["#", "#", "#", "#", "#", "#"]
    ]
    coordinates = ["a","b","c","d","e","f"]


class Game():
    current_move = ""
    def beggin():

        player1.player_name = str(input("Введите имя первого игрока: "));
        player2.player_name = str(input("Введите имя второго игрока: "));

    def load():
        sys.stdout.write("Загрузка")
        for i in range(3):
            time.sleep(.05)
            sys.stdout.write('.')
            # sys.stdout.flush()
            time.sleep(.25)
        sys.stdout.write('\n')
    def move(player_name):
        print(f"Ходит: {player_name}!")
        if player_name == player1_name:
            print(field_player1)
        else:
            print(field_player2)
    def get_cords():
        cord = []
        while cord != None:
            try:
                cord = [str(input("Введите координату (Буква слева): ")),
                        int(input("Введите координату (Цифра сверху): "))]
                if cord[0] not in Field.coordinates or (cord[1] < 0 or cord[1] > 6):
                    print("Ошибка")
                else:
                    print("Координаты записаны!")
                    break
            except ValueError:
                print("Ошибка")
        return cord

    def create_move(player_move, field, cs, direct):
        Game.display_field(field)
        if cs == "1":
            print("Корабль: Большой @@@")
            ship_size = 3
        elif cs == "2":
            print("Корабль: Средний @@")
            ship_size = 2
        else:
            print("Корабль: Малый @")
            ship_size = 1
        cord = Game.get_cords()
        if direct == "1":
            x = Field.coordinates.index(cord[0])
            y = cord[1] - 1
            cm = Game.place_ship_horizonatal(y, x, ship_size, current_field)
        else:
            x = Field.coordinates.index(cord[0])
            y = cord[1] - 1
            cm = Game.place_ship_vertical(y, x, ship_size, current_field)
        return cm

    def place_ship_horizonatal(y, x, ship_size, field):
        flag = False
        break_flag = False
        for i in range(x - 1, x + 2):
            if break_flag:
                break
            if i < 0 or i >= 6:
                continue
            for j in range(y - 1, ship_size + y + 1):
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
        Game.display_field(field)
        return flag

    def place_ship_vertical(y, x, ship_size, field):
        flag = False
        break_flag = False
        for i in range(x - 1, ship_size + x + 1):
            if break_flag:
                break
            if i < 0 or i >= 6:
                continue
            for j in range(y - 1, y + 2):
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
            if 6 - x >= ship_size:
                for k in range(x, ship_size + x):
                    field[k][y] = "B"
            elif 6 - x < ship_size:
                print("Не хватает места для корабля такого размера!")
        Game.display_field(field)
        return flag

    def display_field(field):
        row = 0
        colums = 0
        for k in range(6):
            row += 1
            print('   ', f"{row}", end='')
        print()

        for i in field:
            print(Field.coordinates[colums], end='   ')
            colums += 1
            for j in i:
                print(j, end='    ')
            print()

    def choose_ship(player_name, bs, ms, ss):
        while bs != 0 or ms != 0 or ss != 0:
            print(f"Большие: {bs}. Средние: {ms}. Малые: {ss}.")
            print("Для выбора введите цифру")
            print(
                f"{player_name}, выберите корабль : \n[1] - Больших кораблей: {bs} (@@@).\n[2] - Средних кораблей: {ms} (@@).\n[3] - Малых кораблей: {ss}. (@)")
            choosen_ship = input()
            if choosen_ship == "1" and bs != 0:
                cd = Game.choose_direct(player_name, bs, ms, ss)
                cm = Game.create_move(Game.current_move, Field.field, choosen_ship, cd)
                if cm:
                    bs -= 1
            elif choosen_ship == "2" and ms != 0:

                cd = Game.choose_direct(player_name, bs, ms, ss)
                cm = Game.create_move(Game.current_move, Field.field, choosen_ship, cd)
                if cm:
                    ms -= 1
            elif choosen_ship == "3" and ss != 0:

                cd = Game.choose_direct(player_name, bs, ms, ss)
                cm = Game.create_move(Game.current_move, Field.field, choosen_ship, 1)
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

player1 = Player()
player2 = Player()
field1 = Field()
field2 = Field()
game1 = Game
current_field = field1.field

class Main():
    game1.beggin()
    #game1.load()
    game1.clearConsol()
    game1.current_move = player1.player_name


    print("Расстановка кораблей!", "\n", f"Ходит игрок: {game1.current_move}")

    while (player1.big_ship != 0 and player1.medium_ship  != 0 and player1.small_ship != 0):
        game1.choose_ship(game1.current_move, player1.big_ship, player1.medium_ship, player1.small_ship)
        pass

    print(f"Игрок: {player1.player_name} закончил расставлять корабли")

    while (player2.big_ship != 0 and player2.medium_ship  != 0 and player2.small_ship != 0):

        pass
    while player1.alive_ships != 0 or player2.alive_ships != 0:

        pass

Main()