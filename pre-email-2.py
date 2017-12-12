# Another before-class e-mail, same problem.
# Demonstration of threading class

import sys,threading

class zThread(threading.Thread):

  def __init__(self, x, y, max):
    threading.Thread.__init__(self)
    self.x=x
    self.y=y
    self.max=max

  def run(self):
    z=5
    while z<=self.max:
      zs=str(z)
      num1=int(str(self.x)+str(self.y)+zs)
      num2=int(zs+zs+zs)
      if num1*3 == num2:
        print "3 * (", x, "+", y, "+", z, ") =", num2
      z*=10

max = sys.maxint
x=0
y=0
while x<=max:
  while y<=max:
    zThread(x,y,max).start()
    y+=1
  x+=1
  y=0

