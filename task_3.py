"""
Hanoi Tower.
"""


def hanoi(
    n: int,
    source: str,
    target: str,
    auxiliary: str,
    pegs: dict
) -> None:
    """
    Recursive function to move disks from the source peg to the target peg.

    Args:
        n (int): The number of disks to move.
        source (str): The source peg.
        target (str): The target peg.
        auxiliary (str): The auxiliary peg.
        pegs (dict): The current state of the pegs.
    """
    if n == 1:
        # Move the top disk directly to the target peg
        disk = pegs[source].pop()
        pegs[target].append(disk)
        print(f"Move disk {source} to {target}: {disk}")
        print("Current state:", pegs)
    else:
        # Move n-1 disks from source to auxiliary, using target as auxiliary
        hanoi(n - 1, source, auxiliary, target, pegs)
        # Move the nth disk to target
        disk = pegs[source].pop()
        pegs[target].append(disk)
        print(f"Move disk {source} to {target}: {disk}")
        print("Current state:", pegs)
        # Move the n-1 disks from auxiliary to target using source as auxiliary
        hanoi(n - 1, auxiliary, target, source, pegs)


def input_integer() -> int:
    """
    Prompts the user to enter an integer and validates the input.
    """
    while True:
        try:
            user_input = int(input("Enter the number of disks: "))
            if user_input < 0:
                raise ValueError(
                    "Number of disks must be a non-negative integer."
                )
            return user_input
        except ValueError as e:
            print(f"Invalid input: {e}")


def main() -> None:
    """
    Main function.
    """
    n = input_integer()
    # Initial state of the pegs
    pegs = {
        'A': list(range(n, 0, -1)),  # Start with disks in descending order
        'B': [],
        'C': []
    }

    print("Starting state:", pegs)
    hanoi(n, 'A', 'C', 'B', pegs)
    print("Final state:", pegs)


if __name__ == "__main__":
    main()
