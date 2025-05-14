import random

class NumberGuessingGame:
  def printWelcome(self)  -> str:
    return """
    Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.
    You have 5 chances to guess the correct number.
    """
  
  def userLevel(self) -> int:
    showLevels = """
    Please select the difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)
    """

    print(showLevels)
    level = int(input("Enter your choice: "))    
    if level == 1:
      chances = 20
    elif level == 2:
      chances = 5
    elif level == 3:
      chances = 3
    else:
      print("Invalid choice")  
      self.userLevel()
    
    return chances

  def play(self, chances):
    counter = 0
    number = random.randint(1,100)

    while counter < chances:
      counter += 1
      guess = int(input("Enter your guess: "))
      if guess == number:
        print(f"Congratulations! You guessed the correct number in {counter} attempts.")
        break
      elif guess < number:
        print(f"Incorrect! The number is more than {guess}.")  
      else: 
        print(f"Incorrect! The number is less than {guess}.")   


    print(f"Sorry, you did not guess the correct number. You attempted {counter} out of {chances} times")    

def main():
  g1 = NumberGuessingGame()
  g1.printWelcome()
  level = g1.userLevel()
  g1.play(level)

if __name__ == "__main__":
  main()