emails = {}
email = input("Email: ")
while email != '':
    fullname = email.split("@")[0]
    try:
        firstname = fullname.split(".")[0]
        lastname = fullname.split(".")[1]
        choice = input(f"Is your name {firstname.capitalize()} {lastname.capitalize()}? (y/n) ").lower()
    except IndexError:
        firstname = fullname.split(".")[0]
        lastname = ''
        choice = input(f"Is your name {firstname.capitalize()} ? (y/n) ").lower()
    if choice[0].lower() == 'n':
        fullname = input("Name: ").split()
        firstname = fullname[0].capitalize()
        lastname = fullname[1].capitalize()
        emails[email] = f"{firstname.capitalize()} {lastname.capitalize()}"
    else:
        emails[email] = f"{firstname.capitalize()} {lastname.capitalize()}"
    email = input("Email: ")
for email in emails:
    print(f'{emails[email]} ({email})')
