class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def __gt__(self, other):
    return True if self.age > other.age else False

roger = Dog("Roger", 8)
shaggy = Dog("Shaggy", 7)

print(roger > shaggy)
    
"""

__add__       ( + )
__sub__       ( - )
__mul__       ( * )
__truediv__   ( / )
__floordiv__  ( // )
__mod__       ( % )
__pow__       ( ** )
__rshift__    ( >> )
__lshift__    ( << )
__and__       ( & )
__or__        ( | )
__xor__       ( ^ )

"""