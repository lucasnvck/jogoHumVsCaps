import menu_interactions.cli_prints as cli_prints
from menu_interactions.end_game import game_ended_on_first_menu
import utils.clear_terminal as cl

expected_options = ["1", "2"]

def start_menu():
    cli_prints.first_menu_choice()
    user_menu_choice = input()

    while user_menu_choice not in expected_options:
        cl.clear_terminal()
        cli_prints.first_menu_choice()
        print("Por favor, escolha apenas algo válido.")
        user_menu_choice = input()

    match user_menu_choice:
        case "1":
                print("Função de iniciar o game")
        case "2": 
                game_ended_on_first_menu()