class Doctor(object):

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.available = False

    def availabe_button(self, button):
        try:
            button = button.lower()
            if button not in ["yes", "no"]:
                print("Error: Try Again!")
            else:
                if button == "yes":
                    self.available = True
                else:
                    self.available = False

        except:
            print("Please Input a String")






class Database(object):

    def __init__(self):
        self.phonebook = []

    def add_object_number(self, object1):
        if object1.available == True:
            self.phonebook.append(object1.phone_number)
        else:
            pass

    def remove_if_inactive(self):
        for a in list(range(len(self.phonebook))):
            if self.phonebook[a].available:
                continue
            else:
                self.phonebook.pop(a)

data = Database()

doc1 = Doctor("gio", "558966580")
doc2 = Doctor("gia", "599261699")

doc1.available_button("yes")
doc2.available_button("yes")

Database.add_object_number(doc1)
Database.add_object_number(doc2)

print(Database.phonebook)
