
import PhoneClass as p

phone1 = p.Phone("Apple", "Iphone 15", 1299)

print(f'{"Manufacturer:":15}', phone1.get_manufact())
print(f'{"Model:":15}', phone1.get_model())
print(f'{"Retail Price:":15}', phone1.get_retail_price())
print()
manufacturer = input("Manufacturer Name? ")
model = input("Model? ")
retail_price = input("Price? ")
phone1.set_manufact(manufacturer)
phone1.set_model(model)
phone1.set_retail_price(retail_price)
print()
print(f'{"Updated Manufacturer:":22}', phone1.get_manufact())
print(f'{"Updated Model:":22}', phone1.get_model())
print(f'{"Updated Retail Price:":22}', phone1.get_retail_price())
