#!/usr/bin/env python3
import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    names: tuple[str, ...] = ("Alice", "Bob", "Charlie", "Dylan")
    actions: tuple[str, ...] = ("run",
                                "eat",
                                "sleep",
                                "grab",
                                "move",
                                "release",
                                "climb")
    while True:
        name: str = random.choice(names)
        action: str = random.choice(actions)
        yield (name, action)


def consume_event(lst: list[tuple[str, str]]) -> typing.Generator[
                                                                  tuple[str,
                                                                        str],
                                                                  None,
                                                                  None]:
    while len(lst) > 0:
        len_lst: int = len(lst) - 1
        gevent: tuple[str, str] = lst.pop(random.randint(0, len_lst))
        yield gevent


if __name__ == "__main__":
    gen = gen_event()
    i = 0
    for i in range(1000):
        event = next(gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
        i += 1

    lst_event: list[tuple[str, str]] = []
    i = 0
    for _ in range(10):
        lst_event.append(next(gen))
    print(f"Built list of 10 events: {lst_event}")

    for event in consume_event(lst_event):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {lst_event}")
