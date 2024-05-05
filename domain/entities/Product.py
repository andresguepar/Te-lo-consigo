from enums.Category import Category


class Product:
  def __init__(self,id = None ,name = None, category = Category, stock = None,):
    self.id = id
    self.name = name
    self.category = category
