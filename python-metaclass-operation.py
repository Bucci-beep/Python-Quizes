'''
A simple project demonstrating Python metaclasses, including how 
they work and how they can be used to track class creation dynamically.
'''

class Meta(type):
    def __init__(cls, name, bases, dct):
       print("Initializing: ", name)
class A(metaclass=Meta):
    pass