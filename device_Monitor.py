"""Simulated Device Monitoring and Alert System (CPP102 Week 17 project)."""

WARNING_LIMIT = 30    # 30 and above is at least WARNING
CRITICAL_LIMIT = 35   # above 35 is CRITICAL (35 itself is still WARNING)
LOWEST_VALID = 0
HIGHEST_VALID = 100


def get_initial_readings():
    """Return the starting list of simulated temperature readings."""
    return [28, 31, 35, 37, 29]


def display_menu():
    """Print the main menu."""
    print("SIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")
    print()


def is_whole_number(text):
    """Return True if text is a whole number such as 33 or -5."""
    if len(text) == 0:
        return False
    start = 0
    if text[0] == "-":          # a minus sign is allowed only at the front
        start = 1
    if start == len(text):      # the text is only "-"
        return False
    for index in range(start, len(text)):
        if text[index] not in "0123456789":
            return False
    return True


def display_readings(readings):
    """Print every reading with its position number."""
    print("CURRENT READINGS")
    print("----------------")
    for index in range(len(readings)):
        print(f"Reading {index + 1}: {readings[index]} °C")


def add_reading(readings, lowest, highest):
    """Ask for one reading and append it to readings only if it is valid."""
    text = input("Enter new reading: ").strip()
    print()
    if len(text) == 0:
        print("Invalid input. The reading cannot be empty.")
    elif not is_whole_number(text):
        print("Invalid input. Enter a whole number only.")
    elif int(text) < lowest or int(text) > highest:
        print(f"Invalid reading. Enter a value from {lowest} to {highest}.")
    else:
        readings.append(int(text))
        print("Reading added successfully.")


def classify_reading(reading, warning_limit, critical_limit):
    """Return NORMAL, WARNING, or CRITICAL for one reading."""
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:     # boundary: 35 is still WARNING
        return "WARNING"
    else:
        return "CRITICAL"


def display_classification(readings, warning_limit, critical_limit):
    """Print every reading with its classification."""
    print("READING CLASSIFICATION")
    print("----------------------")
    for reading in readings:
        category = classify_reading(reading, warning_limit, critical_limit)
        print(f"{reading} °C -> {category}")


def compute_total(readings):
    """Return the total of all readings (computed with a loop)."""
    total = 0
    for reading in readings:
        total = total + reading
    return total


def compute_average(readings):
    """Return the average of all readings."""
    return compute_total(readings) / len(readings)


def find_minimum(readings):
    """Return the smallest reading (starts from the first reading, not 0)."""
    minimum = readings[0]
    for reading in readings:
        if reading < minimum:
            minimum = reading
    return minimum


def find_maximum(readings):
    """Return the largest reading (starts from the first reading, not 0)."""
    maximum = readings[0]
    for reading in readings:
        if reading > maximum:
            maximum = reading
    return maximum


def count_category(readings, warning_limit, critical_limit, category):
    """Return how many readings belong to the given category."""
    count = 0
    for reading in readings:
        if classify_reading(reading, warning_limit, critical_limit) == category:
            count = count + 1
    return count


def compute_percentage(count, whole):
    """Return count as a percentage of whole."""
    return count / whole * 100


def determine_overall_status(warning_count, critical_count):
    """Return the overall monitoring status."""
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def display_summary(readings, warning_limit, critical_limit):
    """Print the full numerical summary and the overall status."""
    number = len(readings)
    normal = count_category(readings, warning_limit, critical_limit, "NORMAL")
    warning = count_category(readings, warning_limit, critical_limit, "WARNING")
    critical = count_category(readings, warning_limit, critical_limit, "CRITICAL")

    print("MONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings  : {number}")
    print(f"Total of readings   : {compute_total(readings)}")
    print(f"Average temperature : {compute_average(readings):.2f} °C")
    print(f"Minimum temperature : {find_minimum(readings)} °C")
    print(f"Maximum temperature : {find_maximum(readings)} °C")
    print()
    print(f"NORMAL   : {normal} ({compute_percentage(normal, number):.2f}%)")
    print(f"WARNING  : {warning} ({compute_percentage(warning, number):.2f}%)")
    print(f"CRITICAL : {critical} ({compute_percentage(critical, number):.2f}%)")
    print()
    print(f"Overall Status: {determine_overall_status(warning, critical)}")


def main():
    """Run the menu loop until the user chooses Exit."""
    readings = get_initial_readings()
    running = True
    while running:
        display_menu()
        choice = input("Enter choice: ").strip()
        print()
        if choice == "1":
            display_readings(readings)
        elif choice == "2":
            add_reading(readings, LOWEST_VALID, HIGHEST_VALID)
        elif choice == "3":
            display_classification(readings, WARNING_LIMIT, CRITICAL_LIMIT)
        elif choice == "4":
            display_summary(readings, WARNING_LIMIT, CRITICAL_LIMIT)
        elif choice == "5":
            print("Thank you for using the Device Monitoring System.")
            running = False
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
        if running:
            print()


main()