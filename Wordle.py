USER_PROMPT = "Guess the world: "

def score_letter(letter, position, true_word):
    if (true_word[position]==letter): 
        return "*" #for correct position
    if (letter in true_word):
        return "o" #for correct letter, incorrect position
    else:
        return "-"

def score_word(guess, true_word):
    # score_word("APPL", "ABBA")
    # "*---"
    if len(guess) != len(true_word):
        return "THE TWO WORDS ARE NOT THE SAME LENGHT"

    score = ""

    N = len(true_word)
    for position in range(N):
        score = score + score_letter(guess[position], position, true_word)
    return score

def get_and_score_guess(true_word):
    guess = input(USER_PROMPT)
    score= score_word(guess, true_word)
    print(len(USER_PROMPT) * " " + score)
    return score

def loop_until_sucess(true_word):
    correct_guess = False
    while not correct_guess:
        score = get_and_score_guess(true_word)
        if score == 6 * "*":
            correct_guess = True


message = score_word("APPB","ABBA")
print(message)

loop_until_sucess("across")




