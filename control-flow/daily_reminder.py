# daily_reminder.py

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
            print("Invalid priority level entered.")
            return

    if time_bound == "yes":
        if priority in ["high", "medium"]:
            reminder += " that requires immediate attention today!"
        elif priority == "low":
            reminder += ". Even though it's low priority, it's time-sensitive!"
    elif time_bound == "no":
        if priority == "low":
            reminder += ". Consider completing it when you have free time."
        else:
            reminder += "."

    print(reminder)

if __name__ == "__main__":
    main()