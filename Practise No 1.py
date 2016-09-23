#import datetime 
#get = datetime.datetime.now()


#name = input("What is your name?")
#currentage =int( input("What is your age?"))

#currentYear = get.year
#print(currentYear)

##lastAge = 100 - currentage
##lastyear = 2016 + lastAge

##print (" " +name+ " will be 100 years on %0.0d "  %lastyear)
############
#number = int(input("Enter the number:\n"))

#if number%2 == 0:
#    print("The number is even")
#    if number%4 ==0:
#        print("The number is multiple of 4")
#else:
#    print("The number is odd")
#######################        


#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#num_list = int(input("Choose a number:\n"))

#new_List = []

#for i in a:
#    if i < num_list:
#        new_List.append(i)
#print(new_List)

######

#number = int(input("Please choose a number to divide:\n"))



#divisorList = []

#for i in range(1,number+1):
#    if number%i == 0:
#        divisorList.append(i)
        
#print(divisorList)
##########

#list = []

#for i in range(2,10):
#    list.append(i)
    
#print (list)
#######

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#list = []

#for i in b:
#    if i in a:
#        list.append(i)
#print(list)

##for i in a:
###    for j in b:
###        if i== j:
###            list.append(i)
###print(list)

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#c = []
##j = 0
##for i in a:
##	if i != j:
##		if i in b:
##			c.append(i)
##		j = i
##print(c)
####################

##import random

##a = random.sample(range(0,100),10)
##print(a)

##b = random.sample(range(0,100),10)
##print(b)
##a = [random.randint(0,15) for r in range(10)]
##print(a)
##b = [random.randint(0,15) for r in range(10)]
##print(b)
##c = []

#for i in a:
#    if i in b and i not in c :
#        c.append(i)
#print(c)
################
#a = [5, 10, 15, 20, 25, 30, 35, 40]
#print(a[0:7:3])# prints list from 0 and leaves 3 numbers and prints again
##################################

#word = []
#word = list(input("Enter the word to check if it is a palindrom:\n"))
##frontward = (word[0:])
#backward =(word[::-1])
#palindrome = []
##print(frontward)
#print(backward)

#if word == backward:
#    print("The word is palindrome")
#else:
#    print("The word is not palindrome")
    
################################
#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#b =[]

#for i in a:
#    if i%2 ==0:
#        b.append(i)
#print(b)
#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#b = [i for i in a if ik % 2 == 0]

#print (b)
    
#######################
#import sys
#import random
#welcomemesg=input("Would you like to play rock,paper,scissors game?").upper()
#if welcomemesg == ("YES" or "YAP" or "Y"):
#    def playgames():
   
#        player1 =(input("What would you like to choose? Rocks, Paper or Scissors?").upper())
#        player2 =(input("What would you like to choose? Rocks, Paper or Scissors?").upper())
#        if player1 == player2:
#            print("please choose different!")
#        elif player1 == "ROCK" and player2 =="PAPER":
#            print("Player 2 wins")
#        elif player1 == "PAPER" and player2 =="SCISSORS":
#            print("Player 2 wins")
#        elif player1 =="SCISSORS" and player2 == "ROCK":
#            print("Player 1 wins")
#        elif player2 == "ROCK" and player1 =="PAPER":
#            print("Player 1 wins")
#        elif player2 == "PAPER" and player1 =="SCISSORS":
#            print("Player 1 wins")
#        elif player2 =="SCISSORS" and player1 == "ROCK":
#            print("Player 2 wins")

#        else:
#            print("Thank you for playing with us!")

#        playagain()
#else:
#    print("Thank you for visiting us!")
#def playagain():
#    player= input("Would you like to play the game again?").upper()
#    if player == ("YES" or "YA" or "YUP" or "Y"):
#        playgames()
#    else:
#        print("Thanks for playing!")
        
#    playgames()

#########################################
#import random
#import sys

