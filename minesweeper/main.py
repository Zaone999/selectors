from src.gameBoard import GameBoard
from src.database import Player, session
from time import time
def get_player_name():
    while True:
        player_name = input('Enter your name: ')
        if len(player_name) > 50 and len(player_name) < 1:
            print('Invalid name')
        else:
            break
    return player_name

def get_game_difficulty():
    while True:
        difficulty = input('Enter game difficulty: ')
        if difficulty in ['easy', 'medium', 'hard']:
            break
        else:
            print('Invalid difficulty')
    return difficulty

def play():
    print('Playing Minesweeper')
    status = 'undecided'
    player_name = get_player_name()
    difficulty = get_game_difficulty()
    game_board = GameBoard(difficulty)
    game_board.fill()
    try:
        start_time = time()
        while True:
            print(game_board)
            x, y = input('Enter coordinates (eg B 2 ): ').split()
            x, y = ord(x) - 65, int(y) - 1
            game_board.propagate(x, y)
            if game_board.bomb_found:
                print('Game over')
                status = 'lose'
                break
            if all(cell.is_open or cell.is_bomb for row in game_board.board for cell in row):
                print('You win!')
                status = 'win'
                break
    except KeyboardInterrupt:
        print('Quitting game')
    finally:
        end_time = time()
        game_time = end_time - start_time
        print(game_board)
        print('Saving game')
        # Save result to database
        if status == 'win':
            player = Player(name=player_name, timer=game_time)                                                                                                          
            session.add(player)
            session.commit()

         
def leaderboard():
    print('Leaderboard')
    # Get last played games from database
    players = session.query(Player).limit(10)
    for player in players:
        print(f'{player.name} in {player.timer:.2f} seconds')

while __name__ == '__main__':
    print('Welcome to Minesweeper!')
    print('1. Play')
    print('2. Leaderboard')
    print('3. Quit')
    choice = input('Enter your choice: ')
    if choice == '1':
        play()
    elif choice == '2':
        leaderboard()
    elif choice == '3':
        break
    else:
        print('Invalid choice')