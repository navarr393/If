gender = ['male', 'female']
county = ['LA County', 'Orange County', 'Riverside County']
residence = [(genders, counties) for genders in gender for counties in county]

print(residence)

residence = [(genders, counties) for counties in county for genders in gender]

print(residence)

residence = [(counties, genders) for counties in county for genders in gender]

print(residence)

residence = [(counties, genders) for genders in gender for counties in county]

print(residence)
