import random, math, socket
import hashlib
import pyjokes

class BackendCompute:

    def __init__(self, myHostName):
        self.name = myHostName
         
    def get_a_joke(self):
         return pyjokes.get_joke(language='en', category="neutral")
