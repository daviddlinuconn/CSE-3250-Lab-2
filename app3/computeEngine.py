import random, math, socket
import hashlib
import pyjokes

class BackendCompute:

    def __init__(self, myHostName):
        self.name = myHostName
         
    def get_a_joke(self):
      random_integer = random.randint(1,2)
      if (random_integer == 1):
         return pyjokes.get_joke(language='en', category="neutral")
      else:
         return pyjokes.get_joke(language='es', category="neutral")
         
