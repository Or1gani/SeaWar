# a = [0,4, 0,1, 0,2, 0,0, 0,3]
# b = [0,0]
# for i in range(0,len(a)-1,2):
#     if b[0] == a[i] and b[1] == a[i+1]:
#         print(True)
#     else:
#         print(False)
#     print(a[i])
alive_ships1 = 1
alive_ships2 = 1

while alive_ships1 > 0 and alive_ships2 > 0:
    alive_ships1 -=1
print(alive_ships1, alive_ships2)