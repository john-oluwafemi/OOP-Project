
import RetailItemClass as rick


# item_description1 = input('\n\nWhat is the first item description? ')
# inventory1 = int(input('How many units are in inventory? '))
# price1 = float(input('How much is the unit price? '))

# item_description2 = input('\n\nWhat is the second item description? ')
# inventory2 = int(input('How many units are in inventory? '))
# price2 = float(input('How much is the unit price? '))

# item_description3 = input('\n\nWhat is the third item description? ')
# inventory3 = int(input('How many units are in inventory? '))
# price3 = float(input('How much is the unit price? '))

# item1 = rick.RetailItem(item_description1, inventory1, price1)
# item2 = rick.RetailItem(item_description2, inventory2, price2)
# item3 = rick.RetailItem(item_description3, inventory3, price3)


item1 = rick.RetailItem('Jacket', 12, 59.95)
item2 = rick.RetailItem('Designer Jeans', 40, 34.95)
item3 = rick.RetailItem('Shirt', 20, 24.95)

print(f"{' ' * 7} {'DESCRIPTION':15} {'UNITS IN INVENTORY':20} {'PRICE'}")
print(f"ITEM 1: {item1.get_item_description():15} {item1.get_inventory():<20} {item1.get_price()}")
print(f"ITEM 2: {item2.get_item_description():15} {item2.get_inventory():<20} {item2.get_price()}")
print(f"ITEM 3: {item3.get_item_description():15} {item3.get_inventory():<20} {item3.get_price()}")
