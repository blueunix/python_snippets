#/usr/bin/python
class ObserverManager(object):
  observers = []
  
  def __init__(self,name = "manager"):
    self.name = name

  def register(self,observer):
    ObserverManager.observers.append(observer)
  

class AppleObserver(object):

  def __init__(self,name = "apple"):
    print "create AppleObserver"

  def handle(self):
    print "handled by AppleObserver"

class OrangeObserver(object):
  def __init__(self,name = "orange"):
    print "create OrangeObserver"
  
  def handle(slef):
    print "handled by OrangeObserver"


def handle(Manager):
  for observer in Manager.observers:
    observer.handle()


if __name__ == "__main__":
  om = ObserverManager()
  apple = AppleObserver()
  orange = OrangeObserver()
  om.register(apple)
  om.register(orange)
  

  #under some conditions,will call this handle() func
  handle(om)



  
