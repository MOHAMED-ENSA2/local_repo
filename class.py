# this source code for creating a class and used it in python
class student : 
  def __init__(self, name) : 
     self.name = name 
  def disp(self) :
     print ("your name is " + self.name)
Student1 = student("Mohamed")
Student1.disp()
