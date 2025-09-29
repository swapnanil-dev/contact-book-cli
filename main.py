import json
try:
    with open('contacts.json','r') as file:
        contacts=json.load(file)
except FileNotFoundError:
    contacts=[]
print("Welcome to Contact Book!")
print("------------------------")
while True:
    print("Main Menu : ")
    a = (input("""What would you like to do?
    > Type 'add' to add a new contact.
    > Type 'view' to see all your contacts.
    > Type 'search' to find a contact.
    > Type 'exit' to close the program.
    """).lower()).title()
    if(a=="Add"):
        while True:
             b = {"Name":"", "Phone number":0, "E-Mail ID":""}
             b.update({"Name":((input("Enter the name : ")).lower()).title()})
             b.update({"Phone number":(input("Enter the Phone number : "))})
             b.update({"E-Mail ID":(input("Enter the E-Mail ID : "))})
             contacts.append(b)
             p=input("""Do you want to save another contact?
Type Yes to add another contact
Type No for going to main menu \n""").lower()
             if(p=="no"):
                 break
             if(p=="yes"):
                 continue
    elif(a=="Exit"):
        with open('contacts.json','w') as file:
            json.dump(contacts,file)
            print("Contacts are saved sucessfully! ")
        break
    elif(a=="View"):
        print("The list of contacts are : ")
        n = len(contacts)
        i=0
        while i<n:
            j=contacts[i]
            print(f"Name = {j["Name"]} ")
            print(f"Phone number = {j["Phone number"]} ")
            print(f"E-Mail ID = {j["E-Mail ID"]} ")
            print("=================================")
            i+=1
    elif(a=="Search"):
        inp = (input("Enter the name you want to search : ").lower()).title()
        n=len(contacts)
        i=0
        while i<n:
            j=contacts[i]
            if(j["Name"]==inp):
                print(f"Name = {j["Name"]} ")
                print(f"Phone number = {j["Phone number"]} ")
                print(f"E-Mail ID = {j["E-Mail ID"]} ")
                print("=================================")
                break
            else:
                print("No name found!")
                i+=1
    else:
        print("Wrong option typed")