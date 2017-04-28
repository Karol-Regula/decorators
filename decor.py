import time

def argsDec(func):#returns the name and arguments of the function
  def inner(*args):
    print "function name: " + str(func.func_name)
    print "running with args: " + str(args)
    func(*args)
    return
  return inner

def timeDec(func):#returns the execution time for the function
  def inner(*args):
    initial = time.time()
    func(*args)
    final = time.time()
    print "execution time: " + str(final - initial)
    return
  return inner

@timeDecs
def testFunction1(i, j):
  for x in range(i):
    x*x
  for x in range(j):
    x*x
  return

@argsDec
def testFunction2(i, j):
  for x in range(i):
    x*x
  for x in range(j):
    x*x
  return

testFunction1(10000000, 2000)
testFunction2(10000000, 2000)
