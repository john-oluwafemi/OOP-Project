
class RetailItem:
    def __init__(self, item_description, inventory, price):
        self.__item_description = item_description
        self.__inventory = inventory   
        self.__price = price    

    def get_item_description(self):
        return self.__item_description
    
    def get_inventory(self):
        return self.__inventory

    def get_price(self):
        return self.__price
