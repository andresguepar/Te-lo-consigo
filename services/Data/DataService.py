from abc import ABC

from interfaces.IDataManager import IDataManager
from domain.entities.DetailProduct import DetailProduct

class DataService:
    def __init__(self, product: IDataManager):
        self.product = product

    def load_data(self, detailProduct):
        self.product.load(detailProduct)