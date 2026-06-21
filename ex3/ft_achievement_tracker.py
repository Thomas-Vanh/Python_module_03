#!/usr/bin/env python3

import random


def gen_player_achievements() -> set[str]:
    achievements: list[str] = [
                                "First Steps",
                                "Welcome to the World",
                                "First Blood",
                                "Apprentice",
                                "Explorer",
                                "Collector",
                                "Victor",
                                "Seasoned Fighter",
                                "Master of the Lands",
                                "Treasure Hunter",
                                "Survivor",
                                "Hero",
                                "Legend",
                                "Perfectionist",
                                "Incredible",
                                "Invincible",
                                "Ghost",
                                "Demiurge",
                                "Omnipotent",
                                "Total Accomplishment"]
    i = 0
    player_set: set[str] = set()
    while i <= random.randint(5, 6):
        player_set.add(achievements[random.randrange(0, 19)])
        i += 1
    return player_set


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    player_1: set[str] = gen_player_achievements()
    player_2: set[str] = gen_player_achievements()
    player_3: set[str] = gen_player_achievements()
    player_4: set[str] = gen_player_achievements()
    print(f"Player Alice: {player_1}")
    print(f"Player Bob: {player_2}")
    print(f"Player Charlie: {player_3}")
    print(f"Player Dylan: {player_4}\n")

    player_union: set[str] = set.union(player_1, player_2, player_3, player_4)
    print(f"All distinct achievements: {player_union}\n")

    player_inter: set[str] = set.intersection(player_1, player_2, player_3,
                                              player_4)
    print(f"Common achievements: {player_inter}\n")

    print(f"Only Alice has: "
          f"{player_1.difference(player_2, player_3, player_4)}")
    print(f"Only Bob has: {player_2.difference(player_1, player_3, player_4)}")
    print(f"Only Charlie has: "
          f"{player_3.difference(player_1, player_2, player_4)}")
    print(f"Only Dylan has: "
          f"{player_4.difference(player_1, player_2, player_3)}\n")

    print(f"Alice is missing: {player_union.difference(player_1)}")
    print(f"Bob is missing: {player_union.difference(player_2)}")
    print(f"Charlie is missing: {player_union.difference(player_3)}")
    print(f"Dylan is missing: {player_union.difference(player_4)}")
