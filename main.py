def linear_search(numbers, target):
    """
    Searches through the list one item at a time.
    Returns the index of the target and the number of checks made.
    """

    checks = 0

    for index, number in enumerate(numbers):
        checks += 1

        if number == target:
            return index, checks

    return -1, checks


def binary_search(numbers, target):
    """
    Searches a sorted list by repeatedly cutting the search range in half.
    Returns the index of the target and the number of checks made.
    """

    left = 0
    right = len(numbers) - 1
    checks = 0

    while left <= right:
        checks += 1
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle, checks
        elif numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1, checks


def run_search_experiment():
    input_sizes = [10, 100, 1000, 10000]

    print("Linear Search vs Binary Search")
    print("-" * 55)
    print(f"{'Input Size':<15}{'Linear Checks':<20}{'Binary Checks'}")
    print("-" * 55)

    for size in input_sizes:
        numbers = list(range(1, size + 1))
        target = size

        linear_index, linear_checks = linear_search(numbers, target)
        binary_index, binary_checks = binary_search(numbers, target)

        print(f"{size:<15}{linear_checks:<20}{binary_checks}")


def main():
    run_search_experiment()


if __name__ == "__main__":
    main()
    