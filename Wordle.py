def score_letter(letter, position, true_word):
    # for example, score_letter("A", 0, "ABBA") should be correct position~
    # ex: >>> score_letter("A", 0, "ABBA")
    #'* Good Job!'
    # score_letter("B", 0, "ABBA")
    #'o Almost there!'
    # score_letter("C", 0, "ABBA")
    # '- Try Again :('
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
    guess = input("Guess the word: ")
    print(score_word(guess, true_word))


message = score_word("APPB","ABBA")
print(message)

get_and_score_guess("across")


