# Contact Management System 

contacts ={}

def add_contact():

    name = input("Enter contact name: ")
    phone = input("Enter contact phone: ")
    email = input("Enter contact email: ")

    if phone in contacts :
        print("Contact already exists!")

    else :

        contacts[phone] ={
            "name" : name ,
            "email" : email 
        }

        print("Contact added successfully")


def view_contact():

    if not contacts :
        print("No Contacts available!")

    else:
        print("\n==== SAVED CONTACTS ====")

    for phone , details in contacts.items() :

        print("------------------")
        print("Name",details["name"])
        print("Phone",phone)
        print("Email",details["email"])


def search_contact() :

    search_name = input("Enter name to search: ")

    for phone , details in contacts.items():

        if search_name.lower() in details["name"].lower():

            print("\nContact Found!")
            print("Name", details["name"])
            print("Phone",phone)
            print("Email", details["email"])
            break
        else:
            print("Contact not found!")


def update_contact():

    phone = input("Enter your phone number to update: ")

    if phone in contacts:

        print("Contact Found!")

        new_name = input("Enter new name: ")
        new_email = input("Enter new Email: ")

        contacts[phone]["name"] = new_name
        contacts[phone]["email"] = new_email

        print("Contact updated successfully!")

    else:
        print("Contact not found!")


def delete_contact():

    phone = input("Enter your phone number to delete: ")

    if phone in contacts:

        del contacts[phone]

        print("Contact deleted successfully!")

    else:
        print("Contact not found!")


while True :
    print("\n============================")
    print("\nContact Management System    ")
    print("\n============================")

    print("1.Add Contact")
    print("2.View All Contacts")
    print("3.Search Contact")
    print("4.Update Contact")
    print("5.Delete Contact")
    print("6.Exit")


    choice=input("\nEnter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contact()

    elif choice == "3":
        search_contact()

    elif choice =="4":
        update_contact()

    elif choice =="5":
        delete_contact()

    elif choice =="6" :
        print("Thankyou for using Contact Management System !!!")
        break

    else:
        print("Invalid choice! Please try again.")



    