#player1 = input("What would you like to choose? Rock, Paper or Scissors?").upper()
#player2 = random.choice(["ROCK","PAPER","SCISSORS"])
#print("Computer chose " + player2)
#if player1 == player2:
#   print("please choose different!")
#elif player1 == "ROCK" and player2 =="PAPER":
#    print("Player 2 wins")
#elif player1 == "PAPER" and player2 =="SCISSORS":
#    print("Player 2 wins")
#elif player1 =="SCISSORS" and player2 == "ROCK":
#    print("Player 1 wins")
#elif player2 == "ROCK" and player1 =="PAPER":
#    print("Player 1 wins")
#elif player2 == "PAPER" and player1 =="SCISSORS":
#    print("Player 1 wins")
#elif player2 =="SCISSORS" and player1 == "ROCK":
#    print("Player 2 wins")
#else:
#    print("Thank you for playing with us!")
#######################################

#import random
#import sys
#print("Welcome players!! ")
#def main():
#    while True:
       
#        player1 = input("What would you like to choose? Rocks,Paper, Scissors?\n").upper()
#        player2 = random.choice(["ROCK","PAPER","SCISSORS"])
#        game(player1,player2)
#        while True:
#            playgameagain= input("Would you like to play it again? Write yes or no \n").upper()
#            if playgameagain ==("YES"or"YAP" or"YA" or "Y"):
#                print("Welcome to the rock,scissors and paper game again ")
#                break
#            elif playgameagain==("NO" or "NOPE" or "NAH"):
#                print("Thank you for coming by")
#                sys.exit()
#            else:
#                print("Please say yes or no")
#                continue

#def game(player1 , player2):
#    if player1 == player2:
#        print("please choose different!")
#        main()
#    elif player1 == "ROCK" and player2 =="PAPER":
#        print("Computer chose "+ player2 +",Player 2 wins")
#    elif player1 == "PAPER" and player2 =="SCISSORS":
#        print("Computer chose "+ player2 +",Player 2 wins")
#    elif player1 =="SCISSORS" and player2 == "ROCK":
#        print("Computer chose "+ player2 +",Player 1 wins")
#    elif player2 == "ROCK" and player1 =="PAPER":
#        print("Computer chose "+ player2 +",Player 1 wins")
#    elif player2 == "PAPER" and player1 =="SCISSORS":
#        print("Computer chose "+ player2 +",Player 1 wins")
#    elif player2 =="SCISSORS" and player1 == "ROCK":
#        print("Computer chose "+ player2 +",Player 2 wins")
#    else:
#        print("Thank you for playing with us!")
    
        
#main()
##############################################
##guessing game solution

#import random   
#import sys

#print("Welcome to the game")
#number1 = 0
#number2 = random.randint(0,10)
#count = 0

#while number1 !="exit" and number1 != number2:
#    number1 = (input("Can you guess the number? Enter \"exit\" to quit the game\n"))
#    if number1 =="exit":
#        break
#    number1 = int(number1)
#    count +=1
   

#    if number1>number2:
#        print("The number is too high")
#    elif number1<number2:
#        print("The number is too low")
#    else:
#        print("You are right")
#        print("You have guessed ",count,"times")
##########################################################################
#list overlap comprehension solutions
#import random
#a =[]
#b=[]
#a = random.sample(range(1,30),10)
#print(a)
#b = random.sample(range(1,30),10)
#print(b)

#c = [ i for i in set(a) if i in b]
#print(c)
#result = []
#for element in c:
#    if element not in result:
#        result.append(element)
#print(result)
################################################3#########################
#check primality function solution
#import sys

#number = int(input("Enter the number:\n"))
#prime = True

#if number >0:


#    for checknumber in range(2,number-1):
#        print(checknumber)

#        if(number %checknumber) ==0:
#            continue
#        elif number % checknumber ==0:
#            print("the number is not prime")
#            #sys.exit()
#    print("the number is prime")
#    #sys.exit()
#elif number == 0:
#    print("the number is not prime")
#    sys.exit()
#else:
#    print("the number is not prime")
#    sys.exit()

print ("hello world")
print("hello world")

    