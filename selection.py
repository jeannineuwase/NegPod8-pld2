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

