print('Exame calculator')
print()
name = input('Name of exam: ')
print()
max = float(input('Max. Possible Score: '))
print()
score = float(input('Your score: '))
per = round((score / max)*100, 2)
print(per)
if per == 90 :
  print('You got a',str(per) + '%', 'which is a A+' )
else :
  print('try again')



# 90 = a+
# 80 = a-
# 70 = b
# 60 = c
# 50 = d
# 40 = u

# print(per)
