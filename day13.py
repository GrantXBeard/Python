print('Exame calculator')
print()
name = input('Name of exam: ')
print()
max = float(input('Max. Possible Score: '))
print()
score = float(input('Your score: '))
per = round((score / max)*100, 2)
print(per)
if per >= 90 :
  print('You got a',str(per) + '%', 'on the', name, 'exam. Your grade is an A+')
elif per < 90 and per >= 80 :
  print('You got a',str(per) + '%', 'on the', name, 'exam. Your grade is an A-')
elif per < 80 and per >= 70 :
  print('You got a',str(per) + '%', 'on the', name, 'exam. Your grade is an B')
elif per < 70 and per >= 60 :
  print('You got a',str(per) + '%', 'on the', name, 'exam. Your grade is an C')
elif per < 60 and per >= 50 :
  print('You got a',str(per) + '%', 'on the', name, 'exam. Your grade is an D')
elif per < 50 :
  print('You got a',str(per) + '%', 'on the', name, 'exam. Your grade is an U')
else :
  print('try again')


# 90 = a+
# 80 = a-
# 70 = b
# 60 = c
# 50 = d
# 40 = u

# print(per)
