#contact book
contacts={}
def show_menu():
 print("\n---Contact Book Menu---")
 print("1.Add Contact")
 print("2.View Contact")
 print("3.Search Contact")
 print("4.Edit Contact")
 print("5.Delete Contact")
 print("6. Exit Contact Book")

def add_contact():
 name=input("Enter contact name:")
 phone= input("Enter contact number:")
 email=input("Enter contact email:")
 contacts[name]={"phone":phone,"email":email}
 print(f"Contact {name} has been added to your contatc book successfully!")

def view_contacts():
 if contacts:
  print("\n---Contact List---")
  for name, details in contacts.items():
   print(f"Name:{name}")
   print(f"Phone: {details['phone']}")
   print(f"Email: {details['email']}")
 else:
  print("Your contact book is empty.")
   
def search_contact():
 name=input("Enter the name of the contact you want to search:")
 if name in contacts:
  print(f"---Contact details for {name}---")
  print(f"Name:{name}")
  print(f"Phone: {contacts[name]['phone']}")

def edit_contact():
 name=input("Enter the name of the contact you want to search:")
 if name in contacts:
  print(f"\n---Enter the name of the contact you want to edit: ")
  if name in contacts:
   phone =input("Enter new phone number:")
   email=input("Enter new email:")
   contacts[name]={"phone":phone,"email":email}
   print(f"Contact {name} has been updated successfully!")
  else:
   print(f"Contact {name} not found in your contact book.")

def delete_contact():
 name=input("Enter the name of the contact you want to delete:")
 if name in contacts:
  del contacts[name]
  print(f"Contact {name} has been deleted successfully!")
 else:
  print(f"Contact {name} not found in your contact book")

while True:
 show_menu()
 choice=input("Enter your choice(1-6)")

 if choice=="1":
  add_contact()
 elif choice=="2":
  view_contacts()
 elif choice=="3":
  search_contact()
 elif choice=="4":
  edit_contact()
 elif choice=="5":
  delete_contact()
 elif choice=="6":
  print("Thank you for using the Contact book, Goodbye!")
  break
 else:
  print("Invalid choice. Please select a valid option (1-6)")
