from p import *
splits = "split \n strings \n everywhere"
p(splits)

tabs = "1\t2\t3\t"
p(tabs)

single_quote_apostrophe_interpolation = 'bruce said "he\'s got this"'
double_quote_quote_interpolation = "bruce said \"he's got this\""
p(single_quote_apostrophe_interpolation)
p(double_quote_quote_interpolation)

triple_quote_split = """this is going
to be
split over
a couple of lines"""
p(triple_quote_split)

triple_quote_quote_interpolation = """bruce said "he's got this" """
#leaves a space at the end
p(triple_quote_quote_interpolation)
triple_quote_quote_interpolation2 = '''bruce said "he's got this"'''
p(triple_quote_quote_interpolation2)

#3.6 interpolation
age = 39
string = f"I am {age} years old"
p(string)

parrot = 'norwiegen blue'
p(parrot[6])
p(parrot[-1])

#slicing, different from ruby bc this is a range
#does not inclue last integer, very frustrating
p(parrot[0:6])
p(parrot[:6])
p(parrot[1:6])

p(parrot[6:-1])
p(parrot[6:])
#doesn't work
p(parrot[6:0])
# skip by x
p(parrot[0:6:2])
p(parrot[0::2])
#misc
p('what' 'is' 'up')
p('hello' *5)

#other interpolation
# p("My age is " + str{age} + " years")
#not functioning in 3,6
p("my age is {0} years".format(age))
#relational assignment 0,1,2 = a, b, c
p("my age is {0} and you are not {0}. you are {1}".format(age, 44))
#python 2 assignment
# % and data type
p("my age is %d is years" % age)
p("my age is %d %s, %d %s" % (age, 'years', 6, 'months'))

for i in range(1,6):
    #number after percent means the number of availbale spaces to replace(width)
    p("No. %2d squared is %4d and cubed is %4d" %(i, i **2, i**3))
for i in range(1,6):
    p("No. %d squared is %d and cubed is %d" %(i, i **2, i**3))
for i in range(1,6):
    #second number is the width
    # < left justify
    p("No. {0:1} squared is {1:2} and cubed is {2:<3}".format(i, i **2, i**3))

p("pi is ~ %f" % (22/7))
p("pi is ~ %.50f" % (22/7))
#if f is left out it becomes a range for decimals and misses the last one
p("pi is ~ {0:.50f}".format(22/7))
