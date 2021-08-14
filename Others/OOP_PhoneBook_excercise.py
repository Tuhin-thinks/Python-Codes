from typing import List, Union, Dict, Any
from dataclasses import dataclass, asdict


@dataclass
class Contact:
    name: str
    email: str
    phone: str
    gender: str
    age: int


class Agenda:
    def __init__(self, contacts: Union[List, None] = None):
        self.contacts = []
        if contacts:
            for contact in contacts:
                self.register(contact)

    def register(self, contact):
        self.contacts.append(contact)

    def query(self, search_param_dict: Dict[str, Any], get_param=None):
        if type(search_param_dict) == dict:
            results = []

            for contact in self.contacts:

                flag = True
                for k, v in search_param_dict.items():
                    if hasattr(contact, k):
                        attr_ = getattr(contact, k)
                        if callable(v):
                            if v(attr_) is False:
                                flag = False
                        elif attr_ != v:
                            flag = False
                if flag:
                    if get_param is None:
                        results.append(contact)
                    elif get_param == 'all':
                        results.append(asdict(contact))
                    elif type(get_param) == list:
                        res = []
                        for key in get_param:
                            if hasattr(contact, key):
                                res.append(getattr(contact, key))
                        results.append(res)
                    elif type(get_param) == str:
                        results.append(getattr(contact, get_param))
            return results
        else:
            print("Invalid query")
            return None

    def consult(self, contact_param: Union[int, str, List]):
        if type(contact_param) != list:
            contact_param = [contact_param]

        results = []
        for contact in self.contacts:
            name = contact.name
            email = contact.email
            phone = contact.phone
            gender = contact.gender
            age = contact.age

            if (set(contact_param) - {name, email, phone, gender, age}) == set():
                results.append(contact)
        return results

    def edit_contact(self, contact: 'Contact', new_param_values: Dict):
        if not isinstance(contact, Contact):
            print("Not a valid contact")
            return -1
        else:
            if contact in self.contacts:
                pass
            else:
                print("Required contact is not added in the phone-book")
                return -1

            for k, v in new_param_values.items():
                if hasattr(contact, k):
                    setattr(contact, k, type(getattr(contact, k))(v))
        return 1

    def delete(self, contact: 'Contact'):
        if not isinstance(contact, Contact):
            print("Not a valid contact")
            return -1
        else:
            if contact in self.contacts:
                self.contacts.remove(contact)
                return 1  # success code
            else:
                print("Required contact is not added in the phone-book")
                return -1

    def count_contacts(self) -> int:
        return len(self.contacts)

    def average_contacts_age(self) -> float:
        if len(self.contacts) > 0:  # check to avoid ZeroDivisionError
            return sum({i.age for i in self.contacts}) / len(self.contacts)
        else:
            return -1


def show_menu():
    display_string = '''\n
            :::MENU:::
    1.Register a new contact;
    2.Consult a specific contact;
    3.Change the data of any contact;
    4.Delete a particular contact;
    5.Find out how many people were registered;
    6.Find out the average age of people;
    7.Print a list with the women who are registered on the agenda;
    8.Print a list with the men who are registered in the agenda;
    9.Print a list of people over a certain age;
    10.Print a list of registered emails;
    0. QUIT
Enter your choice:'''
    print(display_string, end="")


def register_contact(agenda: 'Agenda'):
    print("Enter contact details:")
    name = input("    name:")
    email = input("    email:")
    mobile = input("    mobile:")
    gender = input("    gender(M/W):").upper()
    age = int(input("    age:"))

    c_temp = Contact(name, email, mobile, gender, age)
    agenda.register(c_temp)


def accept_choice():
    show_menu()
    try:
        choice = int(input())
        return choice
    except ValueError:
        print("Invalid choice, try again")
        return accept_choice()


def consult_contact(agenda: 'Agenda'):
    contact_search_param = input("Enter contact name:")
    res = agenda.consult(contact_search_param)
    for item in res:
        print(asdict(item))


def edit_contact(agenda: 'Agenda'):
    name = input("Enter contact name:")
    contact_list = agenda.consult(name)
    contact = contact_list[0]

    field_name = input("Enter field to edit:")
    data = input("Enter data to replace with:")

    res = agenda.edit_contact(contact, {field_name: data})
    if res == 1:
        print("Edit success!\n")
    else:
        print("Edit failed.\n")


def delete_contact(agenda: 'Agenda'):
    name = input("Enter contact name:")
    contact_list = agenda.consult(name)
    if contact_list:
        contact = contact_list[0]
    else:
        print("No such contact found.")
        return -1

    res = agenda.delete(contact)
    if res == 1:
        print("Deleted successfully!\n")
    elif res == -1:
        print("Deletion failed.\n")


def process():
    agenda = Agenda([p1, p2, p3, p4, p5])
    while True:
        choice = accept_choice()
        print("".center(50, '='), '\n')

        if choice == 1:
            register_contact(agenda)
        elif choice == 2:
            consult_contact(agenda)
        elif choice == 3:
            edit_contact(agenda)
        elif choice == 4:
            delete_contact(agenda)
        elif choice == 5:
            n = agenda.count_contacts()
            print(f"{n} people registered.\n")
        elif choice == 6:
            avg_age = agenda.average_contacts_age()
            print(f"Average age of people: {avg_age}\n")
        elif choice == 7:
            res = agenda.query({'gender': 'W'}, get_param='name')
            print("Women who registered:")
            print("\n\t".join(res))
            print()
        elif choice == 8:
            res = agenda.query({'gender': 'M'}, get_param='name')
            print("Men who registered:")
            print('    '+"\n    ".join(res))
            print()
        elif choice == 9:
            age_threshold = int(input("Age lower threshold:"))
            res = agenda.query(search_param_dict={'age': lambda x: x > age_threshold},
                               get_param='all')
            for item in res:
                print(item)
        elif choice == 10:
            res = agenda.query(search_param_dict={}, get_param='email')

            print("Registered emails:")
            for item in res:
                print(item)
        elif choice == 0:
            print("Exiting program.")
            break
        else:
            print("Wrong choice, try again")

    print("Thank you!".center(20, '-'))


if __name__ == '__main__':
    p1 = Contact("John", "john@gmail.com", "+60123334138", "M", 17)
    p2 = Contact("Angel", "angel@yahoo.com", "+5433 214 229", "F", 23)
    p3 = Contact("Danny", "danny@hotmail.com", "+065229 776", "M", 52)
    p4 = Contact("Lisa", "lisa@jobstreet.com", "+02 7288 9944", "F", 32)
    p5 = Contact("Jennifer", "jennifer@gmail.com", "+606 528 2233", "F", 12)

    # agenda = Agenda([p1, p2, p3, p4, p5])
    # min_age = int(input("age min:"))
    # res = agenda.query(search_param_dict={'age': lambda x: x >= min_age},
    #                    get_param='all')
    #
    # for item in res:
    #     print(item)
    process()
