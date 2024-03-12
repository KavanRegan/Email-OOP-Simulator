### --- OOP Email Simulator --- ###

# Email class
class Email():
    # - Class variable with a False default value
    has_been_read = False
    # - Initialise constructor for email address, subject line and email content
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
    # - Class method to change has_been_read variable to True
    def mark_as_read(self):
        if self.has_been_read == False:
            return False
        return True
    # - Using __str__ special method to make content readable
    def __str__(self):
        return "'{}', '{}', '{}'".format(self.email_address, self.subject_line, self.email_content)

# Initialise an empty list to store the email objects.
inbox = []

# --- Functions --- #
 
def populate_inbox():
    '''
    populate_inbox function:
    
    - Creates email objects with email address, subject line and email content
    - Add email objects to empty inbox list '''

    email1 = Email("James@mail.com", "Greetings", "Hello, how are you?")
    email2 = Email("Laura@mail.com", "Overtime" , "Are you availible for overtime saturday?")
    email3 = Email("Pete@mail.com", "Lunch", "Where we going for lunch today?")
    
    inbox.append(email1)
    inbox.append(email2)
    inbox.append(email3)

def list_emails():
    '''
    list_emails function:

    - Lists subject line with a corrisponding number'''
    
    print("\n  Subject:\n")
    for index, email in enumerate(inbox, 1):
        print(f"{index} {email.subject_line}")
    
def read_email(index):
    '''
    read_email function:
    
    - Grab the email the user has selected
    - Print the email address, subject line and email content
    - Change the has_been_read variable to True'''

    if 1 <= index <= len(inbox):
        email = inbox[index - 1]
        print(f'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~             
From: {email.email_address}
Subject: {email.subject_line}

{email.email_content}

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
        
        
        email.has_been_read = True
    else:
        print("Invalid Email Number")
        

# --- Email Program --- #

# - Call populate_inbox function to add email objects to the inbox list
populate_inbox()

menu = True

while True:
    user_choice = int(input('''\nWould you like to:
1. Read an email
2. View unread emails
3. Quit application

Enter selection: '''))
       
    if user_choice == 1:
        # - Call list_emails function
        list_emails()
        # - Get the user to enter the email number
        index = input("\nEnter the number of the email you would like to read: ")
        if index.isdigit():
            index = int(index)
            # - Call read_email function with the email index number
            read_email(index)
        else:
            print("Invalid Input")
        
    elif user_choice == 2:
        # - List comprehension to store unread emails
        unread_emails = [email for email in inbox if not email.has_been_read]
        # - Print unread email subject line 
        if unread_emails:
            print("\nUnread Emails:")
            for i, email in enumerate(unread_emails, 1):
                print(f"{i} {email.subject_line}")
        else:
            print("No Unread Emails")

    elif user_choice == 3:
        break
    
    else:
        print("Oops - incorrect input.")