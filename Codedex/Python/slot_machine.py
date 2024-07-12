import random

def play():
  symbols = [ '🍒',' 🍇', '🍉', '7️⃣']
  win = 0
  result = []
  
  for i in range(3):
    result.append(random.choice(symbols))
    
    if result[i] == '7️⃣':
      win += 1

  print('\n' + result[0] + ' | ' + result[1] + ' | ' + result[2])
  
  if win == 3:
    print('jackpot!💰')

again = 'y'
while again == 'y':
  play()
  while True:
    again = input('\nAgain? y/n: ').strip().lower()
    if again in ['y','n']:
      break
    print("Please enter 'y' or 'n'.")
