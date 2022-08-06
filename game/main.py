import player
import messages
import gameplay
import pickle


if __name__ == "__main__":
    
    # load the dictionary and make one if doesn' exist
    try:
        players = pickle.load(open("../playersdict.pickle", "rb"))
    except (OSError, IOError) as e:
        players = {}
    
    

    # give user the greetings message for the first time
    messages.greetings()

    while True:

        # give the user the options to choose from
        messages.choices()

        # wait for user's answer and proceed accordingly
        match input():
            case '1': # if the user wants to create an account
                player.create_account(players)

            case '2': # if the user wants to login to his/her account
                login = player.login_account(players)

                # if the user has logged in
                if login != False:
                    gameplay.player_panel(login)

            case '3': # if the user wants to see the scoreboard
                player.scoreboard(players)

            case '4': # if the user wants to exit the program
                messages.exit_program()
                exit()

            case _: # if the input of the user is invalid
                messages.invalid_input()
        
        # save players dictionary after each action
        with open('../playersdict.pickle', 'wb') as handle:
            pickle.dump(players, handle, protocol=pickle.HIGHEST_PROTOCOL)
                