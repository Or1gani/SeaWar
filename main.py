import time

field = [

    ["B", "B", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#"],
    ["#", "B", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#"]
]
coordinates = ["a","b","c","d","e","f"]

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


def get_cords():
    cord = []
    while cord != None:
        try:
            cord = [str(input()), int(input())]
            if cord[0] not in coordinates or (cord[1]<0 or cord[1]>6) :
                print("Ошибка")
            else:
                print("Координаты записаны!")
                break
        except ValueError:
            print("Ошибка")
    return cord


def place_ship_horizonatal(y, x, ship_size):
    flag = True
    break_flag = False
    print(x, y)
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
                print("Рядом стоит корабль!")
                flag = False
                break_flag = True
                break

    if flag:
        if 6 - y >= ship_size:
            for k in range(y, ship_size + y):
                field[x][k] = "B"
            print("Корабль на воде!")
        elif 6 - y < ship_size:
            print("Не хватает места для корабля такого размера!")
    display_field(field)
    print(flag)
def place_ship_vertical(y, x, ship_size):
    print(x, y)
    for j in range(y-1, ship_size+y+1):
        if j < 0 or j >= 6:
            continue
        for i in range(x-1, 3):
            if i < 0 or i >= 6:
                continue
            if field[i][j] == "#":
                if field[x][y] == field [i][j] and 6-x >= ship_size:
                    for k in range(x, ship_size+x):
                        print("--------", 6-x)
                        field[k][y] = "B"
                elif 6-x < ship_size:
                    print("Не хватает места для корабля такого размера!")
                    break
    display_field(field)

def display_ship(direct, field, cord, ship, ship_size):
    if direct == "1":
        x = coordinates.index(cord[0])
        y = cord[1] - 1
        place_ship_horizonatal(y, x,ship_size)
    elif direct == "2":
        x = coordinates.index(cord[0])
        y = cord[1] - 1
        place_ship_vertical(y,x, ship_size)



display_field(field)
display_ship("1", field, get_cords(), "1", 3)
#display_ship("1", field, get_cords(), "2", 2)
#display_field(field)
#get_cords()