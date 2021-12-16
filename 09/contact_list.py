class Contact_List():

    def __init__(self):
        self.contacts = []

    def add_contact(self,other):
        self.contacts.append({
            "name": other.name,
            "email": other.email,
            "telephone": other.telephone
        })

    def display(self):
        for i in self.contacts:
            print(f"{i['name']}     {i['email']}    {i['telephone']}")


