#!/usr/bin/python
class lambdaOp(object):
  f = None
  def __init__(self,name = "lambdaOp",num1 = "1 ",num2 = "2 "):
    self.name = name
    self.num1 = num1
    self.num2 = num2
    self.lam = lambda x,y :x + y
    if lambdaOp.f == None:
      lambdaOp.f = open(name,"w")

  def Op1(self):
    #a = lambda x,y:x + y
    yield "lambdaOp\n"
    yield self.lam(self.num1,self.num2)
  
  def log(self,func):
    def handle(*args,**kwargs):
      s = fun(*args,**kwargs)
      lambdaOp.f.write("".join(s))
    return handle

  def write(self):
    lambdaOp.f.write("".join(self.Op1()))


if __name__ == "__main__":
  c = lambdaOp()
  c.write()


  #d = lambdaOp()
  #d.log( d.Op1())
  
