grocery_dict: dict[str, int] = {"milk": 3, "eggs": 24, "salad": 5, "pickles": 10}
store_inventory: dict[str, int] = {"eggs": 20, "milk": 10, "rasins": 5, "cheese": 3}
purchases: dict[str, int] = {}

# for item in grocery_dict:
#     if item in store_inventory:
#         purchases[item] = grocery_dict[item]

# for item in purchases:
#     if purchases[item] > store_inventory[item]:
#         purchases[item] = store_inventory[item]

# print(purchases)

new_list: list[str] = []

for key in grocery_dict:
    if key in store_inventory and grocery_dict[key] <= store_inventory[key]:
        new_list.append(key)

print(new_list)