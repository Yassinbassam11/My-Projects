class person:
    def __init__(self,name=None,number=None,email=None,address=None):
        self.name=name
        self.number=number
        self.email=email
        self.address=address

    def edit(self,name=None,number=None,email=None,address=None):
        if name!=None:
            self.name=name
        if number!=None:
            self.number=number
        if email!=None:
            self.email=email
        if address!=None:
            self.address=address

    def show_person(self):
        return(f"Name: {self.name}  Number: {self.number}  Email: {self.email}  Address: {self.address}")

class contact():
    def __init__(self):
        self.list=[]

    def add_contact(self,name,number,email,address):
        self.list.append(person(name,number,email,address))
        print("\nContact added Successfully\n")

    def update_contact(self,no_on_list,name=None,number=None,email=None,address=None):
        if len(self.list)>=no_on_list:
            self.list[no_on_list-1].edit(name,number,email,address)
            print("\nContact updated Successfully\n")
        else:
            print("Out of Contact range to update")

    def delete_contact(self,no_on_list):
        if len(self.list)>=no_on_list:
            del self.list[no_on_list-1]
            print("\nContact deleted Successfully\n")
        else:
            print("Out of Contact range to Delete")   
    
    def show_contacts_by_name(self):
        if self.is_empty()==True:
            print("\nNo Contacts\n")
        else:
            x=1
            print("\nContact List by Name:")
            for i in self.list:
                print(f"{x}) {i.name}")
                x+=1
            print("")

    def show_contacts_by_number(self):
        if self.is_empty()==True:
            print("\nNo Contacts\n")
        else:
            x=1
            print("\nContact List by Number:")
            for i in self.list:
                print(f"{x}) {i.number}")
                x+=1
            print("")

    def show_contacts_by_all(self):
        if self.is_empty()==True:
            print("\nNo Contacts\n")
        else:
            x=1
            print("\nContact List:")
            for i in self.list:
                print(f"{x}) {i.show_person()}\n")
                # print(f"{x}) ",end="")
                # i.show_person
                x+=1
            print("")
    
    def is_empty(self):
        if len(self.list)==0:
            return True
        else:
            return False

contact_book=contact()
print("\nWelcome to Yassin Bassam Contact Book\n")
while True:
    i1=input("Menu:\n1) Show Contacts\n2) Add contact\n3) Edit Contact\n4) Delete Contact\n5)Exit\nEnter your choice:")
    while i1!="1" and i1!="2" and i1!="3" and i1!="4" and i1!="5":
        print("\nPlease Enter Valid Number!\n")
        i1=input("Menu:\n1) Show Contacts\n2)Add contact\n3) Edit Contact\n4) Delete Contact\n5)Exit\nEnter your choice:")
    if i1=="1":
        i2=input("\nShow Contacts Menu\n1) Show Contacts by Name\n2) Show Contacts by Number\n3) Show Contacts by all details\nEnter your choice:")
        while i2!="1" and i2!="2" and i2!="3":
            print("\nPlease Enter Valid Number!\n")
            i2=input("\nShow Contacts Menu\n1) Show Contacts by Name\n2) Show Contacts by Number\n3) Show Contacts by all details\nEnter your choice:")
        if i2=="1":
            contact_book.show_contacts_by_name()
        elif i2=="2":
            contact_book.show_contacts_by_number()
        elif i2=="3":
            contact_book.show_contacts_by_all()
        else:
            print("I will never show LoL")
    elif i1=="2":
        i2=input("\nEnter the name:")
        if i2=="":
            i2=None
        i3=input("Enter the number:")
        if i3=="":
            i3=None
        i4=input("Enter the Email:")
        if i4=="":
            i4=None
        i5=input("Enter the Address:")
        if i5=="":
            i5=None
        contact_book.add_contact(i2,i3,i4,i5)
    elif i1=="3":
        contact_book.show_contacts_by_all()
        i2=int(input("Enter The number of contact that you want to update:"))
        while i2>len(contact_book.list):
            print("\nOut of range try agin!\n")
            i2=int(input("Enter The number of contact that you want to update:"))
        i3=input("Enter the new name:")
        if i3=="":
            i3=None
        i4=input("Enter the new number:")
        if i4=="":
            i4=None
        i5=input("Enter the new Email:")
        if i5=="":
            i5=None
        i6=input("Enter the new Address:")
        if i6=="":
            i6=None
        contact_book.update_contact(i2,i3,i4,i5,i6)
    elif i1=="4":
        contact_book.show_contacts_by_all()
        i2=int(input("Enter The number of contact that you want to delete:"))
        while i2>len(contact_book.list):
            print("\nOut of range try agin!\n")
            i2=int(input("Enter The number of contact that you want to delete:"))
        contact_book.delete_contact(i2)
    elif i1=="5":
        print("Bye!")
        break
    else:
        print("I will never show LoL")