__author__ = "James Elkins"
__copyright__ = "Copyright 2015"
__credits__ = ["James Elkins"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "James Elkins"
__email__ = "jelkinsiv@gmail.com"
__date__="2015/05/24"

import sys
import array
import random

#Returns a random number within the dice parameters
def getDiceNum(dString):
    dieParts = dString.split("d")
    diceTotal = 0
    for dice in range(0, int(dieParts[0])):
        dieRoll = random.randrange(1, (int(dieParts[1]))+1)
        print("Die rolled " + str(dieRoll)) + " on a d" + dieParts[1]
        diceTotal = diceTotal + dieRoll
    return diceTotal

#starts rolling the dice or adding the bonus
def rolldice(dString):

    if '+' in dString:
        dArray = dString.split("+")
        dTotal = 0
        for d in dArray:
            if "d" in d:
                dTotal = dTotal + getDiceNum(d)
            else:
                print("Adding Bonus of " + d)
                dTotal = dTotal + int(d)
    else:
        dTotal = getDiceNum(dString)

    print("Total rolled is " + str(dTotal) +"\n")

#get the string that contains the request rolls
diceString = sys.argv[1]

try:
    if len(sys.argv) == 3:
        for x in range(int(sys.argv[2])):
            rolldice(diceString)
    else:
        rolldice(diceString)
except:
    print("!!Invalid dice string!!\n     "
          "Dice Format number of dice d dice type (ex 1d20)\n     "
          "You can add dice by using a plus (+) with no space (ex 1d4+1d8)\n     "
          "You can add a bonus modifier with a plus (+) ex 1d20+4)\n     "
          "You can run the roll as many times as needed by adding a second parameter (ex 1d20 2)")