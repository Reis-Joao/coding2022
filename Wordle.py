def score_letter(letter, position, true_word):
    # for example, score_letter("A", 0, "ABBA") should be correct position~
    # ex: >>> score_letter("A", 0, "ABBA")
    #'Good Job!'
    # score_letter("B", 0, "ABBA")
    #'Almost there!'
    # score_letter("C", 0, "ABBA")
    # 'Try Again :('
    if (true_word[position]==letter): 
        return "Good Job!" #for correct position
    if (letter in true_word):
        return "Almost there!" #for correct letter, incorrect position
    else:
        return "Try Again :("

def score_word(guess, true_word):
    # score_word("APPL", "ABBA")
    # "*---"
    N = len(true_word)
    for position in range(N):
        print(position, guess[position], true_word[position], score_letter(guess[position], position, true_word))

score_word("APPL", "ABBA")