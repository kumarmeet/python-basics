# enums are readable names that bound constant values

from enum import Enum

class State(Enum):
  INACTIVE = 0
  ACTIVE = 1

State.ACTIVE
State.INACTIVE

print(State.ACTIVE)
print(State.ACTIVE.value)
print(State(1))
print(State["INACTIVE"])

print(list(State))
print(len(list(State)))