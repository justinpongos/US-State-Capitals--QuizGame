#  Name: Justin Pongos & Louis Pavlovsky
#  Date: 02/12/2024
import random

#  Desc: The State Capitals Quiz, a ten question quiz where a user is asked the capital for a random U.S. state. The user is given four multiple choice answers and is asked to select the correct capital, they would select a letter A, B, C, or, D. From the response they will be told if they had gotten the capital correct or wrong, if they select a improper selection they will be asked to input another selection A-D. Lastly the user is given a score at the end for how many question they answered correctly.

def read_file(file_name):
  """Opens and reads each line organizing it to be a pair and returning it as a 2D List.

  Args:
      file_name (String): represent the path to a file

  Returns:
      [[String, String]]: 2D list of state and capital pairs
  """
  with open(file_name, 'r') as file:
    list = file.readlines()
    temp = []
    states_and_capitals = []
    for line in list:
      temp = line.split(",")
      capital_formated = temp[1]
      if temp[1][-1] == '\n':
        capital_formated = temp[1][:-1]
      states_and_capitals.append([temp[0], capital_formated])
  return states_and_capitals

def get_random_state(states):
  """Randomly selects a state and capital from the list and returns it as a list of state and capital.

  Args:
      states (String): list with all the states and capitals
      
  Returns:
      [String, String]: a list of state and capital
  """
  #   from the list and return the two-item list
  rand_state = random.choice(states)
  return rand_state

def get_random_choices(states, correct_capital):
  """Randomly selects three incorrect capitals and one correct capital that are not a duplication from the list and returns them as a list.

  Args:
      states(String), correct_capital(String): represents a list of states and its capitals and the correct capital from random state
      
  Returns:
      [String]: list of three random capitals and a correct capital
  """
  list_without_correct_capital = []
  #  Removes the correct capital from the list to avoid duplication
  for pair in states:
    if pair[1] != correct_capital:
      list_without_correct_capital.append(pair[1])

  #  Gets directly 3 randoms capitals to avoid duplication
  rand_choices = random.sample(list_without_correct_capital, 3)
  rand_choices.append(correct_capital)
  #  Shuffles everything once the last capital was added
  random.shuffle(rand_choices)
  return rand_choices

def ask_question(correct_state, possible_answers):
  """Displays the question and possible answers and returns the user's answer index.

  Args:
      correct_state(String), possible_answers(List): represents a list of three possible answers and the correct selection from random state
      
  Returns:
      [index]: returns the index of the letter that the correct selection is located at
  """
  print(f"The capital of {correct_state} is:")
  print(
      f"\tA. {possible_answers[0]}  B. {possible_answers[1]}  C. {possible_answers[2]}  D. {possible_answers[3]}")
  choices = "ABCD"
  letter = 0
  valid = False
  #  Ask the user to input a letter A-D, if they input anything else they will be asked to input another letter.
  while not valid:
    letter = input("Enter selection: ").upper()
    if letter in choices:
      valid = True
    else:
      print("Invalid input. Input choice A-D.")
  #  Returns directly the index of the letter
  return choices.index(letter)

def main():
  """Runs the whole game, asks the user ten questions and prints their score.
  """
  print("- State Capitals Quiz -")
  file = read_file("statecapitals.txt")
  correct_count = 0
  question = 0

  #  Opens file and selects a random state, asks the user ten different questions.
  while question < 10:
    question += 1
    rand_state = get_random_state(file)
    rand_choice = get_random_choices(file, rand_state[1]) 
    print(f"{question}. ", end="")
    user_answer_index = ask_question(rand_state[0], rand_choice)
    #  Checks if the user selects the correct capital or not. than the game ends and adds up all the correct answers.
    if rand_choice[user_answer_index] == rand_state[1]:
      print("Correct!")
      correct_count += 1
    else:
      print(f"Incorrect!  The correct answer is: {rand_state[1]}.")
  print(f"End of test.  You got {correct_count} correct.")
main()