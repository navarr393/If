current_users = ['David', 'John', 'Daisy', 'Steph', 'Marco']
new_users = ['David', 'John', 'Tom', 'Carl', 'Mario']
new_list = ['DAVID', 'JOHN', 'DAISY', 'STEPH', 'MARCO']

for user in new_users:
    if user in current_users and user.upper() in new_list:
        print("Sorry ", user,  "has already been used. Try again.")
    else:
        print(user, " is available as a username.")
    

    
