from enums.Category import Category


class Product:
  def __init__(self,id = None ,name = None, category = Category):
    self.id = id
    self.name = name
    self.category = category
