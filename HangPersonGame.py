# Danny Grimmig
# HangPerson


import random


def print_gallows(num_missed):
    '''
    Make a poor-human's representation of the hangperson gallows.
    Parameter to the function is the number of missed words (7 misses
    means that the player is fully strung up).
    '''
    print()
    print()
    print('       |||========|||')
    if num_missed > 0:
        print('       |||         |')
    else:
        print('       |||          ')

    if num_missed > 1:
        print('       |||         O')
    else:
        print('       |||          ')

    if num_missed > 2:
        if num_missed > 4:
            print('       |||        /|\\')
        elif num_missed > 3:
            print('       |||        /| ')
        else:
            print('       |||        /  ')
    else:
        print('       |||           ')

    if num_missed > 5:
        if num_missed > 6:
            print('       |||        / \\')
        else:
            print('       |||        /  ')
    else:
        print('       |||           ')

    print('       |||')
    print('       |||')
    print('     =====          =======')
    print()



def start_key(secret):      #Thought of this as a lock and key, the secret being the lock, key being your guesses
    state = ''
    for i in range(len(secret)): #the "_ _ _ _ " for however many spots in the secret
        state += '_ '
    return state


def ask_guess(guessed_letters):   #Asks the user for their guess
    valid = False
    while not valid:
        guess = input("What is your guess? ").upper()     
        if guess in "QWERTYUIOPASDFGHJKLZXCVBNM" and len(guess) == 1:   #if the guess isnt a singular letter, asks again
            if guess in guessed_letters:
                print("You already guessed that") # if already guessed, tells them and asks again
            else:
                valid = True
        else:
            print("One letter, please!")
    return guess.upper()


def update_key(guess, secret, key): #updates the keycard (the guess)
    old = key
    new = ''
    final = ''
    for i in range(len(secret)):  #check new key with your secret code
        if guess == secret[i]:
            new += guess +' '
        else:
            new += '_ '
    for j in range(len(old)):  #check new key with your previous updated key
        if old[j] in "QWERTYUIOPLKJHGFDSAZXCVBNM":
            final += old[j]
        else:
            final += new[j]  

    return final


def unbreakable_code(secret):    #The MASTER LOCK! S E C R E T, to be checked with the updating key to see if you win
    mylist = ''
    for i in range(len(secret)):
        mylist+= secret[i] + ' '
    return mylist

def update_remaining_letters(guess, remaining_letters):  #keeps updating the remaining letters
    original = remaining_letters  #takes previously updated letters
    new = ''
    if guess in original:  #takes out the guess!
        new = original.replace(guess,'')
   
    return new

def play(secret):  #Play function
    guess = ''
    lock = unbreakable_code(secret)
    remaining_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    guessed_letters = ''
    num_missed = 0
    key = start_key(secret)
    win = False
    playing = True
    while playing:  #While you either havent lost or while you havent won           #1,print the gallow
        print_gallows(num_missed)                                                   #2, remaining letter update
        print(key)
        remaining_letters = update_remaining_letters(guess, remaining_letters)      #3, get a guess
        print("Remaining letters: " + remaining_letters)                            #4, add guess to key, check key to lock. if 7 misses, game over you lose, if key matches lock you win
        guess = ask_guess(guessed_letters)
        guessed_letters += guess
        key = update_key(guess, secret, key)
        if guess not in secret:
            num_missed += 1
            if num_missed == 7:
                playing = False
        if lock == key:
            playing = False
            win = True
    if win:
        print()
        print(key)
        print("Congrats! You have outsmarted the computer!")
    else:
        print_gallows(7)
        print("Boo hoo! You lost! The word was " + secret)
        
      
        
        
      
        
       
        




def main():
    '''() -> ()

    main function for playing hangperson
    '''
    words = ['SPRING', 'LEAVES', 'MUD', 'SUNNY', 'DAFFODIL', 'HAPPY', 'SUNSHINE', 'WINTER']
    secret = random.choice(words)
    play(secret)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()
