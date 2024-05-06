from domain.entities.DetailProduct import DetailProduct


from domain.entities.Product import Product
from services.Data.APIDataService import APIDataService
from services.Data.DataService import DataService
from services.Data.IndividualDataService import IndividualDataService
from services.Data.MassiveDataService import MassiveDataService
from services.ProductService import ProductService


def main():
    product = DetailProduct()
    productService = ProductService()

    apiData = APIDataService()
    indData = IndividualDataService()
    massData = MassiveDataService()

    loadApi = DataService(apiData)
    loadInd = DataService(indData)
    loadMass = DataService(massData)
    


    while True:
        print("\nOptions:")
        print("1. CRUD ")
        print("2. Load Data ")
        print("3. Exit")


        choice = input("Select an option: ")
        if choice == '1':
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
                    description = input("Description: ")
                    price = input("Price: ")
                    category = input("Type of client (1. Smartphones - 2. Computers - 3. Electronic Accesory - 4. Decorative Accesory): ")
                    stock = input("Stock: ")
                    product = Product(1,name,category)

                    product2 = DetailProduct(1,name,product,description,price,category,stock)
                    productService.Add(product2)
                    print("Product added.")


                elif choice == '2':
                    id1 = input("Id: ")
                    description = input("Description: ")
                    price = input("Price: ")
                    category = input("Type of client (1. Smartphones - 2. Computers - 3. Electronic Accesory - 4. Decorative Accesory): ")
                    stock = input("Stock: ")

                    product2 = DetailProduct(id1,name,description,price,category,stock)

                    productService.Edit(id1, product2)
                    print("Product updated.")

                elif choice == '3':
                    id2 = int(input("Ingrese el índice del producto a eliminar: "))
                    productService.Delete(id2) 
                    print("Product deleted.")
        
                elif choice == '4':
                    print("Products:")
                    productService.List()
                
                elif choice == '5':
                    print("Exiting...")
                    break
                else:
                    print("Option No Valid.")

        elif choice == '2':
          while True:
                print("\Loads:")
                print("1. API ")
                print("2. Individual ")
                print("3. Massive ")
                print("4. Exit ")

                category = input("Select an option: ")

                if category == 'SP':
                    detailProduct = "Product uploaded"
                    loadApi.load_data(detailProduct)
                elif category == '':
                    detailProduct = "Product uploaded"
                    loadInd.load_data(detailProduct)
                elif category == '3':
                    detailProduct = "Product uploaded"
                    loadMass.load_data(detailProduct)

        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Option No Valid.")
if __name__ == "__main__":
    main()