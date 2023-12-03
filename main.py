def count_batteries_by_health(present_capacities):
    # Initialize counts for healthy, exchange, and failed batteries
    counts = {
        "healthy": 0,
        "exchange": 0,
        "failed": 0
    }
    # Loop through each battery's present capacity
    for capacity in present_capacities:
        # Calculate State-of-Health (SoH) percentage for the current battery
        soh_percentage = (capacity / 120) * 100

        # Classify batteries based on SoH
        if soh_percentage > 80:
            counts["healthy"] += 1
        elif 62 <= soh_percentage <= 80:
            counts["exchange"] += 1
        else:
            counts["failed"] += 1

    return counts

def test_count_batteries_by_health():
    print("Testing count_batteries_by_health function...\n")
    # Example list of present capacities for testing
    present_capacities = [113, 116, 80, 95, 92, 70]
    # Call the function to get the counts for each battery classification
    counts = count_batteries_by_health(present_capacities)
    # Assertions to check if the counts match the expected results
    assert counts["healthy"] == 2
    assert counts["exchange"] == 3
    assert counts["failed"] == 1
    # Print the counts for better visibility
    print("Counts:", counts)
    print("Done counting :)\n")
def test_count_batteries_by_health_with_boundaries():
    print("Testing count_batteries_by_health function with boundary conditions...\n")
    # Test case with all batteries having the lowest SoH
    present_capacities_lowest_soh = [60, 61, 62]
    counts_lowest_soh = count_batteries_by_health(present_capacities_lowest_soh)
    assert counts_lowest_soh["healthy"] == 0
    assert counts_lowest_soh["exchange"] == 0
    assert counts_lowest_soh["failed"] == 3
    # Test case with all batteries having the highest SoH
    present_capacities_highest_soh = [119, 120, 121]
    counts_highest_soh = count_batteries_by_health(present_capacities_highest_soh)
    assert counts_highest_soh["healthy"] == 3
    assert counts_highest_soh["exchange"] == 0
    assert counts_highest_soh["failed"] == 0
    # Print the counts for better visibility
    print("Counts - Lowest SoH:", counts_lowest_soh)
    print("Counts - Highest SoH:", counts_highest_soh)
    print("Done counting with boundary conditions :)\n")

def test_count_batteries_by_health_with_random_distribution():
    print("Testing count_batteries_by_health function with random distribution...\n")
    # Test case with batteries having a random distribution of SoH
    present_capacities_random = [78, 92, 68, 105, 82, 74, 88]
    counts_random = count_batteries_by_health(present_capacities_random)
    assert counts_random["healthy"] == 3
    assert counts_random["exchange"] == 2
    assert counts_random["failed"] == 2

    # Print the counts for better visibility
    print("Counts - Random Distribution:", counts_random)
    print("Done counting with random distribution :)\n")

def test_count_batteries_by_health_with_large_list():
    print("Testing count_batteries_by_health function with a large list...\n")

    # Test case with a larger list of batteries
    present_capacities_large_list = [85] * 1000
    counts_large_list = count_batteries_by_health(present_capacities_large_list)
    assert counts_large_list["healthy"] == 1000
    assert counts_large_list["exchange"] == 0
    assert counts_large_list["failed"] == 0

    # Print the counts for better visibility
    print("Counts - Large List:", counts_large_list)
    print("Done counting with a large list :)\n")

def test_count_batteries_by_health_with_single_battery():
    print("Testing count_batteries_by_health function with a single battery...\n")

    # Test case with a single battery
    present_capacities_single_battery = [90]
    counts_single_battery = count_batteries_by_health(present_capacities_single_battery)
    assert counts_single_battery["healthy"] == 1
    assert counts_single_battery["exchange"] == 0
    assert counts_single_battery["failed"] == 0

    # Print the counts for better visibility
    print("Counts - Single Battery:", counts_single_battery)
    print("Done counting with a single battery :)\n")

def test_count_batteries_by_health_with_equal_distribution():
    print("Testing count_batteries_by_health function with an equal distribution of SoH...\n")

    # Test case with batteries having an equal distribution of SoH
    present_capacities_equal_distribution = [80, 85, 90, 75, 95, 70]
    counts_equal_distribution = count_batteries_by_health(present_capacities_equal_distribution)
    assert counts_equal_distribution["healthy"] == 2
    assert counts_equal_distribution["exchange"] == 2
    assert counts_equal_distribution["failed"] == 2

    # Print the counts for better visibility
    print("Counts - Equal Distribution:", counts_equal_distribution)
    print("Done counting with an equal distribution of SoH :)\n")

def test_count_batteries_by_health_with_empty_input():
    print("Testing count_batteries_by_health function with an empty input list...\n")

    # Test case with an empty list of batteries
    present_capacities_empty = []
    counts_empty = count_batteries_by_health(present_capacities_empty)
    assert counts_empty["healthy"] == 0
    assert counts_empty["exchange"] == 0
    assert counts_empty["failed"] == 0

    # Print the counts for better visibility
    print("Counts - Empty Input List:", counts_empty)
    print("Done counting with an empty input list :)\n")

if __name__ == '__main__':
    test_count_batteries_by_health()
    test_count_batteries_by_health_with_boundaries()
    test_count_batteries_by_health_with_random_distribution()
    test_count_batteries_by_health_with_large_list()
    test_count_batteries_by_health_with_single_battery()
    test_count_batteries_by_health_with_equal_distribution()
    test_count_batteries_by_health_with_empty_input()
