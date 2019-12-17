from enum import IntEnum
class Month(IntEnum):
  JANUARY = 1
  FEBRUARY = 2
  MARCH = 3
  APRIL = 4
  MAY = 5
  JUNE = 6
  JULY = 7
  AUGUST = 8
  SEPTEMBER = 9
  OCTOBER = 10
  NOVEMBER = 11
  DECEMBER = 12

def isInt(input):
  val = int(input)

def getFirstName():
  try:
    fName = input("First Name: ")
    if(len(fName) > 30):
      print("Please type in a reasonable first name")
      getName()
    #does not work
    if(fName.isalpha() == False):
      print("Stop")
      getFirstName()
  except ValueError:
    print("\nPlease input letters only")

def getLastName():
  try:
    lName = input("Last Name: ")
    if(len(lName) > 30):
      print("Please type in a reasonable last name")
      getName()
    if(lName.isalpha() == False):
      print("Stop")
      getLastName()
  except ValueError:
    print("\nPlease input letters only")

def getName():
  #no numbers
  getFirstName()
  getLastName()


def getDOB():
  #don't accept too recent of dates
  print("\nPlease input the following in numbers")
  try:
    month = int(input("Month: "))
    isInt(month)
    if (month < Month.JANUARY or month > Month.DECEMBER):
      print("Please enter a valid month")
      getDOB()
  except ValueError:
    print("Please enter an integer value")
    getDOB()
  try:
    #will clean this up
    date = int(input("Date: "))
    if (date < 1 or date > 31):
      print("Please enter a valid day")
      getDOB()
    if (month == Month.FEBRUARY):
      if (date < 1 or date > 29):
        print("Please enter a valid day for February")
        getDOB()
    if(month == Month.APRIL or month == Month.JUNE or month == Month.SEPTEMBER or month == Month.NOVEMBER):
      if (date < 1 or date > 30):
        print("This month only has 30 days. Please try again")
        getDOB()
    isInt(date)
  except ValueError:
    print("Please enter an integer value")
  try:
    year = int(input("Year: "))
    if (year > 50 and year < 99):
      print("Did you mean" + year + 1900)
    if(year <2010):
      isInt(year)
  except ValueError:
    print("Please enter an integer value")

def getEmail():
  #check for back containing . something
  email = ("Please type in your email: ")

def getAddress():
  #import dictionary of possible options
  zipcode = input("Zipcode: ")
  city = input("City: ")
  state = input("State: ")

def getRace():
  #make this one optional
  race = input("Race: ")

def getAge():
  age = input("Age: ")

def getSex():
  sex = input("Sex: ")
  # if sex not in (Gender.MALE, Gender.FEMALE, Gender.N_A):
  #   raise ValueError('gender not valid')

def main():
  #store and print this information next
  getName()
  getDOB()
  getEmail()
  getAddress()
  getRace()
  getAge()
  getSex()

main()
