def reset_game():
    return 3, 1, "playing"

def update_game(player_hit, enemy_hit, lives, enemies, state):
    if player_hit:
        lives -= 1
        print(f"Lives left: {lives}")

        if lives == 0:
            print("Game over!")
            state = "lost"

    if enemy_hit:
        enemies -= 1
        print(f"Enemies left: {enemies}")

        if enemies == 0:
            print("You win!")
            state = "won"

    return lives, enemies, state