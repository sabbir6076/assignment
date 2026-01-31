import json
import os
from students import Students
import show_menu_bar

print("Welcome to the Student Record Management System!")
filename='record.json'
if not os.path.exists(filename) or os.path.getsize(filename) == 0:
    with open(filename, "w") as f:
        json.dump([], f, indent=4)

with open(filename, "r") as f:
    list1 = json.load(f)

with open(filename,'r') as a:
    h=json.load(a)
    for i in h:
        list1.append(i)
    print("Loading student records from record.json... Done!")
while True:
    show_menu_bar.to_show_menu()
    c=input(" Enter choice: ")
    if c=='1':
        def student_details():
            if len(list1)==0:
                print(" There is no student record")
            else:
                print("All students records")
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

            s=Students(n,r,e,d)
        
            list1.append(s.to_dict())
            with open("record.json", "w") as j:
                json.dump( list1,j, indent=4)
            print("records added successfully")

    elif c=='3':
        r=(input((" Enter Roll no : ")))
        def to_search(r):
            for q,dict in enumerate(list1):
                if dict.get("roll")==r:
                    print(list1[q])
            else:
                print("The record does")
        to_search(r)

    elif c=='4':
        r=int(input((" Enter Roll no : ")))
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
    else:
        print("Invalid choice")
        continue

        with open(filename, "w") as j:
            json.dump( list1,j, indent=4)
    if c=='5':
        print("Thank you for using the Student Record Management System. Goodbye!")
        break


