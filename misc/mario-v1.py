def form():
    fname = input("Enter first name ").strip()
    print(f"Your first name is {fname}")
    lname = input("Enter last name ").strip()
    print(f"Your last name is {lname}")
    dob = input("Enter Date of Birth ").strip()
    print(f"Your Date of Birth is {dob}")#format date and return age as well
    email = input("Enter email ").strip()
    print(f"Your email is {email}")
    zip_code = input("Enter zip code ").strip()
    print(f"Your zip code is {zip_code}")#return city and state as well
    race = input("Enter first race or press enter to skip ").strip()
    print(f"Your race is {race}")
    sex = input("Enter gender ").strip()
    print(f"Your gender is {sex}")

if __name__ == "__main__":
    form()
