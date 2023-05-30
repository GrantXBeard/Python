print("generation identifier")
year = int(input("what year were you born? > "))
if year >= 1883 and year <= 1900 :
  print("lost generation")
elif year >= 1901 and year <= 1927 :
  print("greatest generation")
elif year >= 1928 and year <= 1945 :
  print("silent generation")
elif year >= 1946 and year <= 1964 :
  print("baby boomers")
elif year >= 1965 and year <= 1980 :
  print("gen x")
elif year >= 1981 and year <= 1996 :
  print("millenials")
elif year >= 1997 and year < 2012 :
  print("gen z")
elif year >= 2013 and year < 2023 :
  print("gen alpha")
else : 
  print("out of range")