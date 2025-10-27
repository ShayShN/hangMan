from tkinter import N
import hangman.game


def prompt_guess() -> str:
    while True:
        user_ask = input("enter a letter: ")
        if user_ask and user_ask.isalpha() and len(user_ask) == 1:
            return user_ask.lower()
        continue

def print_status(state: dict) -> None:
    return f''' the word: {state["display"]}\n
                your guessed: >> {state["guessed"]}\n
                tries left: >> {state["max_tries"] - state["wrong_guesses"]}
                '''                
    
def print_result(state: dict) -> None:
    if hangman.game.is_won(state):
        return f''' you won!!!\n
                    the secret: >> {state["secret"]}\n
                    your guessed: >> {state["guessed"]}\n
                    '''
    return f''' you are lost!\n
                the secret word is: >>> {state["secret"]}'''