import random, math, socket
import hashlib
import pyjokes

class BackendCompute:

    def __init__(self, myHostName):
        self.hashFunction = hashlib.new('sha256')
        self.name = myHostName

    def processPRandomInteger(self):
        data = self.name
        myBytes = data.encode()
        self.hashFunction.update(myBytes)
        self.seed = int(self.hashFunction.hexdigest(),base=16) % 2**32
        random.seed(self.seed)
         
    def get_a_joke(self):
      random_integer = random.randint(1,2)
      if (random_integer == 1):
         return pyjokes.get_joke(language='en', category="neutral")
      else:
         return pyjokes.get_joke(language='es', category="neutral")
         
