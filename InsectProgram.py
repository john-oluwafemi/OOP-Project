import InsectClass as I


def main():

    mosquito = I.Insect(2, 4, "mosquito")
    housefly = I.Insect(2, 4, "housefly")

    print(f"\n{mosquito.get_name()} can fly: {mosquito.get_miles()} miles")
    print(f"{housefly.get_name()} can fly: {housefly.get_miles()} miles")


    mosquito.flightlength()
    housefly.flightlength()

    mosquito.__name = 'MS'          #-----ignored bcos attr is hidden
    print(f"\n{mosquito.get_name().title()} can fly up to {mosquito.get_miles()} miles")
    print(f"{housefly.get_name().title()} can fly up to {housefly.get_miles()} miles\n")
    
main()

