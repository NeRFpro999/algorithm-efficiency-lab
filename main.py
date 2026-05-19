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


def bubble_sort(numbers):
    """
    Sorts a list using bubble sort.
    Returns the sorted list and the number of comparisons made.
    """

    numbers = numbers.copy()
    comparisons = 0

    for i in range(len(numbers)):
        for j in range(0, len(numbers) - i - 1):
            comparisons += 1

            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers, comparisons


def merge_sort(numbers):
    """
    Sorts a list using merge sort.
    Returns the sorted list and the number of comparisons made.
    """

    if len(numbers) <= 1:
        return numbers, 0

    middle = len(numbers) // 2

    left_half, left_comparisons = merge_sort(numbers[:middle])
    right_half, right_comparisons = merge_sort(numbers[middle:])

    merged_list, merge_comparisons = merge(left_half, right_half)

    total_comparisons = left_comparisons + right_comparisons + merge_comparisons

    return merged_list, total_comparisons


def merge(left, right):
    merged = []
    comparisons = 0
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        comparisons += 1

        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged, comparisons


def run_search_experiment():
    input_sizes = [10, 100, 1000, 10000]

    print("Linear Search vs Binary Search")
    print("-" * 55)
    print(f"{'Input Size':<15}{'Linear Checks':<20}{'Binary Checks'}")
    print("-" * 55)

    for size in input_sizes:
        numbers = list(range(1, size + 1))
        target = size

        _, linear_checks = linear_search(numbers, target)
        _, binary_checks = binary_search(numbers, target)

        print(f"{size:<15}{linear_checks:<20}{binary_checks}")


def run_sorting_experiment():
    input_sizes = [10, 100, 1000]

    print()
    print("Bubble Sort vs Merge Sort")
    print("-" * 60)
    print(f"{'Input Size':<15}{'Bubble Comparisons':<25}{'Merge Comparisons'}")
    print("-" * 60)

    for size in input_sizes:
        numbers = list(range(size, 0, -1))

        _, bubble_comparisons = bubble_sort(numbers)
        _, merge_comparisons = merge_sort(numbers)

        print(f"{size:<15}{bubble_comparisons:<25}{merge_comparisons}")


def main():
    run_search_experiment()
    run_sorting_experiment()

    print()
    print("Conclusion:")
    print("Linear search and bubble sort are simple, but they become inefficient as the input grows.")
    print("Binary search and merge sort are faster because they reduce the amount of work needed.")


if __name__ == "__main__":
    main()