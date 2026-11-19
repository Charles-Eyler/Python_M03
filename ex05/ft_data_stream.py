import random
import typing

player_name = ["Bethany", "Amber", "Lloyd", "Ghulam", "Gail"
               "Eve", "Alexis", "Brett", "Isabelle", "Tyrone"]

player_action = ["Beach cleanups", "Breathing exercises",
                 "Sound bath meditation", "Ice skating", "Bird watching"
                 "Drone flying", "Cliff diving", "RC car racing",
                 "Sculpture making", "Archery"]


def gen_events() -> typing.Generator[tuple[str, str], None, None]:
    yield (random.choice(player_name), random.choice(player_action))


def print_events() -> None:
    for i in range(0, 1000):
        event_tuple: tuple[str, str] = next(gen_events())
        print(f"Event {i}: Player {event_tuple[0]}"
              f" did action {event_tuple[1]}")


def create_event_list() -> list:
    event_list: list[tuple] = []
    for i in range(0, 10):
        event_list.append(next(gen_events()))
    return event_list


def remove_elements(event_list) -> typing.Generator[
                                    tuple[str, str], None, None]:
    for i in range(0, 10):
        removed = random.choice(event_list)
        event_list.remove(removed)
        yield removed


def ft_data_stream():
    print("=== Game Data Stream Processor ===")
    print_events()
    event_list = create_event_list()
    print("Build list of 10 events:", event_list)
    for event in remove_elements(event_list):
        print("Got an event from list:", event)
        print("Remains in list:", event_list)


if __name__ == "__main__":
    ft_data_stream()