import hangman.io


def init_state(secret: str, max_tries: int) -> dict:
    return  {
            "secret": secret,   
            "display": ["_" for i in secret], 
            "guessed": set(),   
            "wrong_guesses": 0,   
            "max_tries": max_tries  
    }        
                                        

def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:
    if ch not in guessed:
        return "well Dun!!"
    return "oops alrady guessed!"

def apply_guess(state: dict, ch: str) -> bool:
    if ch in state["secret"]:
        return True
    return False

def is_won(state: dict) -> bool:
    if "_" not in state["display"]:
        return True
    return False

def is_lost(state: dict) -> bool:
    return state["wrong_guesses"] >= state["max_tries"]

def render_display(state: dict) -> str:
    for i in range(len(state["secret"])):  
        for j in state["guessed"]:
            if j == state["secret"][i]:
                state["display"][i] = j
    return state["display"]          

def render_summary(state: dict) -> str:
    return f'the word: {state["secret"]}\n your guessed: {state["guessed"]}'

                

            
        
    
    