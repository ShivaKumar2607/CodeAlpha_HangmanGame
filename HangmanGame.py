import random
WORDS=["python","java","javascript","html","css"]
def choose_word():
    return random.choice(WORDS)
def display_word(word,guessed_letters):
    result=""
    for i in range(len(word)):
        if word[i] in guessed_letters:
            result += word[i]+" "
        else:
            result += "_ "
    return result  

def get_guess(guessed_letters):
    while(True):
        guess=input("Enter a letter: ").lower()
        if guess.isalpha() and len(guess)==1 and guess not in guessed_letters:
            break
        else:
            print("invalid input, enter again")
    return guess
def main():
    word=choose_word()
    guessed_letters=[]
    wrong_guesses = 0   
    while wrong_guesses < 6 and not all(letter in guessed_letters for letter in word):
        print(f"Find the word: {display_word(word,guessed_letters)}")
        print(f"You have { 6 - wrong_guesses} attempts to guess the word.")
        guess=get_guess(guessed_letters)
        guessed_letters.append(guess)
        if guess not in word:
            wrong_guesses +=1
    if all(letter in guessed_letters for letter in word):
        print("Congratulations, you won!")
    else:
        print(f"You lost! the actual word is: {word}")

main()
