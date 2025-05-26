def main():
    # Get user input
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Initialize reminder message
    reminder = ""

    # Match case to handle priority
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority. Please enter high, medium, or low.")
            return

    # Add time-sensitivity info
    if time_bound == "yes":
        reminder = f"Reminder: {reminder} that requires immediate attention today!"
    elif time_bound == "no":
        if priority == "low":
            reminder = f"Note: {reminder}. Consider completing it when you have free time."
        else:
            reminder = f"Reminder: {reminder}."
    else:
        print("Invalid input for time sensitivity. Please enter 'yes' or 'no'.")
        return

    # Output final reminder
    print("\n" + reminder)

if __name__ == "__main__":
    main()
