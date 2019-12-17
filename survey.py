import re
name_exp = r'[^\d\`\~\!\@\#\$\%\^\&\*\(\)|-|_\+\=\{\}\[\]\:\;\'\"\<\,\>\.\?\/\\]+'

fname = str(input("Please Enter your first name"))
while re.fullmatch(name_exp, fname) == None:
    print("This first name your provided is not valid")
    fname = str(input("Please Enter your first name"))

lname = str(input("Please Enter your last name"))
if(lname.isdigit()):
    print("This last name your provided is not valid")
        return
    else:
dob = input("Enter your date of birth in the format DD/MM/YYYY")
while re.fullmatch(r'\d{2}\/\d{2}\/\d{4}', dob) == None:
    print("The Date of Birth you provided is incorrect")
    dob = input("Enter your date of birth in the format DD/MM/YYYY")


r'\w+\@\w+\.\w+'


email = str(input("Enter your email address"))
if(email.isdigit()):
    print("Your email address is incorrect")
        return
    else:
zip = int(input("Enter your 5 digit zipcode"))
if(zip.isalpha():
    print("Your zipcode incorrect")
        return
    else:
city = str(input("Enter your city"))
if(city.isdigit()):
    print("Your city incorrect")
        return
    else:
state = str(input("Enter your state in two letter format"))
if(state.isdigit()):
    print("Your state is incorrect")
        return
    else:
state = str(input("Enter your state in two letter format"))
while re.fullmatch(r'[A-Z]{2})'
if(state.isdigit()):
    print("Your state is incorrect")
        return
    else:
race = str(input("Enter your race or who you identify as"))
if(race.isdigit()):
    print("Your race is incorrect")
        return
    else:
sex = str(input("Enter your sex or gender identification"))
if(race.isdigit()):
    print("Your gender identification is incorrect")
        return
    else:


age = int(input("Enter your age"))
while not (1 <= age <= 120):
    print("The age you entered is invalid")
    age = int(input("Enter your age"))

while true:
    try:
        name = pollInput()
    except AscertionError:
        continue
    break

assert(not fname.isdigit()), 'User Provided Digit, Invalid...'

obj = Obj()

obj and obj.func()
