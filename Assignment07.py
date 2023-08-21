# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with Pickle Module,
#              and Structured Error Handling
# ChangeLog (Who,When,What):
# LEspinoza,08.19.2023, Created started script
# ---------------------------------------------------------------------------- #

import pickle

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
fltN1 = None  # first argument
fltN2 = None  # second argument
fltR1 = []  # list with results of basic math
objFile = "BasicMathList.txt"   # An object that represents a file
objFileBin = "BasicMathList.dat" # An object that represents a binary format file

# Processing  --------------------------------------------------------------- #
def saveData (data, file_name):
    """ Saves list data to a plain text file"""
    file = open(file_name, "w")
    file.write(str(data))
    file.close()

def saveDataBin (data, file_name): # Pickling
    """ Saves list data to a binary format file"""
    file = open(file_name, "wb") # write to a binary file
    pickle.dump (data, file)
    file.close()

def readDataBin (file_name): # Unpickling
    """ Read the last list data saved in binary format file"""
    try:
        file = open(file_name, "rb") # read from a binary file
        fileData = pickle.load (file)
        file.close()
        print("Sum" + "=" + str(fileData[0]))
        print("Difference" + "=" + str(fileData[1]))
        print("Product" + "=" + str(fileData[2]))
        print("Quotient" + "=" + str(fileData[3]))
    except:
        print ("file not found!!")

def MathValues(value1, value2):
    """ the four formulas of basic math"""
    try:
        add = value1 + value2
        difference = value1 - value2
        product = value1 * value2
        quotient = value1 / abs(value2)
        return [add, difference, product, quotient]
    except ZeroDivisionError as e: # to find a ZeroDivisionError in the quotient formula
        print("There was an error")
        print(e.__doc__)


# Presentation (Input/Output)  -------------------------------------------- #
print ("These were the last results saved")
readDataBin(objFileBin) # calling the readDataBin function
print ("----------------------------------------")

input ("Please press Enter Key to continue: ")

try:
    fltN1 = float(input("Enter value 1: ")) # Asking the user to enter the first value
    fltN2 = float(input("Enter value 2: ")) # Asking the user to enter the second value
except ValueError as e: # I want the user enter only numbers
    print ("That was not a number!")
    print (e)
fltR1 = MathValues(fltN1, fltN2) # variable to catch the list with results
print("The Sum of %.2f and %.2f is %.2f" % (fltN1, fltN2, fltR1[0]))
print("The difference of %.2f and %.2f is %.2f" % (fltN1, fltN2, fltR1[1]))
print("The product of %.2f and %.2f is %.2f" % (fltN1, fltN2, fltR1[2]))
print("The quotient of %.2f and %.2f is %.2f" % (fltN1, fltN2, fltR1[3]))

saveData(fltR1, objFile) # calling the saveData function
saveDataBin(fltR1, objFileBin) # calling the saveDataBin function
print ("Data saved in both format .txt and .dat")