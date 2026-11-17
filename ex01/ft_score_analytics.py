import sys

args = sys.argv


def create_valid_args() -> list:
    valid_args = []
    count = 1
    error = False
    while count < len(args):
        try:
            valid_args.append(int(args[count]))
        except ValueError:
            print(f"Invalid parameter '{args[count]}'")
            error = True
        finally:
            count += 1
    if error is True:
        scores_not_valid()
    return valid_args


def scores_not_valid():
    return print("No scores provided. Usage: python3"
                 " ft_score_analytics.py <score1> <score2> ...")


def ft_score_analytics() -> None:
    print("=== Player Scores Analytics ===")
    valid_args = create_valid_args()
    try:
        if len(valid_args) == 0:
            scores_not_valid()
            raise ZeroDivisionError
        print("Scores processed: ", valid_args)
        print("Total players:", len(valid_args))
        print("Total score:", sum(valid_args))
        print("Average score:", sum(valid_args) / len(valid_args))
        print("High score:", max(valid_args))
        print("low score:", min(valid_args))
        print("Score range:", max(valid_args) - min(valid_args))
    except ZeroDivisionError:
        return


if __name__ == "__main__":
    ft_score_analytics()
