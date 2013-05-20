#!/usr/bin/python
class generatorOp(object):
  
  def __init__(self,name= "generatorOp",number = 5):
    self.name = name
    self.num = number
    self.f = open(name,"w")

  def Op1(self):
    while self.num > 0:
      yield "Output is %d \n" % self.num
      self.num -= 1
    yield "generator finished\n"

  def write(self):
    s = self.Op1()
    self.f.writelines(s)


  def Op2(self):
    pass


if __name__ == "__main__":
  c = generatorOp()
  c.write()

  d = generatorOp(number = 10)
  str = d.Op1()
  s = "".join(str)
  print s

      

