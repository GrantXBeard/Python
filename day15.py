counter = 0
while counter <= 100:
  print(counter)
  counter +=1
exit = ""
while exit != "yes":
  print("🥳")
  exit = input("Exit?: ")


print('cow, frog, snake')
exit = ''
while exit != 'yes' :
  animal = input('Please choose an animal from the list above > ')
  if animal == 'cow' :
    print('MOOOOO')
  elif animal == 'frog' : 
    print('Ribit! Ribit!')
  elif animal == 'snake' :
    print('SSSSSSsssssssss')
  else :
    print('please choose from the list')
  exit = input('Would you like to exit? > ')
print('Thank You! Goodbye')



exit = "no"
while exit == "no":
  animal_sound = input("What animal sound do you want to hear?")
  
  if animal_sound == "cow" or animal_sound == "Cow":
    print("🐮 Moo")
  elif animal_sound == "pig" or animal_sound == "Pig":
    print ("🐷 Oink")
  elif animal_sound == "sheep" or animal_sound == "Sheep":
    print ("🐑 Baaa")
  elif animal_sound == "duck" or animal_sound == "Duck":
    print("🦆 Quack")
  elif animal_sound == "dog" or animal_sound == "Dog":
    print("🐶 Woof")
  elif animal_sound == "cat" or animal_sound == "Cat":
    print("🐱 Meow")
  else: 
    print("I don't know that animal sound. Try again.")
  exit = input("Do you want to exit?: ")

