#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    APPROVED_BREEDS = ["Pug", "German Sherpherd", "Bulldog", "Golden Retriever"]

    def __init__(self, name=None, breed=None):
        if name is not None:
            if type(name)is not str or len(name) < 1 or len(name) > 25:
                print("Name must be string between 1 and 25 characters.")
        self.name = name  

        if breed is not None:
            if breed not in self.APPROVED_BREEDS:
                print("Breed must be in list of approved breeds.")  
        self.breed = breed        
    pass
