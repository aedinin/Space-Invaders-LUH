from game_logic import reset_game, update_game

print("Game started!")
lives, enemies, state = reset_game()

while True:
    command = input("Enter a command (d = damage, h = hit, r = restart, q = quit): ")

    if command == "q":
        break

    if command == "r":
        lives, enemies, state = reset_game()
        print("New game started!")
        continue

    if state != "playing":
        continue

    player_hit = command == "d"
    enemy_hit = command == "h"
    lives, enemies, state = update_game(player_hit, enemy_hit, lives, enemies, state)





