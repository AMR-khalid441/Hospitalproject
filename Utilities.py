def add_value(start: int, end: int) -> str:
    print(f"start: {start}, end: {end}")  # Debugging print
    while True:
        try:
            value = int(input(f"Enter the Choice (From {start} to {end} ) : "))
            if value < start or value > end:
                print("The choice is not valid.")
            else:
                return value
        except ValueError:
            print("Please enter an integer value.")


def printing_list(ls):
    print(*ls, sep="\n")



if __name__ == "__main__":
    add_value(2, 5)