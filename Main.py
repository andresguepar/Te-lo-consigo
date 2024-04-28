from typing import Self
from AdminService import AdminService
from MessageService import MessageService
from SendMessage import SendMessage
from ShowInScreen import ShowInScreen
from User import User


def main():
    adminService = AdminService()
    sendEmail = SendMessage()
    showScreen = ShowInScreen()

    notificationEmail = MessageService(sendEmail)
    notificationScreen = MessageService(showScreen)
    
    while True:
        print("\nOptions:")
        print("1. Add ")
        print("2. Edit ")
        print("3. Delete ")
        print("4. List ")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            type = input("Type of client (1. Ocassional - 2. Wholesaler): ")
            
            if type == '2':
               message = "Welcome there are your terms and conditions "
               notificationEmail.send_notification(name,message)
            elif type == '1':
                message = "Register Succesfully"
                notificationScreen.send_notification(name,message)
            else:
                print("User Not Valid.")
                continue

            user = User(name,phone,email,type)

            adminService.Add(user)
            print("User added.")
            

        elif choice == '2':
            id1 = input("Id: ")
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            type = input("Type of client (1. Ocassional, 2. Wholesaler): ")
            user2 = User(name,phone,email,type)

            adminService.Edit(id1, user2)
            print("User updated.")

        elif choice == '3':
            id2 = int(input("Ingrese el índice del usuario a eliminar: "))
            adminService.Delete(id2) 
            print("User deleted.")
        
        elif choice == '4':
            print("Users:")
            adminService.List()
        
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Option No Valid.")

if __name__ == "__main__":
    main()
