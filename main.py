import random

computerOptions = ["Rock", "Paper", "Scissors"]
computerChoice = computerOptions[random.randint(0,2)]

print("Welcome to Rock, Paper, Scissors!")

userChoice = input("Choose your weapon: ")

if (computerChoice == "Rock" and userChoice == "Paper"):
  print("You won! I chose rock!")
elif (computerChoice == "Scissors" and userChoice == "Rock"):
  print("You won! I chose Scissors!")
elif (computerChoice == "Paper" and userChoice == "Scissors"):
  print("You won! I chose Paper!")
elif (computerChoice == "Rock" and userChoice == "Scissors"):
  print("You lost! Bozo I chose Rock!")
elif (computerChoice == "Paper" and userChoice == "Rock"):
  print("You lost! Bozo I chose Paper!")
elif (computerChoice == "Scissors" and userChoice == "Paper"):
  print("You lost! Bozo I chose Scissors")
elif (computerChoice == "Scissors" and userChoice == "Scissors"):
  print("We Tied")
elif (computerChoice == "Rock" and userChoice == "Rock"):
  print("We Tied")
elif (computerChoice == "Paper" and userChoice == "Paper"):
  print("We Tied")