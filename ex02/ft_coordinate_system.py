import math


def get_player_pos() -> tuple:
    coords = input("Enter new coordinates as floats 'x, y, z': ").split(",")
    vector = 0
    coords_tuple = tuple(map(float, coords))

    if len(coords_tuple) != 3:
        print("Invalid syntax")
        get_player_pos()
    for i in coords_tuple:
        if (not isinstance(coords_tuple[vector], float)):
            print(f"Error on parameter '{coords_tuple[vector]}': \
            could not convert string to float: {coords_tuple[vector]}")
            get_player_pos()
        vector += 1
    return coords_tuple


def ft_coordinate_system():
    first_coords = get_player_pos()
    print("Got first tuple", first_coords)
    print(f"It includes \
    x={first_coords[0]}, y={first_coords[1]}, z={first_coords[2]}")
    center_distance = math.sqrt((first_coords[0] - 0) ** 2 +
                                (first_coords[1] - 0) ** 2 +
                                (first_coords[2] - 0) ** 2)
    
    print("Distance to center = ", center_distance)
    print("\n")
    print("Get a second set of coordinates")
    second_coords = get_player_pos()
    points_distance = math.sqrt((first_coords[0] - second_coords[0]) ** 2 +
                                (first_coords[1] - second_coords[1]) ** 2 + 
                                (first_coords[2] - second_coords[2]) ** 2)
    print("Distance between the 2 sets of coordinates: ", points_distance)


if __name__ == "__main__":
    ft_coordinate_system()
