"""
Abstraction
encapsulation
inheritence
polymorphism
class:collection of a data members and member functions (methods) that act on these data members
-it is a blue print/templsate for the objects
-class is an abstraction/representation/declaration of the real world entities called objects have some characterictics and behaviour
object:real worls entity that is having some charectistics/attributes/property and behaviour(methods)
-object is an instance of class
-the process of object creation is known as instiation
-we can create as manby objects as required of any class.
-evrey object is independent from another object
**Every object has the following featurea
-->Identity:Everry object must be uniquely defined.
-->State?Charecteristics/Attribute/Property:An object has some attribute that represent a state of objects.
-->Behaviour:An object has methods that represents its behaviour.
-->functioned defined insed class is called method
"""
"""
class Circle:
    #OPtional docString"""
    #variable:A class variable and instance variable
    #class variable:A variable declared within a class but outside from the class methods
    #instance variable:It is a variable within methods of class
    #method:
    #constructor intialize varaiabled of a  class
    #-->called automatically when obj of class is created.
    #-->types of constructer:default constructor,parameterless constructor,parameterised constructor
    #destructor
    #to create object of any class
  #syntax:objname=Classname()
"""  
    PI=3.141
    def m1(self):#self is used to represent current object
        print("This a simple method")
    def Area(self,r):
        self.r1=r
        print("Area of circle : ",(Circle.PI*self.r1*self.r1))
   

class Student:
    def __init__(self):
        self.x=10
        self.y=20
    def add(self):
        return self.x+self.y

"""
class Student:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
