# Write code below 💖

rating = float(input('Set a number of stars'))

if rating > 4.5 :
  print('Extraordinary')
elif rating > 4 and rating < 4.5:
  print('Excellent')
elif rating > 3 and rating < 2:
  print('good') 
elif rating > 2 and rating < 3:
  print('Fair')
else: 
  print('Poor')