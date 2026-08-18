import random, sys

print('ROCK, PAPER, SCISSORS')

#these variables keep track of the W, L and D

wins = 0
losses = 0
draws = 0

while True:     #The player Input loop, runs until the player quits with 'q'
    #show the running totals and percentages
    total = wins + losses + draws
    if total > 0:
        print('%s Wins (%.1f%%), %s Losses (%.1f%%), %s Draws (%.1f%%)' % (
            wins, wins / total * 100,
            losses, losses / total * 100,
            draws, draws / total * 100))
    else:
        print('%s Wins, %s Losses, %s Draws' % (wins, losses, draws))
    print('Enter your choice: r, p, s or q')
    player_move = input('>')
    if player_move == 'q':sys.exit() #quit the program
    if player_move != 'r' and player_move != 'p' and player_move != 's':
        print('Type one of r, p, s or q.')
        continue    #invalid input, ask again

#dispay what the player chose:
    if player_move == 'r':
        print('Player move: ROCK')
    elif player_move == 'p':
        print('Player move: PAPER')
    elif player_move == 's':
        print('Player move: SCISSORS')

#display what the computer chose:
    move_number = random.randint(1,3)
    if move_number == 1:
        computer_move = 'r'
        print('Computer move: ROCK')
    elif move_number == 2:
        computer_move = 'p'
        print('Computer move: PAPER')
    else:
        computer_move = 's'
        print('Computer move: SCISSORS')

#display and record win/loss/draw\
    if player_move == computer_move:
        print('It\'s a draw')
        draws += 1
    elif player_move == 'r' and computer_move == 's':
        print('You win.')
        wins += 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win')
        wins += 1
    elif player_move == 's' and computer_move == 'p':
        print('You win')
        wins += 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose')
        losses += 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose')
        losses += 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose')
        losses += 1

