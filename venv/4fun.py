import time, sys, os


class Player():
    player_name = ""

    big_ship = 1
    medium_ship = 2
    small_ship = 3
    alive_ships = 6

class Field():
    field_name = f"{Player.player_name}_field"

    def __init__(self):
        self.field = [
            ["#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#"]
        ]
        self.mark_field = [
            ["#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#"]
        ]
        self.ship_location = {
        }
    coordinates = ["a","b","c","d","e","f"]


class Game():
    def field(name):
        if name == player1.player_name:
            current_field = field1.field
            current_move = player1.player_name
        else:
            current_field = field2.field
            current_move = player2.player_name
        return current_move, current_field

    def beggin():
        player1.player_name = str(input("Введите имя первого игрока: "));
        player2.player_name = str(input("Введите имя второго игрока: "));
        for i in range(1, Player.big_ship+1):
            field1.ship_location.setdefault(f"bs{i}", [])
            field2.ship_location.setdefault(f"bs{i}", [])
        for i in range(1, Player.medium_ship+1):
            field1.ship_location.setdefault(f"ms{i}", [])
            field2.ship_location.setdefault(f"ms{i}", [])
        for i in range(1, Player.small_ship + 1):
            field1.ship_location.setdefault(f"ss{i}", [])
            field2.ship_location.setdefault(f"ss{i}", [])

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

    def get_cords():
        cord = []
        while cord != None:
            try:
                cord = [str(input("Введите координату (Буква слева): ")),
                        int(input("Введите координату (Цифра сверху): "))]
                if cord[0] not in Field.coordinates or (cord[1] < 0 or cord[1] > 6):
                    print("Ошибка")
                else:
                    #print("Координаты записаны!")
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
            cm = Game.place_ship_horizonatal(y, x, ship_size, field)
        else:
            x = Field.coordinates.index(cord[0])
            y = cord[1] - 1
            cm = Game.place_ship_vertical(y, x, ship_size, field)
        return cm



    def place_ship_horizonatal(y, x, ship_size, field):
        ship_coordinates = []
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
                    ship_coordinates.append(x)
                    ship_coordinates.append(k)
                print("Корабль на воде!")
            elif 6 - y < ship_size:
                print("Не хватает места для корабля такого размера!")
                flag = False
        Game.display_field(field)
        return flag, ship_coordinates

    def place_ship_vertical(y, x, ship_size, field):
        ship_coordinates = []
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
                    ship_coordinates.append(k)
                    ship_coordinates.append(y)
            elif 6 - x < ship_size:
                print("Не хватает места для корабля такого размера!")
                flag = False
        Game.display_field(field)
        return flag, ship_coordinates

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
    def set_value_cords(cords : list, player_name, ship_amount, ship_size):
        if player_name == player1.player_name:
            if ship_size == "1":
                field1.ship_location[f"bs{ship_amount}"] += cords
            elif ship_size == "2":
                field1.ship_location[f"ms{ship_amount}"] += cords
            elif ship_size == "3":
                field1.ship_location[f"ss{ship_amount}"] += cords
            print(field1.ship_location)
        else:
            if ship_size == "1":
                field2.ship_location[f"bs{ship_amount}"] += cords
            elif ship_size == "2":
                field2.ship_location[f"ms{ship_amount}"] += cords
            elif ship_size == "3":
                field2.ship_location[f"ss{ship_amount}"] += cords
            print(field2.ship_location)


    def choose_ship(player_name, bs, ms, ss):
        current_move = Game.field(player_name)[0]
        current_field = Game.field(player_name)[1]
        while bs != 0 or ms != 0 or ss != 0:
            print(f"Большие: {bs}. Средние: {ms}. Малые: {ss}.")
            print("Для выбора введите цифру")
            print(
                f"{player_name}, выберите корабль : \n[1] - Больших кораблей: {bs} (@@@).\n[2] - Средних кораблей: {ms} (@@).\n[3] - Малых кораблей: {ss}. (@)")
            choosen_ship = input()
            if choosen_ship == "1" and bs != 0:
                cd = Game.choose_direct(player_name, bs, ms, ss)
                cm = Game.create_move(current_move,current_field, choosen_ship, cd)
                Game.set_value_cords(cm[1], player_name, bs, choosen_ship)
                if cm[0]:
                    bs -= 1
            elif choosen_ship == "2" and ms != 0:

                cd = Game.choose_direct(player_name, bs, ms, ss)
                cm = Game.create_move(Game.current_move, current_field, choosen_ship, cd)
                Game.set_value_cords(cm[1], player_name, ms, choosen_ship)
                if cm[0]:
                    ms -= 1
            elif choosen_ship == "3" and ss != 0:

                cd = Game.choose_direct(player_name, bs, ms, ss)
                cm = Game.create_move(Game.current_move, current_field, choosen_ship, "1")
                Game.set_value_cords(cm[1], player_name, ss, choosen_ship)
                if cm[0]:
                    ss -= 1
            else:
                print("Такие корабли у вас кончились!!!")

    def choose_direct(player_name, bs, ms, ss):
        print("Для выбора введите цифру")
        print(f"{player_name}, выберите направление: \n[1] - Горизонатльно\n[2] - Вертикально")
        choosen_direct = (input())
        if len(choosen_direct) != 1 and (choosen_direct != "1" or choosen_direct != "2"):
            print("Ошибка!")
            game1.choose_direct(player_name, bs, ms, ss)
            #choose_direct(player_name, bs, ms, ss)
        else:
            return choosen_direct

    def clearConsol():
        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')


    def queue(count):
        if count % 2 == 0:

            current_field = field2.field
            current_mark_field = field1.mark_field
            current_move = player1.player_name
        else:

            current_field = field1\
                .field
            current_mark_field = field2.mark_field
            current_move = player2.player_name

        return current_move, current_mark_field, current_field


    def shoot(mark_field, current_move, cords, field):
        if field[cords[0]][cords[1]] == "#":
            print('ПРОМАХ!')
            mark_field[cords[0]][cords[1]] = "◯"
            game1.display_field(mark_field)
            return 0
        else:
            print('ПОПАДАНИЕ!')
            mark_field[cords[0]][cords[1]] = "●"
            game1.display_field(mark_field)
            return 1

