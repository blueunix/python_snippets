#/usr/bin/python
class typeOp(object):
  num_instance = 0 
  li = []
  def __init__(self,name = "typeOp"):
    print "create instance"
    self.name = name
    typeOp.li.append(name)
    typeOp.num_instance += 1

  def __del__(self):
    print "delete instance"
    typeOp.num_instance -= 1

  def typeTest(self,instance,cls):
    try:
      if isinstance(instance,cls):
        print "%(instance)s is %(cls)s, yes" % locals()
      else:
        print "%(instance)s is not %(cls)s,no" % locals()
    except AttributeError:
      print "AttributeError handled"
   
  def lambdaTest(self,x,y):x+y

        
class typeOpApple(typeOp):
  def __init__(self,name = "testApple"):
    typeOp.__init__(self,name) 
    self.logs = []




if __name__ == '__main__':
  obj = typeOp("test")
  objApple = typeOpApple()
  obj.typeTest(obj,typeOp)
  obj.typeTest(objApple,typeOp)
  obj.typeTest(objApple,typeOpApple)
  obj.typeTest(obj,typeOpApple)

  #print "lambdaTest is " % obj.lambdaTest(1,2)

  del obj
  del objApple

  
