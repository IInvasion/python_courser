def user_data(**kwargs):
    """Return user_data."""
    return(kwargs)


for key, value in user_data(first_name=input('Enter your first name: '), last_name=input('Enter your last name: '),
                            year_of_birth=input('Enter your year of birth: '), city_of_residence=input('Enter your city of residence: '),
                            email=input('Enter your email: '), phone=input('Enter your phone: ')).items():
    print(key, '-', value, end='; ')