leap = input('is it a leap year? > ')
if leap == 'yes' or leap == 'Yes' : 
  secs = ((60 * 60) * 24) * 365
  print('there are', secs, 'seconds in this year')
elif leap == 'no' or leap == 'No':
  secs = ((60 * 60) * 24) * 366
  print('there are', secs, 'seconds in this year')
else :
  print('well find out!')