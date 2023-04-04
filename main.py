print("Welcome to Appoint Doc")
info = {'john': 12345, 'anissa': 00000, 'jacques': 20011, 'umutoni': 20008}
def sign_up():
    name = input('Enter your name: ')
    password = int(input('Enter your password and should be 5 digits: '))
    if name not in info or password != info[name]:
        info[name] = password
        print('Sign up successful.')
    elif name in info or password == info[name]:
        print('Username or account existed')
                
def log_in():
    name = input('Enter your name: ')
    password = int(input('Enter your password and should be 5 digits: '))
    
    if name in info and password == info[name]:

        print('Log in successful')
        
    else:
        print('Log in denied.create an account or try again!')
        sign_up()
                       
# Prompt the user if they have an account
answer = input("Do you have an account? (Yes/No) ")
if answer == "Yes":
    print("Great! Please sign in.")
    log_in()
elif answer == "No":
    print("No problem. Please sign up to continue booking an appointment with our available doctors.")
    sign_up()
    # Code for sign up
else:
    print("Invalid input. Please enter 'Yes' or 'No', Otherwise, you will not be able to process.")    
def consultation(hours):
    print("Available time you can book")
    for i, hour in enumerate(hours):
        x= i + 1
        print("{}. {}".format(x, hour))
def dentist(hours):
    print("Available time you can book")
    for i, hour in enumerate(hours):
        x = i + 1
        print("{}. {}".format(x, hour))
def cardiology(hours):
    print("Available time you can book")
    for i, hour in enumerate(hours):
        x = i + 1
        print("{}. {}".format(x, hour))
def neurology(hours):
    print("Available time you can book")
    for i, hour in enumerate(hours):
        x = i + 1
        print("{}. {}".format(x, hour))  
def pyschology(hours):
    print("Available time you can book2")
    for i, hour in enumerate(hours):
        x = i + 1
        print("{}. {}".format(x, hour))                      
hours = [ '1st jan, 8:00AM', '1st Jan, 9:00AM', '1st Jan, 10:00AM', '1st Jan, 11:00AM', '3rd Jan, 1:00PM', '3rd Jan, 2:00PM', '3rd Jan, 3:00PM', '3rd Jan, 4:00PM']
def ServiceMenu():
    print("Available Services We Offer")
    print("1. Consultation")
    print("2. Dentist")
    print('3. Cardiology')
    print("4. Neurology")
    print("5.Psychology")
    service = int(input('Select the the number that corresponds with service you want: '))
    if service == 1:
        consultation(hours)
    elif service == 2:
        dentist(hours)
    elif service == 3:
        cardiology(hours)
    elif service == 4:
        neurology(hours)
    elif service == 5:
        pyschology(hours)    
    else:
        print('Invalid choice.')        
ServiceMenu()           

# Prompt the user to enter a time slot for the appointment
appointment_time = input("Enter a time slot for the appointment (e.g. '1st jan, 8:00AM'): ")

# Check if the time slot is available
if appointment_time in hours :
    # Book the appointment
    print("Appointment booked for", appointment_time)
    hours .remove(appointment_time)
    # Remove the booked time slot from the list of available time slots
    print("Updated list of available time slots:")
    for time_slot in hours :
        print(time_slot)
else:
    # Print an error message if the time slot is already taken
    print("Sorry, the time", appointment_time, "is already booked.")
