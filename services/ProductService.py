
from domain.entities.DetailProduct import DetailProduct


class ProductSevice:
    def __init__(self):

        self.product = []

    def Add(self, product: DetailProduct):

        self.product.append(product)

    def Delete(self, id: int):
        del self.product[id]

    def Edit(self, id: str, new_product: DetailProduct):
        self.product[id] = new_product

    def List(self):
        for i, product in enumerate(self.product):
            print(f"Product {i}| Name: {product.name}, {product.phone} {product.email}|")