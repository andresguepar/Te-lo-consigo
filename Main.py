import AdminService
from User import User


def main():
    adminService = AdminService()
    
    while True:
        print("\nOptions:")
        print("1. Add ")
        print("2. Update ")
        print("3. Delete ")
        print("4. List ")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            type = input("Type of client (1. Ocassional, 2. Wholesaler): ")
            
            """if type.upper() == 'O':
                user = CompradorOcasional(nombre, identificacion, direccion, telefono, correo, intereses)
            elif tipo_usuario.upper() == 'M':
                user = CompradorMayorista(nombre, identificacion, direccion, telefono, correo, intereses)
            else:
                print("Tipo de usuario no válido.")
              continue"""
            
            adminService.Add(User)
            print("USer added.")

        elif choice == '2':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            type = input("Type of client (1. Ocassional, 2. Wholesaler): ")

            adminService.update(id, User)
            print("User updated.")

            """ if tipo_usuario.upper() == 'O':
                usuario = CompradorOcasional(nombre, identificacion, direccion, telefono, correo, intereses)
            elif tipo_usuario.upper() == 'M':
                usuario = CompradorMayorista(nombre, identificacion, direccion, telefono, correo, intereses)
            else:
                print("Tipo de usuario no válido.")
                continue """
       
        elif choice == '3':
            id = int(input("Ingrese el índice del usuario a eliminar: "))
            adminService.delete(id) # type: ignore
            print("User deleted.")
        
        elif choice == '4':
            print("Users:")
            adminService.list()
        
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Option No Valid.")

if __name__ == "__main__":
    main()
