#!/usr/bin/env python3
import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    lst_plyr: list[str] = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
                           'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {lst_plyr}")
    plyr_acapt: list[str] = [plyr.capitalize() for plyr in lst_plyr]
    print(f"New list with all names capitalized: {plyr_acapt}")
    plyr_capt: list[str] = [plyr for plyr in lst_plyr
                            if plyr == plyr.capitalize()]
    print(f"New list of capitalized names only: {plyr_capt}")
    dict_plyr: dict[str, int] = {plyr: random.randint(0, 1000)
                                 for plyr in plyr_acapt}
    print(f"Score dict: {dict_plyr}")
    if len(dict_plyr) == 0:
        average: float = 0.0
    else:
        average = sum(dict_plyr.values()) / len(dict_plyr)
    print(f"Score average: {round(average, 2)}")
    high_score: dict[str, int] = {name: score for name, score
                                  in dict_plyr.items() if score > average}
    print(f"High scores: {high_score}")


if __name__ == "__main__":
    main()
