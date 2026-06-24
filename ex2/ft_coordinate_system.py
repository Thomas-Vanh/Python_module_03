#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            npos: str = input("Enter new coordinates "
                              "as floats in format 'x,y,z':")
        except EOFError:
            print("\nExiting coordinate input.")
            exit(0)
        pos: list[str] = npos.split(",")
        if len(pos) != 3:
            print("Invalid Syntax")
            continue
        try:
            part_x: str = pos[0].strip()
            part_y: str = pos[1].strip()
            part_z: str = pos[2].strip()

            x: float = float(part_x)
            y: float = float(part_y)
            z: float = float(part_z)

            return (x, y, z)
        except ValueError:
            for part in (pos[0], pos[1], pos[2]):
                clean: str = part.strip()
                try:
                    float(clean)
                except ValueError:
                    print(f"Error on parameter '{clean}': could not convert "
                          f"string to float: '{clean}'")
                    break


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    pos1: tuple[float, float, float] = get_player_pos()

    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    dist_cent: float = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
    print(f"Distance to center: {round(dist_cent, 4)}\n")

    print("Get a second set of coordinates")
    pos2: tuple[float, float, float] = get_player_pos()
    dist_points: float = math.sqrt(
        (pos2[0]-pos1[0])**2 +
        (pos2[1]-pos1[1])**2 +
        (pos2[2]-pos1[2])**2)
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(dist_points, 4)}")
