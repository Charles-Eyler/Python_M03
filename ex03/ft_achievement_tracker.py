import random

achievements = ["Crafting Genius", "Strategist", "World Savior",
                "Speed Runner", "Survivor", "Master Explorer",
                "Treasure Hunter",  "Unstoppable", "First Steps",
                "Colector Supreme", "Untouchable", "Sharp Mind",
                "Boss Slayer"]


def gen_player_achievement() -> set:
    player_achieve = random.sample(achievements, 
                                random.randrange(0, len(achievements)))
    return set(player_achieve)


def ft_achievement_tracker() -> None:
    player1 = gen_player_achievement()
    player2 = gen_player_achievement()
    player3 = gen_player_achievement()
    player4 = gen_player_achievement()
    common = set.intersection(player1, player2, player3, player4)
    print("=== Achievement Tracker System ===")
    print("Player Alice: ", player1)
    print("Player Bob: ", player2)
    print("Player Charlie: ", player3)
    print("Player Dylan: ", player4)
    print("\n")
    print("Common achievements:", common)
    print("\n")
    print("Only Alice has: ", player1.difference(player2, player3, player4))
    print("Only Bob has: ", player2.difference(player1, player3, player4))
    print("Only Charile has: ", player3.difference(player1, player2, player4))
    print("Only Dylan has: ", player4.difference(player1, player2, player3))
    print("\n")
    print("Alice is missing: ", set(achievements).difference(player1))
    print("Bob is missing: ", set(achievements).difference(player2))
    print("Charile is missing: ", set(achievements).difference(player3))
    print("Dylan is missing: ", set(achievements).difference(player4))


if __name__ == "__main__":
    ft_achievement_tracker()