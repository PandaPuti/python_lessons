#Global Scope : variables defined outside function are in global scope means they can be accessed from anywhere, they are called global variable
def addDC(x):     #function addDC is called it creates a new scope 'Scope addDC' where they access the global variable, after they return the function scope deletes
    b = x + "DC" #b is local variable as it is defined in the function, local to this function
    print(b)
x = 'AC'
addDC(x) #ACDC
print(x) #AC

def Thriller(): # Scope Thriller Date = 1982 return value of Date
  Date = 1982
  return Date
Thriller()
1982

Date # in the global scope variable named Date is not Defined so it throws an error

NameError: name 'Date' is not defined


#local and global variable can have same name
def Thriller():
  Date = 1982
  return Date
localDate = Thriller()
Date = 2017
print(Date) #2017
print(localDate) #1982

#if a variable is not defined in the local scope of a function then the function checks for it the global function
def addRating(rate):
  print(Rating)
  return Rating + rate

Rating = 6
Z = addRating(2)
print(Z)

6
8
def PinkFloyd():
    global ClaimedSales
    ClaimedSales = '45 millions'
    return ClaimedSales
print(PinkFloyd())
ClaimedSales

45 millions
'45 millions'
