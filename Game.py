import os
import random;

def run():
  HANGMANPICS = [
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
  ]


  DB = [
    "JAVASCRIPT", "PHP", "MONGODB", "JAVA", "PYTHON", "MYSQL",
    "ant", "baboon", "badger", "bat", "bear", "beaver", "camel", 'cat', "clam", "cobra", 'cougar', 'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox' 'frog', 'goat'
    ];

  word = random.choice(DB).upper();
  spaces = ["_"] * len(word);
  attemps = 6;

  while True:
    os.system('clear');
    for character in spaces:
      print (character, end =' ');
    print (HANGMANPICS[attemps])
    letter = input("Elige una letra: \n").upper();

    found = False;
    for idx, character in enumerate(word):
      if character == letter:
        spaces[idx] =letter;
        found = True;

    if not found:
      attemps -= 1;

    if "_" not in spaces:
      os.system("clear");
      print("GANASTE");
      break;
      input();

    if attemps == 0:
      print("PERDISTE ESTAS AHORCADO :(");
      print("\n La palabra correcta era: " + word);
      break;
      input();

if __name__ == '__main__':
  run();
