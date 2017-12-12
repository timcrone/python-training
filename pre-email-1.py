# E-mail problem to whet the appetite:
# Solve the problem posted on door of one of our team:
#     Red Blue Green
# +   Red Blue Green
# +   Red Blue Green
# ------------------
#  Green Green Green

max = 1000
for x in range(0,max):
  for y in range(0,max):
    for z in range(0,max):
      num1=int(str(x)+str(y)+str(z))
      num2=int(str(z)+str(z)+str(z))
      if num1*3 == num2:
        print "X is "+str(x)
        print "Y is "+str(y)
        print "Z is "+str(z)
        print "Result is "+str(num2)

# I sent along these notes to encourage experimentation:
#So far my largest answer involves Y=683, but you can tweak max= to your heart's content.
#Some optimization possibilities:
# - You could reduce the memory footprint by using other kinds of loops, since range() creates long arrays.
# - After the first few results you will see a pattern that will let you reduce the number of times you need to multiply.
# - I think there's a way to reduce the str() and int() calls
# - No doubt plenty I am missing
