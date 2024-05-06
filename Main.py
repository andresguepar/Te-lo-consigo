from domain.entities.User import User  # Importa la clase User desde el módulo domain.entities
from services.AdminService import AdminService  # Importa la clase AdminService desde el módulo services.AdminService
from services.message.MessageService import MessageService  # Importa la clase MessageService desde el módulo services.message.MessageService
from services.message.SendMessage import SendMessage  # Importa la clase SendMessage desde el módulo services.message.SendMessage
from services.message.ShowInScreen import ShowInScreen  # Importa la clase ShowInScreen desde el módulo services.message.ShowInScreen

# Función principal del programa
def main():
    # Creación de una instancia de AdminService
    adminService = AdminService()
    # Creación de una instancia de SendMessage
    sendEmail = SendMessage()
    # Creación de una instancia de ShowInScreen
    showScreen = ShowInScreen()

    # Creación de una instancia de MessageService para notificaciones por email
    notificationEmail = MessageService(sendEmail)
    # Creación de una instancia de MessageService para notificaciones en pantalla
    notificationScreen = MessageService(showScreen)
    
    # Bucle principal del programa
    while True:
        # Menú principal
        print("\nOptions:")
        print("1. Add ")
        print("2. Edit ")
        print("3. Delete ")
        print("4. List ")
        print("5. Exit")

        # Elección del usuario
        choice = input("Select an option: ")

        # Manejo de las opciones del menú
        if choice == '1':  # Add a user
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            type = input("Type of client (1. Ocassional - 2. Wholesaler): ")
            
            if type == '2':  # Wholesaler user
               message = "Welcome there are your terms and conditions "
               notificationEmail.send_notification(name, message)  # Envío de notificación por email
            elif type == '1':  # Occasional user
                message = "Register Succesfully"
                notificationScreen.send_notification(name, message)  # Envío de notificación en pantalla
            else:
                print("User Not Valid.")
                continue

            # Creación de una instancia de User
            user = User(name, phone, email, type)
            adminService.Add(user)  # Llamada al método Add de AdminService para agregar el usuario
            print("User added.")
            
        elif choice == '2':  # Edit a user
            id1 = input("Id: ")
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            type = input("Type of client (1. Occasional, 2. Wholesaler): ")
            user2 = User(name, phone, email, type)  # Creación de una instancia de User
            adminService.Edit(id1, user2)  # Llamada al método Edit de AdminService para editar el usuario
            print("User updated.")

        elif choice == '3':  # Delete a user
            id2 = int(input("Enter the index of the user to delete: "))
            adminService.Delete(id2)  # Llamada al método Delete de AdminService para eliminar el usuario
            print("User deleted.")
        
        elif choice == '4':  # List users
            print("Users:")
            adminService.List()  # Llamada al método List de AdminService para listar los usuarios
        
        elif choice == '5':  # Exit the program
            print("Exiting...")
            break
        else:
            print("Option not valid.")

# Verificación de si el archivo es el programa principal y llamada a la función main
if __name__ == "__main__":
    main()
