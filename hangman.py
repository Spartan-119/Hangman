# Program to create a simple Hangman game
import random
import word_list

def get_word():
    word = "Aman" #random.choice(word_list)
    word = word.upper()
    return word

def Play(word):
    
    # initially only underscores will be displayed
    completed_word = "_" * len(word)
    
    guessed = False
    
    guessed_words = []
    guessed_letters = []
    tries_left = 6
    
    print("Let's play hangman!")
    print(display_hangman(tries_left))
    print(completed_word)
    print()
    print()
    
    while not guessed and tries_left > 0:
        guess = input("Please enter a letter or a word: ").upper()
        
        # there will be 3 possible conditionals
        if len(guess) == 1 and guess.isalpha():
            
            if guess in guessed_letters:
                print("You already guessed this letter: ", guess)
            elif guess not in guessed_letters:
                print(guess, " is NOT in the word!")
                tries_left -= 1
                guessed_letters.append(guess)
            else:
                print("Good job! ", guess, " is in the word")
                guessed_letters.append(guess)
                
                # Now here we will display all the occurances of the correct
                # letter in the word
                word_as_list = list(completed_word)
                index = []
                
                count = -1
                for i in word:
                    count += 1
                    if i == guess:
                         index.append(count)
                
                for i in index:
                    word_as_list[i] = guess
                
                completed_word = "".join(word_as_list)
                
                guessed = True # to exit the loop
        
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word")
            elif guess != word:
                print(guess, " is NOT the word")
                tries_left -= 1
                guessed_words.append(guess)
            else:
                guessed = True # to exit the loop
                completed_word = word
        
        else:
            print("This is NOT a valid guess!")
        
        print(display_hangman(tries_left))
        print(completed_word)
        print("\n")
    
    if guessed:
        print("Congratulations, you win!!!")
    else:
        print("Sorry, you ran out of attempts. The word was ", word, ". Better luck next time :)")
        


def display_hangman(tries_left):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries_left]


def main():
    word = get_word()
    Play(word)
    
    # giving the option to the user to continue playing or not
    while input("Do you want to play again? Y/N: ").upper() == "Y":
        word = get_word()
        Play(word)
        
if __name__ == "__main__":
    main()