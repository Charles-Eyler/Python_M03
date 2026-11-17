import sys


def ft_command_quest():
    args_num = 1
    print("=== Comand Quest ===")
    print("Program name: ", sys.argv[0])
    if len(sys.argv) > 1:
        print("Arguments recieved: ", len(sys.argv) - 1)
        for i in sys.argv:
            print("Argument ", args_num, ": ", i)
            args_num += 1
    else:
        print("No arguments Provided")
    return (print("Total arguments: ", len(sys.argv)))


if __name__ == "__main__":
    ft_command_quest()
