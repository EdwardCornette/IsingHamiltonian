import numpy as np
import math


class BitString:
    """
    Simple class to implement a config of bits
    """

    def __init__(self, N):  # costructor
        self.N = N
        self.config = np.zeros(
            N, dtype=int
        )  # creates an int array of length n, with default values of 0

    def __repr__(self):  # returns a string representing the object
        temp = ""
        for i in range(0, self.N):
            temp = temp + str(self.config[i])
        return temp

    def __eq__(self, other):  # defines the requirements for equality between objects
        if self.N != other.N:
            return False

        for i in range(0, self.N):

            if self.config[i] != other.config[i]:
                return False

        return True

    def __len__(self):  # returns the length of the object
        return self.N

    def on(self):  # number of on bits
        counter = 0
        for i in range(0, self.N):
            if self.config[i] == 1:
                counter = counter + 1
        return counter

    def off(self):  # number of off bits
        counter = 0
        for i in range(0, self.N):
            if self.config[i] == 0:
                counter = counter + 1
        return counter

    def flip_site(self, i):  # toggles bit at given location
        if self.config[i] == 1:
            self.config[i] = 0
        else:
            self.config[i] = 1

    def int(self):  # returns base ten value of bitstring
        total = 0
        for i in range(0, self.N):
            total = total + (2**i * self.config[self.N - 1 - i])

        return total

    def set_config(self, s: list[int]):  # creates bitstring from list
        for i in range(0, self.N):
            if s[i] == 0:
                self.config[i] = 0
            else:
                self.config[i] = 1

    def set_int_config(self, dec: int):  # creates bitstring from base 10 value
        val = dec
        temp = np.zeros(self.N, dtype=int)
        counter = 0
        while val != 0:
            counter = counter + 1
            temp[-counter] = val % 2
            val = val // 2
        self.set_config(temp)
