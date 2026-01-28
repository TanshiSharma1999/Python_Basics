import random

word_list=["slaying","pookie","magenta","banana","pomegranate","iceland","pajamas","artificial","intelligence"]

#Create a function to make a jumble word.

def Make_me_jumble(word):#For example if the word was "Mark".
  word_to_list=list(word)#Then after becoming a list it would look like ["m","a","r",K"].
  random.shuffle(word_to_list)#Then it would jumble the list like this ["k","m","r","a"].
  return "".join(word_to_list)#Then change back that shuffled list into a string/word "kmra" 



def want_hint(word):
    # Provide the first letter of the word as a hint
    return "The first letter of the word is: {}".format(word[0].upper())
  
def My_game():
    rounds=7
    score=0
    print(" *.~.~.~Welcome To Jumbled Letter Game~.~.~.* ")
    for i in range(1,rounds+1):#this just repeats the game 7 times
        word=random.choice(word_list)
        jumble=Make_me_jumble(word)
    
        print("Round "+str(i))
        print("Here is the scrambled word:" + jumble )
    
        hint_choice = input("Do you want a hint? (Y/N): ").upper()

        if hint_choice == "Y":#Check if user wants a hint
            print(want_hint(word))
        guess = input("Guess the original word: ").lower()

        while not guess.isalpha():#if guess was not an alphabet
            print("Please enter a valid word!")
            guess = input("Guess the original word: ").lower()

        if guess == word:#check if word==guess
            print("Well Done! That's correct!")
            score += 1  # Increase the score for a correct guess
        else:
            print("Oh No! The correct word was: {}".format(word))
    
        # Final score
        print("\nGame Over! Final Score = {}/{}.".format(score,rounds))
            
    
My_game()