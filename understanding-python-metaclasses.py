'''
This project explores how Python metaclasses work, 
including custom metaclasses and how they influence class creation
'''

class Meta(type):
    pass
class A(metaclass=Meta):
    pass
print(type(A))