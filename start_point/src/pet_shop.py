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

# 7
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


def get_customer_cash(how_much):
    return how_much["cash"]


def remove_customer_cash(customer_buy,how_much):
    customer_buy["cash"] -= how_much


def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer,new_pet):
    customer["pets"].append(new_pet)


def customer_can_afford_pet(customer,new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False


def sell_pet_to_customer(pet_shop, need_pet, customer_purchase):
    add_pet_to_customer(customer_purchase, need_pet)
    increase_pets_sold(pet_shop, 1)
    price = need_pet["price"]
    remove_customer_cash(customer_purchase, price)
    add_or_remove_cash(pet_shop, price)


    # return get_customer_pet_count(customer_purchase)
    # return get_pets_sold(pet_shop)
    # return get_customer_cash(customer_purchas)
    # return get_total_cash(pet_shop)

        #     self.assertEqual(1, get_customer_pet_count(customer))
        # self.assertEqual(1, get_pets_sold(self.cc_pet_shop))
        # self.assertEqual(100, get_customer_cash(customer))
        # self.assertEqual(1900, get_total_cash(self.cc_pet_shop))
