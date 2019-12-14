# importing the regular expression
import re
# this is the regular expression that check for non standard characters
name_exp = r'[^\d\`\~\!\@\#\$\%\^\&\*\(\)|-|_\+\=\{\}\[\]\:\;\'\"\<\,\>\.\?\/\\]+'
# this is the regular expression that checks for a-z A-Z characters only
alpha_exp = r'[a-zA-Z]+'
# this is the input line that asks for your first name
fname = str(input("Please Enter your first name"))
# this is the while loop that runs the validation check
while re.fullmatch(name_exp, fname) == None:
    print("This first name your provided is not valid")
    fname = str(input("Please Enter your first name"))
