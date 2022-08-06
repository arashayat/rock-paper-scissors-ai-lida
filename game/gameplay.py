import random
import messages

# the method to go to the user panel
def player_panel(player):
    # welcome the user
    messages.panel_greetings(player.name)

    while True:
        # give user the choices
        messages.panel_choices()

        match input():
            case '1': # if the user wants to start a game
                start_game(player)

            case '2': # if the user wants to see his/her stats
                messages.show_stats(player)
                    
            case '3': # if the user wants to log out
                messages.logged_out()
                return

            case _: # if the input of the user is invalid
                messages.invalid_input()

def start_game(player):
    
    # play the game with the acquired number of rounds
    def play_game(num_rounds):

        user_score = 0
        pc_score = 0

        
        for round in range(1, num_rounds+1):

            while True: # we use the true while to handle invalid inputs or draws

                messages.game_play(round, num_rounds)

                # pc chooses its move
                pc_move = random.choice(['rock', 'paper', 'scissors'])

                # user chooses her/his move
                user_move = input()
                match user_move: # checking the moves and change the scores accordingly
                    case 'rock':
                        if pc_move == 'paper':
                            pc_score+=1
                            messages.game_round_result(pc_move, user_move, False, user_score, pc_score)
                            break
                        elif pc_move == 'scissors':
                            user_score+=1
                            messages.game_round_result(pc_move, user_move, True, user_score, pc_score)
                            break
                        else:
                            messages.game_draw()

                    case 'paper':
                        if pc_move == 'scissors':
                            pc_score+=1
                            messages.game_round_result(pc_move, user_move, False, user_score, pc_score)
                            break
                        elif pc_move == 'rock':
                            user_score+=1
                            messages.game_round_result(pc_move, user_move, True, user_score, pc_score)
                            break
                        else:
                            messages.game_draw()

                    case 'scissors':
                        if pc_move == 'rock':
                            pc_score+=1
                            messages.game_round_result(pc_move, user_move, False, user_score, pc_score)
                            break
                        elif pc_move == 'paper':
                            user_score+=1
                            messages.game_round_result(pc_move, user_move, True, user_score, pc_score)
                            break
                        else:
                            messages.game_draw()

                    case _: # if the move of user is invalid
                        messages.invalid_input()

        # calculate the winner at the end of the game
        if user_score > pc_score:
            messages.game_result(True)
            return True
        else:
            messages.game_result(False)
            return False


    messages.game_greetings(player.name)

    while True: # we use the true while to handle invalid user inputs (if even)

        messages.game_choice()

        num_rounds = int(input())

        if num_rounds%2 == 0:
            messages.game_not_odd()
        else:

            # play the game and choose the winner
            is_winner = play_game(num_rounds)       

            if is_winner:
                player.update_stats(True) 
            else:
                player.update_stats(False)
            
            break


