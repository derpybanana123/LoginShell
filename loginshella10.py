import random

#def end():
    #break
#define programs (self test, hello world, etc.)
def selftest():
    print("PROGRAM SELF TEST")
    print("")
    print("If you can see this text then you have configured LOGINSHELL correctly")
def helloworld():
    print("Hello World!")
def progs():
    print("Current Programs:")
    print("SELF TEST - Prints a test statement")
    print("HELLO WORLD - Runs the classic Hello World program")
    print("ROLL DICE - Rolls a dice")
    print("GUESS GAME - Guess the word")
    print("HANGMAN - The classic hangman game")
def rolldice():
    min = 1
    max = 6

    roll_again = "yes"

    while roll_again == "yes" or roll_again == "y":
        print "Rolling the dices..."
        print "The values are...."
        print random.randint(min, max)
        print random.randint(min, max)
        roll_again = raw_input("Roll the dices again?")
def guessgame():
    n = random.randint(1, 99)
    guess = int(raw_input("Enter an integer from 1 to 99: "))
    while n != "guess":
        print
        if guess < n:
            print "guess is low"
            guess = int(raw_input("Enter an integer from 1 to 99: "))
        elif guess > n:
            print "guess is high"
            guess = int(raw_input("Enter an integer from 1 to 99: "))
        else:
            print "you guessed it!"
            #end()
        print
def hman():
    name = raw_input("What is your name? ")
    print "Hello, " + name, "Time to play hangman!"
    print ""
    time.sleep(1)
    print "Start guessing..."
    time.sleep(0.5)
    word = "secret"
    guesses = ''
    turns = 10
    while turns > 0:         
        failed = 0             
        for char in word:      
            if char in guesses:    
                print char,    
            else:
                print "_",     
                failed += 1    
        if failed == 0:        
            print "You won"  
            #end()              
        print
        guess = raw_input("guess a character:") 
        guesses += guess                    
        if guess not in word:  
            turns -= 1        
            print "Wrong"    
            print "You have", + turns, 'more guesses' 
            if turns == 0:           
                print "You Loose"  

print("Welcome to LOGINSHELL v1.1 Alpha running on PYTHON TERMINAL")
print("------------------------------------------")

admin = "admin"
Pa55word = "Pa55word"
#define username and password
usr = "admin"
pw = "admin"

pwinput = ""
#begin login prompt
print("Username and Password must be surrounded by inverted commas")
usrinput = input("User Name: ")
if usrinput == usr:
    pwinput =  input("Password: ")
    if pwinput == pw:
        #correct username and password
        print("Login Success!")
        print("------------------------------------------")
        print("Type 1 for Self Test")
        print("Type 2 to run Hello World")
        print("Type 3 for Help")
        print("Type 4 for Games")
        print("Type 5 to change username or password")
        sel = input("Enter your selection: ")
        if sel == 1:
            selftest()
            #end()
        if sel == 2:
            helloworld()
            #end()
        if sel == 3:
            progs()
        if sel == 4:
            print("Games")
            print("Type 1 for Dice Roll")
            print("Type 2 for Guess Game")
            print("Type 3 for Hangman")
            game = input("Enter Game Number: ")
            if game == 1:
                rolldice()
                #end()
            if game == 2:
                guessgame()
                #end()
            if game == 3:
                hman()
                #end()
            if game >= 4:
                print("Invalid Game Selection")
                #end()
        if sel == 5:
            print("Type 1 for username")
            print("Type 2 for password")
            print("New Username and Password must be surrounded by inverted commas")
            psel = input("Enter your selection: ")
            if psel == 1:
                usr = input("New Username: ")
            if psel == 2:
                pw = input("New Password: ")
            if psel >= 3:
                print("Invalid Selection!")

        if sel >= 6:
            print("Invalid Selection!")
            #end()
        
    else:
        #wrong password
        print("Incorrect Password!")
        #end()
else:
    #wrong username
    print("Incorrect User Name!")
    #end()
