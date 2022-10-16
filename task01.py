#  1. Создайте программу для игры в "Крестики-нолики".
game = """Крестики-нолики    Номер позиции
   |   |             7 | 8 | 9
---+---+---         ---+---+---
   |   |             4 | 5 | 6
---+---+---         ---+---+---
   |   |             1 | 2 | 3
"""

positions = [
    None,
    (5, 1),
    (5, 5),
    (5, 9),
    (3, 1),
    (3, 5),
    (3, 9),
    (1, 1),
    (1, 5),
    (1, 9),
]

win = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3],
    [7, 5, 3],
    [1, 5, 9]
]

board = []
for row in game.splitlines():
    board.append(list(row))

player = "X"
playing = True
turn = 0
while True:
    for t in board:
        print("".join(t))
    if not playing:
        break
    if turn == 9:
        print("Никто не выиграл!")
        break
    position = int(input("Выбирайте, ваш ход (1-9) (Игрок '%s'): " % player))
    if position < 1 or position > 9:
        print("Некорректный ввод! Выбирайте  от 1 до 9.")
        continue

    if board[positions[position][0]][positions[position][1]] != " ":
        print(board[positions[position][0]][positions[position][1]])
        print("Позиция уже занята. Выбирайте другую")
        continue

    board[positions[position][0]][positions[position][1]] = player

    for p in win:
        for x in p:
            if board[positions[x][0]][positions[x][1]] != player:
                break
        else:
            print("\nИгрок '%s' выиграл (%s): " % (player, p))
            playing = False
            break
    player = "X" if player == "O" else "O"
    turn += 1

print("\nИгра окончена!")
