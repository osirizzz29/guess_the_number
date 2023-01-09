import random
import os

print("   =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("   |  [~] My Discord: R3W333#7701              |")
print("   |  [~] My Github: https://github.com/r3w33  |")
print("   =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("")
print("     [X] Let's play `Guess the number` ")
print(" ")
print("     [1] Start game")
print("     [2] Exit")
print("")

option = input("   [X] Option: ")
os.system('cls') # Close the program

if option == "1":
  print(" ")
  print("     [X] Choose a number between 1 and 5")
  ai = random.randrange(0, 5) # (start, stop) - you can edit them however you want!
  correct_number = ai

  while True: # While loop in case the user did not guessed the correct number!
      print(" ")
      number = int(input("     [~] Number: "))
      
      if number == correct_number:
          print("     [+] You win!")
          print("     [~] Thank you for playing. ")
          break
      else:
          print("")
          print("     [-] You lose!")
          print("     [~] The correct number was: " + str(correct_number)) 
          ai = random.randrange(0, 5) # Generate a new random number
          correct_number = ai
  
elif option == "2":
  os.system('exit')
  
else:
  print("Choose a valid option")
