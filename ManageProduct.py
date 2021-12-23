def getID(list,pd_id):
    if pd_id in list:
        return list[pd_id]

def update(list,pd_id,new_name):
    if getID(list, pd_id) is None:
        list.update({pd_id : new_name})
    else:
        list[pd_id]=new_name


while True:
    print("Do you want to...")
    option=int(input("Press: 1.Add    2.Update  3.Remove  4.Exit"))

    if option==1:
        pd_id=int(input("Product ID: "))
        if getID(list,pd_id) is None:
            new_name=input("Name your product")
            update(list,pd_id,new_name)
        else:
            print("The ID is available")

    elif option==2:
        pd_id = int(input("Product ID: "))
        if getID(list, pd_id) is None:
            print("The ID is not available")
        else:
            new_name = input("Update your product's name")
            update(list, pd_id, new_name)

    elif option==3:
        pd_id = int(input("Product ID: "))
        if getID(list, pd_id) is None:
            print("The ID is not available")
        else:
            list.pop(pd_id)
            print("Remove successfully")

    elif option==4:
        break;

    else:
        print("Request is unavailable")

print(list)

