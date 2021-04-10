# quiz-game
# This is code for a quiz game

def verify_guess(guess, answer):
    global score
    cont_guessing = True
    attempt = 0
    while cont_guessing and attempt < 5:
        if guess.lower() == answer.lower():
            print("Correct Answer! You guessed correctly!")
            score = score + 1
            cont_guessing = false
        else:
            if attempt < 4:
                guess = input("Wrong Answer. Try again.")
            attempt = attempt + 1
    if attempt == 5:
        print("The correct answer is: ", answer)


score = 0
print("Guess the Movie quote")
guess1 = input("I was born in the darkness, you were merely molded by it")
verify_guess(guess1, "The Dark Knight Rises")
guess2 = input("How do you get fired on your day off")
verify_guess(guess2, "Friday")
guess3 = input("You need people like me so you can point your fingers and say, 'That's the bad guy.")
verify_guess(guess3, "Scarface")

print("Your Score is " + str(score))
