import json
import os
#create
def save_user_data():

    user_list=[]

    while True:
        name = input("Enter name (or 'quit' to exit the program: ")
        if name =='quite':
            break
        email = input("Enter email")
        contact = input("Enter contact")

        #creating a dictionary
        user_data = {
            "name": name,
            "email": email,
            "contact": contact
        }
        # add user data to the list
        user_list.append(user_data)

    if os.path.exists("user_data.json"):
        with open("user_data.json", 'r') as file:
            existing_data = json.load(file)
        user_list.extend(existing_data)

    with open("user_data.json", 'w') as file:
        json.dump(user_list, file)
        print("User data saved successfully")

#read
def read_user_data():
    if not os.path.exists("user_data.json"):
        print("No usr data found")
        return

    with open("user_data.json", "r") as file:
        user_lists = json.load(file)
        for user_data in user_lists:
            print("Name: ", user_data["name"])
            print("Email: ", user_data["email"])
            print("Contact: ", user_data["contact"])
            print("\n")

#update
def edit_user_data(name):
    if not os.path.exists("user_data.json"):
        print("No user data found")
        return
    with open('user_data.json', 'r') as file:
        user_list = json.load(file)
    user_flag = False
    for user_data in user_list:
        if user_data["name"].lower() == name.lower():
            email = input("Enter updated email: ")
            contact = input("Enter updated contact")

            user_data["email"]= email
            user_data["contact"]= contact
            user_found = True
            break
    if not user_found:
        print("User not found")

    with open("user_data.json",'w') as file:
        json.dump(user_list,file)
    print("User data updated successfully")

#delete
def delete_user_data(name):
    if not os.path.exists("user_data.json"):
        print("No user data found")
        return

    with open('user_data.json', 'r') as file:
        user_list = json.load(file)

    user_flag = False
    for user_data in user_list:
        if user_data["name"].lower() == name.lower():
            user_list.remove(user_data)
            user_found = True
            break
    if not user_found:
        print("User not found")

    with open("user_data.json",'w') as file:
        json.dump(user_list,file)
    print("User data deleted successfully")



#edit_name = input("Enter name wich you want to edit data for: ")
edit_name = input("Enter name wich you want to delete from data: ")

#edit_user_data(edit_name)
delete_user_data(edit_name)

read_user_data()

#save_user_data()
#read_user_data()


