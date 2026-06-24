#!/usr/bin/env python3

import sys


def main() -> None:
    if len(sys.argv) < 2:
        print("At least one item needed - Exit of the program")
        return
    invent: dict[str, int] = {}
    args: list[str] = sys.argv[1:]
    print("=== Inventory System Analysis ===")
    for stuff in args:
        if ":" not in stuff:
            print(f"Error - invalid parameter '{stuff}'")
            continue
        idx: int = stuff.find(":")
        item_name: str = stuff[:idx]
        quantity_str: str = stuff[idx+1:]

        if item_name in invent:
            print(f"Redundant item '{item_name}' - discarding")
            continue
        try:
            quantity = int(quantity_str)
        except ValueError:
            print(f"Quantity error for '{item_name}' : invalid literal for"
                  f"int() with base 10: '{quantity_str}'")
            continue
        invent[item_name] = quantity

    print(f"Got inventory: {invent}")
    items_list: list[str] = list(invent.keys())
    print(f"Item list: {items_list}")

    total_qty: int = sum(invent.values())
    print(f"Total quantity of the {len(invent)} items: {total_qty}")

    for item in items_list:
        percent: float = round((invent[item] / total_qty)*100, 1)
        print(f"Item {item} represents {percent}%")

    most_abund: str | None = None
    least_abund: str | None = None

    for item in items_list:
        qty: int = invent[item]
        if most_abund is None or qty > invent[most_abund]:
            most_abund = item
        if least_abund is None or qty < invent[least_abund]:
            least_abund = item
    final_most: str = str(most_abund)
    final_least: str = str(least_abund)
    print(f"Item most abundant: {final_most} "
          f"with quantity {invent[final_most]}")
    print(f"Item least abundant: {final_least} "
          f"with quantity {invent[final_least]}")

    invent.update({"magic_item": 1})
    print(f"Updated inventory: {invent}")


if __name__ == "__main__":
    main()
