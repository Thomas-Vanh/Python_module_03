#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    i: int = 0
    lst: list[str] = sys.argv[1:]
    lst_len: int = len(lst)
    if lst_len < 2:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
    else:
        lst_int: list[int] = [0] * lst_len
        valid_count: int = 0
    while i < lst_len:
        try:
            lst_int[valid_count] = int(lst[i])
            valid_count += 1
        except ValueError:
            print(f"Invalid parameter: {lst[i]}")
        i += 1
    lst_final = lst_int[:valid_count]
    if not lst_final:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
    else:
        print(f"Score processed: {lst_final}")
        print(f"Total players: {valid_count}")
        print(f"Total score: {sum(lst_final)}")
        print(f"High score: {max(lst_final)}")
        print(f"Low score: {min(lst_final)}")
        print(f"Score range: {max(lst_final)-min(lst_final)}")


if __name__ == "__main__":
    main()
