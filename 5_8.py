usernames = ['david', 'josh', 'mary', 'sophia', 'admin']

for name in usernames:
    if name == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello ", name.title(), "thank you for logging in again.")