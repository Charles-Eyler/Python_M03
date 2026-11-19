import math


def get_player_pos() -> tuple:
    while True:
        coords = input("Enter new coordinates as floats in format "
                       "x, y, z': ").split(",")
        vector = 0

        if len(coords) != 3:
            print("Invalid syntax")
        if len(coords) == 3:
            try:
                while vector < 3:
                    coords[vector] = float(coords[vector])
                    vector += 1
            except ValueError as e:
                vector = 0
                print(e)
        if vector == 3:
            break
    coords_tuple = tuple(coords)
    return coords_tuple


def ft_coordinate_system():
    first_coords = get_player_pos()
    print("Got first tuple", first_coords)
    print(f"It includes"
          f"x={first_coords[0]}, y={first_coords[1]}, z={first_coords[2]}")
    center_distance = round(math.sqrt((first_coords[0] - 0) ** 2 +
                                      (first_coords[1] - 0) ** 2 +
                                      (first_coords[2] - 0) ** 2), 4)

    print("Distance to center = ", center_distance)
    print("\n")
    print("Get a second set of coordinates")
    second_coords = get_player_pos()
    points_distance = round(math.sqrt((first_coords[0] - second_coords[0])
                                      ** 2 + (first_coords[1] -
                                      second_coords[1]) ** 2 +
                                      (first_coords[2] - second_coords[2])
                                      ** 2), 4)
    print("Distance between the 2 sets of coordinates: ", points_distance)


if __name__ == "__main__":
    ft_coordinate_system()
