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
