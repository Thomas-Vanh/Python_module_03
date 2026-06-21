#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    lst_len: int = len(sys.argv)
    if lst_len > 1:
        print(f"Arguments received: {lst_len}")
        i: int = 1
        while i < lst_len:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    else:
        print("No arguments provided!")
    print(f"Total arguments: {lst_len}")


if __name__ == "__main__":
    main()
