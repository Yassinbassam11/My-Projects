class to_do_list:
    def __init__(self): #constructor
        self.list=[]

    def add_item(self,item):  #to add item to the list
        self.list.append([item,False])

    def edit_item(self,num,new_item):  #to edit item in the list
        if len(self.list)>= num:
            self.list[num-1][0]=new_item
        else:
            print("\nThere is No Item to Edit\n")

    def delete_item(self,num):  #to delete item from the list
        if len(self.list)>= num:
            del self.list[num-1]
        else:
            print("\nThere is No Item to Delete\n")

    def complete_item(self,num):  #to mark the item to be completed
        if len(self.list)>= num:
            self.list[num-1][1]=True
        else:
            print("\nThere is No Item to Complete\n")

    def uncomplete_item(self,num):  #to mark the item to be uncompleted
        if len(self.list)>= num:
            self.list[num-1][1]=False
        else:
            print("\nThere is No Item to Uncomplete\n")

    def is_empty(self):  #to check if the list is empty
        if len(self.list) == 0:
            return True
        else:
            return False
    
    def show_list(self):  #to display all the list
        x=1
        if self.is_empty()==True:
            print("No Item Found")
        for i in self.list:
            print(f"{x}. {i[0]}",end="")
            if i[1]==True:
                print("  (Completed)")
            else:
                print("")
            x=x+1
        print("")

list1=to_do_list()
print("\nWelcom to Yassin Bassam To-Do List\n")
try:
    while(True):
        print("1 - Add Item\n2 - Show Items\n3 - Edit Item\n4 - Delete Item\n5 - Complete Item\n6 - Exit\n")
        i1=int(input("Enter number from 1 to 6:"))
        if i1==1:
            i2=input("Enter The Item:")
            list1.add_item(i2)
        elif i1==2:
            list1.show_list()
        elif i1==3:
            list1.show_list()
            i3=int(input("Enter number of Item:"))
            i4=input("Enter the New Item:")
            list1.edit_item(i3,i4)
        elif i1==4:
            list1.show_list()
            i5=int(input("Enter number of Item:"))
            list1.delete_item(i5)
        elif i1==5:
            list1.show_list()
            i6=int(input("Enter number of Item:"))
            list1.complete_item(i6)
        elif i1==6:
            break
        else:
            print("Please Enter number from 1 to 6:")

except ValueError:
    print("Please Enter Valid Number")
except Exception as e:
    print("Unexpected Error:",e)
