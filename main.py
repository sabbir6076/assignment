import json
import os
from students import Students
import show_menu_bar

print("Welcome to the Student Record Management System!")
filename='record.json'

# First checking whether the file exist in the folder or it is empty.
# if it does not exist, then creating one and storing empty list
if not os.path.exists(filename) or os.path.getsize(filename) == 0:
    with open(filename, "w") as f:
        json.dump([], f, indent=4)

with open(filename, "r") as f:
    list1 = json.load(f)
    for i in f:
        list1.append(i)
    print("Loading student records from record.json... Done!")

while True:
    show_menu_bar.to_show_menu()    # showing menu bar
    c=input(" Enter choice: ")

    if c=='1':
        def student_details():
            if len(list1)==0:
                print(" There is no student record")
            else:
                print("------All students--------")
                for i in list1:
                    for k,v in i.items():
                        print(f"{k} : {v}")
                    print("")
                print("----THE END-------")
        student_details()

    elif c=='2':
        try:
            r=int(input("enter roll: "))
        except ValueError:
            print("Roll must be interger")
            continue
        exists= False
        for i in list1:
            if i["roll"] ==r:
                print("Error: Roll number already exists for another student")
                exists=True
                break
        if exists==False:
            n=input("enter name: ")
            e=input("enter email: ")
            d=input("enter dept: ")
            if n.isalpha() and d.isalpha():
                s=Students(n,r,e,d) 
                list1.append(s.to_dict())
                with open("record.json", "w") as j:
                    json.dump( list1,j, indent=4)
                print("records added successfully")
            else:
                print("name and dept must be alphabets")

    elif c=='3':

        r=input((" Enter name/roll/email : "))

        def to_search(r):
            for item in list1:
                for value in item.values():
                    if r in str(value).lower():
                        for k, v in item.items():
                            print(f"{k} : {v}")
                        print()
                        break 
        to_search(r)

    elif c=='4':
        try:
            r=int(input((" Enter Roll no : ")))
        except ValueError:
            print("Roll must be interger")
        
        g=input(f"Are you sure to delete this roll no : {r}. type (y/n) : ")
        
        def to_delete(r):
            for q,dict in enumerate(list1):
                if dict.get("roll")==r:
                    list1.pop(q)
                    print(" data removed successfully")
        if g =='y':
            to_delete(r)
        elif g=='n':
            continue
        else:
            print("Invalid choice")
            continue
        # now writing the modified list1 to record.json
        with open(filename, "w") as j:    
            json.dump( list1,j, indent=4)
            
    elif c=='5':
        print("Thank you for using the Student Record Management System. Goodbye!")
        break
    else:
        print("Invalid choice")
        continue


