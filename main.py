from hangman.game import init_state,is_won,validate_guess,render_display,render_summary,is_lost
from hangman.words import choose_secret_word
from hangman.io import print_status,print_result,prompt_guess


words = ["apple"]


def play(words: list[str], max_tries: int = 6) -> None:
    the_rand_secret = choose_secret_word(words)
    create_state = init_state(the_rand_secret, max_tries)
    while not is_won(create_state) and not is_lost(create_state):
        user_asking_letter = prompt_guess()
        create_state["guessed"].add(user_asking_letter)
        print(validate_guess(user_asking_letter, create_state["guessed"]))
        create_state["wrong_guesses"] += 1
        display = render_display(create_state)
        print(print_status(create_state))
        
    print(print_result(create_state))   
    print(render_summary(create_state))
        
if __name__ == "__main__":
    play(words,6)