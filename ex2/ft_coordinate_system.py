#!/usr/bin/env python3

import math

def get_player_pos():
    new_pos = input("Enter new coordinates as floats in format 'x,y,z':")
    i = 0
    while i < 4:
        try:
            float(new_pos)
        except ValueError:
            print(f"Invalid Syntax")


if __name__ == "__main__":
    get_player_pos()