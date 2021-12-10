import random

### Here we are making a player class to represent the players in the game.
class Player:

    ### These are the functions for the player class.

    ### This is the default constructor for the player class. 
    def __init__(self, name, score):
        self.name = name
        self.score = score 

    def getScore(self):
        return self.score

    def setScore(self, x):
        self.score = x
    
    def getName(self):
        return self.name

    def setName(self, x):
        self.name = x

###This function right here will print out the phrase. It takes in the phrase and a set of the letters that the players have guessed correctly.
#It prints underscores for each letter, unless it has been guessed correctly in which case it prints the letter. 
def printBoard(guess_word, correct_guesses):
    for i in range(0, len(guess_word)):
        if guess_word[i].lower() in correct_guesses:
            print(guess_word[i], end =" ")
        elif guess_word[i] == " ":
            print(" ", end=" ")
        else:
            print("_", end=" ")
    print()

print("Welcome to Wheel of Fortune. We are excited to have you here. May the better player win!")

name_1 = input("Player1 Please Enter Your Name ")
p1 = Player(name_1, 0)
print(f"Welcome {p1.getName()}")

name_2 = input("Player2 Please Enter Your Name ")
p2 = Player(name_2, 0)
print(f"Welcome {p2.getName()}")

###Right here we are reading from a file that holds the phrases.

file = open("CSE_310\Project_05\phrases.txt")
phrases = file.readlines()
phrases = [phrase.strip() for phrase in phrases ]
file.close()
##print(phrases)

###This line of code selects a random phrase from the list of phrases. 

guess_word = phrases[random.randint(0, len(phrases)-1)]

correct_letters = set()
correct_guesses = set()

### This for loop adds each letter from the phrase into a set. The set allows no duplicate letters. 
for i in range(0, len(guess_word)):
    if guess_word[i] != " ":
        correct_letters.add(guess_word[i].lower())

game_end = False

#print(correct_letters)

### This loop is responsible for playing the game. 
while True:
    
    printBoard(guess_word, correct_guesses)
    #print(guess_word)
    print(f"{p1.getName()}, it is your turn ")
    guess = input("Enter a letter: ")

###This if statement checks if the letter that has been guessed is in the set of correct letters. 
    if guess in correct_letters:
        if guess in correct_guesses:
            print("That letter has already been picked.")
        else:
            print("Correct!")
            correct_guesses.add(guess)
            p1.setScore(p1.getScore() + 10)

###This if statement checks if all the correct letters have been guessed by player one in which case we exit the loop.
            if len(correct_guesses) == len(correct_letters):
                break

    else:
        print("Incorrect")

    printBoard(guess_word, correct_guesses)

    print(f"{p2.getName()}, it is your turn ")
    guess = input("Enter a letter: ")

    if guess in correct_letters:
        if guess in correct_guesses:
            print("That letter has already been picked.")
        else:
            print("Correct!")
            correct_guesses.add(guess)
            p2.setScore(p2.getScore() + 10) 

###This if statement checks if all the correct letters have been guessed by player two in which case we exit the loop.
            if len(correct_guesses) == len(correct_letters):
                break
    else:
        print("Incorrect")

printBoard(guess_word, correct_guesses)

###This if statement determines who won and prints the name of the winner and the score. 
if p1.getScore() == p2.getScore():
    print("We have a tie!")
elif p1.getScore() > p2.getScore():
    print(f"We have a winner... Congradulations {p1.getName()}, you won with {p1.getScore()} points")
elif p1.getScore() < p2.getScore():
    print(f"We have a winner... Congradulations {p2.getName()}, you won with {p2.getScore()} points")
file = open("CSE_310\Project_05\scores.txt", "a")
file.write(f"{p1.getName()} - {p1.getScore()}\n")
file.write(f"{p2.getName()} - {p2.getScore()}\n")

file.close()