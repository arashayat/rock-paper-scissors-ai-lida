
# printing the greetings when launching the program
def greetings():
    print('Hello there, welcome to the game of rock, paper, scissors')

# printing the choices of the user in the menu  
def choices():
    print('please choose one of the options below by typing in the number of the choice:')
    print('1.Signup\n2.Login\n3.Scoreboard\n4.Exit')

def invalid_input():
    print("invalid input")

def exit_program():
    print('exiting the program, have a nice day.')

# printing the go back to the menu message
def back_to_menu():
    print('going back to the menu')

#  printing the signup and login menu messages
def enter_username():
    print('Please enter the username: (to go back to the menu enter 1)')

def space_in_username():
    print("The username can't have spaces in it")

def invalid_username():
    print('The username entered cannot be less than 5 characters')

def redundant_username():
    print('This username already exists')

def enter_name():
    print('Please enter your full name: (to go back to the menu enter 1)')

def invalid_name():
    print('The name entered cannot be empty')


def enter_password():
    print('Please enter the password: (to go back to the menu enter 1)')

def invalid_password():
    print('Password is too weak (less than 5 characters')

def account_created():
    print("account created successfuly")
    back_to_menu()

def username_not_exist():
    print("username doesn't exist")

def password_not_match():
    print("the password is incorrect")

def logged_in():
    print('logged in successfuly')
    back_to_menu()

# player panel messages
def panel_greetings(name):
    print(f"welcome {name}.")

def panel_choices():
    print('please choose one of the options below by typing in the number of the choice:')
    print('1.start a game\n2.your stats\n3.save and logout')

def show_stats(player): # show stats for the requested player
    print(f"{player.name}, your stats are as follows:")
    print(f"number of wins: {player.num_win}")
    print(f"number of losses: {player.num_loss}")
    print(f"win rate: {int(player.win_rate*100)}%")

def logged_out():
    print("successfuly logged out")
    back_to_menu()

def scoreboard():
    pass

# messages for the gameplay
def game_greetings(name):
    print(f"welcome to the game {name}.")

def game_choice():
        print("enter the number of rounds (only odd numbers)")

def game_not_odd():
    print('please enter an odd number of rounds')

def game_play(round, limit):
    print(f'round {round}/{limit}, go your move(rock, paper, scissors)')

def game_round_result(pc_move, user_move, is_winner, user_score, pc_score):
    print(f"PC move is {pc_move}, your move is {user_move}")

    if is_winner:
        print("you won the round")
    else:
        print("the PC won the round")

    print(f"your score is {user_score}, PC score is {pc_score}")

def game_result(is_winner):

    if is_winner:
        print('you won')
    else:
        print("PC won")

def game_draw():
    print("it's a draw")


