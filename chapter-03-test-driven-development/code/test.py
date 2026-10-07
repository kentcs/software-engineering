from maths import *

def test_add():
   assert add5(2,2) == 4
   assert add5(3,3) == 6
   assert add5(4,4) == 8
   assert add5(3,4) == 7
   for i in range(0,1000):
      for j in range(0,1000):
         assert(i+j == add5(i,j))
   assert 7.299999999 < add5(3.1,4.2) < 7.30000000000001
   assert add5(-3, -4) == -7
   assert add5(123.456, 123.456) == 123.456 + 123.456


if __name__ == "__main__":
   test_add()


