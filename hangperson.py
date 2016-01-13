#hangman.py
# A program about hanging people if you don't spell things correctly.

from random import randint

words = ["petrichor", "galavant", "shire", "stardust", "bookworm", "galaxy", "doctor"]
numWrong = 0
listedWord = [None]

# A function that starts and plays the hangperson game.
# Users can be wrong a maximum of 5 times before they lose,
# the 6th wrong guess triggering Game Over.
def hangperson():
   global listedWord

   # Greet the user
   print("Let's play a game of hangperson!")

   # Randomly select a word from the list of words
   word_length = len(words)

   random_index = randint(0,word_length-1)
   #Make the randomly selected word into a list object
   listedWord = list(words[random_index])
   
   # Make another list the same length as the word, but with
   # '_' instead of letters. This will track the user's progress.
   # Use the variable name currentState
   currentState = list("_" * len(listedWord))

   #Initialize the wrong guess list
   incorrect = []

   #Print the initial state of the game
   printHangperson(currentState, incorrect)

   # Start the game! Loop until the user either wins or loses
   while currentState != listedWord and numWrong < 6:
     #first ask the user to guess
      guess = userGuess()
      #see if the guess is in the word, update accordingly
      bundledList = updateState(guess, currentState, incorrect) 
      currentState = bundledList[0]
      incorrect = bundledList[1]

      printHangperson(currentState, incorrect)

   # Determine if the user won or lost, and then tell them accordingly
   if listedWord == currentState:
      print("You've won! Congratuations! Your hangperson thanks you.")
      playAgain = input("Would you like to play again? YES or NO?> ")

      if playAgain.lower() == "yes":
         hangperson()

      elif playAgain.lower() == "no":
         print("Thanks for playing!")
         exit()

   elif listedWord != currentState:
      print("You've lost. RIP hangperson.")

# Update the state of the game based on the user's guess.
# guess: a character guessed by the user
# currentState: the current state of the word/game
def updateState(guess, currentState, incorrect):
   global numWrong

   # First, determine if the letter guessed is in the word.
   numInWord = listedWord.count(guess)

      # If it isn't, tell the user and update the numWrong var
   if numInWord == 0:
      numWrong += 1
      incorrect.append(guess)
      print("Incorrect answer! there's " + str(numInWord) + " of the letter " + (guess) + " in the word. Your poor hang person...")
      # If it is, congratulate them and update the state of the game.
   elif numInWord > 0:
      print("Yes, that is an answer! You found " + str(numInWord) + " of the letter " + (guess) + " in the word.")
         #right answer
   #    To update the state, make sure to replace ALL the '_' with
   #    the guessed letter.
   #two conditions in the while loop
      numFound = 0
      index = 0
      while numFound < numInWord and index < len(listedWord):
         #See if letter is in word at index
         if listedWord[index] == guess:
             #while we still have letters to find, keep looping
            currentState[index] = guess
            numFound += 1

         index += 1
   
   # return currentState
   return [currentState, incorrect]


# This helpful function prompts the user for a guess,
# accepting only single letters.
#
# returns a letter
def userGuess():
   guess = input("Guess a letter in the word! (Say 'exit' to stop playing)> ")
   while len(guess) != 1:
      
      #user has given us too long of a response. Check to see if it is exit. Exit if so. 
      if guess.lower() == "exit":
         print("Thanks for playing! Goodbye!")
         exit()
      #make the user guess again if they mistyped. 
      #Give an error message and loop back around to guess again
      else:
         print("I do not understand!")
         guess = input("Please enter just one letter you have not guessed already.> ")


   return guess

################# DO NOT EDIT BELOW THIS LINE ##################

# A helpful function to print the hangman.
# DO NOT CHANGE
#
# state: current state of the word
def printHangperson(state, incorrect):
   person = [" O "," | \n | ", "\| \n | ", "\|/\n | ", "\|/\n | \n/  ", "\|/\n | \n/ \\"]
   print()

   if numWrong > 0:
      print(person[0])

   if numWrong > 1:
      print(person[numWrong-1])

   print("\n\n")

   for i in state:
      print(i, end=" ")

   print("\n")

   print("Incorrect Guesses: {0}".format(incorrect))
   print("")

# This line runs the program on import of the module
hangperson()