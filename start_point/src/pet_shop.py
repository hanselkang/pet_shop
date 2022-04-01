# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop_name):
    return pet_shop_name["name"]


def get_total_cash(total_cash):
    return total_cash["admin"]["total_cash"]


def add_or_remove_cash(money_budget, input_money):
    money_budget["admin"]["total_cash"] += input_money
    return money_budget["admin"]["total_cash"]


def get_pets_sold(sold_pets):
    return sold_pets["admin"]["pets_sold"]


def increase_pets_sold(sold_state, sold_number):
    sold_state["admin"]["pets_sold"] += sold_number
    return sold_state["admin"]["pets_sold"]


def get_stock_count(stock_inventory):
    return len(stock_inventory["pets"])


def get_pets_by_breed(pets_in_shop, pets_breed):
    list_breed = []
    for pets_select in pets_in_shop["pets"]:
        if pets_select["breed"] == pets_breed:
            list_breed.append(pets_select)
    return list_breed


def find_pet_by_name(pet_shop, pet_name):
    for pets_select in pet_shop["pets"]:
        if pets_select["name"] == pet_name:
            return pets_select


def remove_pet_by_name(pet_shop, pet_name):
    for pets_select in pet_shop["pets"]:
        if pets_select["name"] == pet_name:
            pet_shop["pets"].remove(pets_select)


def add_pet_to_stock(pet_shop, new_one):
    pet_shop["pets"].append(new_one)

