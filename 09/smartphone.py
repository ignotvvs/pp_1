from contact_list import Contact_List
from contact import Contacts

person = Contacts("George Small", "smallg@google.pl", "222999100")
person2 = Contacts("John Brown", "brown@onet.pl", "555234000")
person3 = Contacts("Anna May", "am@o2.pl", "232000199")
person4 = Contacts("Paola Big", "bigpaola@poczta.pl", "100200300")
person5 = Contacts("Izuku Midoriya", "deku@mail.com", "111222333")
clist = Contact_List()
clist.add_contact(person)
clist.add_contact(person2)
clist.add_contact(person3)
clist.add_contact(person4)
clist.add_contact(person5)
clist.display()
