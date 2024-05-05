from domain.enums.Type import Type

class User :
 def __init__(self,id = None ,name = None, phone = None, email = None,type = Type):
  self.id = id
  self.name = name
  self.email = email
  self.phone = phone
  self.type = type