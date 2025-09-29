import json
# --- Load Contacts ---
try:
    with open('contacts.json', 'r') as file:
        contacts = json.load(file)
except FileNotFoundError:
    contacts = []
print("Welcome to Your Contact Book!")
print("------------------------")
# --- Main Program Loop ---
while True:
    print("\n--- Main Menu ---")
    a = input("""What would you like to do?
  > Type 'add' to add a new contact.
  > Type 'view' to see all your contacts.
  > Type 'search' to find a contact.
  > Type 'exit' to close the program.
Enter your command: """).lower()
    # --- Add a Contact ---
    if a == "add":
        while True:
            b = {} 
            b["Name"] = input("Enter the name: ").lower().title()
            b["Phone number"] = input("Enter the Phone number: ")
            b["E-Mail ID"] = input("Enter the E-Mail ID: ")
            contacts.append(b)
            print(f"\nSuccess! '{b['Name']}' has been added.")
            p = input("\nDo you want to add another contact? (yes/no): ").lower()
            if p == "no":
                break
    # --- Exit and Save ---
    elif a == "exit":
        with open('contacts.json', 'w') as file:
            json.dump(contacts, file)
        print("Contacts saved successfully! Goodbye!")
        break
    # --- View All Contacts ---
    elif a == "view":
        print("\n--- Your Contacts ---")
        if not contacts: # A check to see if the list is empty
            print("Your contact book is empty.")
        else:
            for contact in contacts:
                print(f"Name: {contact['Name']}")
                print(f"Phone number: {contact['Phone number']}")
                print(f"E-Mail ID: {contact['E-Mail ID']}")
                print("=================================")
    # --- Search for a Contact ---
    elif a == "search":
        inp = input("Enter the name you want to search for: ").lower().title()
        found_contact = False # This is our "flag"
        # We use a 'for' loop to check every contact
        for contact in contacts:
            if contact["Name"] == inp:
                print("\n--- Contact Found ---")
                print(f"Name: {contact['Name']}")
                print(f"Phone number: {contact['Phone number']}")
                print(f"E-Mail ID: {contact['E-Mail ID']}")
                print("=================================")
                found_contact = True # We flip the flag to True because we found it
                break # We can stop searching now
        # After the loop is finished, we check the flag.
        if not found_contact:
            print(f"\nSorry, no contact named '{inp}' was found.")
    # --- Handle Invalid Input ---
    else:
        print("\nInvalid command. Please try again.")