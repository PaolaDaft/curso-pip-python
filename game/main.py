import random
playing_opc = ('yes', 'no')
options = ('rock', 'paper', 'scissors')
raunds = 0
user_points = 0
computer_points = 0

# Vienvenda
print('''
  🤖 Welcome to rock, paper or scissors game 🙋
      ''')
playing = (input('''       >>> Do you want to play? Yes/No <<<
''')).lower()

while not playing in playing_opc :
  print('This option is not valid 👀')
  playing = (input('''       >>> Do you want to play? Yes/No <<<
''')).lower()
if playing == 'yes' :
  
  while playing == 'yes' :
    # Eligiendo la opción del usuario 
    user_option = (input('Chose! rock, paper o scissors? ')).lower()
    if not user_option in options :
      print('''
      This option is not valid 👀
      ''')
    else :
      raunds += 1
      computer_option = random.choice(options)
      
      print('.' *30)  
      print('RAUND ', raunds)
      print('User option => ', user_option)
      print('Computer option =>', computer_option)
      print('\n')
      
      if user_option == computer_option :
        print("It's a draw! ⚖️")
      elif user_option == 'rock':
        if computer_option == 'scissors':
          print('rock beats scissors')
          print('User wins ✨\n')
          user_points += 1
        else: #computer_option paper
          print('paper beats rock')
          print('Computer wins 🖥️\n')
          computer_points += 1
          
      elif user_option == 'paper':
        if computer_option == 'scissors' :
          print('scissors beats paper')
          print('Computer wins 🖥️\n')
          computer_points += 1
        else: # computer_option rock
          print('paper beats rock')
          print('User wins ✨\n')
          user_points += 1
          
      elif user_option == 'scissors':
        if computer_option == 'paper':
          print('scissors beats paper')
          print('User wins ✨\n')
          user_points += 1
        else: #computer_option rock
          print('rock beats scissors')
          print('Computer wins 🖥️\n')
          computer_points += 1
          
      playing = input('Do you want keep playing? ').lower()  
      while not playing in playing_opc :
        print('This option is not valid 👀')
        playing = input('Do you want keep playing? ').lower()
        
  # Ganador final si es que jugó      
  if raunds > 0 :
    print('\n', '-' * 15, "Who's the winer?", '-' *15, '\n User points => ', user_points,'\n Computer points => ', computer_points)
    if user_points > computer_points :
      print('\n The winer is \n ✨✨✨THE USER✨✨✨ \n')
    elif computer_points > user_points :
      print('\n The winer is \n 🖥️🖥️🖥️THE COMPUTER🖥️🖥️🖥️ \n')
    else :
      print("\n It's a draw! 🤡🤡🤡\n")

# Despedida      
print('See ya! 🖐️')