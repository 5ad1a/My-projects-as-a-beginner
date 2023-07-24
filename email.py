# This programme codes for an email simulation

#===============================================class Email============================================#
# This class defines an email
class Email: 
    def __init__(self, from_address, subject_line, email_contents): 
        self.from_address = from_address
        self.subject_line = subject_line
        self.email_contents = email_contents
        self.has_been_read = False 
        self.is_spam = False

    def mark_as_read(self): 
        self.has_been_read = True 

    def mark_as_spam(self): 
        self.is_spam = True 

#================================================class Inbox==========================================#        
# This class stores all emails

class Inbox(): 
    def __init__(self):
        # empty list where all the email objects will be stored
        self.email_list = []
        
    # add the instances of the class Email to the list
    def add_email(self, email):
        self.add_email.append(email)      

    # returns the subject lines of the emails from a specific sender with a corresponding index    
    def list_messages_from_sender(self, sender_address):
        for index, item in enumerate(self.email_list): 
            if sender_address == item.from_address: 
                return f'{index} {item.subject_line} \n'

    # returns the subject lines of the emails from a specific sender with a corresponding index
    # the user can select to read a specific email using its corresponding number
    # the selected email is marked as read
    def get_email(self, sender_address, index): 
        item_list = []
        for item in self.email_list:
            if sender_address == item.from_address: 
                item_list.append(item)
        
        for it in item_list:  
            print(f'{it[index].subject_line} \n{it[index].email_contents}')
            it.has_been_read = True
            return True 
        return False 

        
    # returns the subject lines of the emails from a specific sender with a corresponding index
    # the user can select a specific email using its corresponding number as a spam
    def mark_as_spam(self, sender_address, index): 
        item_list = []
        for item in self.email_list:
            if sender_address == item.from_address: 
                item_list.append(item)
        
        for item in item_list:  
            item.is_spam = True
            return True 
        return False 

    # returns the subject lines of all the unread emails
    def get_unread_emails(self):
        str = ''
        for item in self.email_list: 
            if item.has_been_read == False: 
                str += f'{item.subject_line} \n'
        return str

    # returns the subject lines of all the emails marked as spams
    def get_spam_emails(self):
        str1 = ''
        for item in self.email_list: 
            if item.is_spam == True: 
                str1 += f'{item.subject_line} \n'
        return str1

    # returns the subject lines of the emails from a specific sender with a corresponding index
    # the user can delete a specific email using its corresponding number
    def delete(self, sender_address, index):     
        it_list = []
        for item in self.email_list:
            if item.from_address == sender_address:
                it_list.append(item)
        
        self.email_list.remove(it_list[index])

#======================================user interactions================================================#
inbox = Inbox()

user_message = print('''
Welcome to the email system! What would you like to do?

s - send email 
l - list emails from a sender
r - read email
m - mark email as spam
gu - get unread emails
gs - get spam emails
d - delete email
e - exit this program
''')

user_choice = (input('Enter your preference: ')).lower()

while True:    
    if user_choice == "s":
        # Creating new values for attributes in the class Email
        sender_address = input("Please enter the address of the sender: ")
        subject_line = input("\nPlease enter the subject line of the email: ")
        email_contents = input("\nPlease enter the contents of the email :")

        # Creating a new Email object
        new_email = Email(sender_address, subject_line, email_contents)

        # The new email is added to the inbox
        inbox.add_email(new_email)

        print("Email has been added to inbox.")
        pass


    elif user_choice == "l":
        # Asking the user to select an email sender 
        sender_address = input("Please enter the address of an email sender: ")

        # Printing a list of email subject lines from that specific user with their relative indices 
        inbox.list_messages_from_sender(sender_address)

        pass


    elif user_choice == "r":
        # Asking the user to select an email sender
        sender_address = input("Please enter the address of an email sender: ")
        
        # Showing all emails from this sender (with indexes)
        inbox.list_messages_from_sender(sender_address)
        
        # Ask the user for the index of the email and marking that email as read
        index = int(input("Please enter the index of the email that you would like to read: "))

        # Displaying the email (subject line + content)
        inbox.get_email(sender_address, index)

        pass


    elif user_choice == "m":
        # Asking the user to select an email sender
        sender_address = input("Please enter the address of an email sender: ")

        # Showing all emails from this sender (with indexes)
        inbox.list_messages_from_sender(sender_address)

        # Asking the user for the index of the email
        index = int(input("Please enter the index of the email that you would like to mark as spam: "))

        # Marking the email as spam 
        inbox.mark_as_spam(sender_address, index)

        print("Email has been marked as spam")

        pass

    elif user_choice == "gu":
        inbox.get_unread_emails()
        pass

    elif user_choice == "gs":
        inbox.get_spam_emails()
        pass

    elif user_choice == "d":
        # Showing emails from the sender
        sender_address = input("Please enter the address of an email sender: ")

        # Showing all emails from this sender (with indexes)
        inbox.list_messages_from_sender(sender_address)

        # Asking the user for the index of the email they want to delete
        index = int(input("Please enter the index of the email that you would like to delete: "))

        # Deleting the email
        inbox.delete(sender_address, index)

        pass

    elif user_choice == "e":
        print("Goodbye!")
        break
    
    else:
        print("Oops - incorrect input")