print(" Welcome To My Quiz Game \n Interesting Game to Play")
Player = input(" Do you want to play the game? \n" )
if Player.lower() != 'yes':
    print("Good Bye")
    quit()  

name_player = input("Enter Your Name: ")

print("Let's Start the Game :) ",name_player)

score = 0

answer = input(' What is the correct extension of the Python file? \n ')
if answer.lower() == '.py':
    print("Correct")
    score += 1
else:
    print('Wrong')
 
answer = input(' Which keyword is used for function in Python language? \n ')
if answer.lower() == 'def':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' What will be the output of the following Python function? len(["hello",2, 4, 6])  \n ')
if answer.lower() == '4':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' Which statement is used to create an empty set in Python? \n ')
if answer.lower() == 'set()':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' Which data type does Python not natively support? \n ')
if answer.lower() == 'Array':
    print("Correct")
    score += 1
else:
    print('Wrong')
    
print("You got the " + str(score)+ " correct answers out of 5 Questions")
print("You got the " + str((score/5) *100)+ "% of correct answers")
