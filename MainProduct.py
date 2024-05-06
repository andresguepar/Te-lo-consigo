# Importación de las clases necesarias desde sus respectivos módulos
from domain.entities.DetailProduct import DetailProduct
from domain.entities.Product import Product
from services.Data.APIDataService import APIDataService
from services.Data.DataService import DataService
from services.Data.IndividualDataService import IndividualDataService
from services.Data.MassiveDataService import MassiveDataService
from services.ProductService import ProductService

# Función principal del programa
def main():
    # Creación de una instancia de DetailProduct
    product = DetailProduct()
    # Creación de una instancia de ProductService
    productService = ProductService()

    # Creación de instancias de los servicios de datos
    apiData = APIDataService()
    indData = IndividualDataService()
    massData = MassiveDataService()

    # Creación de instancias de DataService para cargar datos
    loadApi = DataService(apiData)
    loadInd = DataService(indData)
    loadMass = DataService(massData)

    # Bucle principal del programa
    while True:
        # Menú principal
        print("\nOptions:")
        print("1. CRUD ")
        print("2. Load Data ")
        print("3. Exit")

        # Elección del usuario
        choice = input("Select an option: ")
        
        # Manejo de la elección del usuario
        if choice == '1':  # CRUD Operations
            while True:
                # Menú para las operaciones CRUD
                print("\nOptions:")
                print("1. Add ")
                print("2. Edit ")
                print("3. Delete ")
                print("4. List ")
                print("5. Exit")

                # Elección del usuario para las operaciones CRUD
                choice = input("Select an option: ")

                # Manejo de las operaciones CRUD
                if choice == '1':  # Add a product
                    name = input("Name: ")
                    description = input("Description: ")
                    price = input("Price: ")
                    category = int(input("Type of client (1. Smartphones - 2. Computers - 3. Electronic Accesory - 4. Decorative Accesory): "))
                    stock = input("Stock: ")
                    product = Product(1, name, category)  # Creación de una instancia de Product
                    product2 = DetailProduct(1, product, name, description, price, category, stock)  # Creación de una instancia de DetailProduct
                    productService.Add(product2)  # Llamada al método Add de ProductService
                    print("Product added.")

                elif choice == '2':  # Edit a product
                    id1 = input("Id: ")
                    description = input("Description: ")
                    price = input("Price: ")
                    category = input("Type of client (1. Smartphones - 2. Computers - 3. Electronic Accesory - 4. Decorative Accesory): ")
                    stock = input("Stock: ")
                    product2 = DetailProduct(id1, name, description, price, category, stock)  # Creación de una instancia de DetailProduct
                    productService.Edit(id1, product2)  # Llamada al método Edit de ProductService
                    print("Product updated.")

                elif choice == '3':  # Delete a product
                    id2 = int(input("Enter the index of the product to delete: "))
                    productService.Delete(id2)  # Llamada al método Delete de ProductService
                    print("Product deleted.")
        
                elif choice == '4':  # List products
                    print("Products:")
                    productService.List()  # Llamada al método List de ProductService
                
                elif choice == '5':  # Exit the CRUD menu
                    print("Exiting...")
                    break
                else:
                    print("Option not valid.")

        elif choice == '2':  # Load Data
            while True:
                # Menú para cargar datos
                print("\nLoads:")
                print("1. API ")
                print("2. Individual ")
                print("3. Massive ")
                print("4. Exit ")

                # Elección del usuario para cargar datos
                option = input("Select an option: ")
                name = input("Name: ")
                description = input("Description: ")
                price = input("Price: ")
                category = int(input("Type of client (1. Smartphones - 2. Computers - 3. Electronic Accesory - 4. Decorative Accesory): "))
                stock = input("Stock: ")
                product = Product(1, name, category)  # Creación de una instancia de Product
                product2 = DetailProduct(1, product, name, description, price, category, stock)  # Creación de una instancia de DetailProduct

                # Manejo de las opciones para cargar datos
                if option == '1':  # Load data from API
                    loadApi.load_data(product2)  # Llamada al método load_data de DataService con APIDataService
                elif option == '2':  # Load individual data
                    loadInd.load_data(product2)  # Llamada al método load_data de DataService con IndividualDataService
                elif option == '3':  # Load massive data
                    loadMass.load_data(product2)  # Llamada al método load_data de DataService con MassiveDataService
                elif option == '4':  # Exit the load data menu
                    print("Exiting...")
                    break
                else:
                    print("Option not valid.")

        elif choice == '3':  # Exit the program
            print("Exiting...")
            break
        else:
            print("Option not valid.")

# Verificación de si el archivo es el programa principal y llamada a la función main
if __name__ == "__main__":
    main()
