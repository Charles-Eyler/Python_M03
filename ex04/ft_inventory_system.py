import sys

args = sys.argv[1:]


class InventoryErrors(Exception):
    def __init__(self, msg):
        self._msg = msg

    def print_error(self):
        return self._msg


class RepError(InventoryErrors):
    def __init__(self, msg):
        pass


def check_key(inventory, key):
    if key in dict.keys(inventory):
        msg = f"Redundant item '{key}' - discarding"
        raise RepError(msg)


def make_inventory() -> dict:
    inventory: dict = {}
    for arg in args:
        try:
            split_args = arg.split(':')
            if len(split_args) == 2:
                check_key(inventory, split_args[0])
                inventory[split_args[0]] = int(split_args[1])
            else:
                print(f"Error - invalid parameter '{arg}'")
        except RepError as e:
            print(e)
        except ValueError as e:
            print(f"Quantity Error for {arg}: {e}")
    return inventory


def item_percentage(inventory):
    for k in dict.keys(inventory):
        print(f"Item {k} represents"
              f" {round(inventory[k]/sum(dict.values(inventory)) * 100, 1)}%")


def most_abundant_item(inventory):
    i = 0
    for key in dict.keys(inventory):
        if i == 0:
            most_ab_key = key
        if i != 0 and inventory[most_ab_key] < inventory[key]:
            most_ab_key = key
        i += 1
    return most_ab_key


def least_abundant_item(inventory):
    i = 0
    for key in dict.keys(inventory):
        if i == 0:
            leat_ab_key = key
        if i != 0 and inventory[leat_ab_key] > inventory[key]:
            leat_ab_key = key
        i += 1
    return leat_ab_key


def ft_inventory_system() -> None:
    print("=== Inventory System Analysis ===")
    inventory = make_inventory()
    print(f"Got inventory: {inventory}")
    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")
    print(f"Total quantity of the {len(dict.keys(inventory))} items:"
          f" {sum(dict.values(inventory))}")
    item_percentage(inventory)
    print(f"Item most abundant: {most_abundant_item(inventory)}"
          f" with quantity {inventory[most_abundant_item(inventory)]}")
    print(f"Item least abundant: {least_abundant_item(inventory)}"
          f" with quantity {inventory[least_abundant_item(inventory)]}")
    inventory.update({"magic_item": 1})
    print("Updated inventory: ", inventory)


if __name__ == "__main__":
    ft_inventory_system()
