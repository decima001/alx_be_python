def main():
    # Prompt the user for input
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low/not_needed): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Match case for priority level
    match priority:
        case "high":
            base_message = f"'{task}' is a high priority task"
        case "medium":
            base_message = f"'{task}' is a medium priority task"
        case "low":
<<<<<<< HEAD
            reminder = f"Note: '{task}' is a low priority task"
        case "Not needed":
            reminder = f"Stress: '{task}' is a not needed task"
        case _:
            print("Invalid priority level. Please enter high, medium, or low.")
=======
            base_message = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority. Please enter high, medium, or low.")
>>>>>>> 40c1bce85de10b18cae5bd99aea8b770b52d6fed
            return

    # Add time-sensitivity to message
    if time_bound == "yes":
<<<<<<< HEAD
        reminder += " that requires immediate attention today!"
=======
        print(f"Reminder: {base_message} that requires immediate attention today!")
>>>>>>> 40c1bce85de10b18cae5bd99aea8b770b52d6fed
    elif time_bound == "no":
        if priority == "low":
            print(f"Note: {base_message}. Consider completing it when you have free time.")
        else:
<<<<<<< HEAD
            reminder += "."
    else:
        print("Invalid time-bound input. Please enter 'yes' or 'no'.")
        return

    print("\n" + reminder)
=======
            print(f"Reminder: {base_message}.")
    else:
        print("Invalid input for time sensitivity. Please enter 'yes' or 'no'.")
>>>>>>> 40c1bce85de10b18cae5bd99aea8b770b52d6fed

if __name__ == "__main__":
    main()
