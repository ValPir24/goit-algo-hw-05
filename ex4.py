def input_error(func): # Function - decorator for errors handling 
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "The mentioned name is not in your list. PLease check."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "There is no such information."
        except Exception as e:
            return f"Error: {e}"
    return inner

@input_error
def parse_input(user_input): # Parse input function 
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts): # Add user and phone to dict function
    if args[0] not in contacts.keys():
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    else:
        print("The contact is already in the list.")

@input_error
def change_contact(args, contacts): # Change user phone function
    if args[0] in contacts.keys():
        add_contact(args, contacts)
        print(f"The phone for {args[0]} is succesfully changed to {contacts[args[0]]}")
    else:
        raise(KeyError)

@input_error
def show_phone(args, contacts): # Show phone of certain name function
    name = args[0]
    return f"{name.upper()} has phone: {contacts[name]}"

@input_error
def show_all(contacts): # Show all names and phones function
    return f"All the contacts: {contacts}"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
