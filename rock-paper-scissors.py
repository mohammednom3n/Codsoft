import random
logo = '''
    ____             __         ____                             _____      _                          
   / __ \____  _____/ /__      / __ \____ _____  ___  _____     / ___/_____(_)_____________  __________
  / /_/ / __ \/ ___/ //_/_____/ /_/ / __ `/ __ \/ _ \/ ___/_____\__ \/ ___/ / ___/ ___/ __ \/ ___/ ___/
 / _, _/ /_/ / /__/ ,< /_____/ ____/ /_/ / /_/ /  __/ /  /_____/__/ / /__/ (__  |__  ) /_/ / /  (__  ) 
/_/ |_|\____/\___/_/|_|     /_/    \__,_/ .___/\___/_/        /____/\___/_/____/____/\____/_/  /____/  
                                       /_/                                                         
'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


print(logo)
print("Welcome to Rock-Paper-Scissors game 🙌\n")

images = [rock, paper, scissors]
user_choice = int(input("What do you choose? \nEnter 0 for rock, 1 for paper and 2 for scissors:"))
print(images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(images[computer_choice])


if user_choice >= 3:
    print("You entered invalid number.")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose.")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose.")
elif user_choice == computer_choice:
    print("It's a draw.")
