import random

players_list = ['Alice', 'bob', 'Charlie', 'dylan',
                'Emma', 'Gregory', 'john', 'kevin', 'Liam']


def ft_data_alchemist():
    print("=== Game Data Alchemist ===")
    cap_list = [name.capitalize() for name in players_list]
    cap_only_list = [name for name in players_list
                     if name == name.capitalize()]
    players_scores = {k: random.randrange(0, 1000) for k in cap_list}
    print("Initial list of players: ", players_list)
    print("New list of players with all names capitalized: ", cap_list)
    print("New list of players with capitalized names only: ",
          cap_only_list)
    print("Score dict: ", players_scores)
    average_scores = round(sum(players_scores.values())/len(cap_list))
    print("Score average is ", average_scores)
    cap_scores = {k: v for k, v in players_scores.items()
                  if v > average_scores}
    print("High scores: ", cap_scores)


if __name__ == "__main__":
    ft_data_alchemist()