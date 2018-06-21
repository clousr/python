from p import *
name = input("please enter your name: ")
age = int(input("how old are you , {0}? ".format(name))) #changes string to integer

if age >= 18 and age <= 60:
    p('you are able to work')
elif age < 18:
    p("{1}, please come back in {0} years".format(18-age, name))
else:
    p('you are too old to work')
