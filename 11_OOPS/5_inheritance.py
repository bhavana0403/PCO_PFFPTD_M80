"""
There are 4 main pillars of object-oriented programming
1) Inheritance
2) Polymorphism
3) Abstraction
4) Encapsulation
"""
"""
Inheritance
-> Here, we derive the properties from one class to another class
-> Inheritance is a mechanism for creating a new class that specifies or modifies 
   the behavior of an existing class
-> Class from which we inherit the properties is called parent class/ base class/
   super class
-> Class to which we inherit the properties is called subclass/ derived class/ child
   class/ subtype
-> Child class will inherit the properties from parent class, it may add new 
   attributes or redefine any of the properties
-> There are 5 types
    1) Single Level Inheritance
    2) Multi Level Inheritance
    3) Multiple Inheritance
    4) Hierarchical Inheritance
    5) Hybrid Inheritance
"""

"""
Single Level Inheritance
-> Deriving the properties from one class to another class by considering one
   level is called single level inheritance.
-> Every class is a kind of single level inheritance because it inherits some of
   properties (methods) from object class 
-> Syntax:
            class PC:
                SB
            class CC(PC):
                SB
"""

# class A:
#     pass
#
# print(dir(A))

class demo:
    a = 11
    b = 22

    def __init__(self, x, y):
        self.x = x
        self.y = y


class child_demo(demo):
    pass

print(dir(demo))
print(demo.__dict__)    # 'a': 11, 'b': 22

print(dir(child_demo))  # same as that of demo
print(child_demo.__dict__)

obj1 = child_demo(3, 4)
print(obj1.__dict__)    # {'x': 3, 'y': 4}
print(dir(obj1))        # a, b, x, y

obj2 = demo(30, 40)
print(obj2.__dict__)    # {'x': 30, 'y': 40}
print(dir(obj2))        # 'a', 'b', 'x', 'y'

##############################################################################

# child and parent has unique properties

class Demo:
    def __init__(self, value):
        self.value = value

    def apple(self):
        print("Demo.apple", self.value)

    def yahoo(self):
        print("Demo.yahoo", self.value)


class Demo1(Demo):
    def google(self):
        print("Demo1.google", self.value)


obj1 = Demo(11)
obj2 = Demo1(22)

print(dir(Demo))        # 'apple', 'yahoo'
print(Demo.__dict__)    # 'apple', 'yahoo'

# print(dir(Demo1))       # 'apple', 'google', 'yahoo'
# print(Demo1.__dict__)   # 'google'

# print(dir(obj1))        # 'apple', 'value', 'yahoo'
# print(obj1.__dict__)    # {'value': 11}
#
# print(dir(obj2))        # 'apple', 'google', 'value', 'yahoo'
# print(obj2.__dict__)    # {'value': 22}

###############################################################################

# child and parent has same properties

class Demo:
    def __init__(self, value):
        self.value = value

    def apple(self):
        print("Demo.apple", self.value)

    def yahoo(self):
        print("Demo.yahoo", self.value)

class Demo1(Demo):
    def yahoo(self):
        print("Demo1.yahoo", self.value)


# obj1 = Demo(22)
# obj2 = Demo1(33)
#
# print(dir(Demo))
# print(dir(Demo1))
#
# print(Demo.__dict__)        # apple, yahoo
# print(Demo1.__dict__)       # yahoo
#
# obj1.yahoo()        # Demo.yahoo 22
# obj2.yahoo()        # Demo1.yahoo 33

###############################################################################################

"""
-> Suppose you override a parent method in child class but still want to use it
   in child class, we make use of chaining
-> Constructor Chaining
    - Here we invoke the constructor method of parent class by being there in 
      constructor of child class
    - Syntax:
            super().__init__(args)
            parentclassname.__init__(self/obj, args)
            
-> Method Chaining
    - Here, we invoke the method of parent class by being there in method of 
      child class
    - Syntax:
            super().mname(args)
            parentclassname.mname(self/obj, args)
"""

class Demo:
    def __init__(self, value):
        self.value = value

    def apple(self):
        print("Demo.apple", self.value)

    def yahoo(self):
        print("Demo.yahoo", self.value)


class Demo1(Demo):
    def __init__(self, value, extra_value):
        self.extra_value = extra_value
        # super().__init__(value)
        Demo.__init__(self, value)
    def yahoo(self):
        print("Demo1.yahoo", self.extra_value)
        # super().yahoo()
        Demo.yahoo(self)

obj1 = Demo(10)
obj2 = Demo1(11, 22)

obj1.yahoo()        # Demo.yahoo 10
obj2.yahoo()
"""
Demo1.yahoo 22
Demo.yahoo 11
"""