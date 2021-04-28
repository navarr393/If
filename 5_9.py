usernames = ['david', 'josh', 'mary', 'sophia', 'admin']
#usernames.clear()
for name in usernames:
    if len(usernames) == 0:
        print("We need to find some users!")
    if name == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello ", name.title(), "thank you for logging in again.")
    
