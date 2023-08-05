from getpass import getpass as input

print('E P I C    🪨  📄 ✂️    B A T T L E')
print()
print('Select your move (R, P or S)')
print()
player1 = input('Player 1 chooses > ')
player2 = input('Player 2 chooses > ')

if player1 == 'R' :
  if player2 == 'S' :
    print('🪨  beats ✂️  Player 1 wins!')
  elif player2 == 'P' :
    print('📄  beats 🪨  Player 2 wins!')
  elif player2 == 'R' :
    print('Draw!')
  else :
    print('Invalid move Player 2')
elif player1 == 'P' :
  if player2 == 'S' :
    print('✂️  beats 📄  Player 2 wins!')
  elif player2 == 'P' :
    print('Draw!')
  elif player2 == 'R' :
    print('📄  beats 🪨  Player 1 wins!')
  else : 
    print('Invalid move Player 2')
elif player1 == 'S' : 
  if player2 == 'S' :
    print('Draw!')
  elif player2 == 'P' : 
    print('✂️  beats 📄  Player 1 wins!')
  elif player2 == 'R' :
    print('🪨  beats ✂️  Player 2 wins!')
  else : 
    print('Invalid move Player 2')
else :
  print('Invalid move Player 1')

  