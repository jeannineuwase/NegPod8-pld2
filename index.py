print("Welcome to Appoint Doc")

# Prompt the user if they have an account
answer = input("Do you have an account? (Yes/No) ")

# Check the user's answer
if answer == "Yes":
    print("Great! Please sign in.")
    # Code for sign in
elif answer == "No":
    print("No problem. Please sign up to continue booking an appointment with our available doctors.")
    # Code for sign up
else:
    print("Invalid input. Please enter 'Yes' or 'No', Otherwise, you will not be able to process.")
