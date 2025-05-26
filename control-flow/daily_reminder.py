def main():
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task"
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task"
        case "low":
            reminder = f"Note: '{task}' is a low priority task"
        case _:
            print("Invalid priority level. Please enter high, medium, or low.")
            return

    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no":
        if priority == "low":
            reminder += ". Consider completing it when you have free time."
        else:
            reminder += "."
    else:
        print("Invalid time-bound input. Please enter 'yes' or 'no'.")
        return

    print("\n" + reminder)

if __name__ == "__main__":
    main()
