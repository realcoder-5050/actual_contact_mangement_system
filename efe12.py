def add_conatct():
        
    name  = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    person = {"name": name, "age": age, "email": email}
    return person
def delete_contact(people):
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], " | ", person["age"], " | ", person["email"])
    while True:
        number= input("Enter number to delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid selction, or out of range!")
            else:
                break
        except:
            print("Invalid, you have to try again!")
    people.pop(number - 1)
    print("Contact successfully deleted!")
    print(i + 1, "-", person["name"], " | ", person["age"], " | ", person["email"])

print("Welcome to my contact mangement system!")
print("-----------------------------")
people = []
while True:
    print(f"Contact list is {len(people)}!")
    command = input("You can 'add', 'delete', or press 'q' to exit: ").lower()

    if command == "add":
        person = add_conatct()
        people.append(person)
        print("Person added!")
    elif command == "delete":
        delete_contact(people)
    elif command == "q":
        print("This does exit the process!")
        break
    else: 
        print("Invalid selection enetred!")