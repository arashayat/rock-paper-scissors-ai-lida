import messages

# player class contains all the information needed for each player
class Player:
    num_win = 0
    num_loss = 0
    total_games = 0
    win_rate = 0.0
    
    # upon creating the account we store the needed info like username and password
    def __init__(self, username, name, password):
        self.username = username
        self.name = name
        self.__password = password

    # checking if the password is correct when logging (True/False)
    def check_password(self, password):

        if self.__password == password:
            return True
        else:
            return False
    
    # updating the number of wins or losses and the win rate after each game
    def update_stats(self, is_win):
        
        self.total_games += 1

        if is_win:
            self.num_win += 1
        else:
            self.num_loss += 1
        
        self.win_rate = self.num_win / self.total_games

# the process of creating an account
def create_account(players):

    def get_username(): # get the username from the user

        while True:
            messages.enter_username()

            # get the username from the user
            username = input()
            
            if username == '1': # if the user enters 1 and wants to go back to the menu
                messages.back_to_menu()
                return False

            elif ' ' in username: # if the username has spaces in it
                messages.space_in_username()

            elif len(username) < 5: # if the username is less than 5 characters
                messages.invalid_username()

            elif username in players: # if the username already exists
                messages.redundant_username()

            else: # if the username is correct (proceed to taking the password and name)
                return username
                
    def get_name(): #get user's full name

         while True:
            messages.enter_name()

            # get the name from the user
            name = input()
            
            if name == '1': # if the user enters 1 and wants to go back to the menu
                messages.back_to_menu()
                return False

            elif len(name) < 1: # if the name is empty
                messages.invalid_name()

            else: # if the name is correct (proceed to taking the password)
                return name

    def get_password(): # get the password from the user

        while True:
            messages.enter_password()

            # get the password from the user
            password = input()
            
            if password == '1': # if the user enters 1 and wants to go back to the menu
                messages.back_to_menu()
                return False

            elif len(password) < 5: # if the password is less than 5 characters
                messages.invalid_password()

            else: # if the password is correct (proceed to taking the password)
                return password
    
    
    username = get_username()

    # user wants to go back to the menu
    if username == False:
        return
    
    name = get_name()

    # user wants to go back to the menu
    if name == False:
        return
    
    password = get_password()

    # user wants to go back to the menu
    if password == False:
        return

    # when all the inputs are correct create account and return
    players[username] = Player(username, name, password)
    messages.account_created()    

# the process of logging in
def login_account(players):

    def check_username():
        while True:
            messages.enter_username()

            # get the username from the user
            username = input()
            
            if username == '1': # if the user enters 1 and wants to go back to the menu
                messages.back_to_menu()
                return False

            elif username not in players: # if the username does not exist
                messages.username_not_exist()
            
            else: # if the username exists
                return username

    def check_password(username):
        
        while True:
            messages.enter_password()

            # get the password from the user
            password = input()

            if password == '1': # if the user enters 1 and wants to go back to the menu
                messages.back_to_menu()
                return False
            
            elif not players[username].check_password(password):
                messages.password_not_match()
            
            else:
                return True
    
    username = check_username()

    # user wants to go back to the menu
    if username == False:
        return False
    
    
    password = check_password(username)

    # user wants to go back to the menu
    if password == False:
        return False

    # when all the inputs are correct create account and return
    messages.logged_in()
    return players[username]


def scoreboard(players):
    scores = []
    # get each players wins and username to sort
    for username, player in players.items():
        scores.append((player.num_win, username))
    
    # sort players by number of wins
    scores.sort(reverse=True)

    print("position|username|wins|losses|winrate")
    for pos, item in enumerate(scores, start = 1):
        player = players[item[1]]
        print(f'{pos}  {player.username}  {player.num_win}  {player.num_loss}  {player.win_rate}')

    print()
