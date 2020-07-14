from util import get_integer, get_string

def main():
  computer_prompt = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly"
  ans = get_integer(0, 99, "Enter a number")

  guess = 0
  low = 0
  high = 100

  while True:
    guess = (high + low) / 2
    print(f"Is {guess} your secret number?")
    user_decision = get_string(1, 1, computer_prompt, accept_values=['h', 'l', 'c'])
    if user_decision == 'c':
      break
    elif user_decision == 'h':
      high = guess
    elif user_decision == 'l':
      low = guess
    print(f"High: {high}\nLow: {low}\nGuess: {guess}")

  print(f"Final guess: {round(guess)}")

main()