player1 = Player()
player2 = Player()
field1 = Field()
field2 = Field()


# field1.field = [
#             ["B", "B", "B", "#", "#", "#"],
#             ["#", "#", "#", "#", "#", "#"],
#             ["#", "#", "#", "#", "#", "#"],
#             ["#", "#", "#", "#", "#", "#"],
#             ["#", "#", "#", "#", "#", "#"],
#             ["#", "#", "#", "#", "#", "#"]
#         ]
# field2.field = [
#             ["#", "#", "#", "B", "B", "B"],
#             ["#", "#", "#", "#", "#", "#"],
#             ["#", "#", "#", "#", "#", "#"],
#             ["#", "#", "#", "#", "#", "#"],
#             ["#", "#", "#", "#", "#", "#"],
#             ["#", "#", "#", "#", "#", "#"]
#         ]

game1 = Game
class Main():
    game1.beggin()
    #game1.load()
    game1.clearConsol()
    game1.current_move = player1.player_name

    print("Расстановка кораблей!", "\n", f"Ходит игрок: {game1.current_move}")

    game1.choose_ship(game1.current_move, player1.big_ship, player1.medium_ship, player1.small_ship)

    print(f"Игрок: {game1.current_move} закончил расставлять корабли")


    current_field = field2.field
    game1.current_move = player2.player_name
    game1.move(player2.player_name)
    game1.choose_ship(game1.current_move, player2.big_ship, player2.medium_ship, player2.small_ship)

    game1.clearConsol()
    print("БОЙ НАЧИНАЕТСЯ")
    game1.load()
    game1.clearConsol()
    current_field = field2.field
    game1.current_move = player1.player_name
    count = 0
    game1.display_field(field1.mark_field)
    flag = False
    while player1.alive_ships != 0 and player2.alive_ships != 0:

        q = game1.queue(count)
        current_move = q[0]
        current_mark_field = q[1]
        current_field = q[2]
        if flag == True:
            game1.display_field(current_mark_field)

        game1.move(current_move)

        cords = game1.get_cords()
        cords[0] = Field.coordinates.index(cords[0])
        cords[1] = cords[1] -1
        if game1.shoot(current_mark_field, current_move, cords, current_field) == 0:
            flag = True
            count += 1
            print("Переход хода")
        else:
            flag = False


Main()