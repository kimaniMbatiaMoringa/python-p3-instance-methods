#!/usr/bin/env python3
import ipdb
print("Running dog class")
class Dog:
    # Class body goes here
    def __init__(self,breed="Mutt"):
        #self.name = name
        self.breed = breed

    #Instance method definition
    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")    

#fido = Dog("fido")
#ipdb.set_trace()


