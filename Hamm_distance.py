import math
import numpy as np
import pandas as pd
import argparse

input1 = input()
input2 = input()

Hammer = 0
loop = 0

for i in input1:
    if i != input2[loop]:
        Hammer += 1
        loop += 1
    else:
        loop += 1

print(Hammer)


#GAGCCTACTAACGGGAT
#CATCGTAATGACGGCCT