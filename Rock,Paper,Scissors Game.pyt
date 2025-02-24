import random  # Import the random module

def get_choices():  # Function to get the user's choice
  player_choice = input("Enter your choice (Rock, Paper, or Scissors): ")  # Ask the user for their choice
  options = ["rock", "paper", "scissors"]  # Create a list of options
  computer_choice = random.choice(options)  # Get a random choice for the computer"
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):  # Function to check who won
  print(f"You chose {player}")  # Print the player's choice
  if player == computer:
    return "It's a tie!"  # If the player and computer chose the same thing, it's a tie
  elif player == "rock":
    if computer == "Scissors":
      return "Rock smashes scissors! You win!"  # If the player chose Rock and the computer chose Scissors, the player wins
    else:
      return "Paper covers Rock! You lose."  # If the player chose Rock and the computer chose Paper, the player loses
  elif player == "paper":
    if computer == "rock":
      return "Paper covers Rock! You win!"  # If the player chose Paper and the computer chose Rock, the player wins
    else:
      return "Scissors cuts Paper! You lose."  # If the player chose Paper and the computer chose Scissors, the player loses
  elif player == "Scissors":
    if computer == "paper":
      return "Scissors cuts Paper! You win!"  # If the player chose Scissors and the computer chose Paper, the player wins
    else:
      return "Rock smashes Scissors! You lose."  # If the player chose Scissors and the computer chose Rock, the player loses

chocies = get_choices()  # Get the choices
result = check_win(chocies["player"], chocies["computer"])  # Check who won
print(result)  # Print the result

 