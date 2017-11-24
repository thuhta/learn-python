class Task5(object):
   def __init__(self):
       self.s = ""

   def getString(self):
       self.s = raw_input("in put your list: ")

   def printString(self):
       print (self.s.upper())

Result = Task5()
Result.getString()
Result.printString()