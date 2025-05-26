def main():
    # Prompt the user for input
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Match case for priority level
    match priority:
        case "high":
            base_message = f"'{task}' is a high priority task"
        case "medium":
            base_message = f"'{task}' is a medium priority task"
        case "low":
            base_message = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority. Please enter high, medium, or low.")
            return

    # Add time-sensitivity to message
    if time_bound == "yes":
        print(f"Reminder: {base_message} that requires immediate attention today!")
    elif time_bound == "no":
        if priority == "low":
            print(f"Note: {base_message}. Consider completing it when you have free time.")
        else:
            print(f"Reminder: {base_message}.")
    else:
        print("Invalid input for time sensitivity. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
