import random


def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "Draw"

    if is_win(user, computer):
        return "You won"

    return "You lost"

    # r > s, s > p, p > r


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True
